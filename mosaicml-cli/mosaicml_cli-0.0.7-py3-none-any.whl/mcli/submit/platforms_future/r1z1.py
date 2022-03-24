# pylint: disable=duplicate-code

""" R1Z! Platform Definition """
from typing import Dict

from mcli.submit.platforms_future.instance_type import InstanceList
from mcli.submit.platforms_future.platform import GenericK8sPlatform
from mcli.submit.platforms_future.r1z1_instances import R1Z1_INSTANCE_LIST

NUM_MULTI_GPU_TOLERATE = 8
MAX_CPUS = 60

R1Z1_PRIORITY_CLASS_LABELS: Dict[str, str] = {
    'scavenge': 'mosaicml-internal-research-scavenge-priority',
    'standard': 'mosaicml-internal-research-standard-priority',
    'emergency': 'mosaicml-internal-research-emergency-priority'
}


class R1Z1Platform(GenericK8sPlatform):
    """ R1Z1 Platform Overrides """

    allowed_instances: InstanceList = R1Z1_INSTANCE_LIST
    priority_class_labels = R1Z1_PRIORITY_CLASS_LABELS  # type: Dict[str, str]
    default_priority_class: str = 'standard'
