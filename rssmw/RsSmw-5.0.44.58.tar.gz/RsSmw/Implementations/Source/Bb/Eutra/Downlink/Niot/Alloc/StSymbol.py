from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StSymbol:
	"""StSymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stSymbol", core, parent)

	def set(self, start_symbol: enums.EutraDlNbiotStartSymbols, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:STSYmbol \n
		Snippet: driver.source.bb.eutra.downlink.niot.alloc.stSymbol.set(start_symbol = enums.EutraDlNbiotStartSymbols.SYM0, allocationNull = repcap.AllocationNull.Default) \n
		Sets the first symbol in a subframe where NB-IoT channels can be allocated. \n
			:param start_symbol: SYM0| SYM1| SYM2| SYM3
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(start_symbol, enums.EutraDlNbiotStartSymbols)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:STSYmbol {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraDlNbiotStartSymbols:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:STSYmbol \n
		Snippet: value: enums.EutraDlNbiotStartSymbols = driver.source.bb.eutra.downlink.niot.alloc.stSymbol.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the first symbol in a subframe where NB-IoT channels can be allocated. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: start_symbol: SYM0| SYM1| SYM2| SYM3"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:STSYmbol?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDlNbiotStartSymbols)
