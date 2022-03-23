# pylint: disable=duplicate-code

""" R1Z6 Platform Definition """
from typing import Dict, List

from kubernetes import client

from mcli.submit.kubernetes.mcli_job_future import MCLIVolume
from mcli.submit.platforms_future.instance_type import InstanceList
from mcli.submit.platforms_future.platform import GenericK8sPlatform
from mcli.submit.platforms_future.r6z1_instances import R6Z1_INSTANCE_LIST

NUM_MULTI_GPU_TOLERATE = 8
MAX_CPUS = 60

R6Z1_PRIORITY_CLASS_LABELS: Dict[str, str] = {
    'scavenge': 'mosaicml-internal-research-scavenge-priority',
    'standard': 'mosaicml-internal-research-standard-priority',
    'emergency': 'mosaicml-internal-research-emergency-priority'
}


class R6Z1Platform(GenericK8sPlatform):
    """ R6Z1 Platform Overrides """

    allowed_instances: InstanceList = R6Z1_INSTANCE_LIST
    priority_class_labels = R6Z1_PRIORITY_CLASS_LABELS  # type: Dict[str, str]
    default_priority_class: str = 'standard'

    def get_volumes(self) -> List[MCLIVolume]:
        volumes = super().get_volumes()
        volumes.append(
            MCLIVolume(
                volume=client.V1Volume(
                    name='local',
                    host_path=client.V1HostPathVolumeSource(path='/localdisk', type='Directory'),
                ),
                volume_mount=client.V1VolumeMount(
                    name='local',
                    mount_path='/localdisk',
                ),
            ))
        return volumes
