from errr import make_tree as _t, exception as _e

_t(
    globals(),
    ScaffoldError=_e(
        SpatialDimensionError=_e(),
        ConfigurationError=_e(
            ConfigurationFormatError=_e(),
            DynamicClassError=_e(ConfigurableClassNotFoundError=_e(),),
            CastError=_e(
                UnionCastError=_e(),
                ConfigurableCastError=_e(
                    UnknownDistributionError=_e(), InvalidDistributionError=_e(),
                ),
            ),
            CastConfigurationError=_e(),
            RequirementError=_e(),
            ReferenceError=_e(),
        ),
        TypeNotFoundError=_e(),
        LayerNotFoundError=_e(),
        SimulationNotFoundError=_e(),
        AdapterError=_e(
            NestError=_e(
                NestKernelError=_e(NestModuleError=_e(),),
                NestModelError=_e(),
                KernelLockedError=_e(),
                SuffixTakenError=_e(),
                ReceptorSpecificationError=_e(),
            )
        ),
        ConnectivityError=_e(FiberTransformError=_e(QuiverFieldError=_e(),),),
        MorphologyError=_e(
            MorphologyRepositoryError=_e(),
            MissingMorphologyError=_e(),
            IncompleteMorphologyError=_e(),
            MorphologyDataError=_e(),
            CompartmentError=_e(),
        ),
        TreeError=_e(),
        VoxelizationError=_e(VoxelTransformError=_e(),),
        ResourceError=_e(
            DatasetNotFoundError=_e(IntersectionDataNotFoundError=_e(),),
            DataNotFoundError=_e(),
            AttributeMissingError=_e(),
            UnknownStorageEngineError=_e(),
        ),
        DataNotProvidedError=_e(),
        PluginError=_e("plugin"),
        ParserError=_e(
            JsonParseError=_e(JsonReferenceError=_e(), JsonImportError=_e(),),
        ),
        OrderError=_e(),
        ClassError=_e(),
    ),
)


## Warnings


class ScaffoldWarning(UserWarning):
    pass


class ConfigurationWarning(ScaffoldWarning):
    pass


class UserUserDeprecationWarning(ScaffoldWarning):
    pass


class PlacementWarning(ScaffoldWarning):
    pass


class ConnectivityWarning(ScaffoldWarning):
    pass


class QuiverFieldWarning(ScaffoldWarning):
    pass


class RepositoryWarning(ScaffoldWarning):
    pass


class SimulationWarning(ScaffoldWarning):
    pass


class KernelWarning(SimulationWarning):
    pass