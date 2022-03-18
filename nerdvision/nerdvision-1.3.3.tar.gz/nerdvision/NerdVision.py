import atexit
import math
import platform
import time
from threading import Thread

import nerdvision
from nerdvision import TYPES
from nerdvision import settings
from nerdvision.BreakpointService import BreakpointService
from nerdvision.ClientRegistration import ClientRegistration
from nerdvision.ContextUploadService import ContextUploadService
from nerdvision.ErrorHandler import ErrorHandler
from nerdvision.settings.ClientConfig import ClientConfig

if TYPES:
    from typing import List, Optional, Dict

class NerdVision(object):
    def __init__(self, client_service=None, set_trace=True, serverless=False):
        self.plugins = []  # type: List[str]
        self.logger = nerdvision.configure_logger(serverless=serverless)
        self.registration = client_service
        self.client_config = ClientConfig()
        self.grpc_service = None
        self.context_service = ContextUploadService(self.client_config)
        self.breakpoint_service = BreakpointService(client_config=self.client_config, set_trace=set_trace,
                                                    context_service=self.context_service)
        self.thread = Thread(target=self.connect, name="NerdVision Main Thread")
        # Python 2.7 does not take 'daemon' as constructor argument
        self.thread.setDaemon(True)
        self.is_shutdown = False
        self.grpc_backoff_multiplier = settings.get_setting('grpc_backoff_multiplier')
        self.grpc_max_backoff = settings.get_setting('grpc_backoff_max')
        self.client_reg_max_backoff = settings.get_setting('client_registration_backoff_max')
        self.client_reg_backoff_multiplier = settings.get_setting('client_registration_backoff_multiplier')
        self.serverless = serverless
        self.error_handler = ErrorHandler(self.context_service, settings.get_setting('source_capture'))
        atexit.register(self.stop)

    def start(self):
        self.logger.debug("--------------------------------------------------------------------------------------")
        self.logger.info("nerd.vision (%s) - Copyright (C) Intergral GmbH. All Rights Reserved", nerdvision.__version__)
        self.logger.debug("%-16s: %s", "Version", nerdvision.__version__)
        self.logger.debug("%-16s: %s", "Git-Commit-ID", nerdvision.__props__['__Git_Commit_Id__'])
        self.logger.debug("%-16s: %s", "Git-Commit-Time", nerdvision.__props__['__Git_Commit_Time__'])
        self.logger.debug("%-16s: %s (%s)", "OS", ClientRegistration.run_with_catch('os name', platform.system),
                          ClientRegistration.run_with_catch('os arch', platform.machine))
        self.logger.debug("%-16s: %s [%s]", "Python", platform.python_version(), platform.python_implementation())
        self.logger.debug("%-16s: %s", "Start Time", time.strftime('%a %b %d T%H:%M:%S %Z %Y'))
        self.logger.debug("--------------------------------------------------------------------------------------")
        self.init_plugins()
        if not self.serverless:
            self.thread.start()
        else:
            self.connect()

    def connect(self):
        if not self.serverless:
            from grpc import RpcError
            from nerdvision.GRPCService import GRPCService
            if self.client_config.session_id is None:
                client_registration = self.get_session_id(self.plugins)
                if 'config' in client_registration:
                    self.client_config.update_config(client_registration['config'])
                if 'tags' in client_registration:
                    self.client_config.tags = client_registration['tags']
                self.client_config.session_id = client_registration['session']

            if self.grpc_service is None:
                self.grpc_service = GRPCService(self.client_config.session_id, client_config=self.client_config)

            try:
                self.grpc_service.connect(self.breakpoint_received)
                if not self.is_shutdown:
                    self.reconnect()
            except RpcError:
                if not self.is_shutdown:
                    self.logger.exception("Something went wrong with grpc connection")
                    self.reconnect()
        else:
            json = self.registration.send_client_registration(self.plugins)
            if json is not None:
                if 'breakpoints' in json and 'session' in json:
                    self.client_config.session_id = json['session']
                    self.breakpoint_service.process_request_serverless(json['breakpoints'])

    def breakpoint_received(self, response):
        self.logger.debug("Received breakpoint request from service message_id: %s", response.message_id)
        self.breakpoint_service.process_request(response)

    def stop(self):
        self.flush()
        self.is_shutdown = True
        self.logger.info("Stopping NerdVision")
        self.breakpoint_service.shut_down()
        if self.grpc_service is not None:
            self.grpc_service.stop()
        if self.thread.is_alive():
            self.thread.join()
        self.logger.info("NerdVision shutdown")

    def get_session_id(self, plugins=None):
        # type: (Optional[List[str]]) -> Optional[Dict]
        count = 0
        while self.client_config.session_id is None:
            count = count + 1
            try:
                client_registration = self.registration.send_client_registration(plugins)
                if client_registration is not None:
                    return client_registration

            except Exception:
                self.logger.exception("Error loading session id")

            delay = self.calculate_backoff_time(count, self.client_reg_max_backoff, self.client_reg_backoff_multiplier)
            self.logger.error("Unable to load session id for agent.")
            self.logger.info("Attempting again in %d seconds", delay)
            time.sleep(delay)

        return self.client_config.session_id

    def reconnect(self):
        from grpc import RpcError
        count = 0
        while True:
            if self.is_shutdown:
                break
            count = count + 1
            delay = NerdVision.calculate_backoff_time(count, self.grpc_max_backoff, self.grpc_backoff_multiplier)
            self.logger.info("Attempting to reconnect (%d) in %d seconds", count, delay)
            time.sleep(delay)
            try:
                self.grpc_service.connect(self.breakpoint_received)
                break
            except RpcError:
                if settings.is_grpc_debug_enabled():
                    self.logger.exception("Something went wrong with grpc connection")
                self.logger.warning("Could not connect client")

    def flush(self):
        """
        Can be used to flush the current queue of uploads before terminating the agent
        """

        self.context_service.flush()

    def add_context_decorator(self, decorator):
        """
        Add a decorator to add custom attributes to the contexts generated by NerdVision.

        :param decorator: a function or lambda that takes a context, and returns a tuple of
         the name of the extension and the data to append to the context.
        :return: the id of the decorator to use to remove later
        """

        return self.client_config.append_decorators(decorator)

    def remove_context_decorator(self, uid):
        """
        Remove a previously registered context decorator

        :param uid: the id to remove
        """

        self.client_config.remove_decorator(uid)

    def capture_exception(self, exception_type_or_tuple=None, value=None, tb=None):
        """
        Checks the session_id exists and tell the error handler to capture an error.

        :param exception_type_or_tuple: the exception to capture (as a tuple or value) or None
        :param value: the exception value
        :param tb: the traceback to process
        """
        if self.client_config.session_id is None:
            self.logger.error("NV needs to be registered before capturing an exception")
        else:
            try:
                self.error_handler.capture_exception(exception_type_or_tuple, value, tb)
            except:
                self.logger.exception("Could not capture exception")

    @staticmethod
    def calculate_backoff_time(attempt, max_delay_in_seconds, multiplier):
        delay_in_seconds = (math.pow(2.0, attempt) - 1.0) * 0.5
        return round(min(delay_in_seconds * multiplier, max_delay_in_seconds))

    def init_plugins(self):
        from nerdvision.plugins import load_plugins
        self.plugins = load_plugins(self)
