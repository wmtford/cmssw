#ifndef SplitClustersProducer_h
#define SplitClustersProducer_h

// Package:    SplitClustersProducer
// Class:      SplitClustersProducer
// 
// Description: Split SiStrip clusters from overlap tracks
//
// Original Author:  Marco Cardaci
//         Created:  Sun Sep 21 15:22:40 CEST 2008
//         Updated:  Sep 2009 (release 3.1.X) wtford
//         Updated:  May 2010 (release 3.5.X) wtford
//         Updated:  May 2011 (release 4.2.X) wtford

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "TRandom.h"

#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"

#include "wtfRecoLocalTracker/SplitClustersProducer/interface/SplitClustersAlgos.h"


#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "CalibTracker/SiStripCommon/interface/SiStripDetInfoFileReader.h"



typedef std::pair<uint32_t, EncodedEventId> SimHitIdpr;

//
// class declaration
//

class SplitClustersProducer : public edm::EDProducer, public SplitClustersAlgos {
   public:
      explicit SplitClustersProducer(const edm::ParameterSet&);
      SplitClustersProducer();
      ~SplitClustersProducer();

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

//
//  Find and dump simTracks associated with the original and new split clusters
//
      void dumpSimTracks(TrackerHitAssociator*, const SiStripCluster*,
			 const SiStripCluster*, const SiStripCluster*, const int);
      
//
// Dump info on DigSimLinks
//
      void dumpDigiSimLinks(uint32_t detID, const SiStripCluster* clust);

      // ----------member data ---------------------------

      TrackerHitAssociator* hitAssociator;
      std::vector<SimHitIdpr> associatedIdpr;
      std::vector<PSimHit> associatedA;
      std::vector<const SiStripCluster*> vPSiStripCluster;
      TRandom rnd;

      edm::Handle<CrossingFrame<PSimHit> > cf_simhit;
      std::vector<const CrossingFrame<PSimHit> *> cf_simhitvec;
      MixCollection<PSimHit>  TrackerHits;
      typedef std::vector<std::string> vstring;
      vstring trackerContainers;
      edm::Handle< edm::DetSetVector<StripDigiSimLink> >  stripdigisimlink;
      edm::FileInPath FileInPath_;
      SiStripDetInfoFileReader* reader;

//
// constants, enums and typedefs
//

      int splitBy;
      std::string splitByString;
      unsigned int maxLayerTIB_;
      unsigned int maxWheelTID_;
      unsigned int maxLayerTOB_;
      unsigned int maxWheelTEC_;
      double MeVperADC_;
      double MeVperMIP_;
      double MIPperADC_;
      double minNormChargeToSplit_;
      double minNormChargeToKeep_;

//
// static data member definitions
//

};

#endif
