import logging

import pssteval


logger = logging.getLogger(pssteval.__name__)

formatter = logging.Formatter('%(name)s %(levelname)s: %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
