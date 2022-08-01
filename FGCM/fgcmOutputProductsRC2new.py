import lsst.fgcmcal.fgcmOutputProducts
assert type(config)==lsst.fgcmcal.fgcmOutputProducts.FgcmOutputProductsConfig, 'config is of type %s.%s instead of lsst.fgcmcal.fgcmOutputProducts.FgcmOutputProductsConfig' % (type(config).__module__, type(config).__name__)
import lsst.pipe.tasks.colorterms
import lsst.meas.algorithms.sourceSelector
import lsst.meas.algorithms.ingestIndexReferenceTask
import lsst.pipe.tasks.photoCal
import lsst.meas.algorithms.loadIndexedReferenceObjects
import lsst.meas.astrom.directMatch
import lsst.meas.algorithms.reserveSourcesTask
import lsst.meas.algorithms.indexerRegistry
# Final fit cycle from FGCM fit
config.cycleNumber=4

# Transfer 'absolute' calibration from reference catalog? This afterburner step is unnecessary if reference stars were used in the full fit in FgcmFitCycleTask.
config.doReferenceCalibration=False

# Output standard stars in reference catalog format
config.doRefcatOutput=True

# Output atmospheres in transmission_atmosphere_fgcm format
config.doAtmosphereOutput=True

# Output zeropoints in fgcm_photoCalib format
config.doZeropointOutput=True

# Compose Jacobian of WCS with fgcm calibration for output photoCalib?
config.doComposeWcsJacobian=True

# Padding to add to 4 all edges of the bounding box (pixels)
config.refObjLoader.pixelMargin=300

# Default reference catalog filter to use if filter not specified in exposure; if blank then filter must be specified in exposure
# config.refObjLoader.defaultFilter='g, r, i, z, N921, y'

# Mapping of camera filter name: reference catalog filter name; each reference filter must exist
config.refObjLoader.filterMap={}

# Require that the fields needed to correct proper motion (epoch, pm_ra and pm_dec) are present?
config.refObjLoader.requireProperMotion=False

# Name of the ingested reference dataset
config.refObjLoader.ref_dataset_name='cal_ref_cat'

# Matching radius, arcsec
config.photoCal.match.matchRadius=0.25

# Apply flux limit?
config.photoCal.match.sourceSelection.doFluxLimit=False

# Apply flag limitation?
config.photoCal.match.sourceSelection.doFlags=True

# Apply unresolved limitation?
config.photoCal.match.sourceSelection.doUnresolved=False

# Apply signal-to-noise limit?
config.photoCal.match.sourceSelection.doSignalToNoise=True

# Apply isolated limitation?
config.photoCal.match.sourceSelection.doIsolated=False

# Select objects with value greater than this
config.photoCal.match.sourceSelection.fluxLimit.minimum=None

# Select objects with value less than this
config.photoCal.match.sourceSelection.fluxLimit.maximum=None

# Name of the source flux field to use.
config.photoCal.match.sourceSelection.fluxLimit.fluxField='slot_CalibFlux_instFlux'

# List of source flag fields that must be set for a source to be used.
config.photoCal.match.sourceSelection.flags.good=[]

# List of source flag fields that must NOT be set for a source to be used.
config.photoCal.match.sourceSelection.flags.bad=['flag_badStar']

# Select objects with value greater than this
config.photoCal.match.sourceSelection.unresolved.minimum=None

# Select objects with value less than this
config.photoCal.match.sourceSelection.unresolved.maximum=0.5

# Name of column for star/galaxy separation
config.photoCal.match.sourceSelection.unresolved.name='base_ClassificationExtendedness_value'

# Select objects with value greater than this
config.photoCal.match.sourceSelection.signalToNoise.minimum=10.0

# Select objects with value less than this
config.photoCal.match.sourceSelection.signalToNoise.maximum=None

# Name of the source flux field to use.
config.photoCal.match.sourceSelection.signalToNoise.fluxField='instFlux'

# Name of the source flux error field to use.
config.photoCal.match.sourceSelection.signalToNoise.errField='instFluxErr'

# Name of column for parent
config.photoCal.match.sourceSelection.isolated.parentName='parent'

# Name of column for nChild
config.photoCal.match.sourceSelection.isolated.nChildName='deblend_nChild'

# Apply magnitude limit?
config.photoCal.match.referenceSelection.doMagLimit=False

# Apply flag limitation?
config.photoCal.match.referenceSelection.doFlags=False

# Apply unresolved limitation?
config.photoCal.match.referenceSelection.doUnresolved=False

# Apply signal-to-noise limit?
config.photoCal.match.referenceSelection.doSignalToNoise=True

# Apply magnitude error limit?
config.photoCal.match.referenceSelection.doMagError=False

# Select objects with value greater than this
config.photoCal.match.referenceSelection.magLimit.minimum=None

# Select objects with value less than this
config.photoCal.match.referenceSelection.magLimit.maximum=None

# Name of the source flux field to use.
config.photoCal.match.referenceSelection.magLimit.fluxField='flux'

# List of source flag fields that must be set for a source to be used.
config.photoCal.match.referenceSelection.flags.good=[]

# List of source flag fields that must NOT be set for a source to be used.
config.photoCal.match.referenceSelection.flags.bad=[]

# Select objects with value greater than this
config.photoCal.match.referenceSelection.unresolved.minimum=None

# Select objects with value less than this
config.photoCal.match.referenceSelection.unresolved.maximum=0.5

# Name of column for star/galaxy separation
config.photoCal.match.referenceSelection.unresolved.name='base_ClassificationExtendedness_value'

# Select objects with value greater than this
config.photoCal.match.referenceSelection.signalToNoise.minimum=10.0

# Select objects with value less than this
config.photoCal.match.referenceSelection.signalToNoise.maximum=None

# Name of the source flux field to use.
config.photoCal.match.referenceSelection.signalToNoise.fluxField='flux'

# Name of the source flux error field to use.
config.photoCal.match.referenceSelection.signalToNoise.errField='flux_err'

# Select objects with value greater than this
config.photoCal.match.referenceSelection.magError.minimum=None

# Select objects with value less than this
config.photoCal.match.referenceSelection.magError.maximum=None

# Name of the source flux error field to use.
config.photoCal.match.referenceSelection.magError.magErrField='mag_err'

config.photoCal.match.referenceSelection.colorLimits={}
# Fraction of candidates to reserve from fitting; none if <= 0
config.photoCal.reserve.fraction=0.0

# This number will be added to the exposure ID to set the random seed for reserving candidates
config.photoCal.reserve.seed=1

# Name of the source instFlux field to use.  The associated flag field
# ('<name>_flags') will be implicitly included in badFlags.
config.photoCal.fluxField='instFlux'

# Apply photometric color terms to reference stars? One of:
# None: apply if colorterms and photoCatName are not None;
#       fail if color term data is not available for the specified ref catalog and filter.
# True: always apply colorterms; fail if color term data is not available for the
#       specified reference catalog and filter.
# False: do not apply.
config.photoCal.applyColorTerms=False

# maximum sigma to use when clipping
config.photoCal.sigmaMax=0.25

# clip at nSigma
config.photoCal.nSigma=3.0

# use median instead of mean to compute zeropoint
config.photoCal.useMedian=True

# number of iterations
config.photoCal.nIter=20

config.photoCal.colorterms.data={}
# Name of photometric reference catalog; used to select a color term dict in colorterms. see also applyColorTerms
config.photoCal.photoCatName=None

# Additional magnitude uncertainty to be added in quadrature with measurement errors.
config.photoCal.magErrFloor=0.003

# Healpix nside to pixelize catalog to compare to reference catalog
config.referencePixelizationNside=64

# Minimum number of stars per healpix pixel to select for comparisonto the specified reference catalog
config.referencePixelizationMinStars=200

# Minimum number of stars matched to reference catalog to be used in statistics
config.referenceMinMatch=50

# Number of healpix pixels to sample to do comparison. Doing too many will take a long time and not yield any more precise results because the final number is the median offset (per band) from the set of pixels.
config.referencePixelizationNPixels=100

# Version number of the persisted on-disk storage format.
# Version 0 had Jy as flux units (default 0 for unversioned catalogs).
# Version 1 had nJy as flux units.
config.datasetConfig.format_version=1

# String to pass to the butler to retrieve persisted files.
config.datasetConfig.ref_dataset_name='fgcm_stars'

# Depth of the HTM tree to make.  Default is depth=7 which gives ~ 0.3 sq. deg. per trixel.
config.datasetConfig.indexer['HTM'].depth=7

config.datasetConfig.indexer.name='HTM'
