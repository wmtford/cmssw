// -*- C++ -*-
//
// Package:    SplitClustersProducer
// Class:      SplitClustersProducer
// 
/**\class SplitClustersProducer SplitClustersProducer.cc wtfRecoLocalTracker/SplitClustersProducer/src/SplitClustersProducer.cc

 Description: Split SiStrip clusters from overlap tracks

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Marco Cardaci
//         Created:  Sun Sep 21 15:22:40 CEST 2008
//         Updated:  Sep 2009 (release 3.1.X) wtford
// $Id: SplitClustersProducer.cc,v 1.1 2011/06/01 22:47:02 wtford Exp $
//
//

// this class header
#include "wtfRecoLocalTracker/SplitClustersProducer/interface/SplitClustersProducer.h"

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Data Formats
#include "DataFormats/Common/interface/DetSet.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
// #include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/SiStripCluster/interface/SiStripClusterCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2DCollection.h"
#include "DataFormats/Common/interface/OwnVector.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/ProjectedSiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
// #include "DataFormats/VertexReco/interface/Vertex.h"
// #include "DataFormats/VertexReco/interface/VertexFwd.h"

// For Pixel RecHits
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"

//TrackAssociator 
#include "SimTracker/TrackAssociation/interface/TrackAssociatorByHits.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
 
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/GeometryVector/interface/LocalPoint.h"

//needed for the geometry:
#include "CommonTools/TrackerMap/interface/TrackerMap.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"  
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetType.h"
// #include "Geometry/CommonTopologies/interface/StripTopology.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h" 

#include "DataFormats/DetId/interface/DetId.h"

#include "SimDataFormats/TrackerDigiSimLink/interface/StripDigiSimLink.h"

//For PSimHit

//#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
//#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"



#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH2I.h"

//
// member functions
//

// ------------ method called to produce the data  ------------
void
SplitClustersProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  // using namespace reco;
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

  // get the beam spot
  edm::Handle<reco::BeamSpot> recoBeamSpotHandle;
//   edm::InputTag bsSrc          = conf_.getParameter<edm::InputTag>("beamSpot");
//   iEvent.getByLabel(bsSrc,recoBeamSpotHandle);
  iEvent.getByLabel("hltOfflineBeamSpot",recoBeamSpotHandle);
  const reco::BeamSpot& bs = *recoBeamSpotHandle;      

  //
  //  Primary vertex from pixels
  //
  // Some code from DPGAnalysis/SiStripTools/plugins/TrackerDpgAnalysis.cc (see also around line 804)
  // load pixel vertices
  // Pixel vertices are handled as primary vertices, but not linked to tracks.
  edm::Handle<reco::VertexCollection>  pixelVertexCollectionHandle;
//   iEvent.getByLabel(pixelVertexLabel_, pixelVertexCollectionHandle);
  iEvent.getByLabel("pixelVertices", pixelVertexCollectionHandle);
  const reco::VertexCollection pixelVertexColl = *(pixelVertexCollectionHandle.product());
//   reco::Vertex::Point pixPriVtx(0, 0, 0);
//   reco::Vertex::Point pixPriVtx(bs.x0(), bs.y0(), bs.z0());
  reco::Vertex::Point pixPriVtx(bs.position());
  iniVertex(pixelVertexColl, pixPriVtx);
//   std::cout << "beamSpot " << bs.position() << "  priVtx " << pixPriVtx << std::endl;
 

  /////////////////////////
  // Cluster collections //
  /////////////////////////
  Handle< edmNew::DetSetVector<SiStripCluster> > dsv_SiStripCluster;
  iEvent.getByLabel("siStripClusters", dsv_SiStripCluster);
//   std::cout << "No. of detIDs " << dsv_SiStripCluster->size() << std::endl;

  /////////////////////////
  // RecHits collections //
  /////////////////////////
  edm::Handle<SiStripMatchedRecHit2DCollection> rechitsmatched;
  edm::Handle<SiStripRecHit2DCollection> rechitsrphi;
  edm::Handle<SiStripRecHit2DCollection> rechitsstereo;
  edm::Handle<SiPixelRecHitCollection> pixelrechits;
  iEvent.getByLabel("siStripMatchedRecHits","matchedRecHit", rechitsmatched);
  iEvent.getByLabel("siStripMatchedRecHits","rphiRecHit", rechitsrphi);
  iEvent.getByLabel("siStripMatchedRecHits","stereoRecHit", rechitsstereo);
  iEvent.getByLabel("siPixelRecHits",pixelrechits);
  hitAssociator = new TrackerHitAssociator(iEvent);

  iEvent.getByLabel("simSiStripDigis", stripdigisimlink);

  edm::ESHandle<TrackerGeometry> tkgeom;
  iSetup.get<TrackerDigiGeometryRecord>().get( tkgeom );
  const TrackerGeometry &tracker(*tkgeom);

  // LOOP on DetSetVector<SiStripCluster> to get cluster and fill the split ones
  int iclusCnt = 0;
  auto_ptr< edmNew::DetSetVector<SiStripCluster> > splitSiStripClusters(new edmNew::DetSetVector<SiStripCluster>());
  splitSiStripClusters->reserve(10000,4*10000); //FIXME
  // Loop over sensors
  for(edmNew::DetSetVector<SiStripCluster>::const_iterator DSViter=dsv_SiStripCluster->begin(); DSViter != dsv_SiStripCluster->end(); DSViter++ ) {

    iclusCnt += DSViter->size();
  
    uint32_t detID=DSViter->id();
//     std::cout << "  detID " << detID << " No. of clusters " << DSViter->size() << std::endl;

    // DetSetVector to contain the clusters we produce
    edmNew::DetSetVector<SiStripCluster>::FastFiller ssc(* splitSiStripClusters, DSViter->id());

    //
    // Check if we want to apply cluster splitting to this detector
    //
    bool skipThisLayer = false;
    DetId theDet(detID);
    int subDet = theDet.subdetId();
    const StripGeomDetUnit* DetUnit = 0;
    DetUnit = (const StripGeomDetUnit*) tracker.idToDetUnit(theDet);
    if (subDet == int(StripSubdetector::TIB)) {
      TIBDetId tibId(detID);
      if (tibId.layer() > maxLayerTIB_) skipThisLayer = true; 
    } else if (subDet == int(StripSubdetector::TID)) {
      TIDDetId tidId(detID);
      if (tidId.wheel() > maxWheelTID_) skipThisLayer = true;
    } else if (subDet == int(StripSubdetector::TOB)) {
      TOBDetId tobId(detID);
      if (tobId.layer() > maxLayerTOB_) skipThisLayer = true;
    } else if (subDet == int(StripSubdetector::TEC)) {
      TECDetId tecId(detID);
      if (tecId.wheel() > maxWheelTEC_) skipThisLayer = true;
    }
    if (splitBy == SplitClustersAlgos::noSplit || skipThisLayer) {
      // We don't want to split clusters in this sensor; just store them in the output DetSetVector
      // Traverse the clusters for this sensor
      for(edmNew::DetSet<SiStripCluster>::const_iterator ClusIter= DSViter->begin(); ClusIter!=DSViter->end();ClusIter++) {
	const SiStripCluster* clust = ClusIter;
	std::vector<uint8_t> amp=clust->amplitudes();
	std::vector<uint16_t> amp_temp;
	for(size_t j=0;j<amp.size();++j) amp_temp.push_back(amp[j]);
	SiStripCluster* newCluster = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), amp_temp.begin(), amp_temp.end() );
	ssc.push_back(SiStripCluster( *newCluster ));
      }
      continue;
    }

    float thePathLength = straightPathlength(pixPriVtx, tracker, detID);
    edm::DetSetVector<StripDigiSimLink>::const_iterator isearch = stripdigisimlink->find(detID);

    // Insert the DetSet<SiStripCluster> in the  DetSetVec<SiStripCluster>

    // Traverse the clusters for this sensor
    for(edmNew::DetSet<SiStripCluster>::const_iterator ClusIter= DSViter->begin(); ClusIter!=DSViter->end();ClusIter++) {
      const SiStripCluster* clust = ClusIter;
//       dumpDigiSimLinks(detID, clust);  continue;

      std::vector<uint8_t> amp=clust->amplitudes();
      int clusiz = amp.size();
      float charge = 0;
      bool saturates = false;
      for (int i=0; i<clusiz; ++i) {
	charge+=amp[i];
	if (amp[i] == 254 || amp[i] == 255) saturates = true;
      }
      associatedIdpr.clear();
      associatedA.clear();
      hitAssociator->associateSimpleRecHitCluster(clust, associatedIdpr, associatedA);

//       vector<PSimHit>::const_iterator simhitsIter = associatedA.begin();
//       Local3DPoint entry = simhitsIter->entryPoint();
//       Local3DPoint exit =  simhitsIter->exitPoint();
//       Local3DVector segment = exit - entry;
//       float normCharge = .0003*charge/max(float(1.e-6), segment.mag());

      float perDx = MIPperADC_ / max(float(1.e-6), thePathLength);
      float normCharge = charge*perDx;

      size_t splittableClusterSize = 0;
      if (splitBy == SplitClustersAlgos::byHits) {
        splittableClusterSize = associatedA.size();
      } else if (splitBy == SplitClustersAlgos::byTracks) {
        splittableClusterSize = associatedIdpr.size();
      } else if (splitBy == SplitClustersAlgos::noSplit) {
        splittableClusterSize = 0;
      } else std::cout << "SplitClustersProducer:  Invalid splitBy value" << std::endl;

      // Fill the vector of SimHits associated with this Cluster

//    std::cout << "Tracks/cluster = " << splittableClusterSize << " saturates = " << saturates << " normCharge = " << normCharge << std::endl;
      if(splittableClusterSize > 1 && amp.size()>2 && !saturates && normCharge > minNormChargeToSplit_) {

        // We have a cluster that meets the criteria for splitting

// 	std::cout << "\tsplitting cluster, normChg = " << normCharge << std::endl;

	int first  = clust->firstStrip();
        int last   = first + clusiz;
        uint16_t rawAmpl = 0, currentAmpl = 0;

        bool first_link = false;
        bool first_firstStrip1 = false;
        bool first_firstStrip2 = false;
        int first_CFpos = 0;
        std::vector<uint16_t> tmp1, tmp2;
        int firstStrip1 = 9999;
        int firstStrip2 = 9999;

        std::vector<int> firstStrip;
        std::vector<bool> trackInStrip;
        std::vector<unsigned int> trackID;
        std::vector<float> trackFraction;
        std::vector< std::vector<uint16_t> > trackAmp;
        unsigned int currentChannel(9999);
        unsigned int thisTrackID = 0;

        if(isearch != stripdigisimlink->end()) {
	  edm::DetSet<StripDigiSimLink> link_detset = (*isearch);
	  if (printOut) std::cout << "detID = " << detID << std::endl;
	  for(edm::DetSet<StripDigiSimLink>::const_iterator linkiter = link_detset.data.begin();
	      linkiter != link_detset.data.end(); linkiter++){
	    if( (int)(linkiter->channel()) >= first  && (int)(linkiter->channel()) < last ){
	      int currentCFPos = linkiter->CFposition()-1;
	      int stripIdx = (int)linkiter->channel()-first;
	      rawAmpl = (uint16_t)(amp[stripIdx]);
	      if (printOut)
		printf("%s%4d%s%5d%s%8d%s%8d%s%3d%s%8.4f\n", "CHANNEL = ", linkiter->channel(), " Ampl = ", rawAmpl,
		       " TrackID = ", linkiter->SimTrackId(), " CFPos-1 = ", currentCFPos, " Process = ",
		       TrackerHits.getObject(currentCFPos).processType(), " fraction = ", linkiter->fraction());

	      if (splitBy == SplitClustersAlgos::byHits) {

		if (first_link == false) {
		  first_CFpos = currentCFPos;
		  first_link = true;
		}
		uint16_t thisAmpl;
		if ((thisAmpl=rawAmpl) < 254) thisAmpl = min(uint16_t(253), max(uint16_t(0), (uint16_t)(rawAmpl*linkiter->fraction()+0.5)));
		if(currentCFPos == first_CFpos) {
		  tmp1.push_back(thisAmpl);
		  if(!first_firstStrip1) {
		    firstStrip1 = linkiter->channel();
		    first_firstStrip1 = true;
		  }
		} else {
		  tmp2.push_back(thisAmpl);
		  if(first_firstStrip2 == false) {
		    firstStrip2 = linkiter->channel();
		    first_firstStrip2 = true;
		  }
		}

	      } else if (splitBy == SplitClustersAlgos::byTracks) {

	      // DigiSimLinks are ordered first by channel; there can be > 1 track, and > 1 simHit for each track

		if (linkiter->channel() != currentChannel) {
	          // New strip; store amplitudes for the previous one
		  uint16_t thisAmpl;
		  for (size_t i=0; i<trackID.size(); ++i) {
		    if (trackInStrip[i]) {
		      if ((thisAmpl=currentAmpl) < 254)
			thisAmpl = min(uint16_t(253), max(uint16_t(0), (uint16_t)(currentAmpl*trackFraction[i]+0.5)));
		      trackAmp[i].push_back(thisAmpl);
		    }
		    trackFraction[i] = 0;
		    trackInStrip[i] = false;
		  }
		  currentChannel = linkiter->channel();
		  currentAmpl = rawAmpl;
		}

                // Now deal with this new DigiSimLink
		thisTrackID = linkiter->SimTrackId();
                // Have we seen this track yet?
		bool newTrack = true;
		int thisTrackIdx = 9999;
		for (size_t i=0; i<trackID.size(); ++i) {
		  if (trackID[i] == thisTrackID) {
		    thisTrackIdx = i;
		    newTrack = false;
		  }
		}
		if (newTrack) {
		  trackInStrip.push_back(false);  // We'll set it true below
		  trackID.push_back(thisTrackID);
		  firstStrip.push_back(currentChannel);
		  std::vector<uint16_t> ampTmp;
		  trackAmp.push_back(ampTmp);
		  trackFraction.push_back(0);
		  thisTrackIdx = trackID.size()-1;
		}
		trackInStrip[thisTrackIdx] = true;
		trackFraction[thisTrackIdx] += linkiter->fraction();
		currentAmpl = rawAmpl;
	      } else {};
	    }
	  }  // end of loop over DigiSimLinks

	  if (splitBy == SplitClustersAlgos::byHits) {
	    SiStripCluster* newCluster1 = new SiStripCluster( clust->geographicalId(), firstStrip1, tmp1.begin(), tmp1.end() );
	    SiStripCluster* newCluster2 = new SiStripCluster( clust->geographicalId(), firstStrip2, tmp2.begin(), tmp2.end() );

            if (printOut || firstStrip1 < first || firstStrip1 >= last || firstStrip2 < first
		|| firstStrip2 >= last || tmp1.size() <= 0 || tmp2.size() <= 0)
	      dumpSimTracks(hitAssociator, clust, newCluster1, newCluster2, splitBy);

//             // Check if there are clusters with all amplitudes = 0
// 	    bool tmp1_check = false;
// 	    if(tmp1.size() > 0){ for(size_t j=0;j<tmp1.size();++j){ if(tmp1[j] >0){ tmp1_check = true; }}}
// 	    bool tmp2_check = false;
// 	    if(tmp2.size() > 0){ for(size_t j=0;j<tmp2.size();++j){ if(tmp2[j] >0){ tmp2_check = true; }}}

            // Exclude clusters with firstStrip uninitialized, size of the vector of amplitudes =< 0 and clusters with charge below threshold
// 	    if(firstStrip1 != 9999 && tmp1.size() > 0 && tmp1_check == true){ssc.push_back(SiStripCluster( *newCluster1 ));
	    float clusterAmp = 0.;
	    for(size_t j=0; j<tmp1.size(); ++j) clusterAmp += tmp1[j];
	    if ( firstStrip1 != 9999 && tmp1.size() > 0 && clusterAmp*perDx > minNormChargeToKeep_ ) {
	      ssc.push_back(SiStripCluster( *newCluster1 ));
	    } else {
// 	       std::cout << "\t\tRejecting new cluster1, normChg = " << clusterAmp*perDx << std::endl;
	      delete newCluster1;
	    }

// 	    if(firstStrip2 != 9999 && tmp2.size() > 0 && tmp2_check == true){ssc.push_back(SiStripCluster( *newCluster2 ));
	    clusterAmp = 0.;
	    for(size_t j=0; j<tmp2.size(); ++j) clusterAmp += tmp2[j];
	    if ( firstStrip2 != 9999 && tmp2.size() > 0 && clusterAmp*perDx > minNormChargeToKeep_ ) {
	      ssc.push_back(SiStripCluster( *newCluster2 ));
	    } else {
// 	       std::cout << "\t\tRejecting new cluster2, normChg = " << clusterAmp*perDx << std::endl;
	      delete newCluster2;
	    }

	  } else if (splitBy == SplitClustersAlgos::byTracks) {

	    std::vector<SiStripCluster*> newCluster;
	    // Fill amplitudes for the last strip and create a cluster for each track
	    uint16_t thisAmpl;
	    for (size_t i=0; i < trackID.size(); ++i) {
	      if (trackInStrip[i]) {
		if ((thisAmpl=rawAmpl) < 254) thisAmpl = min(uint16_t(253), max(uint16_t(0), (uint16_t)(rawAmpl*trackFraction[i]+0.5)));
		trackAmp[i].push_back(thisAmpl);
	      }
	      SiStripCluster* newClusteri = new SiStripCluster(clust->geographicalId(), firstStrip[i],
							       trackAmp[i].begin(), trackAmp[i].end() );
	      newCluster.push_back(newClusteri);
	    }
            if (printOut || firstStrip[0] < first || firstStrip[0] >= last || firstStrip[1] < first
		|| firstStrip[1] >= last || trackAmp[0].size() <= 0 || trackAmp[1].size() <= 0)
	      dumpSimTracks(hitAssociator, clust, newCluster[0], newCluster[1], splitBy);
	    for (size_t i=0; i < trackID.size(); ++i) {
// 	      bool emptyCluster = true;
// 	      for(size_t j=0; j<trackAmp[i].size(); ++j) if((trackAmp[i])[j] >0) emptyCluster = false;
// 	      if (!emptyCluster && firstStrip[i] != 9999 && trackAmp[i].size() > 0) {
	      float clusterAmp = 0.;
	      for(size_t j=0; j<trackAmp[i].size(); ++j) clusterAmp += (trackAmp[i])[j];
	      if ( firstStrip[i] != 9999 && trackAmp[i].size() > 0 && clusterAmp*perDx > minNormChargeToKeep_ ) {
		ssc.push_back(SiStripCluster( *newCluster[i]));
	      } else {
// 		std::cout << "\t\tRejecting new cluster" << i << ", normChg = " << clusterAmp*perDx << std::endl;
		delete newCluster[i];
	      }
	    }
	  } else {};

	} else {
	  std::vector<uint16_t> amp_temp;
//           std::cout << "Missing digisimlink!!!" << std::endl;
	  for(size_t j=0;j<amp.size();++j) amp_temp.push_back(amp[j]);
	  SiStripCluster* newCluster = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), amp_temp.begin(), amp_temp.end() );
	  ssc.push_back(SiStripCluster( *newCluster ));
	}

      }else {
        // We don't have a splittable cluster; just store cluster in the output DetSetVector
	std::vector<uint16_t> amp_temp;
	for(size_t j=0;j<amp.size();++j) amp_temp.push_back(amp[j]);
	SiStripCluster* newCluster = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), amp_temp.begin(), amp_temp.end() );
	ssc.push_back(SiStripCluster( *newCluster ));
      }
    }  // traverse clusters in subdetector
  }  // traverse subdetectors
 /*
  std::cout << "Number of initial clusters = " << iclusCnt << std::endl;
  int oclusCnt = 0;
  for(edmNew::DetSetVector<SiStripCluster>::const_iterator ODSViter=splitSiStripClusters->begin(); ODSViter != splitSiStripClusters->end(); ODSViter++ )   oclusCnt += ODSViter->size();
  std::cout << "Number of split clusters = " << oclusCnt << std::endl;
 */
  iEvent.put( splitSiStripClusters , "" );
  delete hitAssociator;
}

//
//  Find and dump simTracks associated with the original and new split clusters
//
void
SplitClustersProducer::dumpSimTracks(TrackerHitAssociator* hitAssociator, const SiStripCluster* origCluster,
				     const SiStripCluster* newCluster1, const SiStripCluster* newCluster2,
				     const int splitBy)
{
  std::vector<uint8_t> amp0 = origCluster->amplitudes();
//   if (amp0.size() < 4) return;
  std::vector<uint8_t> amp1 = newCluster1->amplitudes();
  std::vector<uint8_t> amp2 = newCluster2->amplitudes();
  if (splitBy == SplitClustersAlgos::byHits) {
    std::vector<PSimHit> simHitOrig;  simHitOrig.clear();
    std::vector<PSimHit> simHitNew1;  simHitNew1.clear();
    std::vector<PSimHit> simHitNew2;  simHitNew2.clear();
    hitAssociator->associateSimpleRecHitCluster(origCluster, simHitOrig);  std::cout << "-------------" << std::endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster1, simHitNew1);  std::cout << "............." << std::endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster2, simHitNew2);
    std::cout << "No. of simhits (orig, 1, 2): ";
    std::cout << simHitOrig.size() << ", " << simHitNew1.size() << ", " << simHitNew2.size();
  } else {  // byTracks
    std::vector<SimHitIdpr> simTkIdOrig;  simTkIdOrig.clear();
    std::vector<SimHitIdpr> simTkIdNew1;  simTkIdNew1.clear();
    std::vector<SimHitIdpr> simTkIdNew2;  simTkIdNew2.clear();
    hitAssociator->associateSimpleRecHitCluster(origCluster, simTkIdOrig);  std::cout << "-------------" << std::endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster1, simTkIdNew1);  std::cout << "............." << std::endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster2, simTkIdNew2);
    std::cout << "No. of simhits (orig, 1, 2): ";
    std::cout << simTkIdOrig.size() << ", " << simTkIdNew1.size() << ", " << simTkIdNew2.size();
  }
//   std::cout << ", widths:  " << amp0.size()
//        << ", " << amp1.size()
//        << ", " << amp2.size();
//   std::cout << ", first: " << origCluster->firstStrip();  std::cout << ", amps:" ;
  std::cout << ", first, width:  " << origCluster->firstStrip() << ", " << amp0.size() << " || "
       << newCluster1->firstStrip() << ", " << amp1.size() << " | "
       << newCluster2->firstStrip() << ", " << amp2.size() << std::endl << "  Amps:";
  for (size_t i=0; i<amp0.size(); ++i) std::cout << " " << int(amp0[i]);  std::cout << " ||";
  for (size_t i=0; i<amp1.size(); ++i) std::cout << " " << int(amp1[i]);  std::cout << " |";
  for (size_t i=0; i<amp2.size(); ++i) std::cout << " " << int(amp2[i]);  std::cout << std::endl;
  std::cout << "dumpSimTracks end ================================================================" << std::endl;
}

// Dump info on DigSimLinks
void
SplitClustersProducer::dumpDigiSimLinks(uint32_t detID, const SiStripCluster* clust) {

  unsigned short Nstrips = reader->getNumberOfApvsAndStripLength(detID).first*128;

  std::vector<uint8_t> amp = clust->amplitudes();
  int clusiz = amp.size();
  int first  = clust->firstStrip();
  int last   = first + clusiz;
  edm::DetSetVector<StripDigiSimLink>::const_iterator isearch = stripdigisimlink->find(detID);

  if(isearch != stripdigisimlink->end()) {
    edm::DetSet<StripDigiSimLink> link_detset = (*isearch);
    for (int iChan = first; iChan < last; ++iChan) {
      int nLinks = 0;
      for(edm::DetSet<StripDigiSimLink>::const_iterator linkiter = link_detset.data.begin();
	  linkiter != link_detset.data.end(); linkiter++) {
        if( (int)(linkiter->channel()) == iChan ) nLinks++;
      }
      printf ("%10d %4d %4d %4d %3d %3d\n", detID, int(Nstrips), first, iChan, last, nLinks);
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
SplitClustersProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SplitClustersProducer::endJob() {
}

//
// constructors and destructor
//

SplitClustersProducer::SplitClustersProducer(const edm::ParameterSet& iConfig) :
  FileInPath_("CalibTracker/SiStripCommon/data/SiStripDetInfo.dat"),
  splitByString(iConfig.getParameter<std::string>("splitBy")),
  maxLayerTIB_(iConfig.getParameter<int32_t>("maxLayerTIB")),
  maxWheelTID_(iConfig.getParameter<int32_t>("maxWheelTID")),
  maxLayerTOB_(iConfig.getParameter<int32_t>("maxLayerTOB")),
  maxWheelTEC_(iConfig.getParameter<int32_t>("maxWheelTEC")),
  MeVperADC_(iConfig.getParameter<double>("MeVperADC")),
  MeVperMIP_(iConfig.getParameter<double>("MeVperMIP")),
  minNormChargeToSplit_(iConfig.getParameter<double>("minNormChargeToSplit")),
  minNormChargeToKeep_(iConfig.getParameter<double>("minNormChargeToKeep"))
{
  produces< edmNew::DetSetVector<SiStripCluster> >( "" );
  if (splitByString == "byHits") splitBy = SplitClustersAlgos::byHits;
  else if (splitByString == "byTracks") splitBy = SplitClustersAlgos::byTracks;
  else if (splitByString == "noSplit") splitBy = SplitClustersAlgos::noSplit;
  else splitBy = SplitClustersAlgos::unknown;
  reader = new SiStripDetInfoFileReader(FileInPath_.fullPath());
  MIPperADC_ = MeVperADC_/MeVperMIP_;
}


SplitClustersProducer::~SplitClustersProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

//define this as a plug-in
// DEFINE_FWK_MODULE(SplitClustersProducer);
