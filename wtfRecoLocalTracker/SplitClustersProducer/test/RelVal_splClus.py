import FWCore.ParameterSet.Config as cms
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

process = cms.Process("TkVal")
process.load("FWCore.MessageService.MessageLogger_cfi")

### standard includes
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'START44_V4::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold = 'Info'
# process.MessageLogger.cerr.threshold = 'Debug'

# process.source = source
process.source = cms.Source("PoolSource",
#                             fileNames = cms.untracked.vstring('file:cmsData/step2sc_4MTV_3T_440p9_splSST_829.root'
#                             fileNames = cms.untracked.vstring('file:cmsData/step2sc_4MTV_3T_440p9_splSSTbrl_reco_1k.root'
                            fileNames = cms.untracked.vstring('file:cmsData/step2sc_4MTV.root'
							      )
			    )
#                                                              Set lastRun below, if ncesssary

### validation-specific includes
#process.load("SimTracker.TrackAssociation.TrackAssociatorByChi2_cfi")
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")
process.load("Validation.RecoTrack.cuts_cff")
process.load("Validation.RecoTrack.MultiTrackValidator_cff")
process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
process.load("DQMServices.Components.EDMtoMEConverter_cff")

process.load("Validation.Configuration.postValidation_cff")

process.TrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')
process.TrackAssociatorByHits.Purity_SimToReco = cms.double(0.75)
process.TrackAssociatorByHits.Cut_RecoToSim = cms.double(0.75)

### configuration MultiTrackValidator ###
process.multiTrackValidator.outputFile = 'val.RelVal_spl.root'
process.multiTrackValidator.runStandalone = True
#process.multiTrackValidator.multiRunLastRun=cms.untracked.int32(139)


# Select step 4 tracks, high purity
# /DataFormats/TrackReco/interface/TrackBase.h
#   case undefAlgorithm: return "undefAlgorithm";
#   case ctf: return "ctf";
#   case rs: return "rs";
#   case cosmics: return "cosmics";
#   case beamhalo: return "beamhalo";
#   case iter0: return "iter0";
#   case iter1: return "iter1";
#   case iter2: return "iter2";
#   case iter3: return "iter3";
#   case iter4: return "iter4";
#   case iter5: return "iter5";
#   case iter6: return "iter6";
#   case iter7: return "iter7";
#   case iter8: return "iter8";
#   case iter9: return "iter9";
#   case iter10: return "iter10";
#   case outInEcalSeededConv: return "outInEcalSeededConv";
#   case inOutEcalSeededConv: return "inOutEcalSeededConv";
#   case nuclInter: return "nuclInter";
#   case standAloneMuon: return "standAloneMuon";
#   case globalMuon: return "globalMuon";
#   case cosmicStandAloneMuon: return "cosmicStandAloneMuon";
#   case cosmicGlobalMuon: return "cosmicGlobalMuon";
#   case iter1LargeD0: return "iter1LargeD0";
#   case iter2LargeD0: return "iter2LargeD0";
#   case iter3LargeD0: return "iter3LargeD0";
#   case iter4LargeD0: return "iter4LargeD0";
#   case iter5LargeD0: return "iter5LargeD0";
#   case bTagGhostTracks: return "bTagGhostTracks";
#   case gsf: return "gsf";
# process.cutsRecoTracks.algorithm = cms.vstring('iter4', 'iter5')
process.cutsRecoTracks.algorithm = cms.vstring()
process.cutsRecoTracks.quality = cms.vstring('highPurity')

process.multiTrackValidator.associators = ['TrackAssociatorByHits']
process.multiTrackValidator.useLogPt=cms.untracked.bool(True)
process.multiTrackValidator.minpT = cms.double(0.1)
process.multiTrackValidator.maxpT = cms.double(1000)
process.multiTrackValidator.nintpT = cms.int32(40)
process.multiTrackValidator.skipHistoFit=cms.untracked.bool(False)
# Added, wtf
# process.multiTrackValidator.ptMinTP = cms.double(0.005)
process.multiTrackValidator.ptMinTP = cms.double(0.9)
# process.multiTrackValidator.tipTP = cms.double(60)
process.multiTrackValidator.tipTP = cms.double(3.5)
# end wtf additions

process.multiTrackValidator.label = ['cutsRecoTracks']
if (process.multiTrackValidator.label[0] == 'generalTracks'):
    process.multiTrackValidator.UseAssociators = cms.bool(False)
else:
    process.multiTrackValidator.UseAssociators = cms.bool(True)
######


#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring (
#    FILENAMES
#    )
#)
#process.extend("RelValTTbar_cff")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)


process.digi2track = cms.Sequence(process.siPixelDigis*process.siStripDigis*
                                  process.trackerlocalreco*
                                  process.ckftracks*
                                  process.cutsRecoTracks*
                                  process.multiTrackValidator)
#redo also tracking particles
process.digi2track_and_TP = cms.Sequence(process.mix*process.trackingParticles*
                                  process.siPixelDigis*process.siStripDigis*
                                  process.trackerlocalreco*
                                  process.ckftracks*
                                  process.cutsRecoTracks*
                                  process.multiTrackValidator)

process.re_tracking = cms.Sequence(process.siPixelRecHits*process.siStripMatchedRecHits*
                                   process.ckftracks*
                                   process.cutsRecoTracks*
                                   process.multiTrackValidator
                                   )

process.re_tracking_and_TP = cms.Sequence(process.mix*process.trackingParticles*
                                   process.siPixelRecHits*process.siStripMatchedRecHits*
                                   process.ckftracks*
                                   process.cutsRecoTracks*
                                   process.multiTrackValidator
                                   )

if (process.multiTrackValidator.label[0] == 'generalTracks'):
    process.only_validation = cms.Sequence(process.multiTrackValidator)
else:
    process.only_validation = cms.Sequence(process.cutsRecoTracks*process.multiTrackValidator)
    
if (process.multiTrackValidator.label[0] == 'generalTracks'):
    process.only_validation_and_TP = cms.Sequence(process.mix*process.trackingParticles*process.multiTrackValidator)
else:
    process.only_validation_and_TP = cms.Sequence(process.mix*process.trackingParticles*process.cutsRecoTracks*
                                                  process.multiTrackValidator)

#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string('tpNtuple.root')
#)

### customized versoin of the OutputModule
### it save the mininal information which is necessary to perform tracking validation (tracks, tracking particles, 
### digiSimLink,etc..)

process.customEventContent = cms.PSet(
     outputCommands = cms.untracked.vstring('drop *')
 )

process.customEventContent.outputCommands.extend(process.RecoTrackerRECO.outputCommands)
process.customEventContent.outputCommands.extend(process.BeamSpotRECO.outputCommands)
process.customEventContent.outputCommands.extend(process.SimGeneralFEVTDEBUG.outputCommands)
process.customEventContent.outputCommands.extend(process.RecoLocalTrackerRECO.outputCommands)
process.customEventContent.outputCommands.append('keep *_simSiStripDigis_*_*')
process.customEventContent.outputCommands.append('keep *_simSiPixelDigis_*_*')
process.customEventContent.outputCommands.append('drop SiStripDigiedmDetSetVector_simSiStripDigis_*_*')
process.customEventContent.outputCommands.append('drop PixelDigiedmDetSetVector_simSiPixelDigis_*_*')


process.OUTPUT = cms.OutputModule("PoolOutputModule",
                                  process.customEventContent,
                                  fileName = cms.untracked.string('output.RelVal_3T_spl.root')
                                  )

ValidationSequence="only_validation"

if ValidationSequence=="harvesting":
    process.DQMStore.collateHistograms = False

    process.dqmSaver.convention = 'Offline'

    process.dqmSaver.saveByRun = cms.untracked.int32(-1)
    process.dqmSaver.saveAtJobEnd = cms.untracked.bool(True)
    process.dqmSaver.forceRunNumber = cms.untracked.int32(1)


    process.dqmSaver.workflow = "/MC_42_V9/RelValQCD_Pt_3000_3500/Validation"
    process.DQMStore.verbose=3

    process.options = cms.untracked.PSet(
        fileMode = cms.untracked.string('FULLMERGE')
        )
    for filter in (getattr(process,f) for f in process.filters_()):
        if hasattr(filter,"outputFile"):
            filter.outputFile=""


process.EDMtoMEConverter.convertOnEndLumi = False
process.harvesting= cms.Sequence(process.EDMtoMEConverter*process.postValidation*process.dqmSaver)




### final path and endPath
process.p = cms.Path(process.only_validation)
#process.outpath = cms.EndPath(process.OUTPUT)

file = open('mtvFullconfig_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()


