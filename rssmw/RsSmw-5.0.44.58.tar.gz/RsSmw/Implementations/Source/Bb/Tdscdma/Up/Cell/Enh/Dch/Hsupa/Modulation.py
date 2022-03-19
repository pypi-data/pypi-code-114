from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, modulation: enums.ModulationC, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:MODulation \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.modulation.set(modulation = enums.ModulationC.QAM16, cell = repcap.Cell.Default) \n
		Sets the modulation scheme for each HSDPA RMC or HSUPA FRC. The HSUPA FRCs do not support modulation scheme 64QAM. \n
			:param modulation: QPSK| QAM16| QAM64
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationC)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.ModulationC:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSUPA:MODulation \n
		Snippet: value: enums.ModulationC = driver.source.bb.tdscdma.up.cell.enh.dch.hsupa.modulation.get(cell = repcap.Cell.Default) \n
		Sets the modulation scheme for each HSDPA RMC or HSUPA FRC. The HSUPA FRCs do not support modulation scheme 64QAM. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: modulation: QPSK| QAM16| QAM64"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSUPA:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationC)
