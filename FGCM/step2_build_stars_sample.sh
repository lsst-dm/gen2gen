STACK=w_2020_36
TICKET=26637
srun fgcmBuildStars.py /datasets/hsc/repo --rerun RC/$STACK/DM-${TICKET}-sfm:RC/$STACK/DM-${TICKET}/FGCM --configfile fgcmBuildStarsRC2.py --id ccd=40 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 
