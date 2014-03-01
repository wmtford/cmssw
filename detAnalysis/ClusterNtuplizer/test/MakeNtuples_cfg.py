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
# We don't currently need GEN-SIM-RECO, but include the lines here for reference
#
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/B2F9807F-46EC-E211-8767-003048F1C552.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/CA522058-3AEC-E211-B50C-003048F009B6.root'
#
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/1A4CBAAC-48EC-E211-8A00-001E67397EB8.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/24366CE4-42EC-E211-A3B9-003048D4988C.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/8476F595-44EC-E211-B8E7-003048F00B16.root' 
#
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v1/00000/6C3EAAFC-9114-E311-877D-00261894396D.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v1/00000/2E1BB0B1-8D14-E311-B0D9-002618FDA237.root'
# ]);
# secFiles.extend( [
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/E46F1674-BF9B-E211-8301-0025904B1000.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/ACAC6FB8-C29B-E211-A29A-001E4F3D72E7.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/7E369590-BE9B-E211-A194-003048F17CA0.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/72058A60-BE9B-E211-B673-003048F23B74.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/6491F0AD-BE9B-E211-86AB-001D09F29524.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/3A7A308C-BE9B-E211-B725-003048F1749A.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/2082B7E8-BF9B-E211-9F1F-5404A63886D6.root',
#  '/store/relval/CMSSW_6_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST61_V1-v1/00000/12264B70-BE9B-E211-8435-003048F009C8.root'               ] );
#
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/00CB90CA-30EC-E211-B62B-003048F01080.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/34C2B010-31EC-E211-860A-003048D2BC6C.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/567BAD24-31EC-E211-A94B-003048D374CA.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/70DB230C-31EC-E211-B051-003048945474.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/78227A8F-35EC-E211-B3B9-02163E008D98.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/7CC7F7E5-30EC-E211-87BE-003048CFC64A.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/A8482AE3-30EC-E211-BF92-002481E0E5E6.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/D46345E0-30EC-E211-A57C-003048F1C53C.root',
#        '/store/relval/CMSSW_6_2_0/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/F027A10D-31EC-E211-AC59-5404A63886BE.root' ] );
#
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/AA6688B7-33EC-E211-B9F1-C86000151BDE.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/06EBC486-33EC-E211-BD86-003048D3734E.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/5839CE1A-3CEC-E211-9C9F-5404A640A63D.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/6066095A-32EC-E211-A96F-0025B3203690.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/747E0BD6-32EC-E211-A660-C860001BD920.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/7A2D56E0-32EC-E211-AF47-C860001BD8D4.root',
       '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/8AAF3C3F-33EC-E211-A579-003048F17CCC.root' ] );
#
#  This one file is the single mu
#        '/store/relval/CMSSW_6_2_0/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/70297520-46EC-E211-87C0-001E672CC4C1.root' ] );
#
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/4032602B-7214-E311-A5BE-00304867C034.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/5893C8F0-7014-E311-A162-002618943832.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/A2465BAF-7214-E311-ADA9-0025905964C4.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/241A9902-7314-E311-B38A-002618943985.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/18115DAA-7614-E311-BBBF-002590593902.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/146A96BC-7114-E311-8A36-002590596486.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v1/00000/0EB9CEFE-7114-E311-ACCE-00261894392F.root' ] );
# readFiles.extend( ['file:cmsData/step2_RAW2DIGI_RECO_clearLocAmpl_1k.root'] );
# readFiles.extend( ['file:cmsData/step2sc_3T_420_splSST_1k_4MTV.root'] );
# readFiles.extend( ['file:cmsData/step2sc_3T_420_splSST_trim_1k_4MTV.root'] );
# secFiles.extend( ['file:cmsData/QCD_Pt_3000_3500_7TeV_cfi_DIGI_L1_DIGI2RAW_clearLocAmpl_1k.root'] );

process = cms.Process("makeNtuple")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold = 'Info'

process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
# process.load('Configuration.StandardSequences.L1Reco_cff')
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
                                    printOut = cms.untracked.int32(0)
)

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# process.GlobalTag.globaltag = 'PRE_ST61_V1::All'
# process.GlobalTag.globaltag = 'PRE_ST62_V8::All'
process.GlobalTag.globaltag = 'START62_V1::All'

process.source = source

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cmsData/clusNtp/clusNtuple.root')
)

#process.Timing = cms.Service("Timing")
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.rechits = cms.Sequence(process.siPixelRecHits*process.siStripMatchedRecHits)

#process.event = cms.EDAnalyzer("EventContentAnalyzer")
# process.p1 = cms.Path(process.mix*process.rechits*process.TrackRefitter*process.makeNtuple)
process.p1 = cms.Path(
    process.mix
#     *process.trackingParticles
    *process.RawToDigi
    *process.localreco
    *process.offlineBeamSpot
    *process.recopixelvertexing
#     *process.ckftracks
    *process.makeNtuple
    )

