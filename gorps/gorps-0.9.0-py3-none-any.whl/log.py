import logging


class EmojiLevelFormatter(logging.Formatter):
    emojis = {
        logging.DEBUG: "🔬",
        logging.INFO: "ℹ️",
        logging.WARNING: "⚠️",
        logging.ERROR: "💥",
        logging.CRITICAL: "☢️",
    }

    def format(self, record: logging.LogRecord) -> str:
        record.levelname = self.emojis.get(record.levelno, record.levelname)
        return logging.Formatter.format(self, record)


def setup_logging(log_level: int = logging.INFO) -> None:
    logger = logging.getLogger()
    logger.setLevel(log_level)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(EmojiLevelFormatter("%(levelname)s  %(message)s"))
    logger.addHandler(console_handler)
