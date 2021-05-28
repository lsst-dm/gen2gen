import os, glob, shutil

WEEK='w_2021_16'
DM='29770'
INDIR='/home/emorgan2/HSC/DC2/DM-'+DM
OUTDIR='/datasets/DC2/repoRun2.2i/rerun/'+WEEK+'/DM-'+DM
LOGDIR=OUTDIR+'/logs/'
if not os.path.exists(LOGDIR):
  os.mkdir(LOGDIR)
QALOGDIR=OUTDIR+'/qaLogs/'

PAIRS=[
["01_singleFrameDriver",INDIR+"/dc2sfm*.o*"],
["02_makeSkyMap",INDIR+"/log_makeSkyMap*"],
["03_coaddDriver",INDIR+"/coadd*.o*"],
["04_multiBandDriver",INDIR+"/mt*.o*"],
["05_matchedVisitMetrics",INDIR+"/slurm*.out"],
]
for PAIR in PAIRS[:8]:
   OUTLOG=LOGDIR+PAIR[0]
   if not os.path.exists(OUTLOG):
      os.mkdir(OUTLOG)
   for FILE in glob.glob(PAIR[1]):
#      print(FILE+' '+OUTLOG)
       shutil.copy(FILE,OUTLOG)

print("Output logs in "+LOGDIR)
