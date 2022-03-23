import http.server
import itertools
import json
import logging
import os
import signal
import socketserver
from argparse import ArgumentParser
from tempfile import TemporaryDirectory
from threading import Thread

from pssteval import logger


def get_args():
    parser = ArgumentParser()
    parser.add_argument("json_files", nargs="+")
    parser.add_argument("--log-level", default="INFO", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"))
    parser.add_argument("--start-port", default=8000, type=int)
    return parser.parse_args()


def start_server(json_files, start_port=8000, log_level="INFO"):
    logger.setLevel(log_level)
    AnalysisViewServer.start(analysis_files=json_files, start_port=start_port)

class AnalysisViewServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, path_map):
        self.path_map = path_map
        super().__init__(*args)

    def translate_path(self, path: str) -> str:
        rel_path = os.path.join("/", os.path.relpath(super().translate_path(path), self.directory).lstrip("."))
        mapped = self.path_map.get(rel_path, self.path_map.get("/404.html"))
        return mapped

    def log_message(self, format, *args):
        logger.debug(format % args)

    @classmethod
    def start(cls, *, analysis_files, start_port):
        with TemporaryDirectory() as temp_dir:
            path_map = cls.build_path_map()

            analysis_paths = []
            for file in analysis_files:
                web_path = os.path.join("/analysis-files", os.path.basename(file))
                path_map[web_path] = file
                analysis_paths.append(web_path)

            analysis_files_filename = os.path.join(temp_dir, "analysis-files.json")
            with open(analysis_files_filename, "w") as f:
                json.dump(analysis_paths, f)

            path_map["/analysis-files.json"] = analysis_files_filename
            for port in range(start_port, start_port + 1000):
                try:
                    with socketserver.TCPServer(
                            ("", port),
                            lambda *args: AnalysisViewServer(
                                *args,
                                path_map=path_map,
                            )
                    ) as httpd:
                        logger.info(f"Server started at http://localhost:{port} <-- open this address in your web browser.")
                        logger.info(f"Press ctrl+c to stop server.")
                        signal.signal(signal.SIGINT, lambda *args: (
                            logger.info(f"Shutting down server..."),
                            httpd.shutdown(),
                            httpd.server_close()
                        ))
                        thread = Thread(target=httpd.serve_forever)
                        thread.start()
                        thread.join()
                        logger.info(f"Done."),
                        return
                except OSError as e:
                    if e.errno != 48:
                        raise
                    logger.warning(f"Port {port} already in use.")

    @classmethod
    def build_path_map(cls):
        web_dir = os.path.join(os.path.dirname(__file__), "web")
        path_map = {
            "/": os.path.join(web_dir, "index.html"),
            "/404.html": os.path.join(web_dir, "404.html"),
        }

        for root, dirs, files in os.walk(web_dir):
            rel_dir = os.path.join("/", os.path.relpath(root, web_dir)).rstrip(".")
            for file in files:
                rel_path = os.path.join(rel_dir, file)
                path_map[rel_path] = os.path.join(root, file)

        try:
            import psstdata
            data = psstdata.load()
            for utterance in itertools.chain(data.train, data.valid, data.test):
                web_path = os.path.join("/audio", os.path.basename(utterance.filename))
                path_map[web_path] = utterance.filename_absolute
        except Exception as e:
            logging.warning(f"Error in `psstdata`, won't be able to serve audio.")
            pass
        return path_map


def main():
    args = get_args()
    start_server(**vars(args))


if __name__ == '__main__':
    main()