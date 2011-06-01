import FWCore.ParameterSet.Config as cms

from RecoTracker.DeDx.dedxDiscriminator_Prod_cfi import dedxDiscrimProd

siStripSplitClusters = cms.EDProducer("SplitClustersProducer",
  splitBy = cms.string('byTracks'),
  MeVperADC = dedxDiscrimProd.MeVperADCStrip,
  MeVperMIP = cms.double(2.9),
  minNormCharge = cms.double(1.5),
  maxLayerTIB = cms.int32(4),
  maxWheelTID = cms.int32(3),
  maxLayerTOB = cms.int32(6),
  maxWheelTEC = cms.int32(9)
)

