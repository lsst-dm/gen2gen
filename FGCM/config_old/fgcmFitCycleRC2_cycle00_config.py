"""
HSC-specific overrides for FgcmFitCycle
"""

from lsst.fgcmcal import Sedterm, Sedboundaryterm

# Output file base name for diagnostic plots
config.outfileBase = 'fgcmFitCycleRC2'
# Bands to be used in the fit
config.bands = ['g', 'r', 'i', 'z', 'N921', 'y']
config.fitBands = ['g', 'r', 'i', 'z', 'N921', 'y']
config.filterMap = {'g': 'g', 'r': 'r', 'i': 'i',
                    'z': 'z', 'y': 'y',
                    'N921': 'N921'}
config.maxIterBeforeFinalCycle = 50
# Number of cores to run with python multiprocessing
config.nCore = 4
# Cycle number (should start at 0)
config.cycleNumber = 0
# Value to add to MJD to ensure that different MJDs fall on different nights
# This value will depend on your longitude/time zone!
config.utBoundary = 0.0
# MJD dates on which the mirror was washed
config.washMjds = (56700.0, 57500.0, 57700.0, 58050.0)
# Dividing point between observing epochs (years, camera events, etc.)
config.epochMjds = (56700., 57420., 57606., 59000.0)
# Latitude of the observatory
config.latitude = 19.8256
config.expGrayPhotometricCutDict = {'g': -0.05,
                                    'r': -0.05,
                                    'i': -0.05,
                                    'z': -0.05,
                                    'N921': -0.05,
                                    'y': -0.05}
config.expGrayHighCutDict = {'g': 0.2,
                             'r': 0.2,
                             'i': 0.2,
                             'z': 0.2,
                             'N921': 0.2,
                             'y': 0.2}
config.aperCorrFitNBins = 0
config.aperCorrInputSlopeDict = {'g': -1.1579,
                                 'r': -1.3908,
                                 'i': -1.1436,
                                 'z': -1.6974,
                                 'N921': -1.3310,
                                 'y': -1.2057}
# Mapping from bands to SED boundary term names used is sedterms.
config.sedboundaryterms.data = {'gr': Sedboundaryterm(primary='g', secondary='r'),
                                'ri': Sedboundaryterm(primary='r', secondary='i'),
                                'iz': Sedboundaryterm(primary='i', secondary='z'),
                                'zy': Sedboundaryterm(primary='z', secondary='y'),
                                'N921z': Sedboundaryterm(primary='N921', secondary='z')}
# Mapping from terms to bands for fgcm linear SED approximations.
config.sedterms.data = {'g': Sedterm(primaryTerm='gr', secondaryTerm='ri', constant=1.6),
                        'r': Sedterm(primaryTerm='gr', secondaryTerm='ri', constant=0.9),
                        'i': Sedterm(primaryTerm='ri', secondaryTerm='iz', constant=1.0),
                        'z': Sedterm(primaryTerm='iz', secondaryTerm='zy', constant=1.0),
                        'y': Sedterm(primaryTerm='zy', secondaryTerm='iz', constant=0.25,
                                     extrapolated=True, primaryBand='y', secondaryBand='z',
                                     tertiaryBand='i'),
                        'N921': Sedterm(primaryTerm='N921z', constant=0.5)}
# Color cuts for stars to use for calibration.  Each element is a string with
# band1, band2, range_low, range_high such that range_low < (band1 - band2) < range_high
config.starColorCuts = ('g,r,-0.25,2.25',
                        'r,i,-0.50,2.25',
                        'i,z,-0.50,1.00',
                        'g,i,0.0,3.5')
config.colorSplitBands = ['g', 'i']
# Freeze atmosphere to standard values?  Recommended for first fit cycle.
config.freezeStdAtmosphere = True
# Precompute "superstar" in initial cycle (==00) based on bright star observations?  Recommended for HSC.
config.precomputeSuperStarInitialCycle = True
config.superStarSubCcdDict = {'g': True,
                              'r': True,
                              'i': True,
                              'z': True,
                              'N921': True,
                              'y': True}
# Chebyshev order of sub-ccd superstar fits
config.superStarSubCcdChebyshevOrder = 2
config.ccdGraySubCcdDict = {'g': True,
                            'r': True,
                            'i': True,
                            'z': True,
                            'N921': True,
                            'y': True}
# Model instrumental variation over time per band
config.instrumentParsPerBand = True
config.minStarPerExp = 100
config.expVarGrayPhotometricCutDict = {'g': 0.0025,
                                       'r': 0.0025,
                                       'i': 0.0025,
                                       'z': 0.0025,
                                       'N921': 0.05,
                                       'y': 0.0025}
config.minExpPerNight = 3
config.useRepeatabilityForExpGrayCutsDict = {'g': False,
                                             'r': False,
                                             'i': False,
                                             'z': False,
                                             'N921': True,
                                             'y': False}
config.sigFgcmMaxEGrayDict = {'g': 0.05,
                              'r': 0.05,
                              'i': 0.05,
                              'z': 0.05,
                              'N921': 0.15,
                              'y': 0.05}
config.approxThroughputDict = {'g': 1.0,
                               'r': 1.0,
                               'i': 1.0,
                               'z': 1.0,
                               'N921': 1.0,
                               'y': 1.0}

# Use reference catalog as additional constraint on calibration
config.doReferenceCalibration = True
# Reference star signal-to-noise minimum to use in calibration
config.refStarSnMin = 50.0
# Number of sigma compared to average mag for reference star to be considered an outlier
config.refStarOutlierNSig = 4.0
