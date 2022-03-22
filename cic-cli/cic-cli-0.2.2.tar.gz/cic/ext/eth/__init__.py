# standard imports
import copy
import json
import logging

# external imports
from chainlib.chain import ChainSpec
from chainlib.eth.address import is_address, to_checksum_address
from chainlib.eth.connection import RPCConnection
from chainlib.eth.contract import ABIContractEncoder, ABIContractType
from chainlib.eth.gas import OverrideGasOracle
from chainlib.eth.nonce import RPCNonceOracle
from chainlib.eth.tx import Tx, TxFactory, TxFormat, receipt
from eth_address_declarator import Declarator
from eth_address_declarator.declarator import AddressDeclarator
from eth_token_index import TokenUniqueSymbolIndex
from giftable_erc20_token import GiftableToken
from hexathon import add_0x, strip_0x

# local imports
from cic.ext.eth.rpc import parse_adapter, list_keys
from cic.extension import Extension


logg = logging.getLogger(__name__)


class CICEth(Extension):
    def __init__(
        self,
        chain_spec,
        resources,
        proof,
        signer=None,
        rpc=None,
        outputs_writer=None,
        fee_oracle=None,
    ):

        """Implementation for the eth extension.

        The state of the resources instance will be modified.

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
        :param outputs_writer: Writer interface receiving the output of the processor
        :type outputs_writer: cic.writers.OutputWriter
        :param fee_oracle: Fee oracle required by signer
        :type fee_oracle: chainlib.fee.FeeOracle
        """
        super(CICEth, self).__init__(
            chain_spec,
            resources,
            proof,
            signer=signer,
            rpc=rpc,
            outputs_writer=outputs_writer,
        )
        self.fee_oracle = fee_oracle
        self.tx_format = TxFormat.RAW_ARGS
        if self.rpc is not None:
            self.tx_format = TxFormat.JSONRPC
        elif self.signer is not None:
            self.tx_format = TxFormat.RLP_SIGNED

    def __detect_arg_type(self, v):
        typ = None
        try:
            int(v, 10)
            typ = ABIContractType.UINT256
        except TypeError:
            pass

        if typ is None:
            try:
                vv = strip_0x(v)
                if is_address(vv):
                    typ = ABIContractType.ADDRESS
                else:
                    typ = ABIContractType.BYTES32
            except ValueError:
                pass

        if typ is None:
            try:
                v.encode("utf-8")
                typ = ABIContractType.STRING
            except ValueError:
                pass

        if typ is None:
            raise ValueError(
                f"cannot automatically determine type for value {v}"
            )

        logg.info(f"argument {v} parsed as abi contract type {typ.value}")

        return typ

    def __order_args(self):
        args = [
            self.token_details["name"],
            self.token_details["symbol"],
            self.token_details["precision"],
        ]
        args_types = [
            ABIContractType.STRING.value,
            ABIContractType.STRING.value,
            ABIContractType.UINT256.value,
        ]

        for i, x in enumerate(self.token_details["extra"]):
            args.append(x)
            typ = None
            if self.token_details["extra_types"] is not None:
                typ = self.token_details["extra_types"][i]
            else:
                typ = self.__detect_arg_type(x)
            args_types.append(typ)

        positions = self.token_details["positions"]
        if positions is None:
            positions = list(range(len(args)))

        return (args, args_types, positions)

    def add_outputs(self, k, v):
        """Adds given key/value pair to outputs array.

        :param k: Output key
        :type k: str
        :param v: Output value
        :param v: bytes or str
        """
        logg.debug(f"adding outputs {k} {v}")
        self.outputs.append((k, v))

    def get_outputs(self):
        """Get wrapper for outputs captured from processing.

        :rtype: list of tuples
        :return: Captured outputs
        """
        return self.outputs

    def process_token(self, writer=None):
        """Deploy token, and optionally mint token supply to token deployer account.

        :param writer: Writer interface receiving the output of the processor step
        :type writer: cic.writers.OutputWriter
        """
        if writer is None:
            writer = self.outputs_writer

        (args, args_types, positions) = self.__order_args()

        enc = ABIContractEncoder()

        for i in positions:
            getattr(enc, args_types[i])(args[i])

        code = enc.get()
        if self.token_code is not None:
            code = self.token_code + code

        logg.debug(f"resource {self.resources}")
        signer_address = add_0x(
            to_checksum_address(self.resources["token"]["key_account"])
        )
        nonce_oracle = None
        if self.rpc is not None:
            nonce_oracle = RPCNonceOracle(signer_address, conn=self.rpc)

        c = TxFactory(
            self.chain_spec,
            signer=self.signer,
            nonce_oracle=nonce_oracle,
            gas_oracle=self.fee_oracle,
        )
        tx = c.template(signer_address, None, use_nonce=True)
        tx = c.set_code(tx, code)
        o = c.finalize(tx, self.tx_format)

        token_address_tx = None
        r = None
        if self.rpc is not None:
            r = self.rpc.do(o[1])
            token_address_tx = r
            o = self.rpc.wait(r)
            o = Tx.src_normalize(o)
            self.token_address = o["contract_address"]
        elif self.signer is not None:
            r = o[1]
            token_address_tx = r

        if r is None:
            r = code
        writer.write("token", r.encode("utf-8"))
        writer.write("token_address", self.token_address.encode("utf-8"))
        self.add_outputs("token", r)

        if int(self.token_details["supply"]) > 0:
            c = GiftableToken(
                self.chain_spec,
                signer=self.signer,
                nonce_oracle=nonce_oracle,
                gas_oracle=self.fee_oracle,
            )
            o = c.mint_to(
                self.token_address,
                self.resources["token"]["key_account"],
                self.resources["token"]["key_account"],
                self.token_details["supply"],
            )
            r = None
            if self.rpc is not None:
                r = self.rpc.do(o[1])
                self.rpc.wait(r)
                writer.write("token_supply", r.encode("utf-8"))
            elif self.signer is not None:
                r = o[1]
                writer.write(
                    "token_supply", json.dumps(r, separators=(",", ":")).encode("utf-8")
                )
            else:
                r = o
                writer.write("token_supply", r.encode("utf-8"))

        return token_address_tx

    def process_token_index(self, writer=None):
        """Register deployed token with token index.

        :param writer: Writer interface receiving the output of the processor step
        :type writer: cic.writers.OutputWriter
        """
        if writer is None:
            writer = self.outputs_writer

        signer_address = add_0x(
            to_checksum_address(self.resources["token_index"]["key_account"])
        )
        contract_address = add_0x(
            to_checksum_address(self.resources["token_index"]["reference"])
        )

        gas_oracle = OverrideGasOracle(
            limit=TokenUniqueSymbolIndex.gas(), conn=self.rpc
        )
        nonce_oracle = None
        if self.rpc is not None:
            nonce_oracle = RPCNonceOracle(add_0x(signer_address), conn=self.rpc)
        c = TokenUniqueSymbolIndex(
            self.chain_spec,
            signer=self.signer,
            nonce_oracle=nonce_oracle,
            gas_oracle=gas_oracle,
        )

        o = c.register(
            contract_address,
            signer_address,
            self.token_address,
            tx_format=self.tx_format,
        )
        r = None
        if self.rpc is not None:
            r = self.rpc.do(o[1])
            self.rpc.wait(r)
        elif self.signer is not None:
            r = o[1]
        else:
            r = o

        writer.write("token_index", r.encode("utf-8"))
        self.add_outputs("token_index", r)
        return r

    def process_address_declarator(self, writer=None):
        """Register token proofs with address declarator.

        :param writer: Writer interface receiving the output of the processor step
        :type writer: cic.writers.OutputWriter
        """
        if writer is None:
            writer = self.outputs_writer

        signer_address = add_0x(
            to_checksum_address(self.resources["address_declarator"]["key_account"])
        )
        contract_address = add_0x(
            to_checksum_address(self.resources["address_declarator"]["reference"])
        )

        gas_oracle = OverrideGasOracle(limit=AddressDeclarator.gas(), conn=self.rpc)
        nonce_oracle = None
        if self.rpc is not None:
            nonce_oracle = RPCNonceOracle(signer_address, conn=self.rpc)
        c = Declarator(
            self.chain_spec,
            signer=self.signer,
            nonce_oracle=nonce_oracle,
            gas_oracle=gas_oracle,
        )

        results = []
        # (main_proof, all_proofs) = self.proof.get()

        # for proof in all_proofs:
        # logg.debug('proof {} '.format(proof))

        (k, v) = self.proof.root()

        fk = "address_declarator_" + k
        o = c.add_declaration(
            contract_address,
            signer_address,
            self.token_address,
            k,
            tx_format=self.tx_format,
        )
        r = None
        if self.rpc is not None:
            r = self.rpc.do(o[1])
            self.rpc.wait(r)
        elif self.signer is not None:
            r = o[1]
        else:
            r = o
        self.add_outputs(fk, r)
        results.append(r)
        v = r.encode("utf-8")
        if writer is not None:
            writer.write(fk, v)

        return results

    def prepare_extension(self):
        """Sets token address for extension if defined in settings."""
        super(CICEth, self).prepare_extension()

        if self.token_address is not None:
            self.token_address = add_0x(to_checksum_address(self.token_address))


def new(chain_spec, resources, proof, signer_hint=None, rpc=None, outputs_writer=None):
    """Convenience function to enable object instantiation through predictable module symbol

    See CICEth constructor for details.
    """
    return CICEth(
        chain_spec,
        resources,
        proof,
        signer=signer_hint,
        rpc=rpc,
        outputs_writer=outputs_writer,
    )
