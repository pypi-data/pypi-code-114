from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frc:
	"""Frc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frc", core, parent)

	def set(self, frc: enums.TdscdmaEnhHsFrcMode, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:FRC \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.frc.set(frc = enums.TdscdmaEnhHsFrcMode._1, cell = repcap.Cell.Default) \n
		Selects a predefined E-DCH fixed reference channel or fully configurable user mode. \n
			:param frc: 1| 2| 3| 4| USER
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(frc, enums.TdscdmaEnhHsFrcMode)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:FRC {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaEnhHsFrcMode:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:FRC \n
		Snippet: value: enums.TdscdmaEnhHsFrcMode = driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.frc.get(cell = repcap.Cell.Default) \n
		Selects a predefined E-DCH fixed reference channel or fully configurable user mode. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: frc: 1| 2| 3| 4| USER"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:FRC?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaEnhHsFrcMode)
