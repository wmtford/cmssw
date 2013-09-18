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
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/B2F9807F-46EC-E211-8767-003048F1C552.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v3/00000/CA522058-3AEC-E211-B50C-003048F009B6.root'
#
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v1/00000/6C3EAAFC-9114-E311-877D-00261894396D.root',
#        '/store/relval/CMSSW_7_0_0_pre3/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/PRE_ST62_V8-v1/00000/2E1BB0B1-8D14-E311-B0D9-002618FDA237.root'
# ]);
# secFiles.extend( [
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/AA6688B7-33EC-E211-B9F1-C86000151BDE.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/06EBC486-33EC-E211-BD86-003048D3734E.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/5839CE1A-3CEC-E211-9C9F-5404A640A63D.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/6066095A-32EC-E211-A96F-0025B3203690.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/747E0BD6-32EC-E211-A660-C860001BD920.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/7A2D56E0-32EC-E211-AF47-C860001BD8D4.root',
#        '/store/relval/CMSSW_6_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/8AAF3C3F-33EC-E211-A579-003048F17CCC.root' ] );
#
       '/store/relval/CMSSW_6_2_0/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_ST62_V8-v3/00000/70297520-46EC-E211-87C0-001E672CC4C1.root' ] );
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
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
# process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

# Switch to split clusters (here and in process.makeNtuple)
# process.siStripMatchedRecHits.ClusterProducer = 'siStripSplitClusters'

process.makeNtuple = cms.EDAnalyzer('ClusterNtuplizer',
                                    clusterSourceLabel = cms.InputTag("siStripClusters"),
#                                     clusterSourceLabel = cms.InputTag("siStripSplitClusters"),
#                                     beamSpot = cms.InputTag("hltOfflineBeamSpot"),   # 4_4_0_pre9                             
                                    beamSpot = cms.InputTag("offlineBeamSpot")      # 6_2_0
)

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'PRE_ST62_V8::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold = 'Info'

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

