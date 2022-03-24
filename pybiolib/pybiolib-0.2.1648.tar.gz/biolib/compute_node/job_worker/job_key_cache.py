from biolib.compute_node.job_worker.cache_state import CacheState
from biolib.compute_node.job_worker.cache_types import JobKeyCacheDict


class JobKeyCacheState(CacheState):
    @property
    def _state_path(self) -> str:
        return f'{super()._cache_dir}/job-key-cache-state.json'

    @property
    def _state_lock_path(self) -> str:
        return f'{self._state_path}.lock'

    def _get_default_state(self) -> JobKeyCacheDict:
        return {}
