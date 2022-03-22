# standard imports
import logging

# external imports
from hexathon import valid as valid_hex

# local imports
from cic.writers import StdoutWriter
from cic.contract.components.token import Token

logg = logging.getLogger(__name__)


class Extension:
    """Base class adapter to initialize, serialize and publish extension-specific token resources.

    :param chain_spec: Chain Spec that extension will operate for
    :type chain_spec: chainlib.chain.ChainSpec
    :param resources: Chain application resources to deploy or interface with
    :type resources: dict
    :param proof: Proof object to publish
    :type proof: cic.proof.Proof
    :param signer: Signer capable of generating signatures for chain aplication deployments
    :type signer: funga.signer.Signer
    :param rpc: RPC adapter capable of submitting and querying the chain network node
    :type rpc: chainlib.connection.RPCConnection
    :param writer: Writer interface receiving the output of the processor
    :type writer: cic.writers.OutputWriter
    """

    def __init__(
        self,
        chain_spec,
        resources,
        proof,
        signer=None,
        rpc=None,
        outputs_writer=StdoutWriter(),
    ):
        self.resources = resources
        self.proof = proof
        self.chain_spec = chain_spec
        self.signer = signer
        self.rpc = rpc
        self.token_details = None
        self.token_address = None
        self.token_code = None
        self.outputs = []
        self.outputs_writer = outputs_writer

    # TODO: apply / prepare token can be factored out
    def apply_token(self, token: Token):
        """Initialize extension with token data from settings.

        :param token: Token object
        :type token: cic.token.Token
        :rtype: dict
        :returns: Token data state of extension after load
        """
        return self.prepare_token(
            token.name,
            token.symbol,
            token.precision,
            token.code,
            token.supply,
            token.extra_args,
            token.extra_args_types,
        )

    def prepare_token(
        self,
        name,
        symbol,
        precision,
        code,
        supply,
        extra=None,
        extra_types=None,
        positions=None,
    ):
        """Initialize extension token data.

        :param name: Token name
        :type name: str
        :param symbol: Token symbol
        :type symbol: str
        :param precision: Token value precision (number of decimals)
        :type precision: int
        :param code: Bytecode for token chain application
        :type code: str (hex)
        :param supply: Token supply (in smallest precision units)
        :type supply: int
        :param extra: Extra parameters to pass to token application constructor
        :type extra: list
        :param extra_types: Type specifications for extra parameters
        :type extra_types: list
        :param positions: Sequence of parameter indices to pass to application constructor
        :type positions: list
        :rtype: dict
        :returns: Token data state of extension after load
        """
        self.token_details = {
            "name": name,
            "symbol": symbol,
            "precision": precision,
            "code": code,
            "supply": supply,
            "extra": extra or [],
            "extra_types": extra_types or [],
            "positions": positions,
        }
        logg.debug(f"token details: {self.token_details}")
        return self.token_details

    def prepare_extension(self):
        """Prepare extension for publishing (noop)"""


    def parse_code_as_file(self, v):
        """Helper method to load application bytecode from file into extensions token data state.

        Client code should call load_code instead.

        :param v: File path
        :type v: str
        """
        try:
            f = open(v, "r", encoding="utf-8")
            r = f.read()
            f.close()
            self.parse_code_as_hex(r)
        except FileNotFoundError as e:
            logg.debug(f"could not parse code as file: {e}")
        except IsADirectoryError as e:
            logg.debug(f"could not parse code as file: {e}")

    def parse_code_as_hex(self, v):
        """Helper method to load application bytecode from hex data into extension token data state.

        Client code should call load_code instead.

        :param v: Bytecode as hex
        :type v: str
        """
        try:
            self.token_code = valid_hex(v)
        except ValueError as e:
            logg.debug(f"could not parse code as hex: {e}")

    def load_code(self, hint=None):
        """Attempt to load token application bytecode using token settings.

        :param hint: If "hex", will interpret code in settings as literal bytecode
        :type hint: str
        :rtype: str (hex)
        :return: Bytecode loaded into extension token data state
        """
        code = self.token_details["code"]
        if hint == "hex":
            self.token_code = valid_hex(code)

        for m in [
            self.parse_code_as_hex,
            self.parse_code_as_file,
        ]:
            m(code)
            if self.token_code is not None:
                break

        if self.token_code is None:
            raise RuntimeError("could not successfully parse token code")

        return self.token_code

    def process(self, writer=None):
        """Adapter used by Processor to process the extensions implementing the Extension base class.

        Requires either token address or a valid token code reference to have been included in settings.
        If token address is not set, the token application code will be deployed.

        :param writer: Writer to use for publishing.
        :type writer: cic.writers.OutputWriter
        :rtype: tuple
        :return: Token address, token symbol
        """
        if writer is None:
            writer = self.outputs_writer

        tasks = []
        self.token_address = self.resources["token"]["reference"]

        # TODO: get token details when token address is not none
        if self.token_address is None:
            if self.token_details["code"] is None:
                raise RuntimeError("neither token address nor token code has been set")
            self.load_code()
            tasks.append("token")

        for k in self.resources.keys():
            if k == "token":
                continue
            if self.resources[k]["reference"] is not None:
                tasks.append(k)

        self.prepare_extension()

        for task in tasks:
            logg.debug(f"extension adapter process {task}")
            _r = getattr(self, "process_" + task)(writer=writer)

        return (self.token_address, self.token_details.get("symbol"))
