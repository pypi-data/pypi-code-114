import logging
import os


class util:
    def __init__(self) -> None:
        pass

    def set_logging(file):
        dirname, basename = os.path.split(file)
        log_file = os.path.join(
            dirname, 'log', os.path.splitext(basename)[0] + '.log')
        logging.basicConfig(level=logging.INFO,
                            filename=log_file,
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
