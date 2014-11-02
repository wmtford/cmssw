#include "RecoLocalTracker/SiStripClusterizer/plugins/SiStripClusterizer.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "RecoLocalTracker/SiStripClusterizer/interface/StripClusterizerAlgorithmFactory.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/transform.h"
#include "boost/foreach.hpp"

SiStripClusterizer::
SiStripClusterizer(const edm::ParameterSet& conf) 
  : inputTags( conf.getParameter<std::vector<edm::InputTag> >("DigiProducersList") ),
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

  //  Instantiate a TrackerHitAssociator and configure it.
  //   For a permanent implementation we'd make this configurable via conf.
  vstring trackerContainers;
  trackerContainers.push_back("TrackerHitsTIBLowTof");
  trackerContainers.push_back("TrackerHitsTIBHighTof");
  trackerContainers.push_back("TrackerHitsTIDLowTof");
  trackerContainers.push_back("TrackerHitsTIDHighTof");
  trackerContainers.push_back("TrackerHitsTOBLowTof");
  trackerContainers.push_back("TrackerHitsTOBHighTof");
  trackerContainers.push_back("TrackerHitsTECLowTof");
  trackerContainers.push_back("TrackerHitsTECHighTof");
  edm::ParameterSet associatorParameters;
  associatorParameters.addParameter<bool>("associatePixel", false);
  associatorParameters.addParameter<bool>("associateStrip", true);
  associatorParameters.addParameter<bool>("associateRecoTracks", true);
  associatorParameters.addParameter<vstring>("ROUList", trackerContainers);
  TrackerHitAssociator associator(event, associatorParameters);
  bool useAssociator(true);  // Would be set in conf.

  BOOST_FOREACH( const edm::EDGetTokenT< edm::DetSetVector<SiStripDigi> >& token, inputTokens) {
    if(      findInput( token, inputOld, event) ) {
      if (useAssociator) algorithm->clusterize(*inputOld, *output, associator); 
      else algorithm->clusterize(*inputOld, *output);
    } 
//     else if( findInput( tag, inputNew, event) ) algorithm->clusterize(*inputNew);
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
