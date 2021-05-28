import lsst.fgcmcal.fgcmFitCycle
assert type(config)==lsst.fgcmcal.fgcmFitCycle.FgcmFitCycleConfig, 'config is of type %s.%s instead of lsst.fgcmcal.fgcmFitCycle.FgcmFitCycleConfig' % (type(config).__module__, type(config).__name__)
import lsst.pipe.base.config
import lsst.fgcmcal.sedterms
# Flag to enable/disable metadata saving for a task, enabled by default.
config.saveMetadata=True

# Run multiple fit cycles in one task
config.doMultipleCycles=False

# Final cycle number in multiple cycle mode.  The initial cycle is 0, with limited parameters fit.  The next cycle is 1 with full parameter fit.  The final cycle is a clean-up with no parameters fit.  There will be a total of (multipleCycleFinalCycleNumber + 1) cycles run, and the final cycle number cannot be less than 2.
config.multipleCyclesFinalCycleNumber=5

# Bands to run calibration
config.bands=['g', 'r', 'i', 'z', 'N921', 'y']

# Bands to use in atmospheric fit. The bands not listed here will have the atmosphere constrained from the 'fitBands' on the same night. Must be a subset of `config.bands`
config.fitBands=['g', 'r', 'i', 'z', 'N921', 'y']

# Bands that are required for a star to be considered a calibration star. Must be a subset of `config.bands`
config.requiredBands=[]

# Mapping from 'physicalFilter' to band.
config.physicalFilterMap={'HSC-G': 'g', 'HSC-R': 'r', 'HSC-I': 'i', 'HSC-Z': 'z', 'HSC-Y': 'y', 'NB0921': 'N921'}

# Use reference catalog as additional constraint on calibration
config.doReferenceCalibration=True

# Reference star signal-to-noise minimum to use in calibration.  Set to <=0 for no cut.
config.refStarSnMin=50.0

# Number of sigma compared to average mag for reference star to be considered an outlier. Computed per-band, and if it is an outlier in any band it is rejected from fits.
config.refStarOutlierNSig=4.0

# Apply color cuts to reference stars?
config.applyRefStarColorCuts=True

# Number of cores to use
config.nCore=4

# Number of stars to run in each chunk
config.nStarPerRun=200000

# Number of exposures to run in each chunk
config.nExpPerRun=1000

# Fraction of stars to reserve for testing
config.reserveFraction=0.1

# Freeze atmosphere parameters to standard (for testing)
config.freezeStdAtmosphere=False

# Precompute superstar flat for initial cycle
config.precomputeSuperStarInitialCycle=False

# Per-band specification on whether to compute superstar flat on sub-ccd scale. Must have one entry per band.
config.superStarSubCcdDict={'g': True, 'r': True, 'i': True, 'z': True, 'N921': True, 'y': True}

# Order of the 2D chebyshev polynomials for sub-ccd superstar fit. Global default is first-order polynomials, and should be overridden on a camera-by-camera basis depending on the ISR.
config.superStarSubCcdChebyshevOrder=2

# Should the sub-ccd superstar chebyshev matrix be triangular to suppress high-order cross terms?
config.superStarSubCcdTriangular=False

# Number of sigma to clip outliers when selecting for superstar flats
config.superStarSigmaClip=5.0

# Number of sigma to clip outliers per focal-plane.
config.focalPlaneSigmaClip=4.0

# Per-band specification on whether to compute achromatic per-ccd residual ('ccd gray') on a sub-ccd scale.
config.ccdGraySubCcdDict={'g': True, 'r': True, 'i': True, 'z': True, 'N921': True, 'y': True}

# Order of the 2D chebyshev polynomials for sub-ccd gray fit.
config.ccdGraySubCcdChebyshevOrder=1

# Should the sub-ccd gray chebyshev matrix be triangular to suppress high-order cross terms?
config.ccdGraySubCcdTriangular=True

# Per-band specification on whether to compute focal-plane residual ('ccd gray') corrections.
config.ccdGrayFocalPlaneDict={'N387': True, 'g': True, 'r': True, 'i': True, 'N816': True, 'z': True, 'N921': True, 'y': True, 'N1010': True}

# Minimum number of 'good' CCDs required to perform focal-plane gray corrections.  If there are fewer good CCDs then the gray correction is computed per-ccd.
config.ccdGrayFocalPlaneFitMinCcd=50

# Order of the 2D chebyshev polynomials for focal plane fit.
config.ccdGrayFocalPlaneChebyshevOrder=3

# FGCM fit cycle number.  This is automatically incremented after each run and stage of outlier rejection.  See cookbook for details.
config.cycleNumber=3

# Is this the final cycle of the fitting?  Will automatically compute final selection of stars and photometric exposures, and will output zeropoints and standard stars for use in fgcmOutputProducts
config.isFinalCycle=False

# Maximum fit iterations, prior to final cycle.  The number of iterations will always be 0 in the final cycle for cleanup and final selection.
config.maxIterBeforeFinalCycle=50

# Percentile brightest stars on a visit/ccd to use to compute net offset from local background subtraction.
config.deltaMagBkgOffsetPercentile=0.25

# Compute net offset from local background subtraction per-ccd? Otherwise, use computation per visit.
config.deltaMagBkgPerCcd=False

# Boundary (in UTC) from day-to-day
config.utBoundary=0.0

# Mirror wash MJDs
config.washMjds=[56700.0, 57500.0, 57700.0, 58050.0]

# Epoch boundaries in MJD
config.epochMjds=[56700.0, 57420.0, 57606.0, 59000.0]

# Minimum good observations per band
config.minObsPerBand=2

# Observatory latitude
config.latitude=19.8256

# Maximum gray extinction to be considered bright observation
config.brightObsGrayMax=0.15

# Minimum number of good stars per CCD to be used in calibration fit. CCDs with fewer stars will have their calibration estimated from other CCDs in the same visit, with zeropoint error increased accordingly.
config.minStarPerCcd=5

# Minimum number of good CCDs per exposure/visit to be used in calibration fit. Visits with fewer good CCDs will have CCD zeropoints estimated where possible.
config.minCcdPerExp=5

# Maximum error on CCD gray offset to be considered photometric
config.maxCcdGrayErr=0.05

# Minimum number of good stars per exposure/visit to be used in calibration fit. Visits with fewer good stars will have CCD zeropoints estimated where possible.
config.minStarPerExp=100

# Minimum number of good exposures/visits to consider a partly photometric night
config.minExpPerNight=3

# Maximum exposure/visit gray value for initial selection of possible photometric observations.
config.expGrayInitialCut=-0.25

# Per-band specification on maximum (negative) achromatic exposure residual ('gray term') for a visit to be considered photometric.  Must have one entry per band. Broad-band filters should be -0.05.
config.expGrayPhotometricCutDict={'g': -0.0175, 'r': -0.0075, 'i': -0.01, 'z': -0.01, 'N921': -0.025, 'y': -0.0125}

# Per-band specification on maximum (positive) achromatic exposure residual ('gray term') for a visit to be considered photometric.  Must have one entry per band.  Broad-band filters should be 0.2.
config.expGrayHighCutDict={'g': 0.0225, 'r': 0.01, 'i': 0.0125, 'z': 0.0125, 'N921': 0.035, 'y': 0.0175}

# Maximum (negative) exposure gray to be able to recover bad ccds via interpolation. Visits with more gray extinction will only get CCD zeropoints if there are sufficient star observations (minStarPerCcd) on that CCD.
config.expGrayRecoverCut=-1.0

# Per-band specification on maximum exposure variance to be considered possibly photometric.  Must have one entry per band.  Broad-band filters should be 0.0005.
config.expVarGrayPhotometricCutDict={'g': 0.0025, 'r': 0.0025, 'i': 0.0025, 'z': 0.0025, 'N921': 0.05, 'y': 0.0025}

# Maximum exposure gray error to be able to recover bad ccds via interpolation. Visits with more gray variance will only get CCD zeropoints if there are sufficient star observations (minStarPerCcd) on that CCD.
config.expGrayErrRecoverCut=0.05

# Number of aperture bins used in aperture correction fit.  When set to 0no fit will be performed, and the config.aperCorrInputSlopes will be used if available.
config.aperCorrFitNBins=0

# Per-band specification of aperture correction input slope parameters.  These are used on the first fit iteration, and aperture correction parameters will be updated from the data if config.aperCorrFitNBins > 0.  It is recommended to set this when there is insufficient data to fit the parameters (e.g. tract mode).
config.aperCorrInputSlopeDict={'g': -1.1579, 'r': -1.3908, 'i': -1.1436, 'z': -1.6974, 'N921': -1.331, 'y': -1.2057}

config.sedboundaryterms.data={}
config.sedboundaryterms.data['gr']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['gr'].primary='g'

# name of secondary band
config.sedboundaryterms.data['gr'].secondary='r'

config.sedboundaryterms.data['ri']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['ri'].primary='r'

# name of secondary band
config.sedboundaryterms.data['ri'].secondary='i'

config.sedboundaryterms.data['iz']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['iz'].primary='i'

# name of secondary band
config.sedboundaryterms.data['iz'].secondary='z'

config.sedboundaryterms.data['zy']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['zy'].primary='z'

# name of secondary band
config.sedboundaryterms.data['zy'].secondary='y'

config.sedboundaryterms.data['N921z']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['N921z'].primary='N921'

# name of secondary band
config.sedboundaryterms.data['N921z'].secondary='z'

config.sedterms.data={}
config.sedterms.data['g']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['g'].primaryTerm='gr'

# Name of secondary Sedboundaryterm
config.sedterms.data['g'].secondaryTerm='ri'

# Extrapolate to compute SED slope
config.sedterms.data['g'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['g'].constant=1.6

# Primary band name for extrapolation
config.sedterms.data['g'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['g'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['g'].tertiaryBand=None

config.sedterms.data['r']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['r'].primaryTerm='gr'

# Name of secondary Sedboundaryterm
config.sedterms.data['r'].secondaryTerm='ri'

# Extrapolate to compute SED slope
config.sedterms.data['r'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['r'].constant=0.9

# Primary band name for extrapolation
config.sedterms.data['r'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['r'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['r'].tertiaryBand=None

config.sedterms.data['i']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['i'].primaryTerm='ri'

# Name of secondary Sedboundaryterm
config.sedterms.data['i'].secondaryTerm='iz'

# Extrapolate to compute SED slope
config.sedterms.data['i'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['i'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['i'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['i'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['i'].tertiaryBand=None

config.sedterms.data['z']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['z'].primaryTerm='iz'

# Name of secondary Sedboundaryterm
config.sedterms.data['z'].secondaryTerm='zy'

# Extrapolate to compute SED slope
config.sedterms.data['z'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['z'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['z'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['z'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['z'].tertiaryBand=None

config.sedterms.data['y']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['y'].primaryTerm='zy'

# Name of secondary Sedboundaryterm
config.sedterms.data['y'].secondaryTerm='iz'

# Extrapolate to compute SED slope
config.sedterms.data['y'].extrapolated=True

# Adjustment constant for SED slope
config.sedterms.data['y'].constant=0.25

# Primary band name for extrapolation
config.sedterms.data['y'].primaryBand='y'

# Secondary band name for extrapolation
config.sedterms.data['y'].secondaryBand='z'

# Tertiary band name for extrapolation
config.sedterms.data['y'].tertiaryBand='i'

config.sedterms.data['N921']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['N921'].primaryTerm='N921z'

# Name of secondary Sedboundaryterm
config.sedterms.data['N921'].secondaryTerm=None

# Extrapolate to compute SED slope
config.sedterms.data['N921'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['N921'].constant=0.5

# Primary band name for extrapolation
config.sedterms.data['N921'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['N921'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['N921'].tertiaryBand=None

# Maximum mag error for fitting sigma_FGCM
config.sigFgcmMaxErr=0.01

# Per-band specification for maximum (absolute) achromatic residual (gray value) for observations in sigma_fgcm (raw repeatability).  Broad-band filters should be 0.05.
config.sigFgcmMaxEGrayDict={'g': 0.05, 'r': 0.05, 'i': 0.05, 'z': 0.05, 'N921': 0.15, 'y': 0.05}

# Maximum error on a star observation to use in ccd gray (achromatic residual) computation
config.ccdGrayMaxStarErr=0.1

# Per-band specification of the approximate overall throughput at the start of calibration observations.  Must have one entry per band.  Typically should be 1.0.
config.approxThroughputDict={'g': 1.0, 'r': 1.0, 'i': 1.0, 'z': 1.0, 'N921': 1.0, 'y': 1.0}

# Allowed range for systematic error floor estimation
config.sigmaCalRange=[0.001, 0.003]

# Magnitude percentile range to fit systematic error floor
config.sigmaCalFitPercentile=[0.05, 0.15]

# Magnitude percentile range to plot systematic error floor
config.sigmaCalPlotPercentile=[0.05, 0.95]

# Systematic error floor for all zeropoints
config.sigma0Phot=0.003

# Reference longitude for plotting maps
config.mapLongitudeRef=0.0

# Healpix nside for plotting maps
config.mapNSide=256

# Filename start for plot output files
config.outfileBase='fgcmFitCycleRC2'

# Encoded star-color cuts (to be cleaned up)
config.starColorCuts=['g,r,-0.25,2.25', 'r,i,-0.50,2.25', 'i,z,-0.50,1.00', 'g,i,0.0,3.5']

# Band names to use to split stars by color.  Must have 2 entries.
config.colorSplitBands=['g', 'i']

# Should FGCM model the magnitude errors from sky/fwhm? (False means trust inputs)
config.modelMagErrors=True

# Model PWV with a quadratic term for variation through the night?
config.useQuadraticPwv=False

# Model instrumental parameters per band? Otherwise, instrumental parameters (QE changes with time) are shared among all bands.
config.instrumentParsPerBand=True

# Minimum time change (in days) between observations to use in constraining instrument slope.
config.instrumentSlopeMinDeltaT=20.0

# Fit (intraband) mirror chromatic term?
config.fitMirrorChromaticity=False

# Mirror coating dates in MJD
config.coatingMjds=[56650.0, 58050.0]

# Output standard stars prior to final cycle?  Used in debugging.
config.outputStandardsBeforeFinalCycle=False

# Output standard stars prior to final cycle?  Used in debugging.
config.outputZeropointsBeforeFinalCycle=False

# Per-band specification on whether to use star repeatability (instead of exposures) for computing photometric cuts. Recommended for tract mode or bands with few visits.
config.useRepeatabilityForExpGrayCutsDict={'g': False, 'r': False, 'i': False, 'z': False, 'N921': True, 'y': False}

# Number of sigma for automatic computation of (low) photometric cut. Cut is based on exposure gray width (per band), unless useRepeatabilityForExpGrayCuts is set, in which case the star repeatability is used (also per band).
config.autoPhotometricCutNSig=3.0

# Number of sigma for automatic computation of (high) outlier cut. Cut is based on exposure gray width (per band), unless useRepeatabilityForExpGrayCuts is set, in which case the star repeatability is used (also per band).
config.autoHighCutNSig=4.0

# Be less verbose with logging.
config.quietMode=False

# Make fgcm QA plots.
config.doPlots=True

# Random seed for fgcm for consistency in tests.
config.randomSeed=89234

# name for connection camera
config.connections.camera='camera'

# name for connection fgcmLookUpTable
config.connections.fgcmLookUpTable='fgcmLookUpTable'

# name for connection fgcmVisitCatalog
config.connections.fgcmVisitCatalog='fgcmVisitCatalog'

# name for connection fgcmStarObservations
config.connections.fgcmStarObservations='fgcmStarObservations'

# name for connection fgcmStarIds
config.connections.fgcmStarIds='fgcmStarIds'

# name for connection fgcmStarIndices
config.connections.fgcmStarIndices='fgcmStarIndices'

# name for connection fgcmReferenceStars
config.connections.fgcmReferenceStars='fgcmReferenceStars'

# name for connection fgcmFlaggedStarsInput
config.connections.fgcmFlaggedStarsInput='fgcmFlaggedStars{previousCycleNumber}'

# name for connection fgcmFitParametersInput
config.connections.fgcmFitParametersInput='fgcmFitParameters{previousCycleNumber}'

# name for connection fgcmFitParameters
config.connections.fgcmFitParameters='fgcmFitParameters{cycleNumber}'

# name for connection fgcmFlaggedStars
config.connections.fgcmFlaggedStars='fgcmFlaggedStars{cycleNumber}'

# name for connection fgcmZeropoints
config.connections.fgcmZeropoints='fgcmZeropoints{cycleNumber}'

# name for connection fgcmAtmosphereParameters
config.connections.fgcmAtmosphereParameters='fgcmAtmosphereParameters{cycleNumber}'

# name for connection fgcmStandardStars
config.connections.fgcmStandardStars='fgcmStandardStars{cycleNumber}'

# name for connection fgcmFitParameters0
config.connections.fgcmFitParameters0='fgcmFitParameters0'

# name for connection fgcmFlaggedStars0
config.connections.fgcmFlaggedStars0='fgcmFlaggedStars0'

# name for connection fgcmZeropoints0
config.connections.fgcmZeropoints0='fgcmZeropoints0'

# name for connection fgcmAtmosphereParameters0
config.connections.fgcmAtmosphereParameters0='fgcmAtmosphereParameters0'

# name for connection fgcmStandardStars0
config.connections.fgcmStandardStars0='fgcmStandardStars0'

# name for connection fgcmFitParameters1
config.connections.fgcmFitParameters1='fgcmFitParameters1'

# name for connection fgcmFlaggedStars1
config.connections.fgcmFlaggedStars1='fgcmFlaggedStars1'

# name for connection fgcmZeropoints1
config.connections.fgcmZeropoints1='fgcmZeropoints1'

# name for connection fgcmAtmosphereParameters1
config.connections.fgcmAtmosphereParameters1='fgcmAtmosphereParameters1'

# name for connection fgcmStandardStars1
config.connections.fgcmStandardStars1='fgcmStandardStars1'

# name for connection fgcmFitParameters2
config.connections.fgcmFitParameters2='fgcmFitParameters2'

# name for connection fgcmFlaggedStars2
config.connections.fgcmFlaggedStars2='fgcmFlaggedStars2'

# name for connection fgcmZeropoints2
config.connections.fgcmZeropoints2='fgcmZeropoints2'

# name for connection fgcmAtmosphereParameters2
config.connections.fgcmAtmosphereParameters2='fgcmAtmosphereParameters2'

# name for connection fgcmStandardStars2
config.connections.fgcmStandardStars2='fgcmStandardStars2'

# name for connection fgcmFitParameters3
config.connections.fgcmFitParameters3='fgcmFitParameters3'

# name for connection fgcmFlaggedStars3
config.connections.fgcmFlaggedStars3='fgcmFlaggedStars3'

# name for connection fgcmZeropoints3
config.connections.fgcmZeropoints3='fgcmZeropoints3'

# name for connection fgcmAtmosphereParameters3
config.connections.fgcmAtmosphereParameters3='fgcmAtmosphereParameters3'

# name for connection fgcmStandardStars3
config.connections.fgcmStandardStars3='fgcmStandardStars3'

# name for connection fgcmFitParameters4
config.connections.fgcmFitParameters4='fgcmFitParameters4'

# name for connection fgcmFlaggedStars4
config.connections.fgcmFlaggedStars4='fgcmFlaggedStars4'

# name for connection fgcmZeropoints4
config.connections.fgcmZeropoints4='fgcmZeropoints4'

# name for connection fgcmAtmosphereParameters4
config.connections.fgcmAtmosphereParameters4='fgcmAtmosphereParameters4'

# name for connection fgcmStandardStars4
config.connections.fgcmStandardStars4='fgcmStandardStars4'

# name for connection fgcmFitParameters5
config.connections.fgcmFitParameters5='fgcmFitParameters5'

# name for connection fgcmFlaggedStars5
config.connections.fgcmFlaggedStars5='fgcmFlaggedStars5'

# name for connection fgcmZeropoints5
config.connections.fgcmZeropoints5='fgcmZeropoints5'

# name for connection fgcmAtmosphereParameters5
config.connections.fgcmAtmosphereParameters5='fgcmAtmosphereParameters5'

# name for connection fgcmStandardStars5
config.connections.fgcmStandardStars5='fgcmStandardStars5'

# name for connection fgcmFitParameters6
config.connections.fgcmFitParameters6='fgcmFitParameters6'

# name for connection fgcmFlaggedStars6
config.connections.fgcmFlaggedStars6='fgcmFlaggedStars6'

# name for connection fgcmZeropoints6
config.connections.fgcmZeropoints6='fgcmZeropoints6'

# name for connection fgcmAtmosphereParameters6
config.connections.fgcmAtmosphereParameters6='fgcmAtmosphereParameters6'

# name for connection fgcmStandardStars6
config.connections.fgcmStandardStars6='fgcmStandardStars6'

# name for connection fgcmFitParameters7
config.connections.fgcmFitParameters7='fgcmFitParameters7'

# name for connection fgcmFlaggedStars7
config.connections.fgcmFlaggedStars7='fgcmFlaggedStars7'

# name for connection fgcmZeropoints7
config.connections.fgcmZeropoints7='fgcmZeropoints7'

# name for connection fgcmAtmosphereParameters7
config.connections.fgcmAtmosphereParameters7='fgcmAtmosphereParameters7'

# name for connection fgcmStandardStars7
config.connections.fgcmStandardStars7='fgcmStandardStars7'

# name for connection fgcmFitParameters8
config.connections.fgcmFitParameters8='fgcmFitParameters8'

# name for connection fgcmFlaggedStars8
config.connections.fgcmFlaggedStars8='fgcmFlaggedStars8'

# name for connection fgcmZeropoints8
config.connections.fgcmZeropoints8='fgcmZeropoints8'

# name for connection fgcmAtmosphereParameters8
config.connections.fgcmAtmosphereParameters8='fgcmAtmosphereParameters8'

# name for connection fgcmStandardStars8
config.connections.fgcmStandardStars8='fgcmStandardStars8'

# name for connection fgcmFitParameters9
config.connections.fgcmFitParameters9='fgcmFitParameters9'

# name for connection fgcmFlaggedStars9
config.connections.fgcmFlaggedStars9='fgcmFlaggedStars9'

# name for connection fgcmZeropoints9
config.connections.fgcmZeropoints9='fgcmZeropoints9'

# name for connection fgcmAtmosphereParameters9
config.connections.fgcmAtmosphereParameters9='fgcmAtmosphereParameters9'

# name for connection fgcmStandardStars9
config.connections.fgcmStandardStars9='fgcmStandardStars9'

# Template parameter used to format corresponding field template parameter
config.connections.previousCycleNumber='2'

# Template parameter used to format corresponding field template parameter
config.connections.cycleNumber='3'

