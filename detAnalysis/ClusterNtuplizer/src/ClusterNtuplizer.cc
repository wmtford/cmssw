// -*- C++ -*-
//
// Package:    ClusterNtuplizer
// Class:      ClusterNtuplizer
// 
/**\class ClusterNtuplizer ClusterNtuplizer.cc UserCode/WTFord/detAnalysis/ClusterNtuplizer/src/ClusterNtuplizer.cc

 Description:  Analyze siStrip clusters for multiple track crossings

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  William T. Ford
//         Created:  Sat Nov 21 18:02:42 MST 2009
// $Id: ClusterNtuplizer.cc,v 1.3 2011/06/01 23:22:26 wtford Exp $
//
//

// this class header
// #include "detAnalysis/ClusterNtuplizer/interface/ClusterNtuplizer.h"

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TROOT.h"

#include "TObject.h"
#include "TH1D.h"
#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// Data Formats
#include "DataFormats/Common/interface/DetSet.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
// #include "DataFormats/VertexReco/interface/Vertex.h"
// #include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
// #include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
// #include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "SimDataFormats/CrossingFrame/interface/CrossingFrame.h"
#include "SimDataFormats/CrossingFrame/interface/MixCollection.h"
#include "SimDataFormats/TrackerDigiSimLink/interface/StripDigiSimLink.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

// For the splitter functions
#include "wtfRecoLocalTracker/SplitClustersProducer/interface/SplitClustersAlgos.h"

//
// class declaration
//

class ClusterNtuplizer : public edm::EDAnalyzer, public SplitClustersAlgos {
public:
  explicit ClusterNtuplizer(const edm::ParameterSet&);
  ~ClusterNtuplizer();

private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();
  void printDetInfo(uint32_t detID, const TrackerGeometry& tracker);
//   void fillClusNtp(TrackingParticle* tp, double angNnbr, int TrackNumber, int found, int* NinCone);

      // ----------member data ---------------------------

  typedef std::map<unsigned int, std::vector<PSimHit> > simhit_map;
  simhit_map SimHitMap;
//   typedef std::vector<PSimHit>::const_iterator simhitvec_iterator;

private:
  edm::ParameterSet conf_;
  edm::InputTag theClusterSourceLabel;
  edm::InputTag bsSrc_;
  int printOut_;

  std::vector<const SiStripCluster*> vPSiStripCluster;

  edm::Handle<CrossingFrame<PSimHit> > cf_simhit;
  std::vector<const CrossingFrame<PSimHit> *> cf_simhitvec;
//   MixCollection<PSimHit>  TrackerHits;
  typedef std::vector<std::string> vstring;
  vstring trackerContainers;
  edm::Handle< edm::DetSetVector<StripDigiSimLink> >  stripdigisimlink;

  int evCnt_;

  TTree* clusTree_;  // tree filled for each cluster
  struct ClusterStruct{
    int subDet;
    float thickness;
    int width;
    int NsimHits;
    int firstProcess;
    int secondProcess;
    int thirdProcess;
    int fourthProcess;
    int firstPID;
    int secondPID;
    int thirdPID;
    int fourthPID;
    int Ntp;
    float firstTkChg;
    float secondTkChg;
    float thirdTkChg;
    float fourthTkChg;
    float charge;
    float firstPmag;
    float secondPmag;
    float thirdPmag;
    float fourthPmag;
    float firstPathLength;
    float secondPathLength;
    float thirdPathLength;
    float fourthPathLength;
    float pathLstraight;
    float allHtPathLength;
    float Eloss;
    int sat;
    int tkFlip;
    int ovlap;
    int layer;
    int stereo;

    void init();
    void print();
    } clusNtp_;

  TTree* pvTree_;  // tree filled for each pixel vertex
  struct pvStruct{
    int isValid;
    int isFake;
    int Ntrks;
    int nDoF;
    float chisq;
    float xV;
    float yV;
    float zV;
    float xVsig;
    float yVsig;
    float zVsig;

    void init();
    void print();
    } pvNtp_;

  TH1F* hNpv;
  TH2F* hzV_Iev;
  TH2F* hNtrk_zVerrPri;
  TH2F* hNtrk_zVerrSec;
  TH1F* hZvPri;
  TH1F* hZvSec;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
ClusterNtuplizer::ClusterNtuplizer(const edm::ParameterSet& iConfig): 
 conf_(iConfig),
 theClusterSourceLabel(iConfig.getParameter<edm::InputTag>( "clusterSourceLabel" )),
 bsSrc_(iConfig.getParameter<edm::InputTag>("beamSpot")),
 printOut_(iConfig.getUntrackedParameter<int>("printOut"))

{
   //now do what ever initialization is needed

}


ClusterNtuplizer::~ClusterNtuplizer()
{
 
   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
ClusterNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;

  if (printOut_ > 0) std::cout << std::endl;
  trackerContainers.clear();
  cf_simhit.clear();
  cf_simhitvec.clear();

  evCnt_++;

  edm::Handle<reco::BeamSpot> recoBeamSpotHandle;
  iEvent.getByLabel(bsSrc_, recoBeamSpotHandle);
  const reco::BeamSpot& bs = *recoBeamSpotHandle;      

  edm::Handle<reco::VertexCollection>  pixelVertexCollectionHandle;
//   iEvent.getByLabel(pixelVertexLabel_, pixelVertexCollectionHandle);
  iEvent.getByLabel("pixelVertices", pixelVertexCollectionHandle);
  const reco::VertexCollection pixelVertexColl = *(pixelVertexCollectionHandle.product());
//   nPixelVertices_ = pixelVertexColl.size();
//   std::cout << "No. of pixel vertices = " <<  pixelVertexColl.size() << std::endl;
  hNpv->Fill(int(pixelVertexColl.size()));
  reco::Vertex::Point pixPriVtx(bs.position());
  iniVertex(pixelVertexColl, pixPriVtx);
  float zv = 0, zverr = 0;
  iniZvertex(pixelVertexColl, zv, zverr);
  hZvPri->Fill(zv);
//  iterate over pixel vertices and fill the pixel vertex Ntuple
  int iVtx = 0;
  for(reco::VertexCollection::const_iterator vi = pixelVertexColl.begin(); 
      vi != pixelVertexColl.end(); ++vi) {
    if (printOut_ > 0) std::cout << "  " << vi->tracksSize() << "  " << vi->z() << "+/-" << vi->zError() << std::endl;
    pvNtp_.isValid = int(vi->isValid());
    pvNtp_.isFake = int(vi->isFake());
    pvNtp_.Ntrks = vi->tracksSize();
    pvNtp_.nDoF = vi->ndof();
    pvNtp_.chisq = vi->chi2();
    pvNtp_.xV = vi->x();
    pvNtp_.yV = vi->y();
    pvNtp_.zV = vi->z();
    pvNtp_.xVsig = vi->xError();
    pvNtp_.yVsig = vi->yError();
    pvNtp_.zVsig = vi->zError();
    pvTree_->Fill();
    hzV_Iev->Fill(vi->z(), evCnt_);
    if (iVtx == 0) {
      hNtrk_zVerrPri->Fill(vi->zError(), vi->tracksSize());
    } else {
      hNtrk_zVerrSec->Fill(vi->zError(), vi->tracksSize());
      hZvSec->Fill(vi->z() - zv);
    }
    ++iVtx;
  }
  if (printOut_ > 0) std::cout << "  zv = " << zv << " +/- " << zverr << std::endl;

  //
  // Take by default all tracker SimHits
  //
  trackerContainers.push_back("g4SimHitsTrackerHitsTIBLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTIBHighTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTIDLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTIDHighTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTOBLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTOBHighTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTECLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTECHighTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelBarrelLowTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelBarrelHighTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelEndcapLowTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelEndcapHighTof");


//   unsigned simHitCounter(0);
//   std::vector<std::pair<int,int>> simHitMap;
//   simHitMap.clear();
  for(uint32_t i = 0; i< trackerContainers.size(); i++){
    iEvent.getByLabel("mix", trackerContainers[i], cf_simhit);
    cf_simhitvec.push_back(cf_simhit.product());
//     std::cout << i << "  " << cf_simhit->getNrSignals() << std::endl;
//     if (i == 0) simHitMap.push_back(std::make_pair(StripSubdetector::TIB, simHitCounter));
//     else if (i == 2) simHitMap.push_back(std::make_pair(StripSubdetector::TID, simHitCounter));
//     else if (i == 4) simHitMap.push_back(std::make_pair(StripSubdetector::TOB, simHitCounter));
//     else if (i == 6) simHitMap.push_back(std::make_pair(StripSubdetector::TEC, simHitCounter));
//     simHitCounter += cf_simhit->getNrSignals();
  }
//   std::cout << "simHitMap = " << std::endl;
//   for (std::vector<std::pair<int,int>>::iterator it = simHitMap.begin(); it != simHitMap.end(); ++it)
//     std::cout << ' ' << (*it).first << ", " << (*it).second << std::endl;
  
  std::auto_ptr<MixCollection<PSimHit> > allTrackerHits(new MixCollection<PSimHit>(cf_simhitvec));
//   TrackerHits = (*allTrackerHits);
// cite:  SimTracker/SiStripDigitizer/plugins/DigiSimLinkProducer.cc
//   std::cout << "TrackerHits has " << TrackerHits.sizeSignal() << " signal and " << TrackerHits.sizePileup() << " pileup hits " << std::endl;
    
    //Loop on PSimHit and generate the detID -> PSimHit vector map
  SimHitMap.clear();
  MixCollection<PSimHit>::iterator isim;
  for (isim=allTrackerHits->begin(); isim!= allTrackerHits->end();isim++) {
    SimHitMap[(*isim).detUnitId()].push_back((*isim));
  }

  /////////////////////////
  // Cluster collections //
  /////////////////////////
  Handle< edmNew::DetSetVector<SiStripCluster> > dsv_SiStripCluster;
  iEvent.getByLabel(theClusterSourceLabel, dsv_SiStripCluster);

  iEvent.getByLabel("simSiStripDigis", stripdigisimlink);

  edm::ESHandle<TrackerGeometry> tkgeom;
  iSetup.get<TrackerDigiGeometryRecord>().get( tkgeom );
  if (!tkgeom.isValid()) {
    std::cout << "Unable to find TrackerDigiGeometryRecord in event!";
    return;
  }
  const TrackerGeometry &tracker(*tkgeom);

  // Loop over subdetectors
  int clusterCount = 0;
  int clustersNoDigiSimLink = 0;
  for(edmNew::DetSetVector<SiStripCluster>::const_iterator DSViter=dsv_SiStripCluster->begin();
      DSViter != dsv_SiStripCluster->end(); DSViter++ ) {

    uint32_t detID = DSViter->id();
    DetId theDet(detID);
    int subDet = theDet.subdetId();

//     unsigned int subDetOffset(0);
//     for (std::vector<std::pair<int,int>>::iterator it = simHitMap.begin(); it != simHitMap.end(); ++it)
//       if((*it).first == subDet) subDetOffset = (*it).second;
//     std::cout << "subDet, offset = " << subDet << ", " << subDetOffset << std::endl;

    const StripGeomDetUnit* DetUnit = 0;
    DetUnit = (const StripGeomDetUnit*) tracker.idToDetUnit(theDet);
    float thickness = 0;
    if (DetUnit != 0) thickness = DetUnit->surface().bounds().thickness();
    int layer = 0;
    int stereo = 0;
    if (subDet == int(StripSubdetector::TIB)) {
      TIBDetId tibId(detID);
      layer = tibId.layer();
      if (tibId.isStereo()) stereo = 1;
    }
    if (printOut_ > 0) printDetInfo(detID, tracker);

    LocalPoint locVtx = DetUnit->toLocal(GlobalPoint(pixPriVtx.X(), pixPriVtx.Y(), pixPriVtx.Z()));
//     LocalPoint locVtx = DetUnit->toLocal(GlobalPoint(0., 0., zv));
    float modPathLength = fabs(thickness*locVtx.mag()/locVtx.z());
    if (printOut_ > 0) {
      std::cout << "  Module at " << DetUnit->position() << std::endl;
      std::cout << "  PriVtx at " << locVtx;  printf("%s%7.4f%s%4d%s\n", " path ", modPathLength, ", ", DSViter->size(), " clusters");
    }

    edm::DetSetVector<StripDigiSimLink>::const_iterator isearch = stripdigisimlink->find(detID);

    // Traverse the clusters for this subdetector
    for(edmNew::DetSet<SiStripCluster>::const_iterator ClusIter= DSViter->begin();
	ClusIter!=DSViter->end();ClusIter++) {

      clusterCount++;
      const SiStripCluster* clust = ClusIter;

      std::vector<uint8_t> amp=clust->amplitudes();
      int clusiz = amp.size();
      int first  = clust->firstStrip();
      int last   = first + clusiz;
      float charge = 0;
      bool saturates = false;
      for (int i=0; i<clusiz; ++i) {
	charge+=amp[i];
	if (amp[i] == 254 || amp[i] == 255) saturates = true;
      }
      if (printOut_ > 0) {
	std::cout << "Cluster (width, first, last) = (" << clusiz << ", " << first << ", " << last-1 << ")  charge = " << charge;
	if (saturates) std::cout << "  (saturates)";
	std::cout << endl;
      }
      float clusEloss = 0;
      int tkFlip = 0;
      int ovlap = 0;
      std::vector<unsigned int> trackID;  trackID.clear();

      // Set up to find matching simTracks and simHits
      std::vector<PSimHit> detIDhits;
      detIDhits.clear();
      std::vector<std::vector<PSimHit>::const_iterator> onClusterHits;
      onClusterHits.clear();
      std::map<unsigned int, std::vector<PSimHit> >::const_iterator it = SimHitMap.find(detID);
      if (it!= SimHitMap.end()) {
	detIDhits = it->second;
      } else {
        /// Check if it's the gluedDet   
	std::map<unsigned int, std::vector<PSimHit> >::const_iterator itrphi = SimHitMap.find(detID+2); //iterator to the simhit in the rphi module
	std::map<unsigned int, std::vector<PSimHit> >::const_iterator itster = SimHitMap.find(detID+1); //iterator to the simhit in the stereo module
	if (itrphi!= SimHitMap.end()&&itster!=SimHitMap.end()) {
	  detIDhits = itrphi->second;
	  detIDhits.insert(detIDhits.end(),(itster->second).begin(),(itster->second).end());
	}
      }
      std::vector<unsigned int> hitProcess;
      std::vector<int> hitPID;
      std::vector<float> trackCharge;
      std::vector<float> hitPmag;
      std::vector<float> hitPathLength;

      // Look for a digisimlink matching this cluster
      if(isearch == stripdigisimlink->end()) {
	clustersNoDigiSimLink++;
	if (printOut_ > 0) std::cout << "No digisimlinks for this module" << std::endl;
      } else {
	int prevIdx = -1;
	edm::DetSet<StripDigiSimLink> link_detset = (*isearch);
        for(edm::DetSet<StripDigiSimLink>::const_iterator linkiter = link_detset.data.begin();
	    linkiter != link_detset.data.end(); linkiter++){
	  int stripIdx;
	  if (printOut_ > 3) printf("  %s%4d%s\n", "channel = ", linkiter->channel(), " before matching to cluster");
          if( (int)(linkiter->channel()) >= first  && (int)(linkiter->channel()) < last ){
	    // This digisimlink points to a strip in the current cluster
// 	    unsigned int currentCFPos = linkiter->CFposition()-1 + subDetOffset;
	    stripIdx = (int)linkiter->channel()-first;
	    uint16_t rawAmpl = (uint16_t)(amp[stripIdx]);
	    if (printOut_ > 1)
	      printf("  %s%4d%s%8d%s%8d%s%8d%s%8.4f%s%5d\n", "channel = ", linkiter->channel(),
		     " TrackID = ", linkiter->SimTrackId(), " EventID = ", linkiter->eventId().rawId(),
		     " CFPos-1 = ", linkiter->CFposition()-1, " fraction = ", linkiter->fraction(),
		     " rawAmpl = ", rawAmpl);

	    unsigned int thisTrackID = linkiter->SimTrackId();
	    // Does at least one strip have >1 track?
	    if (stripIdx == prevIdx) ovlap = 1;
            // Have we seen this track yet?
	    bool newTrack = true;
	    if (std::find(trackID.begin(), trackID.end(), thisTrackID) != trackID.end()) newTrack = false;
	    if (newTrack) {
	      // This is the first time we've encountered this track (linked to this cluster)
	      trackID.push_back(thisTrackID);

	      // Find all the PSimHits associated with this simTrack
	      for (std::vector<PSimHit>::const_iterator simHitIter = detIDhits.begin(); simHitIter != detIDhits.end(); ++simHitIter) {
		const PSimHit ihit = *simHitIter;
		unsigned int simHitid = ihit.trackId();
		EncodedEventId simHiteid = ihit.eventId();
	
		if(simHitid == thisTrackID && simHiteid == linkiter->eventId()) {
		  // Found a simHit associated with this simTrack
		  onClusterHits.push_back(simHitIter);
		  unsigned short thisHitProcess = ihit.processType();
		  clusEloss += ihit.energyLoss();
		  hitProcess.push_back(thisHitProcess);
		  hitPID.push_back(ihit.particleType());
		  hitPmag.push_back(ihit.pabs());
		  Local3DPoint entry = ihit.entryPoint();
		  Local3DPoint exit = ihit.exitPoint();
		  Local3DVector segment = exit - entry;
		  hitPathLength.push_back(segment.mag());
		  if (printOut_ > 1) printf("    %s%3d%s%8.4f\n", "Process = ", ihit.processType(),
					    ",                  segment = ", segment.mag());
		}  // simHit matches current track
	      } //  end traverse simHits
	      trackCharge.push_back(linkiter->fraction()*rawAmpl);
	    } else {
	      for (unsigned int i=0; i<trackID.size(); ++i)
		if (trackID[i] == thisTrackID)
		  trackCharge[i] += linkiter->fraction()*rawAmpl;
	    } // if newTrack ... else
	    if (printOut_ > 2) {
	      std::cout << "    Track charge accumulator = ";
	      for (unsigned int it = 0; it < trackCharge.size(); ++it) printf("%7.1f  ", trackCharge[it]);
	      std::cout << std::endl;
	    }
	    prevIdx = stripIdx;
	  }  // DigiSimLink belongs to this cluster
	}  // Traverse DigiSimLinks
	if (ovlap && trackID[1] < trackID[0]) tkFlip = 1;

// RecoTracker/DeDx/python/dedxDiscriminator_Prod_cfi.py, line 12 -- MeVperADCStrip = cms.double(3.61e-06*250)

      // Fill the cluster Ntuple
	clusNtp_.subDet = subDet;
        clusNtp_.thickness = thickness;
        clusNtp_.width = amp.size();
        clusNtp_.NsimHits = onClusterHits.size();
        clusNtp_.firstProcess = hitProcess.size() > 0 ? hitProcess[0] : 0;
        clusNtp_.secondProcess = hitProcess.size() > 1 ? hitProcess[1] : 0;
        clusNtp_.thirdProcess = hitProcess.size() > 2 ? hitProcess[2] : 0;
        clusNtp_.fourthProcess = hitProcess.size() > 3 ? hitProcess[3] : 0;
        clusNtp_.firstPID = hitPID.size() > 0 ? hitPID[0] : 0;
        clusNtp_.secondPID = hitPID.size() > 1 ? hitPID[1] : 0;
        clusNtp_.thirdPID = hitPID.size() > 2 ? hitPID[2] : 0;
        clusNtp_.fourthPID = hitPID.size() > 3 ? hitPID[3] : 0;
        clusNtp_.firstPmag = hitPmag.size() > 0 ? hitPmag[0] : 0;
        clusNtp_.secondPmag = hitPmag.size() > 1 ? hitPmag[1] : 0;
        clusNtp_.thirdPmag = hitPmag.size() > 2 ? hitPmag[2] : 0;
        clusNtp_.fourthPmag = hitPmag.size() > 3 ? hitPmag[3] : 0;
        clusNtp_.firstPathLength = hitPathLength.size() > 0 ? hitPathLength[0]: 0;
        clusNtp_.secondPathLength = hitPathLength.size() > 1 ? hitPathLength[1]: 0;
        clusNtp_.thirdPathLength = hitPathLength.size() > 2 ? hitPathLength[2]: 0;
        clusNtp_.fourthPathLength = hitPathLength.size() > 3 ? hitPathLength[3]: 0;
        clusNtp_.pathLstraight = modPathLength;
        float allHtPathLength = 0;
        for (unsigned int ih=0; ih<hitPathLength.size(); ++ih)
	  allHtPathLength += hitPathLength[ih];
        clusNtp_.allHtPathLength = allHtPathLength;
	clusNtp_.Ntp = trackID.size();
	if (printOut_ > 0 && trackCharge.size() == 2)
  	  cout << "  charge 1st, 2nd, dE/dx 1st, 2nd, asymmetry = "
               << trackCharge[0] << "  "
               << trackCharge[1] << "  "
               << 3.36e-4*trackCharge[0]/modPathLength << "  "
               << 3.36e-4*trackCharge[1]/modPathLength << "  "
  	       << (trackCharge[0]-trackCharge[1]) / (trackCharge[0]+trackCharge[1]) 
               << "  " << tkFlip << endl;
        clusNtp_.firstTkChg = trackCharge.size() > 0 ? trackCharge[0] : 0;
        clusNtp_.secondTkChg = trackCharge.size() > 1 ? trackCharge[1] : 0;
        clusNtp_.thirdTkChg = trackCharge.size() > 2 ? trackCharge[2] : 0;
        clusNtp_.fourthTkChg = trackCharge.size() > 3 ? trackCharge[3] : 0;
        clusNtp_.charge = charge;
        clusNtp_.Eloss = clusEloss;
        clusNtp_.sat = saturates ? 1 : 0;
        clusNtp_.tkFlip = tkFlip;
        clusNtp_.ovlap = ovlap;
        clusNtp_.layer = layer;
        clusNtp_.stereo = stereo;
        clusTree_->Fill();
      }  // DigiSimLinks present for this cluster
    }  // traverse clusters in subdetector
  }  // traverse subdetectors
//   cout << clusterCount << " total clusters; " << clustersNoDigiSimLink << " without digiSimLinks" << endl;
}


// ------------ method called once each job just before starting event loop  ------------
void 
ClusterNtuplizer::beginJob()
{
  int bufsize = 64000;
  edm::Service<TFileService> fs;
  clusTree_ = fs->make<TTree>("ClusterNtuple", "Cluster analyzer ntuple");
  clusTree_->Branch("cluster", &clusNtp_, "subDet/I:thickness/F:width/I:NsimHits:firstProcess:secondProcess:thirdProcess:fourthProcess:firstPID:secondPID:thirdPID:fourthPID:Ntp:firstTkChg/F:secondTkChg:thirdTkChg/F:fourthTkChg:charge:firstPmag:secondPmag:thirdPmag:fourthPmag:firstPathLength:secondPathLength:thirdPathLength:fourthPathLength:pathLstraight:allHtPathLength:Eloss:sat/I:tkFlip:ovlap:layer:stereo", bufsize);
  pvTree_ = fs->make<TTree>("pVertexNtuple", "Pixel vertex ntuple");
  pvTree_->Branch("pVertex", &pvNtp_, "isValid/I:isFake:Ntrks:nDoF:chisq/F:xV:yV:zV:xVsig:yVsig:zVsig", bufsize);

  hNpv = fs->make<TH1F>("hNpv", "No. of pixel vertices", 40, 0, 40);
  hzV_Iev = fs->make<TH2F>("hzV_Iev", "Zvertex vs event index", 20, -10, 10, 100, 0, 100);
  hNtrk_zVerrPri = fs->make<TH2F>("hzVerr_NtrkPri", "Ntracks vs Zvertex error, primary", 50, 0, 0.025, 30, 0, 150);
  hNtrk_zVerrSec = fs->make<TH2F>("hzVerr_NtrkSec", "Ntracks vs Zvertex error, secondary", 50, 0, 0.025, 30, 0, 150);
  hZvPri = fs->make<TH1F>("hZvPri", "Zvertex, primary", 48, -15, 15);
  hZvSec = fs->make<TH1F>("hZvSec", "Zvertex, secondary", 48, -15, 15);
  evCnt_ = 0;

}

// ------------ method called once each job just after ending the event loop  ------------
void 
ClusterNtuplizer::endJob() {
}

// ------------ Print out some tracker geometry info  ------------
void 
ClusterNtuplizer::printDetInfo(uint32_t detID, const TrackerGeometry& tracker) {
  using namespace std;

  DetId theDet(detID);
  int subDet = theDet.subdetId();
  const StripGeomDetUnit* DetUnit = 0;
  DetUnit = (const StripGeomDetUnit*) tracker.idToDetUnit(theDet);
  float thickness = 0;
  if (DetUnit != 0) thickness = DetUnit->surface().bounds().thickness();
  std::cout << std::endl << "detID = " << detID << ": subdet " << subDet;
//   enum SubDetector { UNKNOWN=0, TIB=3, TID=4, TOB=5, TEC=6 }
  if (subDet == int(StripSubdetector::TIB)) {
    TIBDetId tibId(detID);
    std::cout << ", TIB (layer, module) (" << tibId.layer() << ", " << tibId.module()
	 << ") string [" << tibId.string()[0] << ", " << tibId.string()[1] << ",  " << tibId.string()[2] << "]";
    if (tibId.isRPhi()) std::cout << " RPhi ";
    else if (tibId.isStereo()) std::cout << " Stereo ";
    else std::cout << " Double-sided ";
//     std::cout << ", TIB layer " << tibId.layer() << " module " << tibId.module() << " order " << tibId.order() << " side " << tibId.side();
  } else if (subDet == int(StripSubdetector::TID)) {
    TIDDetId tidId(detID);
    std::cout << ", TID side " << tidId.side() << " wheel " << tidId.wheel() << " ring " << tidId.ring()
	 << " module " << tidId.module()[0] << " " << tidId.module()[1];
  } else if (subDet == int(StripSubdetector::TOB)) {
    TOBDetId tobId(detID);
    std::cout << ", TOB layer " << tobId.layer() << " rod " << tobId.rod()[0] << " " << tobId.rod()[1]
	 << " module " << tobId.module();
  } else if (subDet == int(StripSubdetector::TEC)) {
    TECDetId tecId(detID);
    std::cout << ", TEC side " << tecId.side() << " wheel " << tecId.wheel() << " petal " << tecId.petal()[0]
	 << " " << tecId.petal()[1] << " ring " << tecId.ring() << " module " << tecId.module();
  } else std::cout << " not a siStrip subdetector";
  std::cout << " thickness " << thickness << std::endl;
}

// void ClusterNtuplizer::fillClusNtp(TrackingParticle* tp, double angNnbr, int TrackNumber, int found, int* NinCone) 
// {
//   clusNtp_.p = tp->p();

// }

void ClusterNtuplizer::ClusterStruct::print()
{
//   std::cout << "clusNtp_.p = " << p;
  std::cout << std::endl;
}

void ClusterNtuplizer::ClusterStruct::init()
{
//   float dummy_float = -9999.0;
//   int dummy_int = -9999;

//   p = dummy_float;
}


//define this as a plug-in
DEFINE_FWK_MODULE(ClusterNtuplizer);
