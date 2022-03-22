# standard imports
import importlib
import logging
import os
from typing import Optional

# external imports
from cic_types.ext.metadata import MetadataRequestsHandler
from cic_types.ext.metadata.signer import Signer as MetadataSigner

# local imports
from cic.contract.processor import ContractProcessor
from cic.contract.components.proof import Proof
from cic.contract.components.attachment import Attachment
from cic.contract.components.meta import Meta
from cic.contract.network import Network
from cic.contract.components.token import Token
from cic.writers import HTTPWriter, KeyedWriterFactory, MetadataWriter

logg = logging.getLogger(__name__)


def process_args(argparser):
    argparser.add_argument(
        "-d", "--directory", type=str, dest="directory", default=".", help="directory"
    )
    argparser.add_argument(
        "-o",
        "--output-directory",
        type=str,
        dest="output_directory",
        help="output directory",
    )
    argparser.add_argument(
        "--metadata-endpoint",
        dest="metadata_endpoint",
        type=str,
        help="metadata endpoint to interact with",
    )
    argparser.add_argument(
        "-y",
        "--signer",
        type=str,
        dest="y",
        help="target-specific signer to use for export",
    )
    argparser.add_argument("-p", type=str, help="RPC endpoint")
    argparser.add_argument("target", type=str, help="target network type")


def validate_args(args):
    pass


def init_writers_from_config(config):
    w = {
        "meta": None,
        "attachment": None,
        "proof": None,
        "ext": None,
    }
    for v in w.keys():
        k = "CIC_CORE_{}_WRITER".format(v.upper())
        (d, c) = config.get(k).rsplit(".", maxsplit=1)
        m = importlib.import_module(d)
        o = getattr(m, c)
        w[v] = o

    return w


ExtraArgs = {
    "target": str,
    "directory": str,
    "output_directory": str,
    "metadata_endpoint": Optional[str],
    "y": str,
}


def execute(config, eargs: ExtraArgs):
    modname = f"cic.ext.{eargs.target}"
    cmd_mod = importlib.import_module(modname)

    writers = init_writers_from_config(config)

    output_writer_path_meta = eargs.output_directory
    if eargs.metadata_endpoint != None:
        MetadataRequestsHandler.base_url = eargs.metadata_endpoint
        MetadataSigner.gpg_path = os.path.join("/tmp")
        MetadataSigner.key_file_path = config.get("AUTH_KEYFILE_PATH")
        MetadataSigner.gpg_passphrase = config.get("AUTH_PASSPHRASE")
        writers["proof"] = KeyedWriterFactory(MetadataWriter, HTTPWriter).new
        writers["attachment"] = KeyedWriterFactory(None, HTTPWriter).new
        writers["meta"] = MetadataWriter
        output_writer_path_meta = eargs.metadata_endpoint

    ct = Token(path=eargs.directory)
    cm = Meta(
        path=eargs.directory, writer=writers["meta"](path=output_writer_path_meta)
    )
    ca = Attachment(
        path=eargs.directory, writer=writers["attachment"](path=output_writer_path_meta)
    )
    cp = Proof(
        path=eargs.directory,
        attachments=ca,
        writer=writers["proof"](path=output_writer_path_meta),
    )
    cn = Network(path=eargs.directory)

    ca.load()
    ct.load()
    cp.load()
    cm.load()
    cn.load()

    chain_spec = None
    try:
        chain_spec = config.get("CHAIN_SPEC")
    except KeyError:
        chain_spec = cn.chain_spec
        config.add(chain_spec, "CHAIN_SPEC", exists_ok=True)
        logg.debug(f"CHAIN_SPEC config set to {str(chain_spec)}")

    # signer = cmd_mod.parse_signer(eargs.y)
    (rpc, signer) = cmd_mod.parse_adapter(config, eargs.y)

    ref = cn.resource(eargs.target)
    chain_spec = cn.chain_spec(eargs.target)
    logg.debug(
        f"found reference {ref['contents']} chain spec {chain_spec} for target {eargs.target}"
    )
    c = getattr(cmd_mod, "new")(
        chain_spec,
        ref["contents"],
        cp,
        signer_hint=signer,
        rpc=rpc,
        outputs_writer=writers["ext"](path=eargs.output_directory),
    )
    c.apply_token(ct)

    p = ContractProcessor(proof=cp, attachment=ca, metadata=cm, extensions=[c])
    p.process()
