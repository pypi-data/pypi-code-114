'''Provides obtain_lock Base Function.'''

import asyncio
import logging

from pymongo.errors import DuplicateKeyError

import nawah.data as Data
from nawah.classes import NAWAH_DOC, NAWAH_ENV, RESULTS, MethodException, Query
from nawah.enums import DELETE_STRATEGY
from nawah.registry import Registry
from nawah.utils import nawah_func

logger = logging.getLogger('nawah')


@nawah_func
async def obtain_lock(*, module_name: str, env: NAWAH_ENV, doc: NAWAH_DOC) -> RESULTS:
    '''Creates a lock for a module by creating a doc in lock collection and confirms
    it is the top lock doc. If not, deletes lock and raises MethodException.'''

    module = Registry.module(module_name)

    if 'total_attempts' not in doc:
        doc['total_attempts'] = doc['attempts']

    logger.debug('Attempting to obtain lock for \'%s\'', module_name)
    try:
        create_results = await Data.create(
            env=env,
            collection_name=module.collection + '_lock',
            doc=doc,
            attrs={},
        )
        logger.debug(
            'Obtained intermediate lock \'%s\' for \'%s\'',
            create_results['docs'][0]['_id'],
            module_name,
        )
        read_results = await Data.read(
            env=env,
            collection_name=module.collection + '_lock',
            attrs={},
            query=Query([{'tags': {'$in': doc['tags']}}, {'$sort': {'_id': 1}}]),
        )
        logger.debug('Attempting to read current lock for \'%s\'', module_name)

        if create_results['docs'][0]['_id'] == read_results['docs'][0]['_id']:
            logger.debug('Successfully obtained lock for \'%s\'', module_name)
            return {
                'status': 200,
                'msg': f'Obtained lock for \'{module_name}\'',
                'args': create_results,
            }
    except DuplicateKeyError:
        create_results = read_results = {'count': 0, 'docs': [{'_id': None}]}

    logger.warning(
        'Failed to obtain lock for \'%s\', with with created lock_id: \'%s\', but read \'%s\'',
        module_name,
        create_results['docs'][0]['_id'],
        read_results['docs'][0]['_id'],
    )

    if create_results['docs'][0]['_id']:
        logger.warning(
            'Deleting lock \'%s\', for \'%s\'',
            create_results['docs'][0]['_id'],
            module_name,
        )
        lock_delete_results = await Data.delete(
            env=env,
            collection_name=module.collection + '_lock',
            attrs={},
            docs=[create_results['docs'][0]['_id']],
            strategy=DELETE_STRATEGY.FORCE_SYS,
        )

        if lock_delete_results['count'] != 1:
            logger.error(
                'Failed to delete failed lock \'%s\' for \'%s\'. Delete manually now.',
                create_results['docs'][0]['_id'],
                module_name,
            )

    if doc['attempts']:
        await asyncio.sleep(0.2)
        logger.warning('Reattempting to obtain lock for \'%s\'', module_name)
        doc['attempts'] -= 1
        return await obtain_lock(module_name=module_name, env=env, doc=doc)

    raise MethodException(
        {
            'status': 400,
            'msg': f'Failed to obtain lock for \'{module_name}\'',
            'args': {
                'code': f'{module.package_name.upper()}_{module_name.upper()}_FAILED_LOCK'
            },
        }
    )
