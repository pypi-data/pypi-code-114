from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stslot:
	"""Stslot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stslot", core, parent)

	def set(self, starting_slots: enums.EutraLaaStartingSlots, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:STSLot \n
		Snippet: driver.source.bb.eutra.downlink.laa.cell.burst.stslot.set(starting_slots = enums.EutraLaaStartingSlots.FIRSt, cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the starting slot. \n
			:param starting_slots: FIRSt| SECond FIRSt s0: first slot of a subframe SECond s7: second slot of a subframe
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
		"""
		param = Conversions.enum_scalar_to_str(starting_slots, enums.EutraLaaStartingSlots)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:STSLot {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> enums.EutraLaaStartingSlots:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:STSLot \n
		Snippet: value: enums.EutraLaaStartingSlots = driver.source.bb.eutra.downlink.laa.cell.burst.stslot.get(cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the starting slot. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
			:return: starting_slots: FIRSt| SECond FIRSt s0: first slot of a subframe SECond s7: second slot of a subframe"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:STSLot?')
		return Conversions.str_to_scalar_enum(response, enums.EutraLaaStartingSlots)
