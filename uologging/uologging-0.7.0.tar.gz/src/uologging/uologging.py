import logging
import logging.handlers


_logging_format = logging.Formatter(
    '%(asctime)s %(levelname)-8s  %(message)s [%(pathname)s:%(lineno)d]',
    '%Y-%m-%d %H:%M:%S')


syslog_logging_initialized = False
def init_syslog_logging(name:str = None):
    """Setup logging to be output to syslog (via /dev/log).

    Args:
        name (str, optional): Which logger to configure. Default to root logger.

    Example:
        Call this method.
        >>> import uologging
        >>> uologging.init_syslog_logging()

        Then use the Python logging package in each of your package's modules.
        >>> import logging
        >>> logger = logging.getLogger(__name__)

        We use a hardcoded str here to enable this doctest:
        >>> logger = logging.getLogger('examplepkg.just.testing')
        >>> logger.critical('Just kidding, this is a test!')    
    """
    global syslog_logging_initialized
    if syslog_logging_initialized is False:
        syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
        _add_log_handler_with_formatter(syslog_handler, name)
        syslog_logging_initialized = True


console_logging_initialized = False
def init_console_logging(name:str = None):
    """Setup logging to be output to the console.

    Args:
        name (str, optional): Which logger to configure. Default to root logger.

    Example:
        Call this method.
        >>> import uologging
        >>> uologging.init_console_logging()

        Then use the Python logging package in each of your package's modules.
        >>> import logging
        >>> logger = logging.getLogger(__name__)

        We use a hardcoded str here to enable doctest:
        >>> logger = logging.getLogger('examplepkg.just.testing')
        >>> logger.critical('Just kidding, this is a test!')
    """
    global console_logging_initialized
    if console_logging_initialized is False:
        console_handler = logging.StreamHandler()
        _add_log_handler_with_formatter(console_handler, name)
        console_logging_initialized = True


def set_logging_verbosity(verbosity_flag: int, name:str = None):
    """Set the logging verbosity for a logger.

    Args:
        verbosity_flag (int): Higher number means more logging. Choices are [0,2]. 
            Default is 0. Default will captures WARNING, ERROR, and CRITICAL logs.
            Provide 1 to also capture INFO logs. Provide 2 to also capture DEBUG logs.
        name (str, optional): Which logger to configure. Default to root logger.
    """
    root_logger = logging.getLogger(name)
    if verbosity_flag == 1:
        root_logger.setLevel(logging.INFO)
    elif verbosity_flag >= 2:
        root_logger.setLevel(logging.DEBUG)
    else:  # Default to WARNING, following Python logging standards
        root_logger.setLevel(logging.WARNING)


def _add_log_handler_with_formatter(handler: logging.Handler, name:str = None):
    """Add a handler to a logger.

    Args:
        handler (logging.Handler): A logging handler.
        name (str, optional): Which logger to configure. Default to root logger.
    """
    handler.setFormatter(_logging_format)
    root_logger = logging.getLogger(name)
    root_logger.addHandler(handler)
