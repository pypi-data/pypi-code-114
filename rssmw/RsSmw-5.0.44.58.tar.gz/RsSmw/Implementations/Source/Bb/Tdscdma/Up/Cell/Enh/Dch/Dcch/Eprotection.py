from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eprotection:
	"""Eprotection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eprotection", core, parent)

	def set(self, eprotection: enums.EnhTchErr, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:DCCH:EPRotection \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.dcch.eprotection.set(eprotection = enums.EnhTchErr.CON2, cell = repcap.Cell.Default) \n
		Sets the error protection. \n
			:param eprotection: NONE| TURBo3| CON2| CON3
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(eprotection, enums.EnhTchErr)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:DCCH:EPRotection {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.EnhTchErr:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:DCCH:EPRotection \n
		Snippet: value: enums.EnhTchErr = driver.source.bb.tdscdma.up.cell.enh.dch.dcch.eprotection.get(cell = repcap.Cell.Default) \n
		Sets the error protection. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: eprotection: NONE| TURBo3| CON2| CON3"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:DCCH:EPRotection?')
		return Conversions.str_to_scalar_enum(response, enums.EnhTchErr)
