import json
from os.path import exists
from typing import List

from sonusai import SonusAIError
from sonusai import logger


def load_mixid(mixdb: dict, name: str = None) -> List[int]:
    if name is None:
        mixid = list(range(len(mixdb['mixtures'])))
    else:
        if not exists(name):
            logger.error(f'{name} does not exist')
            raise SonusAIError

        with open(file=name, mode='r', encoding='utf-8') as f:
            mixid = json.load(f)
            if not isinstance(mixid, dict) or 'mixid' not in mixid:
                logger.error(f'Could not find ''mixid'' in {name}')
                raise SonusAIError
            mixid = mixid['mixid']

    return mixid
