WEEK=w_2021_18
DM=29946
WORKDIR=/datasets/hsc/repo/rerun/RC/${WEEK}/DM-${DM}/
LOGDIR=$WORKDIR/logs/FGCM
mkdir -p $LOGDIR
. /software/lsstsw/stack/loadLSST.bash 
setup lsst_distrib -t $WEEK
fgcmMakeLut.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmMakeLutRC2.py --clobber-config > $LOGDIR/fgcmMakeLut.log 2>&1 
srun fgcmBuildStars.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmBuildStarsRC2.py --id ccd=40 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --clobber-config > $LOGDIR/fgcmBuildStars.log 2>&1 
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmFitCycleRC2_cycle00_config.py --clobber-config > $LOGDIR/fgcmFitCycle_0.log 2>&1 
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmFitCycleRC2_cycle01_config.py --clobber-config > $LOGDIR/fgcmFitCycle_1.log 2>&1
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmFitCycleRC2_cycle02_config.py --clobber-config > $LOGDIR/fgcmFitCycle_2.log 2>&1
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmFitCycleRC2_cycle03_config.py --clobber-config > $LOGDIR/fgcmFitCycle_3.log 2>&1
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}-sfm:RC/$WEEK/DM-${DM}/FGCM --configfile fgcmFitCycleRC2_cycle04_config.py --clobber-config --config isFinalCycle=True |& tee fitCycle_final.log > $LOGDIR/fgcmFitCycle_4.log 2>&1
fgcmOutputProducts.py /datasets/hsc/repo --rerun RC/$WEEK/DM-${DM}/FGCM --configfile fgcmOutputProductsRC2new.py --config cycleNumber=4 --clobber-config > $LOGDIR/fgcmOutputProducts.log 2>&1

ln -s ${WORKDIR}FGCM/fgcm-results $WORKDIR
