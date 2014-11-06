#include "RecoLocalTracker/SiStripClusterizer/plugins/SiStripClusterizer.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "RecoLocalTracker/SiStripClusterizer/interface/StripClusterizerAlgorithmFactory.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/transform.h"
#include "boost/foreach.hpp"
#include "CalibFormats/SiStripObjects/interface/SiStripQuality.h"
#include "CalibTracker/Records/interface/SiStripQualityRcd.h"
#include "CalibTracker/SiStripCommon/interface/SiStripDetInfoFileReader.h"

SiStripClusterizer::
SiStripClusterizer(const edm::ParameterSet& conf) 
  : conf_(conf.getParameter<edm::ParameterSet>("Clusterizer")), inputTags( conf.getParameter<std::vector<edm::InputTag> >("DigiProducersList") ),
    algorithm( StripClusterizerAlgorithmFactory::create(conf.getParameter<edm::ParameterSet>("Clusterizer")) ) {
  produces< edmNew::DetSetVector<SiStripCluster> > ();
  inputTokens = edm::vector_transform( inputTags, [this](edm::InputTag const & tag) { return consumes< edm::DetSetVector<SiStripDigi> >(tag);} );
}

void SiStripClusterizer::
produce(edm::Event& event, const edm::EventSetup& es)  {

  std::auto_ptr< edmNew::DetSetVector<SiStripCluster> > output(new edmNew::DetSetVector<SiStripCluster>());
  output->reserve(10000,4*10000);

  edm::Handle< edm::DetSetVector<SiStripDigi> >     inputOld;  
//   edm::Handle< edmNew::DetSetVector<SiStripDigi> >  inputNew;  

  algorithm->initialize(es);  

  bool doRefineCluster = conf_.getParameter<bool>("doRefineCluster");
  float occupancyThreshold = conf_.getParameter<double>("occupancyThreshold");
  bool useAssociator = conf_.getParameter<bool>("useAssociator");

  BOOST_FOREACH( const edm::EDGetTokenT< edm::DetSetVector<SiStripDigi> >& token, inputTokens) {
    if(      findInput( token, inputOld, event) ) {
      if (useAssociator) algorithm->clusterize(*inputOld, *output, TrackerHitAssociator(event, conf_));
      else algorithm->clusterize(*inputOld, *output);
      if (doRefineCluster) refineCluster(es, inputOld, output, occupancyThreshold);
    } 
//     else if( findInput( tag, inputNew, event) ) algorithm->clusterize(*inputNew, *output);
    else edm::LogError("Input Not Found") << "[SiStripClusterizer::produce] ";// << tag;
  }

  LogDebug("Output") << output->dataSize() << " clusters from " 
		     << output->size()     << " modules";
  output->shrink_to_fit();
  event.put(output);
}

template<class T>
inline
bool SiStripClusterizer::
findInput(const edm::EDGetTokenT<T>& tag, edm::Handle<T>& handle, const edm::Event& e) {
    e.getByToken( tag, handle);
    return handle.isValid();
}

void SiStripClusterizer::
refineCluster(const edm::EventSetup& es,
	      const edm::Handle< edm::DetSetVector<SiStripDigi> >& input,
	      std::auto_ptr< edmNew::DetSetVector<SiStripCluster> >& output,
	      const float& occupancyThreshold) {
  // Flag merge-prone clusters for expanded CPE errors
  // Criterion is sensor occupancy exceeding threshold
  for (edmNew::DetSetVector<SiStripCluster>::const_iterator det=output->begin(); det!=output->end(); det++) {
    uint32_t detId = det->id();
    // Find the number of good strips in this sensor
    //   (from DPGAnalysis/SiStripTools/OccupancyPlots)
    edm::ESHandle<SiStripQuality> quality;
    es.get<SiStripQualityRcd>().get("",quality);
    SiStripDetInfoFileReader * reader=edm::Service<SiStripDetInfoFileReader>().operator->();
    int nchannideal = reader->getNumberOfApvsAndStripLength(detId).first*128;
    int nchannreal = 0;
    for(int strip = 0; strip < nchannideal; ++strip)
      if(!quality->IsStripBad(detId,strip)) ++nchannreal;

    edm::DetSetVector<SiStripDigi>::const_iterator digis = input->find(detId);
    if (digis != input->end()) {
      int ndigi = digis->size();
      int nmergedclust = 0;
      for (edmNew::DetSet<SiStripCluster>::iterator clust = det->begin(); clust != det->end(); clust++) {
	if (clust->getSplitClusterError() == -1.0) nmergedclust++;
	if (ndigi > occupancyThreshold*nchannreal) clust->setSplitClusterError(-1.0);
	else clust->setSplitClusterError(-99999.9);
      }
     // std::cout << "Sensor:strips_occStrips_clust_merged " << nchannreal << " " << ndigi << " " << det->size() << " " << nmergedclust << std::endl;
    }
  }  // traverse sensors
}
