# standard imports
import logging
import os

# local imports
from cic.contract.base import Data, data_dir

logg = logging.getLogger(__name__)


class Attachment(Data):
    """Processes, serialized and publishes all attachments found in the "attachments" subdirectory of the settings directory.

    :param path: Path to settings directory
    :type path: str
    :param writer: Writer interface receiving the output of the processor
    :type writer: cic.writers.OutputWriter
    """

    def __init__(self, path=".", writer=None, interactive=False):
        super(Attachment, self).__init__()
        self.contents = {}
        self.path = path
        self.writer = writer
        self.attachment_path = os.path.join(self.path, "attachments")
        if interactive:
            self.start()
            input(
                f"Please add attachment files to '{os.path.abspath(os.path.join(self.path,'attachments'))}' and then press ENTER to continue"
            )
            self.load()

    def load(self):
        """Loads attachment data from settings."""
        for s in os.listdir(self.attachment_path):
            fp = os.path.realpath(os.path.join(self.attachment_path, s))
            with open(fp, "rb") as f:
                r = f.read()

            z = self.hash(r).hex()
            self.contents[z] = fp

            logg.debug(f"loaded attachment file {fp} digest {z}")

    def start(self):
        """Initialize attachment settings from template."""
        super(Attachment, self).start()
        os.makedirs(self.attachment_path)

    def get(self, k):
        """Get a single attachment by the sha256 hash of the content.

        :param k: Content hash
        :type k: str (hex)
        """
        return self.contents[k]

    def asdict(self):
        """Output attachment state to dict"""
        return self.contents

    def process(self, token_address=None, token_symbol=None, writer=None):
        """Serialize and publish attachments.

        See cic.processor.Processor.process
        """
        if writer == None:
            writer = self.writer

        for key, value in self.contents.items():
            fp = os.path.join(self.attachment_path, value)
            with open(fp, "rb") as f:
                data = f.read()
            logg.debug(f"writing attachment {key}")
            writer.write(key, data)

    def __str__(self):
        s = ""
        for key, value in self.contents.items():
            s += f"{key} = {value}\n"  # self.digests[i].hex(), self.contents[i])

        return s
