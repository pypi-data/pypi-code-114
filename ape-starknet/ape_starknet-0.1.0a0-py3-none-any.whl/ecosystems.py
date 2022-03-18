from typing import Type, Union

from ape.api import (
    BlockAPI,
    BlockConsensusAPI,
    BlockGasAPI,
    EcosystemAPI,
    ReceiptAPI,
    TransactionAPI,
)
from ape.contracts import ContractLog
from ape.types import AddressType
from eth_utils.hexadecimal import is_0x_prefixed
from ethpm_types.abi import ConstructorABI, EventABI, MethodABI
from hexbytes import HexBytes
from starknet_py.net.models.chains import StarknetChainId  # type: ignore
from starknet_py.utils.data_transformer import DataTransformer  # type: ignore
from starkware.starknet.definitions.fields import ContractAddressSalt  # type: ignore
from starkware.starknet.definitions.transaction_type import TransactionType  # type: ignore
from starkware.starknet.public.abi import get_selector_from_name  # type: ignore
from starkware.starknet.public.abi_structs import identifier_manager_from_abi  # type: ignore
from starkware.starknet.services.api.contract_definition import ContractDefinition  # type: ignore

from ape_starknet.exceptions import StarknetEcosystemError
from ape_starknet.transactions import (
    DeployTransaction,
    InvokeFunctionTransaction,
    StarknetReceipt,
    StarknetTransaction,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (StarknetChainId.MAINNET.value, StarknetChainId.MAINNET.value),
    "testnet": (StarknetChainId.TESTNET.value, StarknetChainId.TESTNET.value),
}


class StarknetBlock(BlockAPI):
    gas_data: BlockGasAPI = None  # type: ignore
    consensus_data: BlockConsensusAPI = None  # type: ignore


class Starknet(EcosystemAPI):
    """
    The starknet ``EcosystemAPI`` implementation.
    """

    def serialize_transaction(self, transaction: TransactionAPI) -> bytes:
        if not isinstance(transaction, StarknetTransaction):
            raise StarknetEcosystemError(f"Can only serialize '{StarknetTransaction.__name__}'.")

        starknet_object = transaction.as_starknet_object()
        return starknet_object.deserialize()

    def decode_receipt(self, data: dict) -> ReceiptAPI:
        txn_type = data["type"]

        if txn_type == TransactionType.INVOKE_FUNCTION.value:
            data["receiver"] = data.pop("contract_address")

        return StarknetReceipt(
            provider=data.get("provider"),
            type=data["type"],
            transaction_hash=data["transaction_hash"],
            status=data["status"].value,
            block_number=data["block_number"],
            events=data.get("events", []),
            contract_address=data.get("contract_address"),
            receiver=data.get("receiver", ""),  # TODO: What should receiver be when Deploy?
        )

    def decode_block(self, data: dict) -> BlockAPI:
        return StarknetBlock(
            number=data["block_number"],
            hash=HexBytes(data["block_hash"]),
            parent_hash=HexBytes(data["parent_block_hash"]),
            size=len(data["transactions"]),  # TODO: Figure out size
            timestamp=data["timestamp"],
        )

    def encode_deployment(
        self, deployment_bytecode: HexBytes, abi: ConstructorABI, *args, **kwargs
    ) -> TransactionAPI:
        salt = kwargs.get("salt")
        if not salt:
            salt = ContractAddressSalt.get_random_value()

        contract = ContractDefinition.deserialize(deployment_bytecode)
        abi_data = abi.dict()
        id_manager = identifier_manager_from_abi(contract.abi)

        # TODO: Consider more about a "FeltConverter"
        constructor_args = [int(a, 16) for a in args if isinstance(a, str) and is_0x_prefixed(a)]

        calldata, _args = DataTransformer(abi_data, id_manager).from_python(*constructor_args)
        return DeployTransaction(
            salt=salt, constructor_calldata=calldata, contract_code=contract.dumps()
        )

    def encode_transaction(
        self, address: AddressType, abi: MethodABI, *args, **kwargs
    ) -> TransactionAPI:
        selector = get_selector_from_name(abi.name)
        return InvokeFunctionTransaction(contract_address=address, entry_point_selector=selector)

    def create_transaction(self, **kwargs) -> TransactionAPI:
        txn_type = kwargs.pop("type")
        txn_cls: Union[Type[InvokeFunctionTransaction], Type[DeployTransaction]]
        if txn_type == TransactionType.INVOKE_FUNCTION:
            txn_cls = InvokeFunctionTransaction
        elif txn_type == TransactionType.DEPLOY:
            txn_cls = DeployTransaction

        return txn_cls(**kwargs)

    def decode_event(self, abi: EventABI, receipt: ReceiptAPI) -> ContractLog:
        raise NotImplementedError("TODO")
