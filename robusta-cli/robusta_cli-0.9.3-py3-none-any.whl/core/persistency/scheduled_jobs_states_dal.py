import json
import logging
from typing import List, Optional
from threading import Lock

import kubernetes
from hikaru.model import ObjectMeta

from ..model.env_vars import INSTALLATION_NAMESPACE
from ...core.schedule.model import ScheduledJob
from ...integrations.kubernetes.autogenerated.v1.models import ConfigMap

JOBS_CONFIGMAP_NAME = "scheduled-jobs"
CONFIGMAP_NAMESPACE = INSTALLATION_NAMESPACE


class SchedulerDal:
    mutex = Lock()

    def __init__(self):
        self.__init_scheduler_dal()

    def __load_config_map(self) -> ConfigMap:
        return ConfigMap.readNamespacedConfigMap(
            JOBS_CONFIGMAP_NAME, CONFIGMAP_NAMESPACE
        ).obj

    def __init_scheduler_dal(self):
        try:
            self.__load_config_map()
        except kubernetes.client.exceptions.ApiException as e:
            # we only want to catch exceptions because the config map doesn't exist
            if e.reason != "Not Found":
                raise
            # job states configmap doesn't exists, create it
            self.mutex.acquire()
            try:
                conf_map = ConfigMap(
                    metadata=ObjectMeta(
                        name=JOBS_CONFIGMAP_NAME, namespace=CONFIGMAP_NAMESPACE
                    )
                )
                conf_map.createNamespacedConfigMap(conf_map.metadata.namespace)
                logging.info(
                    f"created jobs states configmap {JOBS_CONFIGMAP_NAME} {CONFIGMAP_NAMESPACE}"
                )
            finally:
                self.mutex.release()

    def save_scheduled_job(self, job: ScheduledJob):
        self.mutex.acquire()
        try:
            confMap = self.__load_config_map()
            confMap.data[job.job_id] = job.json()
            confMap.replaceNamespacedConfigMap(
                confMap.metadata.name, confMap.metadata.namespace
            )
        finally:
            self.mutex.release()

    def get_scheduled_job(self, job_id: str) -> Optional[ScheduledJob]:
        state_data = self.__load_config_map().data.get(job_id)
        return (
            ScheduledJob(**json.loads(state_data)) if state_data is not None else None
        )

    def del_scheduled_job(self, job_id: str):
        self.mutex.acquire()
        try:
            confMap = self.__load_config_map()
            if confMap.data.get(job_id) is not None:
                del confMap.data[job_id]
                confMap.replaceNamespacedConfigMap(
                    confMap.metadata.name, confMap.metadata.namespace
                )
        finally:
            self.mutex.release()

    def list_scheduled_jobs(self) -> List[ScheduledJob]:
        return [
            self.get_scheduled_job(job_id)
            for job_id in self.__load_config_map().data.keys()
        ]
