DC2_filterMap = {band:'lsst_%s_smeared' % (band) for band in 'ugrizy'}
config.processCcd.calibrate.astromRefObjLoader.filterMap = DC2_filterMap
config.processCcd.calibrate.photoRefObjLoader.filterMap = DC2_filterMap
