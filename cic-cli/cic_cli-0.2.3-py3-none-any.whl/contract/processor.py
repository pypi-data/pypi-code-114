# standard imports
import logging

logg = logging.getLogger(__name__)


class ContractProcessor:
    """Drives the serialization and publishing of contracts, proofs and metadata for the token.

    :param proof: Proof object to publish
    :type proof: cic.proof.Proof
    :param attachment: Attachment object to publish
    :type attachment: cic.attachment.Attachment
    :param metadata: Metadata object to publish
    :type metadata: cic.meta.Meta
    :param writer: Writer interface receiving the output of the processor
    :type writer: cic.writers.OutputWriter
    :param extensions: Extension contexts to publish to
    :type extensions: list of cic.extension.Extension
    """

    def __init__(
        self,
        proof=None,
        attachment=None,
        metadata=None,
        outputs_writer=None,
        extensions=[],
    ):
        self.token_address = None
        self.extensions = extensions
        self.cores = {
            "metadata": metadata,
            "attachment": attachment,
            "proof": proof,
        }
        self.outputs = []
        self.__outputs_writer = outputs_writer

    def writer(self):
        """Return the writer instance that the process is using.

        :rtype: cic.writers.OutputWriter
        :return: Writer
        """
        return self.__outputs_writer

    def get_outputs(self):
        """Return all written outputs.

        This will return nothing unless the process method has been executed.

        :rtype: bytes
        :return: Outputs
        """
        outputs = []
        for ext in self.extensions:
            outputs += ext.outputs
        outputs += self.outputs
        return outputs

    def process(self, writer=None):
        """Serializes and publishes all token data.

        Calls the process method on each extension. For each extension, the process method on attachment, proof and metadata, in that order, for any of them that have provided at processor object instantiation.

        All output written to the publish writer will also be cached so that it subsequently be recalled using the get_outputs method.

        :param writer: Writer to use for publishing.
        :type writer: cic.writers.OutputWriter
        """

        tasks = [
            "attachment",
            "proof",
            "metadata",
        ]

        for ext in self.extensions:
            (token_address, token_symbol) = ext.process()

            for task in tasks:
                a = self.cores.get(task)
                if a is None:
                    logg.debug(f'skipping missing task receiver "{task}"')
                    continue
                v = a.process(
                    token_address=token_address,
                    token_symbol=token_symbol,
                    writer=self.__outputs_writer,
                )
                self.outputs.append(v)
