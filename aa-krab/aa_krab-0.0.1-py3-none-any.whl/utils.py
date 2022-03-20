import logging

DATETIME_FORMAT = "%Y-%m-%d %H:%M"

class Logger(logging.LoggerAdapter):
    """
    add custom tag to a logger
    """

    def __init__(self, my_logger, prefix):
        super(Logger, self).__init__(my_logger, {})
        self.prefix = prefix

    def process(self, msg, kwargs):
        """
        process log items
        :param msg:
        :param kwargs:
        :return:
        """

        return "[%s] %s" % (self.prefix, msg), kwargs

logger = Logger(logging.getLogger(__name__), __package__)