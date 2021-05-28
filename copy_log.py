import os, glob, shutil

WEEK='w_2021_18'
DM='29946'
INDIR='/home/emorgan2/HSC/RC2/rerun_scripts/DM-'+DM
OUTDIR='/datasets/hsc/repo/rerun/RC/'+WEEK+'/DM-'+DM
LOGDIR=OUTDIR+'/logs/'
if not os.path.exists(LOGDIR):
  os.mkdir(LOGDIR)
QALOGDIR=OUTDIR+'/qaLogs/'
PAIRS=[["01_makeSkyMap",INDIR+"/makeSkyMap.log"],["02_singleFrameDriver",INDIR+"/sfm*.o*"],["03_jointcal",INDIR+"/jointcal*.log"],["04_skyCorrection",INDIR+"/sky*.o*"],["05_visitAnalysis",QALOGDIR+"/visitAnalysis/visitAnalysis*out"],["06_compareVisitAnalysis",QALOGDIR+"/compareVisitAnalysis/compareVisitAnalysis*out"],["07_coaddDriver",INDIR+"/coadd*.o*"],["08_multiBandDriver",INDIR+"/mt*.o*"],["09_forcedPhotCcd",LOGDIR+"forcedPhotCcd/frCcd*log"],["10_coaddAnalysis",QALOGDIR+"/coaddAnalysis/coaddAnalysis*log"],["11_colorAnalysis",QALOGDIR+"/colorAnalysis/colorAnalysis*log"],["12_compareCoaddAnalysis",QALOGDIR+"/compareCoaddAnalysis/compareCoaddAnalysis*log"],["13_matchVisits",QALOGDIR+"matchVisits/matchVisits*log"],["16_matchedVisitMetrics",QALOGDIR+"/matchedVisitMetrics/matchedVisitMetrics*log"],["18_validateDrp",LOGDIR+"validateDrp/validateDrp*log"],["20_transformObjectCatalog",""],["21_consolidateObjectTable",""],["22_consolidateSourceTable",""]]
for PAIR in PAIRS[:8]:
   OUTLOG=LOGDIR+PAIR[0]
   if not os.path.exists(OUTLOG):
      os.mkdir(OUTLOG)
   for FILE in glob.glob(PAIR[1]):
#      print(FILE+' '+OUTLOG)
       shutil.copy(FILE,OUTLOG)
