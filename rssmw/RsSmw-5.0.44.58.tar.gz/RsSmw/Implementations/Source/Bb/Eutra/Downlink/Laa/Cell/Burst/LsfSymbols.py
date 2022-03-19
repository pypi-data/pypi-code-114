from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LsfSymbols:
	"""LsfSymbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lsfSymbols", core, parent)

	def set(self, last_sf_symb: enums.EutraLaalAstSf, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:LSFSymbols \n
		Snippet: driver.source.bb.eutra.downlink.laa.cell.burst.lsfSymbols.set(last_sf_symb = enums.EutraLaalAstSf.SY10, cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the number of OFDM symbols in the last subframe of the LAA burst. \n
			:param last_sf_symb: SY3| SY6| SY9| SY10| SY11| SY12| SY14
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
		"""
		param = Conversions.enum_scalar_to_str(last_sf_symb, enums.EutraLaalAstSf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:LSFSymbols {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> enums.EutraLaalAstSf:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:LSFSymbols \n
		Snippet: value: enums.EutraLaalAstSf = driver.source.bb.eutra.downlink.laa.cell.burst.lsfSymbols.get(cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the number of OFDM symbols in the last subframe of the LAA burst. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
			:return: last_sf_symb: SY3| SY6| SY9| SY10| SY11| SY12| SY14"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:LSFSymbols?')
		return Conversions.str_to_scalar_enum(response, enums.EutraLaalAstSf)
