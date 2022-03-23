'''Provides cache utilities'''
import datetime
import logging
from typing import TYPE_CHECKING, Protocol, cast

import redis.exceptions

from nawah.config import Config

if TYPE_CHECKING:
    from bson import ObjectId

    from nawah.classes import NAWAH_DOC

logger = logging.getLogger('nawah')

Config.cache_expiry = cast(int, Config.cache_expiry)


class CacheNotConfiguredException(Exception):
    '''raises if a Cache Utility is called while app is not configured for Cache Workflow'''

    pass


class UpdateCacheRemoveCondition(Protocol):
    '''Provides type-hint for \'update_cache\' Utility \'remove_condition\' callable'''

    def __call__(self, *, update_doc: 'NAWAH_DOC') -> bool:
        ...


async def check_cache_connection(attempt: int = 3):
    '''Attempts to read from cache to force re-connection if broken'''

    try:
        await Config._sys_cache.get('__connection')
    except redis.exceptions.ConnectionError as e:
        if attempt != 0:
            return await check_cache_connection(attempt=attempt - 1)

        raise e


async def reset_cache_channel(channel: str):
    '''Resets specific cache `channel` by deleting it from active Redis db'''

    await check_cache_connection()

    try:
        for key in await Config._sys_cache.client.keys(f'{channel}:*'):
            try:
                await Config._sys_cache.client.delete(key.decode('utf-8'))
            except redis.exceptions.ResponseError:
                logger.error('Failed to delete Cache Key: \'%s\'', key)
    except redis.exceptions.ConnectionError:
        logger.error(
            'Connection with Redis server \'%s\' failed. Skipping resetting Cache Channel \'%s\'.',
            Config.cache_server,
            channel,
        )


async def update_cache(
    *,
    channels: list[str],
    docs: list['ObjectId'],
    update_doc: 'NAWAH_DOC',
    remove_condition: 'UpdateCacheRemoveCondition' = None,
):
    if not (cache := Config._sys_cache):
        raise CacheNotConfiguredException()

    remove_key = False
    try:
        if remove_condition:
            remove_key = remove_condition(update_doc=update_doc)
    except:
        remove_key = True

    for channel in channels:

        if channel.endswith(':'):
            channel += '*'
        elif not channel.endswith(':*'):
            channel += ':*'

        try:
            await check_cache_connection()

            for key in await cache.client.keys(channel):
                key = key.decode('utf-8')

                key_docs = await cache.get(key, '.docs')
                for doc in docs:
                    try:
                        doc_index = key_docs.index({'$oid': str(doc)})
                    except ValueError:
                        continue
                    if remove_key:
                        try:
                            await cache.delete(key, '.')
                        except redis.exceptions.ResponseError:
                            logger.error(
                                'Cache command failed with \'ResponseError\'. Current scope:'
                            )
                            logger.error(locals())
                        continue
                    if await cache.get(
                        key, f'.results.args.docs[{doc_index}]._id.$oid'
                    ) != str(doc):
                        try:
                            await cache.delete(key, '.')
                        except redis.exceptions.ResponseError as e:
                            logger.error(
                                'Cache command failed with \'ResponseError\': \'%s\'',
                                e,
                            )
                            logger.error('Current scope: %s', locals())
                    try:
                        for attr_name in update_doc:
                            if update_doc[attr_name] == None:
                                continue
                            await cache.set(
                                key,
                                f'.results.args.docs[{doc_index}].{attr_name}',
                                update_doc[attr_name],
                            )
                    except redis.exceptions.ResponseError as e:
                        logger.error(
                            'Cache command failed with \'ResponseError\': \'%s\'',
                            e,
                        )
                        logger.error('Current scope: %s', locals())
                        logger.error(
                            'Removing key \'%s\' due to failed update attempt.', key
                        )
                        try:
                            await cache.delete(key, '.')
                        except redis.exceptions.ResponseError as e:
                            logger.error(
                                'Cache command failed with \'ResponseError\': \'%s\'',
                                e,
                            )
                            logger.error('Current scope: %s', locals())
                try:
                    await cache.set(
                        key,
                        '.results.args.cache_time',
                        datetime.datetime.utcnow().isoformat(),
                    )
                except redis.exceptions.ResponseError as e:
                    logger.error(
                        'Cache command failed with \'ResponseError\': \'%s\'',
                        e,
                    )
                    logger.error('Current scope: %s', locals())
        except redis.exceptions.ConnectionError:
            logger.error(
                'Connection with Redis server \'%s\' failed. Skipping updating Cache Channel \'%s\'.',
                Config.cache_server,
                channel,
            )
