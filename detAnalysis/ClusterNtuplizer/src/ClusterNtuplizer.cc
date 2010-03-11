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
// $Id$
//
//


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

#include "TObject.h"
#include "TH1D.h"
#include "TTree.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"

//Data Formats
#include "DataFormats/Common/interface/DetSet.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
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

//
// class decleration
//

class ClusterNtuplizer : public edm::EDAnalyzer {
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

private:
  std::vector<const SiStripCluster*> vPSiStripCluster;

  edm::Handle<CrossingFrame<PSimHit> > cf_simhit;
  std::vector<const CrossingFrame<PSimHit> *> cf_simhitvec;
  MixCollection<PSimHit>  TrackerHits;
  typedef std::vector<std::string> vstring;
  vstring trackerContainers;
  edm::Handle< edm::DetSetVector<StripDigiSimLink> >  stripdigisimlink;

  TTree* clusTree_;  // tree filled for each selected TrackingParticle
  struct ClusterStruct{
    int subDet;
    float thickness;
    int width;
    int NsimHits;
    int firstProcess;
    int secondProcess;
    int firstPID;
    int secondPID;
    int Ntp;
    float charge;
    float firstPmag;
    float secondPmag;
    float firstPathLength;
    float secondPathLength;
    float Eloss;
    int sat;

    void init();
    void print();
    } clusNtp_;

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
ClusterNtuplizer::ClusterNtuplizer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

}


ClusterNtuplizer::~ClusterNtuplizer()
{
 
   // do anything here that needs to be done at desctruction time
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

  bool printOut = false;
  trackerContainers.clear();
  cf_simhit.clear();
  cf_simhitvec.clear();

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

  for(uint32_t i = 0; i< trackerContainers.size();i++){
    iEvent.getByLabel("mix",trackerContainers[i],cf_simhit);
    cf_simhitvec.push_back(cf_simhit.product());
  }
  
  std::auto_ptr<MixCollection<PSimHit> > allTrackerHits(new MixCollection<PSimHit>(cf_simhitvec));
  TrackerHits = (*allTrackerHits);

  /////////////////////////
  // Cluster collections //
  /////////////////////////
  Handle< edmNew::DetSetVector<SiStripCluster> > dsv_SiStripCluster;
  iEvent.getByLabel("siStripClusters", dsv_SiStripCluster);

  iEvent.getByLabel("simSiStripDigis", stripdigisimlink);

  edm::ESHandle<TrackerGeometry> tkgeom;
  iSetup.get<TrackerDigiGeometryRecord>().get( tkgeom );
  if (!tkgeom.isValid()) {
    cout << "Unable to find TrackerDigiGeometryRecord in event!";
    return;
  }
  const TrackerGeometry &tracker(*tkgeom);

  // Loop over subdetectors
  for(edmNew::DetSetVector<SiStripCluster>::const_iterator DSViter=dsv_SiStripCluster->begin();
      DSViter != dsv_SiStripCluster->end(); DSViter++ ) {

    uint32_t detID = DSViter->id();
    DetId theDet(detID);
    int subDet = theDet.subdetId();
    const StripGeomDetUnit* DetUnit = 0;
    DetUnit = (const StripGeomDetUnit*) tracker.idToDetUnit(theDet);
    float thickness = 0;
    if (DetUnit != 0) thickness = DetUnit->surface().bounds().thickness();
    if (printOut) printDetInfo(detID, tracker);

    edm::DetSetVector<StripDigiSimLink>::const_iterator isearch = stripdigisimlink->find(detID);

    // Traverse the clusters for this subdetector
    for(edmNew::DetSet<SiStripCluster>::const_iterator ClusIter= DSViter->begin();
	ClusIter!=DSViter->end();ClusIter++) {
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
      float clusEloss = 0;
      std::vector<unsigned int> trackID;
      std::vector<unsigned int> CFpos;
      std::vector<unsigned int> CFcache;
      std::vector<unsigned int> hitProcess;
      std::vector<int> hitPID;
      std::vector<float> hitPmag;
      std::vector<float> hitPathLength;
//       std::vector<float> hitEloss;
      if(isearch == stripdigisimlink->end()) {
	if (printOut) cout << "No digisimlinks for this module" << std::endl;
      } else {
	edm::DetSet<StripDigiSimLink> link_detset = (*isearch);
        for(edm::DetSet<StripDigiSimLink>::const_iterator linkiter = link_detset.data.begin();
	    linkiter != link_detset.data.end(); linkiter++){
          if( (int)(linkiter->channel()) >= first  && (int)(linkiter->channel()) < last ){
	    unsigned int currentCFPos = linkiter->CFposition()-1;
	    int stripIdx = (int)linkiter->channel()-first;
	    uint16_t rawAmpl = (uint16_t)(amp[stripIdx]);
	    float stripEloss = TrackerHits.getObject(currentCFPos).energyLoss();
	    unsigned short thisHitProcess = TrackerHits.getObject(currentCFPos).processType();
	    if (printOut)
	      printf("%s%4d%s%5d%s%8d%s%8d%s%3d%s%8.4f\n", "CHANNEL = ", linkiter->channel(), " Ampl = ", rawAmpl,
		     " TrackID = ", linkiter->SimTrackId(), " CFPos-1 = ", currentCFPos, " Process = ",
		     thisHitProcess, " fraction = ", linkiter->fraction());
	    clusEloss += stripEloss;
	    unsigned int thisTrackID = linkiter->SimTrackId();
            // Have we seen this track yet?
	    bool newTrack = true;
	    if (std::find(trackID.begin(), trackID.end(), thisTrackID) != trackID.end()) newTrack = false;
	    if (newTrack) trackID.push_back(thisTrackID);
	    bool newHit = true;
	    if (std::find(CFcache.begin(), CFcache.end(), currentCFPos) != CFcache.end()) newHit = false;
	    if (newHit) {
	      CFcache.push_back(currentCFPos);
// 	      if (TrackerHits.getObject(currentCFPos).particleType() != 22) {  // exclude photons
		CFpos.push_back(currentCFPos);
		hitProcess.push_back(thisHitProcess);
		hitPID.push_back(TrackerHits.getObject(currentCFPos).particleType());
		hitPmag.push_back(TrackerHits.getObject(currentCFPos).pabs());
		Local3DPoint entry = TrackerHits.getObject(currentCFPos).entryPoint();
		Local3DPoint exit = TrackerHits.getObject(currentCFPos).exitPoint();
		Local3DVector segment = exit - entry;
		hitPathLength.push_back(segment.mag());
// 	      }
	    }
	  }
	}
      }

// RecoTracker/DeDx/python/dedxDiscriminator_Prod_cfi.py, line 12 -- MeVperADCStrip = cms.double(3.61e-06*250)

      // Fill the Ntuple
//       clusNtp_.init();
//       fillClusNtp();
      clusNtp_.subDet = subDet;
      clusNtp_.thickness = thickness;
      clusNtp_.width = amp.size();
      clusNtp_.NsimHits = CFpos.size();
      clusNtp_.firstProcess = hitProcess.size() > 0 ? hitProcess[0] : 0;
      clusNtp_.secondProcess = hitProcess.size() > 1 ? hitProcess[1] : 0;
      clusNtp_.firstPID = hitPID.size() > 0 ? hitPID[0] : 0;
      clusNtp_.secondPID = hitPID.size() > 1 ? hitPID[1] : 0;
      clusNtp_.firstPmag = hitPmag.size() > 0 ? hitPmag[0] : 0;
      clusNtp_.secondPmag = hitPmag.size() > 1 ? hitPmag[1] : 0;
      clusNtp_.firstPathLength = hitPathLength.size() > 0 ? hitPathLength[0]: 0;
      clusNtp_.secondPathLength = hitPathLength.size() > 1 ? hitPathLength[1]: 0;
      clusNtp_.Ntp = trackID.size();
      clusNtp_.charge = charge;
      clusNtp_.Eloss = clusEloss;
      if (saturates) clusNtp_.sat = 1;  else clusNtp_.sat = 0;
      clusTree_->Fill();
    }  // traverse clusters in subdetector
  }  // traverse subdetectors
}


// ------------ method called once each job just before starting event loop  ------------
void 
ClusterNtuplizer::beginJob()
{
  int bufsize = 64000;
  edm::Service<TFileService> fs;
  clusTree_ = fs->make<TTree>("ClusterNtuple", "Cluster analyzer ntuple");
  //  std::cout << "Making cluster branch:" << std::endl;
  clusTree_->Branch("cluster", &clusNtp_, "subDet/I:thickness/F:width/I:NsimHits:firstProcess:secondProcess:firstPID:secondPID:Ntp:charge/F:firstPmag:secondPmag:firstPathLength:secondPathLength:Eloss:sat/I", bufsize);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ClusterNtuplizer::endJob() {
}

void 
ClusterNtuplizer::printDetInfo(uint32_t detID, const TrackerGeometry& tracker) {
  using namespace std;

  DetId theDet(detID);
  int subDet = theDet.subdetId();
  const StripGeomDetUnit* DetUnit = 0;
  DetUnit = (const StripGeomDetUnit*) tracker.idToDetUnit(theDet);
  float thickness = 0;
  if (DetUnit != 0) thickness = DetUnit->surface().bounds().thickness();
  cout << "detID = " << detID << ": subdet " << subDet;
//   enum SubDetector { UNKNOWN=0, TIB=3, TID=4, TOB=5, TEC=6 }
  if (subDet == int(StripSubdetector::TIB)) {
    TIBDetId tibId(detID);
    cout << ", TIB layer " << tibId.layer() << " module " << tibId.module();
  } else if (subDet == int(StripSubdetector::TID)) {
    TIDDetId tidId(detID);
    cout << ", TID side " << tidId.side() << " wheel " << tidId.wheel() << " ring " << tidId.ring()
	 << " module " << tidId.module()[0] << " " << tidId.module()[1];
  } else if (subDet == int(StripSubdetector::TOB)) {
    TOBDetId tobId(detID);
    cout << ", TOB layer " << tobId.layer() << " rod " << tobId.rod()[0] << " " << tobId.rod()[1]
	 << " module " << tobId.module();
  } else if (subDet == int(StripSubdetector::TEC)) {
    TECDetId tecId(detID);
    cout << ", TEC side " << tecId.side() << " wheel " << tecId.wheel() << " petal " << tecId.petal()[0]
	 << " " << tecId.petal()[1] << " ring " << tecId.ring() << " module " << tecId.module();
  } else cout << " not a siStrip subdetector";
  cout << " thickness " << thickness << endl;
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
