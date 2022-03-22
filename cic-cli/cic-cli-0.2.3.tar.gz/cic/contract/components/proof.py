# standard imports
import json
import logging
import os
import tempfile

# external imports
from hexathon import strip_0x
from cic_types import MetadataPointer
from cic_types.processor import generate_metadata_pointer

# local imports
from cic.contract.base import Data, data_dir
from cic.utils import object_to_str


logg = logging.getLogger(__name__)


class Proof(Data):
    """Proof handles the immutable token proof data mapped to the initial token deployment.

    It processes inputs from the proof.json file in the session directory.

    Optionally, attachment objects can be added to the proof. If added, the resulting proof digest will consists of the attachment digests added to the root digest. These are then are deterministically ordered, regardless of which order attachments were given to the constructor.

    :param path: Path to settings directory
    :type path: str
    :param attachments: List of attachment objects to include in the proof
    :type attachments: cic.attachment.Attachment
    :param writer: Writer interface receiving the output of the processor
    :type writer: cic.writers.OutputWriter
    """

    def __init__(
        self,
        path=".",
        description="",
        namespace="ge",
        issuer="",
        attachments=None,
        writer=None,
        interactive=False,
    ):
        super(Proof, self).__init__()
        self.proofs = []
        self.namespace = namespace
        self.description = description
        self.issuer = issuer
        self.path = path
        self.writer = writer
        self.extra_attachments = attachments
        self.attachments = {}
        self.proof_path = os.path.join(self.path, "proof.json")
        self.temp_proof_path = tempfile.mkstemp()[1]

        if interactive:
            self.description = (
                input(f"Enter Proof Description ({self.description}): ") or self.description
            )
            self.namespace = (
                input(f"Enter Proof Namespace ({self.namespace}): ") or self.namespace
            )
            self.issuer = input(f"Enter Proof Issuer ({self.issuer}): ") or self.issuer

    def load(self):
        """Load proof data from settings."""
        super(Proof, self).load()

        f = open(self.proof_path, "r")
        o = json.load(f)
        f.close()

        self.set_version(o["version"])
        self.description = o["description"]
        self.namespace = o["namespace"]
        self.issuer = o["issuer"]
        self.proofs = o["proofs"]

        if self.extra_attachments != None:
            a = self.extra_attachments.asdict()
            for k in a.keys():
                self.attachments[k] = a[k]

        hshs = self.__get_ordered_hashes()
        self.proofs = list(map(strip_0x, hshs))

        self.inited = True

    def start(self):
        """Initialize proof settings from template."""
        super(Proof, self).start()

        proof_template_file_path = os.path.join(
            data_dir, f"proof_template_v{self.version()}.json"
        )

        with open(proof_template_file_path, "r", encoding="utf-8") as f:
            o = json.load(f)

        o["issuer"] = self.issuer
        o["description"] = self.description
        o["namespace"] = self.namespace

        with open(self.proof_path, "w", encoding="utf-8") as f:
            json.dump(o, f, sort_keys=True, indent="\t")

    def asdict(self):
        """Output proof state to dict."""
        return {
            "version": self.version(),
            "namespace": self.namespace,
            "description": self.description,
            "issuer": self.issuer,
            "proofs": self.proofs,
        }

    # TODO: the efficiency of this method could probably be improved.
    def __get_ordered_hashes(self):
        ks = list(self.attachments.keys())
        ks.sort()

        return ks

    #    def get(self):
    #        hsh = self.hash(b).hex()
    #        self.attachments[hsh] = self.temp_proof_path
    #        logg.debug('cbor of {} is {} hashes to {}'.format(v, b.hex(), hsh))

    def root(self):
        """Calculate the root digest from the serialized proof object."""
        v = self.asdict()
        # b = cbor2.dumps(v)
        b = json.dumps(v, separators=(",", ":"))

        with open(self.temp_proof_path, "w", encoding="utf-8") as f:
            f.write(b)

        b = b.encode("utf-8")
        k = self.hash(b)

        return (k.hex(), b)

    def process(self, token_address=None, token_symbol=None, writer=None):
        """Serialize and publish proof.

        See cic.processor.Processor.process
        """
        if writer is None:
            writer = self.writer

        (k, v) = self.root()
        writer.write(k, v)
        root_key = k

        token_symbol_bytes = token_symbol.encode("utf-8")
        k = generate_metadata_pointer(
            token_symbol_bytes, MetadataPointer.TOKEN_PROOF_SYMBOL
        )
        writer.write(k, v)

        token_address_bytes = bytes.fromhex(strip_0x(token_address))
        k = generate_metadata_pointer(token_address_bytes, MetadataPointer.TOKEN_PROOF)
        writer.write(k, v)

        #        (hsh, hshs) = self.get()
        # hshs = list(map(strip_0x, hshs))
        #        hshs_bin = list(map(bytes.fromhex, hshs))
        #        hshs_cat = b''.join(hshs_bin)

        #        f = open(self.temp_proof_path, 'rb')
        #        v = f.read()
        #        f.close()
        #        writer.write(hsh, v)

        #        r = self.hash(hshs_cat)
        #        r_hex = r.hex()

        # logg.debug('generated proof {} for hashes {}'.format(r_hex, hshs))

        # writer.write(r_hex, hshs_cat)

        o = self.asdict()
        with open(self.proof_path, "w", encoding="utf-8") as f:
            json.dump(o, f, sort_keys=True, indent="\t")

        return root_key

    def __str__(self):
        return object_to_str(
            self, ["description", "issuer", "namespace", "version()", "proofs"]
        )
