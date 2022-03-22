# standard imports
import logging
import os

# local imports
from cic.contract.components.proof import Proof
from cic.contract.components.meta import Meta
from cic.contract.components.attachment import Attachment
from cic.contract.network import Network
from cic.contract.components.token import Token

logg = logging.getLogger(__name__)


def process_args(argparser):
    argparser.add_argument(
        "--target",
        action="append",
        type=str,
        default=[],
        help="initialize network specification file with target",
    )
    argparser.add_argument("--name", type=str, help="token name")
    argparser.add_argument("--symbol", type=str, help="token symbol")
    argparser.add_argument("--precision", type=str, help="token unit precision")
    argparser.add_argument("directory", help="directory to initialize")


def validate_args(args):
    pass


def execute(config, eargs):
    logg.info("initializing in {}".format(eargs.directory))

    os.makedirs(eargs.directory)

    ct = Token(
        eargs.directory, name=eargs.name, symbol=eargs.symbol, precision=eargs.precision
    )
    cp = Proof(eargs.directory)
    cm = Meta(eargs.directory)
    ca = Attachment(eargs.directory)
    cn = Network(eargs.directory, targets=eargs.target)

    ct.start()
    cp.start()
    cm.start()
    ca.start()
    cn.start()
