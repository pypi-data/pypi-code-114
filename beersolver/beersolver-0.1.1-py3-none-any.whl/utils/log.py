import logging
from dataclasses import dataclass, field


@dataclass
class InternalLogger:
    debug: bool = field(default=False)
    logger: logging.Logger = field(default=False, init=False)

    def __post_init__(self):
        if self.debug:
            logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        else:
            logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def log(self, msg: str, level: int = logging.INFO) -> None:
        """
        Wrapper for logging.
        :param msg: message to be issued
        :param level: what level it is being issued to
        """
        self.logger.log(level, msg)


