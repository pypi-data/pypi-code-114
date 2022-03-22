# local imports
from cic.contract.components.proof import Proof
from cic.contract.components.meta import Meta
from cic.contract.components.attachment import Attachment
from cic.contract.network import Network
from cic.contract.components.token import Token


def process_args(argparser):
    argparser.add_argument("-f", "--file", type=str, help="add file")
    argparser.add_argument(
        "-d",
        "--directory",
        type=str,
        dest="directory",
        default=".",
        help="cic data directory",
    )


def validate_args(args):
    pass


def execute(config, eargs):
    ct = Token(path=eargs.directory)
    cp = Proof(path=eargs.directory)
    cm = Meta(path=eargs.directory)
    ca = Attachment(path=eargs.directory)
    cn = Network(eargs.directory)

    ct.load()
    cp.load()
    cm.load()
    ca.load()
    cn.load()

    print(
        """[cic.header]
version = {}\n""".format(
            cp.version()
        )
    )
    print("[cic.token]\n{}".format(ct))
    print("[cic.proof]\n{}".format(cp))
    print("[cic.meta]\n{}".format(cm))
    print("[cic.attachment]\n{}".format(ca))
    print("[cic.network]\n{}".format(cn))
