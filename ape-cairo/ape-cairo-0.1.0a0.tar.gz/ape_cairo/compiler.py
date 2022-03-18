from pathlib import Path
from typing import List, Optional, Set

from ape.api import CompilerAPI
from ape.exceptions import CompilerError
from ape.types import ContractType
from ape.utils import get_relative_path
from pkg_resources import get_distribution
from starknet_py.utils.compiler.starknet_compile import starknet_compile
from starkware.starknet.services.api.contract_definition import ContractDefinition  # type: ignore


class ContractAdapter:
    """
    A class that maps a Starknet cairo contract to an EthPM manifest compliant object.
    """

    def __init__(self, name: str, source_id: str, definition: ContractDefinition):
        self.name = name
        self.source_id = source_id
        self.definition = definition

    @classmethod
    def from_starknet_compile(
        cls, compile_result: str, contract_path: Path, base_path: Optional[Path] = None
    ) -> "ContractAdapter":
        name = contract_path.stem
        source_id = (
            str(get_relative_path(contract_path, base_path)) if base_path else str(contract_path)
        )
        definition = ContractDefinition.loads(compile_result)
        return cls(name, source_id, definition)

    def to_contract_type(self) -> ContractType:
        contract_type_data = {
            "contractName": self.name,
            "sourceId": self.source_id,
            "abi": self.definition.abi,
            "deploymentBytecode": {"bytecode": ""},  # TODO: Test this with constructor
            "runtimeBytecode": {"bytescode": self.definition.program.serialize()}
        }
        contract_type = ContractType(**contract_type_data)
        return contract_type

def convert_starknet_contract(
    compile_result: str, contract_path: Path, base_path: Optional[Path] = None
) -> ContractType:
    adapter = ContractAdapter.from_starknet_compile(compile_result, contract_path, base_path)
    return adapter.to_contract_type()


class CairoCompiler(CompilerAPI):
    @property
    def name(self) -> str:
        return "cairo"

    def get_versions(self, all_paths: List[Path]) -> Set[str]:
        # NOTE: Currently, we are not doing anything with versions.
        return {get_distribution("cairo-lang").version}

    def compile(
        self, contract_filepaths: List[Path], base_path: Optional[Path]
    ) -> List[ContractType]:
        if not contract_filepaths:
            return []

        contract_types = []
        for contract_path in contract_filepaths:
            search_paths = [base_path] if base_path else []

            try:
                result_str = starknet_compile(contract_path.read_text(), search_paths=search_paths)
            except ValueError as err:
                raise CompilerError(f"Failed to compile '{contract_path.name}': {err}") from err

            contract_type = convert_starknet_contract(
                result_str, contract_path, base_path=base_path
            )
            contract_types.append(contract_type)

        return contract_types
