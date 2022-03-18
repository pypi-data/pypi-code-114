__version__ = '1.3.3'
# this has to be set here for the test coverage to work
__name__ = 'nerdvision'
agent_name = 'nerd.vision Python Agent'

__version_major__ = '1'
__version_minor__ = '3'
__version_micro__ = '3'

__props__ = {
    '__Git_Branch__': '1.3.3',
    '__Git_Commit_Id__': 'ce0967c701562f1119370abf26c372438037da32',
    '__Git_Commit_Time__': '2022-03-18 11:04:56+00:00',
    '__Git_Dirty__': 'False',
    '__Git_Remote_Origin_Url__': 'https://gitlab-ci-token:FqxDs6bxLWzUknz7zfNz@gitlab.com/intergral/nerdvision/agents/python-client.git',

    '__X_CI_Pipeline_Id__': '',
    '__X_CI_Pipeline_Iid__': '',
    '__X_CI_Pipeline_Source__': '',
    '__X_CI_Pipeline_Url__': '',
    '__X_CI_Project_Name__': '',
}

try:
    from typing import TYPE_CHECKING as TYPES
except ImportError:
    TYPES = False

if TYPES:
    from typing import Optional

nv_client = None  # type: Optional[NerdVisiion]


def start(api_key=None, name=None, tags=None, agent_settings=None, serverless=False):
    """
    The main entry to NerdVision, call this once to start the agent. The arguments are optional and can
    be set via environment variables for full documentation please see: https://docs.nerd.vision/python/configuration

    :param api_key: the api key to use
    :param name: the name of the agent
    :param tags: custom tags to use
    :param agent_settings: custom agent settings
    :param serverless: indicates this is a serverless start
    :return: A new NerdVision agent
    :rtype: NerdVision
    """
    global nv_client

    if nv_client is not None:
        return nv_client

    if agent_settings is None:
        agent_settings = {}

    agent_settings['name'] = name
    agent_settings['api_key'] = api_key
    agent_settings['tags'] = tags

    from nerdvision import settings
    settings.configure_agent(agent_settings)

    api_key = settings.get_setting("api_key")
    if api_key is None:
        configure_logger(serverless=serverless).error("Nerd.vision api key is not defined.")
        exit(314)

    from nerdvision.NerdVision import NerdVision
    from nerdvision.ClientRegistration import ClientRegistration
    hippo = NerdVision(client_service=ClientRegistration(), serverless=serverless)
    hippo.start()

    nv_client = hippo
    return hippo


def stop():
    global nv_client
    if nv_client is not None:
        nv_client.stop()
        nv_client = None


def configure_logger(force_init=False, serverless=False):
    from nerdvision import settings
    import logging
    from logging.handlers import SysLogHandler

    log_file = settings.get_setting("log_file")
    level = settings.get_setting("log_level")

    our_logger = logging.getLogger("nerdvision")

    if not force_init and len(our_logger.handlers) != 0:
        return our_logger

    if force_init:
        for handler in set(our_logger.handlers):
            our_logger.removeHandler(handler)

    formatter = logging.Formatter('%(asctime)s NerdVision: [%(levelname)s] %(message)s', datefmt='%b %d %H:%M:%S')

    if log_file is not None and not serverless:
        file_handler = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=10000000, backupCount=5, encoding=None,
                                                            delay=0)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        our_logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)

    our_logger.propagate = True
    our_logger.setLevel(level)

    our_logger.addHandler(stream_handler)

    return our_logger


def nv_serverless(f):
    from functools import wraps

    @wraps(f)
    def handler(*args, **kwargs):
        start(serverless=True)
        try:
            return f(*args, **kwargs)
        except Exception as e:
            capture_exception()
            raise e
        finally:
            stop()

    return handler


def capture_exception(exception_type_or_tuple=None, value=None, tb=None):
    """
    Use this function to capture the current (or a specific) exception and send it the NerdVision as a tracepoint trigger.

    :param exception_type_or_tuple: the exception to capture (as a tuple or value) or None
    :param value: the exception value
    :param tb: the traceback to process
    :return: None
    """
    global nv_client
    if nv_client is not None:
        nv_client.capture_exception(exception_type_or_tuple, value, tb)
    else:
        print("Must start %s before capturing exceptions." % agent_name)
