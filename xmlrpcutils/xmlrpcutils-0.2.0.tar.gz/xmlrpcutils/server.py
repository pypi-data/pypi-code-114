
from gevent import monkey; monkey.patch_all()

import logging
from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer

from fastutils import logutils
from daemon_application import DaemonApplication

logger = logging.getLogger(__name__)

class SimpleThreadedXmlRpcServer(ThreadingMixIn, SimpleXMLRPCServer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_introspection_functions()
        self.register_multicall_functions()


class SimpleXmlRpcServer(DaemonApplication):

    def get_default_listen_port(self):
        return getattr(self, "default_listen_port", 8381)
    
    def get_disable_debug_service_flag(self):
        return getattr(self, "disable_debug_service", False)

    def main(self):
        logutils.setup(**self.config)
        self.server_listen = tuple(self.config.get("server", {}).get("listen", ("0.0.0.0", self.get_default_listen_port())))
        logger.warn("Starting xmlrpc server on {server_listen}...".format(server_listen=self.server_listen))
        self.server = SimpleThreadedXmlRpcServer(self.server_listen, allow_none=True, encoding="utf-8")
        self.register_services()
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            logger.warn("Got KeyboardInterrupt signal, stopping the service...")

    def register_services(self):
        disable_debug_service_flag = self.get_disable_debug_service_flag()
        if not disable_debug_service_flag:
            from .service import DebugService
            DebugService().register_to(self.server)
