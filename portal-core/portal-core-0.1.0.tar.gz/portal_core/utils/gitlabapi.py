""" API Wrapper for Gitlab RESTapi """
import json
import logging
import os
import urllib.request
from urllib.error import HTTPError

from django.conf import settings

logger = logging.getLogger('django')

GITLAB_API_KEY = getattr(settings, 'GITLAB_API_KEY',
                         os.getenv('GITLAB_API_KEY', ''))
GITLAB_API_BASE = getattr(settings, 'GITLAB_API_BASE',
                          'https://gitlab.com/api/v4')
GITLAB_PROJECT_ID = getattr(settings, 'GITLAB_PROJECT_ID',
                            os.getenv('GITLAB_PROJECT_ID', ''))


def __request(url, data_dict={}, method='GET'):
    headers = {
        'PRIVATE-TOKEN': GITLAB_API_KEY,
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = json.dumps(data_dict).encode('utf-8')
    request = urllib.request.Request(
        url, data=data, headers=headers, method=method)

    if settings.DEBUG:
        logger.info('data: {}'.format(data.decode('utf-8')))
        return {'iid': 12345}

    try:
        response = urllib.request.urlopen(request)  # nosec
    except HTTPError as error:
        response = error
    try:
        result = json.loads(response.read().decode('utf-8'))
    except json.JSONDecodeError:
        post_data = data.decode('utf-8')
        logger.error(f'Json Decode Error: Post data is "{post_data}"')
        result = {}
    return result


def create_issue(title, description, **kwargs):
    """ 課題を作成する """
    data = {
        'title': title,
        'description': description,
    }
    data.update(kwargs)
    res = __request(
        f'{GITLAB_API_BASE}/projects/{GITLAB_PROJECT_ID}/issues',
        data_dict=data,
        method='POST'
    )
    if res.get('iid') is None:
        logger.error(f"Issue was't created: {title}\n---\n{description}\n---")
    return res


def update_issue(iid, **kwargs):
    """ 課題を更新する """
    res = __request(
        f'{GITLAB_API_BASE}/projects/{GITLAB_PROJECT_ID}/issues/{iid}',
        data_dict=kwargs,
        method='PUT'
    )
    if res.get('iid') is None:
        logger.error(
            f"Issue was't updated: /projects/{GITLAB_PROJECT_ID}/issues/{iid}"
        )
    return res
