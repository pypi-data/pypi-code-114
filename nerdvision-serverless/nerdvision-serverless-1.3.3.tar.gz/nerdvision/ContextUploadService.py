import hashlib
import logging
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor

import requests

from nerdvision import settings, TYPES
from nerdvision.Utils import Utils
from nerdvision.models.NVError import NVError
from nerdvision.settings.ClientConfig import ClientConfig

if TYPES:
    from typing import Optional, Dict

our_logger = logging.getLogger("nerdvision")


class ContextUploadService(object):
    def __init__(self, client_config):
        # type: (ClientConfig) -> None
        self.client_config = client_config  # type: ClientConfig
        self.url = settings.get_context_url()  # type: str
        self.error_url = settings.get_error_url()  # type: str
        self.api_key = settings.get_setting("api_key")  # type: str
        self.version = 2  # type: int
        self.pool = ThreadPoolExecutor(max_workers=2)  # type: ThreadPoolExecutor
        self.pending = {}  # type: Dict[str, Future]

    def send_event(self, event_snapshot):
        try:
            our_logger.debug("Sending snapshot to %s", self.url)
            query = '?breakpoint_id=' + event_snapshot['breakpoint']['breakpoint_id']
            query += '&workspace_id=' + event_snapshot['breakpoint']['workspace_id']

            return self.send_context('eventsnapshot', event_snapshot, query)
        except Exception:
            our_logger.exception("Error while sending event snapshot %s", self.url)

    def send_context(self, ctx_type, data, query=''):
        url = self.url + ctx_type + query

        data['version'] = self.version
        data['id'] = self.generate_id()

        return self.submit_task(url, data)

    def decorate(self, data):
        # type: (Dict)-> Dict
        data['attributes'] = {}

        decorators = dict(self.client_config.decorators)
        for key in decorators.keys():
            decorator = decorators.get(key)
            try:
                resp = decorator(data)
                if resp is not None:
                    name, decorator_data = resp
                    data['attributes'][name] = decorator_data
            except:
                our_logger.exception("Decorator %s %s errored; removing.", key, decorator)
                self.client_config.remove_decorator(key)
        return data

    def pool_task(self, url, data):
        # type: (str, Dict)-> None
        our_logger.debug('Task running in pool: %s', url)
        if settings.is_context_debug_enabled():
            our_logger.debug(data)

        try:
            response = requests.post(url=url, auth=(self.client_config.session_id, self.api_key), json=data ,timeout=30)
            our_logger.debug("Context response: %s, %s", response, response.json)
            response.close()
        except requests.exceptions.ConnectTimeout:
            our_logger.error('Could not register client. Request timed out!')

    def send_skipped(self, skipped):
        return self.send_context('skipped', skipped)

    def send_profile(self, profile):
        return self.send_context("profile", profile)

    def send_nv_error(self, nv_error):
        # type: (NVError)-> Optional[Future]
        as_dict = nv_error.as_dict()
        as_dict['tags'] = self.client_config.tags
        return self.submit_task(self.error_url, as_dict)

    def flush(self):
        # type: ()-> None
        if len(self.pending) > 0:
            for key in dict(self.pending).keys():
                get = self.pending.get(key)
                if get is not None:
                    self.pending[key].result(10)

    def generate_id(self):
        # type: ()-> str
        return hashlib.md5((self.client_config.session_id + Utils.generate_uid()).encode('utf-8')).hexdigest()

    def submit_task(self, url, data):
        # type: (str, dict) -> Optional[Future]
        # there is an at exit in threading that prevents submitting tasks after shutdown, but no api to check this
        try:
            future = self.pool.submit(self.pool_task, url, self.decorate(data))
            self.pending[data['id']] = future

            # cannot use 'del' in lambda: https://stackoverflow.com/a/41953232/5151254
            def callback(arg):
                if data['id'] in self.pending:
                    del self.pending[data['id']]

            future.add_done_callback(callback)
            return future
        except:
            # we cannot report this error as that can cause us to report an error.. which creates a loop here.
            return None
