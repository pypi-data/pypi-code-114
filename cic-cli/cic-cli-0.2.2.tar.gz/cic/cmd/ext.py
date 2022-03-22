# standard imports
import importlib

# external imports
from chainlib.chain import ChainSpec

# local imports
from cic.contract.network import Network


def process_args(argparser):
    argparser.add_argument(
        "--registry", type=str, help="contract registry address"
    )
    argparser.add_argument(
        "-d", "--directory", type=str, dest="directory", default=".", help="directory"
    )
    argparser.add_argument("-p", type=str, help="RPC endpoint")
    argparser.add_argument("-i", type=str, help="chain spec string")
    argparser.add_argument("target", help="target to initialize")


def validate_args(args):
    pass


def execute(config, eargs):
    cn = Network(eargs.directory, targets=eargs.target)
    cn.load()

    chain_spec = ChainSpec.from_chain_str(eargs.i or config.get("CHAIN_SPEC"))
    m = importlib.import_module(f"cic.ext.{eargs.target}.start")
    m.extension_start(
        cn,
        registry_address=eargs.registry or config.get("CIC_REGISTRY_ADDRESS"),
        chain_spec=chain_spec,
        rpc_provider=config.get("RPC_PROVIDER"),
    ) # TODO add key account address
