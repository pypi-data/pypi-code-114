from ..service_def import ServiceBuild
from .service_build import package as service_build_package


def package(base_dir, name, service_build: ServiceBuild):
    if type(service_build) is ServiceBuild:
        return service_build_package(base_dir, name, service_build)
    raise RuntimeError(f"Packaging not defined for build type {type(service_build)}")
