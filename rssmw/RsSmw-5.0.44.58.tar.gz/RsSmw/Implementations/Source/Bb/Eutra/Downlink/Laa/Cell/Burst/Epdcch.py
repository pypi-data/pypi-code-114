from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Epdcch:
	"""Epdcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("epdcch", core, parent)

	def set(self, epdcch_format: enums.EutraPdccFmtLaa, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:EPDCch \n
		Snippet: driver.source.bb.eutra.downlink.laa.cell.burst.epdcch.set(epdcch_format = enums.EutraPdccFmtLaa.F2, cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the (E) PDCCH format. \n
			:param epdcch_format: F2| F3
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
		"""
		param = Conversions.enum_scalar_to_str(epdcch_format, enums.EutraPdccFmtLaa)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:EPDCch {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> enums.EutraPdccFmtLaa:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:EPDCch \n
		Snippet: value: enums.EutraPdccFmtLaa = driver.source.bb.eutra.downlink.laa.cell.burst.epdcch.get(cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the (E) PDCCH format. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
			:return: epdcch_format: F2| F3"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:EPDCch?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPdccFmtLaa)
