__version__ = '0.2.1'

# Set default logging handler to avoid "No handler found" warnings.
import logging
logging.getLogger('atlaspyapi').addHandler(logging.NullHandler())
