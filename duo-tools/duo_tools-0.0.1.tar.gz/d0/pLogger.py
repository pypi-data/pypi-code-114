import logging
import os


class pLogger:
    def __init__(self, file='', name='', log_path='') -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        # if log_path is not set
        if not log_path:
            # if file is set
            if file:
                # then use default set for log_path
                dirname, basename = os.path.split(file)
                log_path = os.path.join(
                    dirname, 'log', os.path.splitext(basename)[0] + '.log')
                dirname, _ = os.path.split(log_path)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
        # if log_path is set
        if log_path:
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
            fh = logging.FileHandler(log_path)
            fh.setFormatter(formatter)
            self.logger.handlers = [fh]

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        # self.logger.info(msg, args, **kwargs)
        self.logger._log(logging.INFO, msg, args, **kwargs)


if __name__ == '__main__':
    p_loggger = pLogger(file=__file__)
    p_loggger.info('hello')
