# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ComputeEngineTargetDefaultsDiskType',
    'ComputeEngineTargetDefaultsLicenseType',
    'ComputeSchedulingOnHostMaintenance',
    'ComputeSchedulingRestartType',
    'SchedulingNodeAffinityOperator',
    'TargetVMDetailsDiskType',
    'TargetVMDetailsLicenseType',
    'UtilizationReportTimeFrame',
    'VmwareVmDetailsPowerState',
]


class ComputeEngineTargetDefaultsDiskType(str, Enum):
    """
    The disk type to use in the VM.
    """
    COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED = "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED"
    """
    An unspecified disk type. Will be used as STANDARD.
    """
    COMPUTE_ENGINE_DISK_TYPE_STANDARD = "COMPUTE_ENGINE_DISK_TYPE_STANDARD"
    """
    A Standard disk type.
    """
    COMPUTE_ENGINE_DISK_TYPE_SSD = "COMPUTE_ENGINE_DISK_TYPE_SSD"
    """
    SSD hard disk type.
    """
    COMPUTE_ENGINE_DISK_TYPE_BALANCED = "COMPUTE_ENGINE_DISK_TYPE_BALANCED"
    """
    An alternative to SSD persistent disks that balance performance and cost.
    """


class ComputeEngineTargetDefaultsLicenseType(str, Enum):
    """
    The license type to use in OS adaptation.
    """
    COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT = "COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT"
    """
    The license type is the default for the OS.
    """
    COMPUTE_ENGINE_LICENSE_TYPE_PAYG = "COMPUTE_ENGINE_LICENSE_TYPE_PAYG"
    """
    The license type is Pay As You Go license type.
    """
    COMPUTE_ENGINE_LICENSE_TYPE_BYOL = "COMPUTE_ENGINE_LICENSE_TYPE_BYOL"
    """
    The license type is Bring Your Own License type.
    """


class ComputeSchedulingOnHostMaintenance(str, Enum):
    """
    How the instance should behave when the host machine undergoes maintenance that may temporarily impact instance performance.
    """
    ON_HOST_MAINTENANCE_UNSPECIFIED = "ON_HOST_MAINTENANCE_UNSPECIFIED"
    """
    An unknown, unexpected behavior.
    """
    TERMINATE = "TERMINATE"
    """
    Terminate the instance when the host machine undergoes maintenance.
    """
    MIGRATE = "MIGRATE"
    """
    Migrate the instance when the host machine undergoes maintenance.
    """


class ComputeSchedulingRestartType(str, Enum):
    """
    Whether the Instance should be automatically restarted whenever it is terminated by Compute Engine (not terminated by user). This configuration is identical to `automaticRestart` field in Compute Engine create instance under scheduling. It was changed to an enum (instead of a boolean) to match the default value in Compute Engine which is automatic restart.
    """
    RESTART_TYPE_UNSPECIFIED = "RESTART_TYPE_UNSPECIFIED"
    """
    Unspecified behavior. This will use the default.
    """
    AUTOMATIC_RESTART = "AUTOMATIC_RESTART"
    """
    The Instance should be automatically restarted whenever it is terminated by Compute Engine.
    """
    NO_AUTOMATIC_RESTART = "NO_AUTOMATIC_RESTART"
    """
    The Instance isn't automatically restarted whenever it is terminated by Compute Engine.
    """


class SchedulingNodeAffinityOperator(str, Enum):
    """
    The operator to use for the node resources specified in the `values` parameter.
    """
    OPERATOR_UNSPECIFIED = "OPERATOR_UNSPECIFIED"
    """
    An unknown, unexpected behavior.
    """
    IN_ = "IN"
    """
    The node resource group should be in these resources affinity.
    """
    NOT_IN = "NOT_IN"
    """
    The node resource group should not be in these resources affinity.
    """


class TargetVMDetailsDiskType(str, Enum):
    """
    The disk type to use in the VM.
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    """
    An unspecified disk type. Will be used as STANDARD.
    """
    STANDARD = "STANDARD"
    """
    A Standard disk type.
    """
    BALANCED = "BALANCED"
    """
    An alternative to SSD persistent disks that balance performance and cost.
    """
    SSD = "SSD"
    """
    SSD hard disk type.
    """


class TargetVMDetailsLicenseType(str, Enum):
    """
    The license type to use in OS adaptation.
    """
    DEFAULT = "DEFAULT"
    """
    The license type is the default for the OS.
    """
    PAYG = "PAYG"
    """
    The license type is Pay As You Go license type.
    """
    BYOL = "BYOL"
    """
    The license type is Bring Your Own License type.
    """


class UtilizationReportTimeFrame(str, Enum):
    """
    Time frame of the report.
    """
    TIME_FRAME_UNSPECIFIED = "TIME_FRAME_UNSPECIFIED"
    """
    The time frame was not specified and will default to WEEK.
    """
    WEEK = "WEEK"
    """
    One week.
    """
    MONTH = "MONTH"
    """
    One month.
    """
    YEAR = "YEAR"
    """
    One year.
    """


class VmwareVmDetailsPowerState(str, Enum):
    """
    The power state of the VM at the moment list was taken.
    """
    POWER_STATE_UNSPECIFIED = "POWER_STATE_UNSPECIFIED"
    """
    Power state is not specified.
    """
    ON = "ON"
    """
    The VM is turned ON.
    """
    OFF = "OFF"
    """
    The VM is turned OFF.
    """
    SUSPENDED = "SUSPENDED"
    """
    The VM is suspended. This is similar to hibernation or sleep mode.
    """
