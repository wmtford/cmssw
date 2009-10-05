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

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "TRandom.h"

#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"

#include "wtfRecoLocalTracker/SplitClustersProducer/interface/SplitClustersAlgos.h"

//
// class declaration
//

class SplitClustersProducer : public edm::EDProducer, public SplitClustersAlgos {
   public:
      explicit SplitClustersProducer(const edm::ParameterSet&);
      SplitClustersProducer();
      ~SplitClustersProducer();
      std::vector<PSimHit> associatedA;

   private:
      virtual void beginJob(const edm::EventSetup&) ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

      TrackerHitAssociator * hitAssociator;
      std::vector<const SiStripCluster*> vPSiStripCluster;
      TRandom rnd;
  /*
      //SiStripClusterInfo* clusterInfo;
      */
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
SplitClustersProducer::SplitClustersProducer(const edm::ParameterSet& iConfig)
{
   produces< edmNew::DetSetVector<SiStripCluster> >( "" );
}


SplitClustersProducer::~SplitClustersProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

#endif
