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

#readFiles.extend( [ 'file:cmsData/step2_RAW2DIGI_RECO_bugLink_defaultNoise_10.root' ] );
#secFiles.extend( [ 'file:cmsData/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_bugLink_defaultNoise_10.root' ] );

#readFiles.extend( [ 'file:cmsData/step2_RAW2DIGI_RECO_corLink_noNoise_100.root' ] );
#secFiles.extend( [ 'file:cmsData/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_corLink_noNoise_100.root' ] );

# readFiles.extend( [ 'file:cmsData/step2_RAW2DIGI_RECO_corLink_1k.root' ] );
# secFiles.extend( [
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_1.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_2.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_3.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_4.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_5.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_6.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_7.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_8.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_9.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_10.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_11.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_12.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_13.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_14.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_15.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_16.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_17.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_18.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_19.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_20.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_21.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_22.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_23.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_24.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_25.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_26.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_27.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_28.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_29.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_30.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_31.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_32.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_33.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_34.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_35.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_36.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_37.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_38.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_39.root',
# '/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_40.root'
#                    ] );

#readFiles.extend( [
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/F8D2BBD0-CC78-DE11-A856-001D09F241D2.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/C4A3A5F2-E278-DE11-8B8A-001D09F25456.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/BAC269B7-CC78-DE11-83E5-001D09F29169.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/5C3EEAB4-CC78-DE11-A47B-001D09F290CE.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/56E7E9BC-CC78-DE11-B3FD-001D09F24D8A.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/4295B70E-D278-DE11-87D7-000423D6CA02.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/3C3597B3-CC78-DE11-998E-000423D98A44.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/3AD98805-CE78-DE11-AB1E-0019B9F7312C.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/34FBEBBE-CC78-DE11-B7BE-001D09F24637.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/28850C22-E978-DE11-90FC-001D09F252DA.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/12CDCEC7-CC78-DE11-88D3-001D09F34488.root']);
#secFiles.extend( [
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/FE575692-CC78-DE11-8E27-001D09F2AF96.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/FC198C97-CC78-DE11-A7A4-001D09F241D2.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/F055C8A3-CC78-DE11-B539-000423D98BC4.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/D6C5D18A-CC78-DE11-A22D-001D09F29114.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/C2BDFDCA-CC78-DE11-AFC2-001D09F2447F.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/C08BBFB8-CE78-DE11-90DB-001D09F24664.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/ACB77B96-CC78-DE11-8C56-0019B9F72CE5.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/AC3183E7-CC78-DE11-A022-001D09F24024.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/A058F3C0-CC78-DE11-91E7-001D09F23A61.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/9EE73BA5-CC78-DE11-97F7-000423D8F63C.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/98818EB9-CC78-DE11-A4E1-001D09F24DDA.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/9691D28E-D278-DE11-BC29-000423D99394.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/94F7E9EE-E278-DE11-9B75-001D09F2516D.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/8AC868A1-CC78-DE11-B8AA-001D09F24664.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/867F88CE-D178-DE11-AF51-000423D9890C.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/84CA3C9A-CC78-DE11-B409-001D09F2532F.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/84C5E1A9-CC78-DE11-A283-0019B9F72F97.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/84B8D800-CD78-DE11-B2E0-000423D99E46.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/80A958A3-CC78-DE11-B4AF-000423D99F1E.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/7230EBA1-CC78-DE11-A023-001D09F251BD.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/7099D79E-CC78-DE11-ACBB-000423D98FBC.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/6E8C60C0-CC78-DE11-9258-001D09F2960F.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/62FBBAC6-CC78-DE11-9C88-001D09F251FE.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/60D47CC9-CC78-DE11-B203-001D09F23A07.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/5C501299-CC78-DE11-8C15-001D09F23A61.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/565584AA-CC78-DE11-ABA7-001D09F295FB.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/56120694-CC78-DE11-914B-0019B9F71A6B.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/50FD14A0-CC78-DE11-8F84-001D09F251FE.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/4891923D-D578-DE11-BBB5-000423D98868.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/400628A3-CC78-DE11-9424-000423D60FF6.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/3EAC289E-CD78-DE11-ADE0-001D09F24EAC.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/20D79C96-CC78-DE11-90F8-001D09F2915A.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1E0A93BF-CC78-DE11-B57D-000423D98BC4.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1C4946CA-CC78-DE11-AE0D-001D09F24EAC.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1A09B692-CC78-DE11-AF45-001D09F248F8.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1057C03A-D178-DE11-A339-000423D98EC4.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/0822DD24-E978-DE11-B43C-001D09F253C0.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/02AAD3A6-D078-DE11-9C9A-000423D98EC8.root']);

readFiles.extend( [
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0014/D0226F78-B313-DF11-B719-002618943858.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0014/806F73D2-6C13-DF11-A864-002618943958.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/F27FE3EF-5213-DF11-86D3-003048678BAC.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/E471DCB2-5313-DF11-AF44-001731230A77.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/CCBF70F7-6213-DF11-A850-001731AF6BC1.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/A4A15542-4C13-DF11-80BF-003048D15E14.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/9230ACCE-6913-DF11-971D-002618943953.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/8A78584E-4E13-DF11-A3E5-003048678A6A.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/64A4CF64-5113-DF11-A28A-0018F3D096F0.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/586DF859-6713-DF11-A3B7-002354EF3BDB.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/56C5C387-5413-DF11-A586-001A92971B80.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/501677B7-4913-DF11-8E1B-001731AF6865.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/4423AEE8-5313-DF11-966E-001A928116D2.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/3EC71364-5213-DF11-BDD3-0018F3D09682.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/229690CA-4D13-DF11-8C14-00304867BEC0.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_3XY_V21-v1/0013/0A54971C-4F13-DF11-837F-0018F3D096BC.root' ] );
secFiles.extend( [
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0014/9C47A1C9-6C13-DF11-8C3E-0030486791DC.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0014/0013E780-B313-DF11-93CE-00304867920A.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/F6F1525B-5213-DF11-A821-0018F3D09600.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/F2C82D75-5313-DF11-9540-0018F3D096BC.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/E69F0CE4-5313-DF11-97D9-003048678A7E.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/E4E208ED-6213-DF11-8BB6-0018F3D095FA.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/E4DE1175-5313-DF11-91BB-001BFCDBD176.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/DCC8B347-4D13-DF11-8366-0030486790BE.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/D233A516-4F13-DF11-90B9-002618943962.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/D0CB3B4A-4E13-DF11-ACF3-003048678F8E.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/CA545003-5313-DF11-85AF-001A92971B9C.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/C2DD4E87-5413-DF11-8B76-0018F3D09664.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/BC39C15D-5113-DF11-8111-0017312B56F7.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/B6B36AC8-6913-DF11-BCAA-002354EF3BDE.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/B670AE0B-5313-DF11-B7C2-00248C55CC40.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/B0095046-4D13-DF11-8521-00304867924A.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/AED7B05E-6713-DF11-81CA-00304867926C.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/AC0E4EDE-5113-DF11-A8E0-0018F3D09630.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/A6475DCD-4D13-DF11-96FC-003048679012.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/A273B44D-4E13-DF11-8D69-003048679166.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/9E2A4010-4813-DF11-898B-0018F3D0968E.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/9E17EBC9-5013-DF11-A9A3-001731EF61B4.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/869E2604-5313-DF11-889E-001A92810AD0.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/84386392-5413-DF11-8BB7-0018F3D09626.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/6AFE27DE-5113-DF11-9CAC-0018F3D09690.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/6A1237D3-4D13-DF11-8FE9-00304866C398.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/62D31887-5413-DF11-B3B8-0018F3D0970E.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/5E422619-4F13-DF11-B157-001A92971BBE.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/5CD0505A-5213-DF11-AE01-0018F3D096F0.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/5ADDC49E-4813-DF11-8B98-001A92810ABA.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/5A260680-5513-DF11-8CC5-0018F3D09710.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/58696828-4B13-DF11-98B7-001731AF6B7F.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/4C36CF63-5113-DF11-BE2F-0017312A247F.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/427CA05E-4413-DF11-B317-001A92811700.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/320B2880-5313-DF11-A826-001A92810A9A.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/30F9C1AE-4913-DF11-A81B-0030486790FE.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/2830D8B2-4B13-DF11-8C2B-001731AF6849.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/22EF8CF5-5413-DF11-B9FA-0018F3D096B6.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/16E34A04-5513-DF11-A887-001BFCDBD160.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/12ED3475-5313-DF11-B89B-001A9281171E.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/10F99461-5213-DF11-A71C-001731AF687F.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/0C7B35B5-4913-DF11-8FE7-0018F3D0969C.root',
       '/store/relval/CMSSW_3_5_0/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V21-v1/0013/0AF55CE4-4D13-DF11-8303-002618FDA26D.root'] );

process = cms.Process("makeNtuple")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.MixingNoPileUp_cff')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
# process.load('Configuration.StandardSequences.L1Reco_cff')
# process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# process.GlobalTag.globaltag = 'MC_31X_V3::All'
process.GlobalTag.globaltag = 'MC_3XY_V21::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))
process.MessageLogger.cerr.FwkReport.reportEvery = 1
#process.MessageLogger.cerr.threshold = 'Info'

# process.source = cms.Source("PoolSource",
# #  fileNames = cms.untracked.vstring('file:cmsData/80_120_splitSST.root'),
# #                             fileNames = cms.untracked.vstring('file:cmsData/scp_3T_2Tk_1k.root'),
#                             fileNames = cms.untracked.vstring('file:cmsData/scp_3T_Qmin_1k.root'),
#   skipEvents = cms.untracked.uint32(0)
# )
process.source = source

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cmsData/clusNtp/clusNtuple.root')
)

#process.Timing = cms.Service("Timing")
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")
process.makeNtuple = cms.EDAnalyzer('ClusterNtuplizer',
                                    clusterSourceLabel = cms.InputTag("siStripClusters")
#                                     clusterSourceLabel = cms.InputTag("siStripSplitClusters")
)

process.rechits = cms.Sequence(process.siPixelRecHits*process.siStripMatchedRecHits)

#process.event = cms.EDAnalyzer("EventContentAnalyzer")
process.p1 = cms.Path(process.mix*process.rechits*process.TrackRefitter*process.makeNtuple)

