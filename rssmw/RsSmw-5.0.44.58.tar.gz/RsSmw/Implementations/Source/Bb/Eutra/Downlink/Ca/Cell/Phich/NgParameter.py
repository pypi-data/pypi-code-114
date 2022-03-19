from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NgParameter:
	"""NgParameter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ngParameter", core, parent)

	def set(self, ng_parameter: enums.PhichNg, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CA:CELL<CH0>:PHICh:NGParameter \n
		Snippet: driver.source.bb.eutra.downlink.ca.cell.phich.ngParameter.set(ng_parameter = enums.PhichNg.NG1, cellNull = repcap.CellNull.Default) \n
		Sets the parameter N_g according to . \n
			:param ng_parameter: NG1_6| NG1_2| NG1| NG2| NGCustom NG1_6 | NG1_2 | NG1 | NG2 Determines the number of PHICH groups. NGCustom (not if carrier aggregation is used) The number of PHICH groups are set with the command [:SOURcehw]:BB:EUTRa:DL[:SUBFst0]:ENCC:PHICh[:CELLccidx]:NOGRoups.
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(ng_parameter, enums.PhichNg)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CA:CELL{cellNull_cmd_val}:PHICh:NGParameter {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.PhichNg:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CA:CELL<CH0>:PHICh:NGParameter \n
		Snippet: value: enums.PhichNg = driver.source.bb.eutra.downlink.ca.cell.phich.ngParameter.get(cellNull = repcap.CellNull.Default) \n
		Sets the parameter N_g according to . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: ng_parameter: NG1_6| NG1_2| NG1| NG2| NGCustom NG1_6 | NG1_2 | NG1 | NG2 Determines the number of PHICH groups. NGCustom (not if carrier aggregation is used) The number of PHICH groups are set with the command [:SOURcehw]:BB:EUTRa:DL[:SUBFst0]:ENCC:PHICh[:CELLccidx]:NOGRoups."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CA:CELL{cellNull_cmd_val}:PHICh:NGParameter?')
		return Conversions.str_to_scalar_enum(response, enums.PhichNg)
