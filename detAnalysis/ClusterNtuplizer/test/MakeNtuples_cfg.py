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

# readFiles.extend( [
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_42_V9-v1/0055/80657C9B-C15E-E011-8F71-0018F3D09660.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_42_V9-v1/0055/485B3BCE-E45E-E011-A89F-00261894392F.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_42_V9-v1/0054/B2DBCC85-845E-E011-BEE2-00304867902C.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_42_V9-v1/0054/96918424-8A5E-E011-9A59-003048678AFA.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_42_V9-v1/0054/508F8F90-885E-E011-A32F-003048678C3A.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_42_V9-v1/0054/2C5CAD82-8E5E-E011-8327-003048B95B30.root'
# ]);
# secFiles.extend( [
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0055/B67E8A1B-CB5E-E011-B39F-003048679168.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0055/B247C513-E75E-E011-8C7F-003048D15D22.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0055/A6B47C94-C15E-E011-A4B3-003048679228.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0055/7E287099-C35E-E011-9849-003048679228.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0055/6A6B8F20-D05E-E011-9CF2-001A928116C0.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/F84B2186-885E-E011-8F37-0026189438EF.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/F43D83F9-925E-E011-8AA1-002618943948.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/EED5DF05-895E-E011-9AA7-0030486790B8.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/D60213F8-855E-E011-AD7D-00261894398C.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/CCB00696-875E-E011-ACF0-001A92971B56.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/C80D750F-8D5E-E011-98DC-003048678E2A.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/BAD0B501-825E-E011-AC5A-00261894393B.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/B4A41A09-895E-E011-8E43-00304867C29C.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/98022B7B-835E-E011-BB3A-0026189438D9.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/829A0C80-8E5E-E011-B687-003048678F78.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/78D977FE-835E-E011-BD54-003048679164.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/4E90A82F-9F5E-E011-864B-001A928116C0.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/2CEEF800-925E-E011-8FCA-00304867901A.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/1EE8FA96-8B5E-E011-A829-001A928116BE.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/182D0C80-845E-E011-8DD2-00304867C034.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/0A935826-8A5E-E011-906B-002618943918.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/04E71810-8D5E-E011-90D2-001A928116DA.root',
# '/store/relval/CMSSW_4_2_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_42_V9-v1/0054/02B56578-845E-E011-990A-002618943843.root'
# ]);
# readFiles.extend( ['file:cmsData/step2_RAW2DIGI_RECO_clearLocAmpl_1k.root'] );
# readFiles.extend( ['file:cmsData/step2sc_3T_420_splSST_1k_4MTV.root'] );
readFiles.extend( ['file:cmsData/step2sc_3T_420_splSST_trim_1k_4MTV.root'] );
secFiles.extend( ['file:cmsData/QCD_Pt_3000_3500_7TeV_cfi_DIGI_L1_DIGI2RAW_clearLocAmpl_1k.root'] );

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
# process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

# Switch to split clusters (here and in process.makeNtuple)
process.siStripMatchedRecHits.ClusterProducer = 'siStripSplitClusters'

process.makeNtuple = cms.EDAnalyzer('ClusterNtuplizer',
#                                     clusterSourceLabel = cms.InputTag("siStripClusters")
                                    clusterSourceLabel = cms.InputTag("siStripSplitClusters")
)

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'MC_42_V9::All'

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
process.p1 = cms.Path(process.mix*process.rechits*process.TrackRefitter*process.makeNtuple)

