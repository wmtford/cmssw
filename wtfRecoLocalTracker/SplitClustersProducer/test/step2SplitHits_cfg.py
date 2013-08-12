import FWCore.ParameterSet.Config as cms

# The cmsSource "source" defined here allows for alternative running on unsplit clusters
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0173/6C552F5A-A4D3-E011-99DE-002618943916.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0172/CC2921ED-A0D2-E011-B626-00304867BFF2.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0172/ACFC099C-A1D2-E011-B9F9-001A928116D2.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0172/9C8C5FA3-A1D2-E011-8D0B-0018F3D096C6.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0172/6465A4FB-9FD2-E011-BBEF-002618943940.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0172/2AAE2104-A2D2-E011-BD9E-001A928116EC.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/START44_V4-v1/0172/20F72E9A-A1D2-E011-88C8-002618943971.root'
]);
secFiles.extend( [
 '/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0173/52FEA7AB-A5D3-E011-9BCB-0018F3D0961E.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/FE12C0D9-9FD2-E011-A947-0026189438E9.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/FC8F84E5-9FD2-E011-9E8F-0018F3D09664.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/FAE278F3-A1D2-E011-8999-002618943924.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/F245BB8D-A1D2-E011-8A7B-002618943934.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/ECDB4EED-A0D2-E011-A29D-00261894394A.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/DAB07F99-A1D2-E011-926D-002618943924.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/D2E0E9E0-9FD2-E011-8D8A-0018F3D096DA.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/CC3CB79D-A1D2-E011-A1F4-002618943914.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/C2380CEA-9FD2-E011-8B21-003048678F8E.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/B8A0235B-A0D2-E011-A181-002618943923.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/AE3825EE-A0D2-E011-BF6E-003048678DD6.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/96A9569A-A1D2-E011-B791-0026189438B9.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/86086DEB-9FD2-E011-91BF-0018F3D096BC.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/7656A695-A1D2-E011-B1BA-00304867BFBC.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/70E1BAFB-A1D2-E011-A7C9-003048678FB2.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/54EB348F-A1D2-E011-BCC0-003048D15DCA.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/4E2FE4ED-A0D2-E011-A75C-0026189438E3.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/42C57382-A2D2-E011-8FA1-003048678BB2.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/3A2D38A0-A1D2-E011-990C-003048678DA2.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/26ECEEF7-A1D2-E011-8E11-00304867C136.root',
'/store/relval/CMSSW_4_4_0_pre9/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V4-v1/0172/0A5A0199-A1D2-E011-A75A-00261894386C.root'
]);

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
process.GlobalTag.globaltag = 'START44_V4::All'

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
process.beamhaloTrackerSeeds.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.combinatorialcosmicseedfinder.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.combinatorialcosmicseedfinderP5.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.cosmicseedfinder.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.cosmicseedfinderP5.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.globalMixedSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.globalPixelLessSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.globalPixelSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.globalSeedsFromPairsWithVertices.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.globalSeedsFromTriplets.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.regionalCosmicTrackerSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.roadSearchSeeds.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.roadSearchSeedsP5.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.siStripClustersBottom.label = cms.InputTag("siStripSplitClusters")
process.siStripClustersTop.label = cms.InputTag("siStripSplitClusters")
process.simpleCosmicBONSeeds.ClusterCheckPSet.ClusterCollectionLabel = cms.InputTag("siStripSplitClusters")
process.topBottomClusterInfoProducer.stripClustersOld = cms.InputTag("siStripSplitClusters")
process.topBottomClusterInfoProducerBottom.stripClustersOld = cms.InputTag("siStripSplitClusters")
process.topBottomClusterInfoProducerTop.stripClustersOld = cms.InputTag("siStripSplitClusters")

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
                            fileNames = cms.untracked.vstring('file:cmsData/scp_3T_440p9_splSSTtibtob_noDEdxcut_1k.root'),
#                             fileNames = cms.untracked.vstring('file:cmsData/scp.root'),
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



process.p1 = cms.Path(process.mix*process.rechits*process.ckftracks*process.TrackRefitter)
process.e = cms.EndPath(process.out)

file = open('step2Fullconfig_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
