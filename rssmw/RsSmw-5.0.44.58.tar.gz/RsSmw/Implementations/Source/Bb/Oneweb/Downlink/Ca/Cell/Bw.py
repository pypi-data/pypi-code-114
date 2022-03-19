from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bw:
	"""Bw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)

	def set(self, bandwidth: enums.OneWebUlChannelBandwidth, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CA:CELL<CH0>:BW \n
		Snippet: driver.source.bb.oneweb.downlink.ca.cell.bw.set(bandwidth = enums.OneWebUlChannelBandwidth.BW20_00, cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param bandwidth: No help available
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.OneWebUlChannelBandwidth)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CA:CELL{cellNull_cmd_val}:BW {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.OneWebUlChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CA:CELL<CH0>:BW \n
		Snippet: value: enums.OneWebUlChannelBandwidth = driver.source.bb.oneweb.downlink.ca.cell.bw.get(cellNull = repcap.CellNull.Default) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: bandwidth: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:CA:CELL{cellNull_cmd_val}:BW?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebUlChannelBandwidth)
