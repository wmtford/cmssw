import FWCore.ParameterSet.Config as cms

# The cmsSource "source" defined here allows for alternative running on unsplit clusters
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/B2F9807F-46EC-E211-8767-003048F1C552.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/CA522058-3AEC-E211-B50C-003048F009B6.root'
# ]);
# secFiles.extend( [
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/AA6688B7-33EC-E211-B9F1-C86000151BDE.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/06EBC486-33EC-E211-BD86-003048D3734E.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/5839CE1A-3CEC-E211-9C9F-5404A640A63D.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/6066095A-32EC-E211-A96F-0025B3203690.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/747E0BD6-32EC-E211-A660-C860001BD920.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/7A2D56E0-32EC-E211-AF47-C860001BD8D4.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/8AAF3C3F-33EC-E211-A579-003048F17CCC.root' ] );

process = cms.Process("step2SplitClusters")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

# #Gavril has ----
# process.load("CondCore.DBCommon.CondDBCommon_cfi")
# process.load("CondCore.DBCommon.CondDBSetup_cfi")
# # ----

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'PRE_ST62_V8::All'

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
#process.TrackRefitter.TrajectoryInEvent = True

from RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi import *
MeasurementTracker.stripClusterProducer = 'siStripSplitClusters'

# # Next 5 lines from Boris
# process.splitClusterMeasurementTracker = process.MeasurementTracker.clone(
#     ComponentName = 'splitClusterMeasurementTracker',
#     stripClusterProducer = 'siStripSplitClusters'
# )
# process.newTrajectoryBuilder.MeasurementTrackerName = 'splitClusterMeasurementTracker'

# From Wenger:
process.siStripMatchedRecHits.ClusterProducer = 'siStripSplitClusters'

# Added at 4.4.0_pre9
from RecoTracker.TkSeedGenerator.SeedGeneratorFromRegionHitsEDProducer_cfi import *
seedGeneratorFromRegionHitsEDProducer.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'

from RecoTracker.IterativeTracking.iterativeTk_cff import *
lowPtTripletStepClusters.stripClusters = cms.InputTag("siStripSplitClusters")
lowPtTripletStepSeeds.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'
pixelPairStepClusters.stripClusters = cms.InputTag("siStripSplitClusters")
pixelPairStepSeeds.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'
detachedTripletStep.stripClusters = cms.InputTag("siStripSplitClusters")
detachedTripletStepClusters.stripClusters = cms.InputTag("siStripSplitClusters")
detachedTripletStepSeeds.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'
mixedTripletStep.stripClusters = cms.InputTag("siStripSplitClusters")
mixedTripletStepClusters.stripClusters = 'siStripSplitClusters'
mixedTripletStepSeedsA.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'
mixedTripletStepSeedsB.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'
# Following line to evade a segv (fixed after 440patch?):  (default value is 100000)
# mixedTripletStepTrackCandidates.maxNSeeds = cms.uint32(33345)
pixelLessStepClusters.stripClusters = cms.InputTag("siStripSplitClusters")
pixelLessStepSeeds.ClusterCheckPSet.ClusterCollectionLabel      = 'siStripSplitClusters'
tobTecStepClusters.stripClusters = cms.InputTag("siStripSplitClusters")
tobTecStepSeeds.ClusterCheckPSet.ClusterCollectionLabel      = 'siStripSplitClusters'

from RecoTracker.IterativeTracking.InitialStep_cff import *
import RecoTracker.TkSeedingLayers.PixelLayerTriplets_cfi
initialStepSeedLayers = RecoTracker.TkSeedingLayers.PixelLayerTriplets_cfi.pixellayertriplets.clone(
    ComponentName = 'initialStepSeedLayers'
    )
initialStepSeeds.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'

from RecoTracker.ConversionSeedGenerators.ConversionStep_cff import *
convClusters.stripClusters = cms.InputTag("siStripSplitClusters")
photonConvTrajSeedFromSingleLeg.ClusterCheckPSet.ClusterCollectionLabel = 'siStripSplitClusters'

# The following didn't generate missing product aborts, but appear in Full_cfg
#  (adding these lines doesn't affect the results)
# process.beamhaloTrackerSeeds.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.combinatorialcosmicseedfinder.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.combinatorialcosmicseedfinderP5.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.cosmicseedfinder.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.cosmicseedfinderP5.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.globalMixedSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.globalPixelLessSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.globalPixelSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.globalSeedsFromPairsWithVertices.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.globalSeedsFromTriplets.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.regionalCosmicTrackerSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.roadSearchSeeds.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.roadSearchSeedsP5.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.siStripClustersBottom.label = cms.InputTag("siStripSplitClusters")
# process.siStripClustersTop.label = cms.InputTag("siStripSplitClusters")
# process.simpleCosmicBONSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
# process.topBottomClusterInfoProducer.stripClustersOld = cms.InputTag("siStripSplitClusters")
# process.topBottomClusterInfoProducerBottom.stripClustersOld = cms.InputTag("siStripSplitClusters")
# process.topBottomClusterInfoProducerTop.stripClustersOld = cms.InputTag("siStripSplitClusters")

# End 4.4.0_pre9 additions

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 1
# #process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
# process.MessageLogger.destinations = cms.untracked.vstring('debugmessages')
# # process.MessageLogger.debugModules = cms.untracked.vstring('mixedTripletStepTrackCandidates')
# process.MessageLogger.debugModules = cms.untracked.vstring('*')
# process.MessageLogger.debugmessages = cms.untracked.PSet(
#   threshold = cms.untracked.string('DEBUG')
# #   ,INFO       =  cms.untracked.int32(0)
# #   ,DEBUG   = cms.untracked.int32(10000000)
# #   ,interestingToMe = cms.untracked.int32(10000000)
#   )

process.source = cms.Source("PoolSource",
#                             fileNames = cms.untracked.vstring('file:cmsData/scp_3T_420_noSplit_1k.root'),
#                             fileNames = cms.untracked.vstring('file:cmsData/scp_3T_440p9_splSSTtibtob_noDEdxcut_1k.root'),
                            fileNames = cms.untracked.vstring('file:cmsData/scp.root'),
#   skipEvents = cms.untracked.uint32(170)  # get to event 6571
#   skipEvents = cms.untracked.uint32(171)
)
# process.source = source

#process.Timing = cms.Service("Timing")
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.out = cms.OutputModule("PoolOutputModule",
 outputCommands = cms.untracked.vstring('keep *_*_*_*'),
 fileName = cms.untracked.string('file:cmsData/step2sc_4MTV.root')
)

process.rechits = cms.Sequence(process.siPixelRecHits*process.siStripMatchedRecHits)

#process.event = cms.EDAnalyzer("EventContentAnalyzer")

# #Based on Gavril's config (alternate to p1)
# from Configuration.StandardSequences.Reconstruction_cff import *
# process.init = cms.Sequence(process.mix*process.RawToDigi*process.localreco*process.offlineBeamSpot+process.recopixelvertexing)
# process.fullreco = cms.Sequence(globalreco*highlevelreco)
# process.path = cms.Path(
#     process.init*
#     #process.splitClusters*
#     process.rechits*
#     process.fullreco
#     #process.p7*
#     #process.postTracking
#     )

#end



process.p1 = cms.Path(
    process.mix
#     *
#     process.rechits
#     *process.ckftracks
#     *process.TrackRefitter
    )
process.e = cms.EndPath(process.out)

file = open('step2Fullconfig_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
