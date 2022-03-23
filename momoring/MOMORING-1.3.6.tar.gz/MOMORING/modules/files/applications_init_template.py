def get_app_init():
    txt = """\
from rdkit import RDLogger
import sys
import os
import warnings

# close rdkit warning
lg = RDLogger.logger()
lg.setLevel(RDLogger.CRITICAL)

warnings.filterwarnings('ignore')

log_path = os.getenv('LOGPATH')
if log_path:
    sys.stdout = open(log_path, 'a')
    sys.stderr = open(log_path, 'a')
    """
    return txt
