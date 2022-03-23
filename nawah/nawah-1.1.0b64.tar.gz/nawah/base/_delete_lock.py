'''Provides delete_lock Base Function.'''

import logging

import nawah.data as Data
from nawah.classes import NAWAH_ENV, RESULTS, Query
from nawah.enums import DELETE_STRATEGY
from nawah.registry import Registry
from nawah.utils import nawah_func

logger = logging.getLogger('nawah')


@nawah_func
async def delete_lock(*, module_name: str, env: NAWAH_ENV, query: Query) -> RESULTS:
    '''Deletes locks for a module matching query \'query\'. If not, raises MethodException.'''

    module = Registry.module(module_name)

    docs_results = results = await Data.read(
        env=env,
        collection_name=module.collection + '_lock',
        attrs={},
        query=query,
        skip_process=True,
    )
    results = await Data.delete(
        env=env,
        collection_name=module.collection + '_lock',
        attrs={},
        docs=[doc['_id'] for doc in docs_results['docs']],
        strategy=DELETE_STRATEGY.FORCE_SYS,
    )

    return {
        'status': 200,
        'msg': f'Deleted {results["count"]} docs.',
        'args': results,
    }
