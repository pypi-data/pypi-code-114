from __future__ import annotations

# standard imports
import os
import json
import logging

# external imports
from cic_types import MetadataPointer
from cic_types.processor import generate_metadata_pointer
from hexathon import strip_0x

# local imports
from cic.contract.base import Data, data_dir
from cic.utils import object_to_str

logg = logging.getLogger(__name__)


class Meta(Data):
    """Serialize and publish metadata for token.

    The token metadata is any mutable data that is not part of the initial token proof, but published simultaneously as the token nonetheless.

    :param path: Path to settings directory
    :type path: str
    :param writer: Writer interface receiving the output of the processor
    :type writer: cic.writers.OutputWriter
    """

    def __init__(
        self, path=".", writer=None, name="", location="", country_code="KE", contact={}, interactive=False
    ):
        super(Meta, self).__init__()
        self.name = name
        self.contact = contact
        self.country_code = country_code
        self.location = location
        self.path = path
        self.writer = writer
        self.meta_path = os.path.join(self.path, "meta.json")

        if interactive:
            self.name = input(f"Enter Metadata Name ({self.name}): ") or self.name
            self.country_code = input(f"Enter Metadata Country Code ({self.country_code}): ") or self.country_code
            self.location = input(f"Enter Metadata Location ({self.location}): ") or self.location
            
            adding_contact_info = True
            contact = {}
            while adding_contact_info:
                value = input("Enter Metadata contact info (e.g 'phone: +254723522718'): ") or None
                if value:
                    data = value.split(":")
                    if len(data) != 2:
                        print("Invalid contact info, you must enter in the format 'key: value'")
                        continue
                    contact[data[0].strip()] = data[1].strip()
                else:
                    adding_contact_info = False
            self.contact = contact

    def load(self):
        """Load metadata from settings."""
        super(Meta, self).load()

        f = open(self.meta_path, "r", encoding="utf-8")
        o = json.load(f)
        f.close()

        self.name = o["name"]
        self.contact = o["contact"]
        self.country_code = o["country_code"]
        self.location = o["location"]
        self.inited = True

    def start(self):
        """Initialize metadata settings from template."""
        super(Meta, self).start()

        meta_template_file_path = os.path.join(
            data_dir, f"meta_template_v{self.version()}.json"
        )

        f = open(meta_template_file_path, encoding="utf-8")
        o = json.load(f)
        f.close()

        o["name"] = self.name
        o["contact"] = self.contact
        o["country_code"] = self.country_code
        o["location"] = self.location

        f = open(self.meta_path, "w", encoding="utf-8")
        json.dump(o, f, sort_keys=True, indent="\t")
        f.close()

    def reference(self, token_address):
        """Calculate the mutable reference for the token metadata."""
        token_address_bytes = bytes.fromhex(strip_0x(token_address))
        return generate_metadata_pointer(
            token_address_bytes, MetadataPointer.TOKEN_META
        )

    def asdict(self):
        """Output proof state to dict."""
        return {
            "name": self.name,
            "country_code": self.country_code,
            "location": self.location,
            "contact": self.contact,
        }

    def process(self, token_address=None, token_symbol=None, writer=None):
        """Serialize and publish metadata.

        See cic.processor.Processor.process
        """
        if writer is None:
            writer = self.writer

        v = json.dumps(self.asdict(), separators=(",", ":"))

        token_address_bytes = bytes.fromhex(strip_0x(token_address))
        k = generate_metadata_pointer(token_address_bytes, MetadataPointer.TOKEN_META)
        writer.write(k, v.encode("utf-8"))

        token_symbol_bytes = token_symbol.encode("utf-8")
        k = generate_metadata_pointer(
            token_symbol_bytes, MetadataPointer.TOKEN_META_SYMBOL
        )
        writer.write(k, v.encode("utf-8"))

        return (k, v)

    def __str__(self):
        return object_to_str(self, ["name", "contact", "country_code", "location"])

