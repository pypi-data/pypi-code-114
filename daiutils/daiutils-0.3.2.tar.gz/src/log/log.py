import logging
import inspect

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    logger = None

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(threadName)s - %(message)s",
            handlers=[
                logging.StreamHandler()
            ])

        self.logger = logging.getLogger(__name__ + '.logger')

    @staticmethod
    def __get_call_info():
        stack = inspect.stack()

        # stack[1] gives previous function ('info' in our case)
        # stack[2] gives before previous function and so on

        fn = stack[2][1]
        ln = stack[2][2]
        func = stack[2][3]

        return fn, func, ln

    def info(self, message, *args):
        message = "{} - {} at line {}: {}".format(*self.__get_call_info(), message)
        self.logger.info(message, *args)



logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(threadName)s - %(message)s",
            handlers=[
                logging.StreamHandler()
            ])

logg = logging.getLogger(__name__ + '.logger')



def info(message):
    stack = inspect.stack()
    # stack[1] gives previous function ('info' in our case)
    # stack[2] gives before previous function and so on
    fn = stack[1][1]
    ln = stack[1][2]
    func = stack[1][3]
    message = "info:{} - {} at line {}: {}".format(fn,func,ln, message)
    logg.info(message)

def error(message):
    stack = inspect.stack()
    # stack[1] gives previous function ('info' in our case)
    # stack[2] gives before previous function and so on
    fn = stack[1][1]
    ln = stack[1][2]
    func = stack[1][3]
    message = "error:{} - {} at line {}: {}".format(fn,func,ln, message)
    logg.error(message)