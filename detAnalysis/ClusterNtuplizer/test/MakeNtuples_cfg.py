import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
duplCheck = cms.untracked.string('noDuplicateCheck')
source = cms.Source ("PoolSource",
                     fileNames = readFiles,
                     secondaryFileNames = secFiles,
                     skipEvents = cms.untracked.uint32(0),
#                     duplicateCheckMode = duplCheck
                     )

readFiles.extend( [
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/E46F1674-BF9B-E211-8301-0025904B1000.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/ACAC6FB8-C29B-E211-A29A-001E4F3D72E7.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/7E369590-BE9B-E211-A194-003048F17CA0.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/72058A60-BE9B-E211-B673-003048F23B74.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/6491F0AD-BE9B-E211-86AB-001D09F29524.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/3A7A308C-BE9B-E211-B725-003048F1749A.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/2082B7E8-BF9B-E211-9F1F-5404A63886D6.root',
 # '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/12264B70-BE9B-E211-8435-003048F009C8.root'
#
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/2EC8AF8C-CB6B-E411-B61C-02163E00E75F.root',
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/308B830D-C16B-E411-8B95-02163E00F425.root',
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/3E4558B7-C06B-E411-975F-002590494D2E.root',
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/A2969D5C-C16B-E411-A6AD-003048C9C1CE.root',
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/C83A6842-BF6B-E411-A6BC-00237DDC5C38.root',
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/E4257B22-C06B-E411-8D86-02163E00F2DF.root',
 '/store/relval/CMSSW_7_3_0_pre2/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/F238586E-C16B-E411-8CF0-02163E00F536.root'
] );
# readFiles.extend( ['file:cmsData/step2_RAW2DIGI_RECO_clearLocAmpl_1k.root'] );
# readFiles.extend( ['file:cmsData/step2sc_3T_420_splSST_1k_4MTV.root'] );
# readFiles.extend( ['file:cmsData/step2sc_3T_420_splSST_trim_1k_4MTV.root'] );
# secFiles.extend( ['file:cmsData/QCD_Pt_3000_3500_7TeV_cfi_DIGI_L1_DIGI2RAW_clearLocAmpl_1k.root'] );
# readFiles.extend( ['file:/usr/users/wtford/cms/rel730pr2/src/Validation/RecoTrack/test/3T_ootb_PR6349_replay/1313.0_QCD_Pt_3000_3500_13+QCD_Pt_3000_3500_13INPUT+DIGIUP15+RECOUP15+HARVESTUP15/step2.root'] );

process = cms.Process("makeNtuple")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold = 'Info'

process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff') # 7_3_0_pre3
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff') # 7_3_0_pre3
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

# Need to override default suppression of crossing frames, as of CMSSW_6_2_?
# from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 
# process = setCrossingFrameOn(process)
# Customized for our needs:
process.mix.mixObjects.mixSH.crossingFrames = cms.untracked.vstring(
#     'TrackerHitsPixelBarrelHighTof',
#     'TrackerHitsPixelBarrelLowTof',
#     'TrackerHitsPixelEndcapHighTof',
#     'TrackerHitsPixelEndcapLowTof',
    'TrackerHitsTECHighTof',
    'TrackerHitsTECLowTof',
    'TrackerHitsTIBHighTof',
    'TrackerHitsTIBLowTof',
    'TrackerHitsTIDHighTof',
    'TrackerHitsTIDLowTof',
    'TrackerHitsTOBHighTof',
    'TrackerHitsTOBLowTof')

# Switch to split clusters (here and in process.makeNtuple)
# process.siStripMatchedRecHits.ClusterProducer = 'siStripSplitClusters'

process.makeNtuple = cms.EDAnalyzer('ClusterNtuplizer',
                                    clusterSourceLabel = cms.InputTag("siStripClusters"),
#                                     clusterSourceLabel = cms.InputTag("siStripSplitClusters"),
#                                     beamSpot = cms.InputTag("hltOfflineBeamSpot"),   # 4_4_0_pre9                             
                                    beamSpot = cms.InputTag("offlineBeamSpot"),      # 6_2_0
                                    printOut = cms.untracked.int32(0),
                                    useCrossingFrames = cms.untracked.bool(False)
)

### conditions
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# process.GlobalTag.globaltag = 'PRE_ST61_V1::All'
# process.GlobalTag.globaltag = 'PRE_ST62_V8::All'
# process.GlobalTag.globaltag = 'START62_V1::All'
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff') # 7_3_0_pre3
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag # 7_3_0_pre3
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '') # 7_3_0_pre3

process.source = source

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cmsData/clusNtp/clusNtuple.root')
)

#process.Timing = cms.Service("Timing")
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.p1 = cms.Path(
    process.mix
    *process.RawToDigi
    *process.trackerlocalreco
    *process.offlineBeamSpot
    *process.siPixelClusterShapeCache # 7_3_0_pre3
    *process.recopixelvertexing
    *process.makeNtuple
    )

