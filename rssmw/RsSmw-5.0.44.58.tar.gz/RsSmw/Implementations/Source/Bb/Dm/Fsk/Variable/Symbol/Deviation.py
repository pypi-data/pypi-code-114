from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Deviation:
	"""Deviation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deviation", core, parent)

	def set(self, deviation: float, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FSK:VARiable:SYMBol<CH0>:DEViation \n
		Snippet: driver.source.bb.dm.fsk.variable.symbol.deviation.set(deviation = 1.0, indexNull = repcap.IndexNull.Default) \n
		Sets the deviation of the selected symbol for variable FSK modulation mode. \n
			:param deviation: float The value range depends on the selected symbol rate (see data sheet) . Range: -40E6 to 40E6, Unit: Hz
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Symbol')
		"""
		param = Conversions.decimal_value_to_str(deviation)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FSK:VARiable:SYMBol{indexNull_cmd_val}:DEViation {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:FSK:VARiable:SYMBol<CH0>:DEViation \n
		Snippet: value: float = driver.source.bb.dm.fsk.variable.symbol.deviation.get(indexNull = repcap.IndexNull.Default) \n
		Sets the deviation of the selected symbol for variable FSK modulation mode. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Symbol')
			:return: deviation: float The value range depends on the selected symbol rate (see data sheet) . Range: -40E6 to 40E6, Unit: Hz"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DM:FSK:VARiable:SYMBol{indexNull_cmd_val}:DEViation?')
		return Conversions.str_to_float(response)
