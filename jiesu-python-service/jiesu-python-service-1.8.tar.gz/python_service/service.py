import logging
import signal
import socket
import sys
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from logging.handlers import RotatingFileHandler
from pathlib import Path, PurePath
from typing import Any, Callable, Match, Optional, Pattern

import py_eureka_client.eureka_client as EurekaClient  # type: ignore

"""
## Dependencies:
pip install Flask py-eureka-client

## Dev Dependencies:
Install typing stubs.
pip install types-Flask

## pip deploy
<https://packaging.python.org/en/latest/tutorials/packaging-projects/>

### Deploy to pip
# update version number in setup.py first.
cd ~/bin/app/python-service
rm dist/ -rf
python3 setup.py sdist
twine upload dist/*
pip3 install jiesu-python-service -U

### Install locally
cd ~/bin/app/python-service
pip3 uninstall jiesu-python-service
pip3 install .

"""


def register_eureka(eureka_server: str, name: str, port: int, instance: str):
    # get hostname explicitly to avoid ambiguity, e.g, acer vs. acer.lan.
    hostname: str = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("router", 1))
    ip: str = s.getsockname()[0]
    return EurekaClient.init(  # type: ignore
        eureka_server=eureka_server,
        app_name=name,
        instance_port=port,
        instance_host=hostname,
        instance_ip=ip,
        instance_id=name + "_" + instance,
        metadata={"name": instance},
    )


def get_log_file(log_base: str, name: str) -> PurePath:
    log_dir = PurePath(log_base, name)
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    return PurePath(log_dir, name + ".log")


def setup_log(log_file: PurePath) -> logging.Logger:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.disabled = True

    log_handler = RotatingFileHandler(
        log_file, mode="a", maxBytes=200 * 1024, backupCount=10, encoding=None
    )
    # logger name is not printed.
    log_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(log_handler)
    return log


class Regex:
    def match(self, re: Pattern[str], string: str) -> bool:
        self.m: Optional[Match[str]] = re.match(string)
        return self.m is not None

    def group(self, index: int) -> str:
        if self.m is None:
            raise Exception("No match found")
        else:
            return self.m.group(index)


class BaseHttpHandler:
    def set_log(self, log: logging.Logger):
        self.log = log

    def set_request_handler(self, request_handler: BaseHTTPRequestHandler):
        self.request_handler = request_handler

    def header(self, content_type: str = "application/json"):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", content_type)
        self.request_handler.end_headers()

    def body(self, content: Any):
        s = content if isinstance(content, str) else str(content)
        self.request_handler.wfile.write(s.encode("utf-8"))

    def get_body(self) -> bytes:
        content_len = int(self.request_handler.headers.get("Content-Length"))
        return self.request_handler.rfile.read(content_len)

    def invalid(self):
        self.request_handler.send_response(404)
        self.request_handler.end_headers()

    def path(self):
        return self.request_handler.path

    def get(self):
        self.invalid()

    def post(self):
        self.invalid()

    def delete(self):
        self.invalid()

    def put(self):
        self.invalid()


class HttpRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, handler: BaseHttpHandler, log: logging.Logger, *args: Any):
        self.handler = handler
        self.log = log
        self.handler.set_request_handler(self)
        BaseHTTPRequestHandler.__init__(self, *args)

    def log_message(self, format, *args):  # type: ignore
        return

    def do_GET(self):
        try:
            # Called by Eureka when clicking the instance link on Eureka web UI.
            if self.path == "/info":
                self.handler.header()
                self.handler.body("A Python Service")
            elif self.path == "/health":
                self.handler.header()
                self.handler.body('{"status":"UP"}')
            else:
                self.handler.get()
        except socket.error:
            pass
        except Exception as ex:
            self.log.exception(ex)

    def do_POST(self):
        self.log.info("Received POST request " + self.path)
        try:
            self.handler.post()
        except socket.error:
            pass
        except Exception as ex:
            self.log.exception(ex)

    def do_DELETE(self):
        self.log.info("Received DELETE request " + self.path)
        try:
            self.handler.delete()
        except socket.error:
            pass
        except Exception as ex:
            self.log.exception(ex)

    def do_PUT(self):
        self.log.info("Received PUT request " + self.path)
        try:
            self.handler.put()
        except socket.error:
            pass
        except Exception as ex:
            self.log.exception(ex)


class Service:
    def __init__(
        self,
        argparser: ArgumentParser,
        cleanup: Callable[[], None] = lambda: None,
    ):
        self.cleanup: Callable[[], None] = cleanup
        argparser.add_argument("-name", type=str, required=True, help="Service name")
        argparser.add_argument("-log", type=str, required=True, help="Base dir for log")
        argparser.add_argument("-port", type=int, required=True, help="Service port")
        argparser.add_argument(
            "-instance",
            type=str,
            required=False,
            default="default",
            help="Eureka instance name",
        )
        argparser.add_argument(
            "-eureka", type=str, required=True, help="Eureka server url"
        )
        self.args: Any = argparser.parse_args()
        self.name: str = self.args.name
        self.instance: str = self.args.instance
        self.port: int = self.args.port
        self.eureka_server: str = self.args.eureka
        self.log_file: PurePath = get_log_file(
            self.args.log, self.name + "_" + self.instance
        )
        self.log: logging.Logger = setup_log(self.log_file)

    def start(self, httpHandler: BaseHttpHandler):
        eureka_client = register_eureka(
            self.eureka_server, self.name, self.port, self.instance
        )

        def unregister_eureka(signal: Any, frame: Any):
            self.cleanup()
            eureka_client.stop()
            sys.exit(0)

        signal.signal(signal.SIGINT, unregister_eureka)
        signal.signal(signal.SIGTERM, unregister_eureka)

        httpHandler.set_log(self.log)

        def handler(*args: Any) -> BaseHTTPRequestHandler:
            return HttpRequestHandler(httpHandler, self.log, *args)

        httpServer = ThreadingHTTPServer(("", self.port), handler)
        self.log.info("Serving at " + str(self.port))
        httpServer.serve_forever()
