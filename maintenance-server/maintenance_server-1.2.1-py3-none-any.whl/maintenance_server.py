import logging
import os
from typing import Optional, Union

from werkzeug.serving import make_server
from werkzeug.wrappers import Response

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
_logger.addHandler(handler)


class Server:
    def __init__(self, host="0.0.0.0", port=8080, html_file_path=None):
        # type: (Optional[str], Union[str, int, float, None], Optional[str]) -> Server
        self.host = host or "0.0.0.0"
        self.port = int(port or 8080)
        if not html_file_path or not os.path.exists(html_file_path):
            html_file_path = os.path.join(os.path.dirname(__file__), "maintenance.html")
        with open(html_file_path) as f:
            text = f.read()
        self.reponse = Response(text, mimetype="text/html")

    def run(self):
        def application(environ, start_response):
            return self.reponse(environ, start_response)

        srv = make_server(self.host, self.port, application, threaded=True)
        srv.serve_forever()


def get_from_env(host=None, port=None, html_file_path=None):
    # type: (Optional[str], Union[str, int, float, None], Optional[str]) -> Server
    HTTP_HOST = (
        host or os.environ.get("MAINTENANCE_HOST") or os.environ.get("HOST") or os.environ.get("HTTP_HOST") or "0.0.0.0"
    )
    HTTP_PORT = (
        port or os.environ.get("MAINTENANCE_PORT") or os.environ.get("PORT") or os.environ.get("HTTP_PORT") or 8080
    )
    PATH_PAGE = html_file_path or os.environ.get("MAINTENANCE_PAGE_PATH")
    _logger.info("###################################")
    _logger.info("Run maintenance Server")
    _logger.info("Conf Page=%s on %s:%s" % (PATH_PAGE or "default", HTTP_HOST, HTTP_PORT))
    _logger.info("###################################")
    return Server(HTTP_HOST, HTTP_PORT, PATH_PAGE)


def run_from_env(host=None, port=None, html_file_path=None):
    # type: () -> None
    get_from_env(host, port, html_file_path).run()
    _logger.info("Stop maintenance Server")


if __name__ == "__main__":
    run_from_env()
