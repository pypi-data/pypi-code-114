import base64
import logging

import grpc
import nerdvision_pb2
import nerdvision_pb2_grpc

from nerdvision import settings

our_logger = logging.getLogger("nerdvision")


class GRPCService(object):
    def __init__(self, remote_id, client_config):
        self.channel = None
        self.shutdown = False
        self.client_config = client_config
        self.api_key = settings.get_setting("api_key")
        self.secure = settings.get_setting("grpc_port") == 443
        self.remote_id = remote_id
        self.service_url = settings.get_grpc_host()
        our_logger.debug("Configured GRPC with remote_id: %s; api_key: %s; service url: %s", self.remote_id, self.api_key,
                         self.service_url)

    def connect(self, call_back):
        if self.remote_id is not None and self.api_key is not None:
            self.channel = self.make_channel()
            if self.shutdown:
                # it is possible that we have been shutdown during a reconnect
                return

            with self.channel as channel:
                breakpoints_stub = nerdvision_pb2_grpc.NerdVisionBreakpointsStub(channel)

                connection = nerdvision_pb2.BreakpointConnection(id=self.client_config.session_id, tags=self.client_config.tags)

                encode = base64.b64encode((self.remote_id + ':' + self.api_key).encode("utf-8"))

                stream_breakpoints = breakpoints_stub.streamBreakpoints(connection, metadata=[
                    ('authorization', "Basic%20" + encode.decode('utf-8'))])

                for response in stream_breakpoints:
                    if response.clientConfig is not None and len(response.clientConfig) > 0:
                        self.client_config.update_config(response.clientConfig)
                    call_back(response)
        else:
            our_logger.error("Cannot make connection to grpc service. remote_id: %s; api_key: %s", self.remote_id, self.api_key)

    def stop(self):
        self.shutdown = True
        our_logger.debug('Shutting down GRPC connection')
        if self.channel is not None:
            our_logger.debug('Channel: %s', str(self.channel))
            self.channel.close()
            self.channel = None

    def make_channel(self):
        if self.secure:
            our_logger.info("Connecting securely with session: %s", self.remote_id)
            our_logger.debug("Connecting securely to: %s (%s)", self.service_url, self.remote_id)
            return grpc.secure_channel(self.service_url, grpc.ssl_channel_credentials())
        else:
            our_logger.info("Connecting with insecure channel with session: %s", self.remote_id)
            our_logger.debug("Connecting with insecure channel to: %s (%s)", self.service_url, self.remote_id)
            return grpc.insecure_channel(self.service_url)
