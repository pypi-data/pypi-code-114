# Python imports
import requests

# Third party imports

# Self imports
from .handlers import DjangoCloudWatchHandler
from .serializers import LogSerializer

class Logger(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    # TODO: Convert scheme to Enum
    def __init__(self, scheme: str, url: str, port: str, log_name: str) -> None:
        # TODO: Check if this violates the singleton pattern. I should not be
        #       able to reconfigure the logger after it has been created.
        self.scheme = scheme
        self.url = url
        self.port = port
        self.log_name = log_name
        self.is_valid()

    def log_to_remote(self, data: dict, log_type: str) -> None:
        '''
        Sends logs to remote server
        '''
        # TODO: Restrict log_types

        log = LogSerializer(data=data)
        response = requests.post(
            url=f"{self.scheme}://{self.url}:{self.port}/{self.log_name}.{log_type}",
            json=log.data
        )

    def is_valid(self):
        # TODO: implement validator
        pass

    def log_to_file() -> None:
        raise NotImplementedError
        

class DjangoLogger:
    LOGGING_CONF = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            "aws": {
                "format": "%(asctime)s [%(levelname)-8s] %(message)s [%(pathname)s:%(lineno)d]",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        'handlers': {
            'console': {'class': 'logging.StreamHandler', 'formatter': 'aws',},
        },
        "loggers": {}
    }
    
    def __init__(self) -> None:
        pass
    
    def set_cloud_watch_logger(
        self, 
        cloud_watch_handler: DjangoCloudWatchHandler,
        handler_name: str,
        logger_name: str,
    ) -> None:
        handler_data = cloud_watch_handler.get_handler_data()
        self.LOGGING_CONF['handlers'][handler_name] = handler_data
        self.LOGGING_CONF['loggers'][logger_name] = {
            'level': cloud_watch_handler.log_level, 
            'handlers': [handler_name], 
            'propogate': False
        }
    
    def get_logging_configuration(self) -> dict:
        return self.LOGGING_CONF
        

class FlaskLogger(Logger):
    pass


class FastApiLogger(Logger):
    pass
