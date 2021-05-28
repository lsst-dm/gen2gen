STACK=w_2020_36
TICKET=26637
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$STACK/DM-${TICKET}-sfm:RC/$STACK/DM-${TICKET}/FGCM --configfile fgcmFitCycleRC2_cycle00_config.py 
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$STACK/DM-${TICKET}-sfm:RC/$STACK/DM-${TICKET}/FGCM --configfile fgcmFitCycleRC2_cycle01_config.py 
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$STACK/DM-${TICKET}-sfm:RC/$STACK/DM-${TICKET}/FGCM --configfile fgcmFitCycleRC2_cycle02_config.py 
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$STACK/DM-${TICKET}-sfm:RC/$STACK/DM-${TICKET}/FGCM --configfile fgcmFitCycleRC2_cycle03_config.py 
fgcmFitCycle.py /datasets/hsc/repo --rerun RC/$STACK/DM-${TICKET}-sfm:RC/$STACK/DM-${TICKET}/FGCM --configfile fgcmFitCycleRC2_cycle04_config.py --config isFinalCycle=True |& tee fitCycle_final.log
