# flake8: noqa
import logging

__author__ = "DataWhys"
__version__ = "0.4.1"

# Configuration variables
auth_enabled = True
api_key = None

api_base = "https://api.datawhys.ai/"

verify_ssl_certs = True
proxy = None
default_http_client = None
enable_telemetry = True
max_network_retries = 0
ca_bundle_path = None

# Set to either 'debug' or 'info', controls console logging
log = None

from datawhys import api  # isort:skip
from datawhys.core.api import DataWhysFrame, DataWhysSeries  # isort:skip
from datawhys.prescriber import Solver  # isort:skip
