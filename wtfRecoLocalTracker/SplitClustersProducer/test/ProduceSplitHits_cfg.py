import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
duplCheck = cms.untracked.string('noDuplicateCheck')
source = cms.Source ("PoolSource",
                     fileNames = readFiles,
#                      secondaryFileNames = secFiles,
                     skipEvents = cms.untracked.uint32(0),
#                     duplicateCheckMode = duplCheck
                     )

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

process = cms.Process("ProduceSplitHits")

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

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
#process.TrackRefitter.TrajectoryInEvent = True

# ######## Hella's code test (per Marco)
# process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
# process.siPixelDigis.InputLabel = 'rawDataCollector'
# process.siPixelDigis.IncludeErrors = True
# # (per Hella)
# process.load('RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi')
# process.siPixelClusters.SplitTheClusters = cms.bool(True)
# #TO DEACTIVATE THE SPLITTER PLEASE REPLACE THE LAST LINE BY
# #process.siPixelClusters.SplitTheClusters = cms.bool(False)


### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'PRE_ST62_V8::All'
# process.GlobalTag.globaltag = 'POSTLS162_V1::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold = 'Info'
process.source = source

#process.Timing = cms.Service("Timing")
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.load('wtfRecoLocalTracker.SplitClustersProducer.SplitCluster_MCtruth_cfi')
# process.siStripSplitClusters.splitBy = cms.string('noSplit')
process.siStripSplitClusters.splitBy = cms.string('byTracks')
process.siStripSplitClusters.minNormChargeToSplit = cms.double(0.0)
process.siStripSplitClusters.minNormChargeToKeep = cms.double(0.0)
# process.siStripSplitClusters.maxLayerTOB = cms.int32(0)
# process.siStripSplitClusters.maxWheelTID = cms.int32(0)
# process.siStripSplitClusters.maxWheelTEC = cms.int32(0)

process.out = cms.OutputModule("PoolOutputModule",
 outputCommands = cms.untracked.vstring('drop *',
  'keep *_siStripSplitClusters_*_*',
  'keep *_siStripDigis_*_*',             # Added (wtf)
  'keep *_rawDataCollector_*_*',     # Added for 4_2_0 pixel cluster splitter (wtf)                 
  'keep *_siPixelClusters_*_*','keep *_offlineBeamSpot_*_*','keep *_pixelVertices_*_*','keep *_g4SimHits_*_*',
  'keep *_simSiPixelDigis_*_*','keep *_simSiStripDigis_*_*','keep *_mergedtruth_*_*'),
# outputCommands = cms.untracked.vstring('keep *'),
 fileName = cms.untracked.string('file:cmsData/scp.root')
)

######## Without Hella's pixel-splitting code
# process.rechits = cms.Sequence(process.siPixelRecHits*process.siStripMatchedRecHits)
######## With Hella's pixel-splitting code
# process.rechits = cms.Sequence(process.siPixelDigis*process.siPixelClusters*process.siPixelRecHits*process.siStripMatchedRecHits)
######## Without RECO tier:
process.rechits = cms.Sequence(
    process.RawToDigi
    *process.localreco
    *process.offlineBeamSpot
    *process.recopixelvertexing
    *process.siPixelDigis
    *process.siPixelClusters
    *process.siPixelRecHits
    *process.siStripMatchedRecHits
    )

#process.event = cms.EDAnalyzer("EventContentAnalyzer")
# process.p1 = cms.Path(process.mix*process.rechits*process.TrackRefitter*process.siStripSplitClusters)
process.p1 = cms.Path(
    process.mix
    *process.rechits
#     *process.TrackRefitter
    *process.siStripSplitClusters
    )
process.e = cms.EndPath(process.out)

file = open('scpFullconfig_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
