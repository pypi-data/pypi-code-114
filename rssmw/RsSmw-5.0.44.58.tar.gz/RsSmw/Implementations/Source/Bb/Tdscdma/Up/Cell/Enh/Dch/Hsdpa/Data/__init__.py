from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def dselect(self):
		"""dselect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dselect'):
			from .Dselect import Dselect
			self._dselect = Dselect(self._core, self._cmd_group)
		return self._dselect

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def set(self, data: enums.DataSourceA, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:DATA \n
		Snippet: driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.data.set(data = enums.DataSourceA.DLISt, cell = repcap.Cell.Default) \n
		The command determines the data source for the HSDPA/HSUPA channels. \n
			:param data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| ZERO| ONE| PATTern PNxx PRBS data as per CCITT with period lengths between 29-1 and 223-1 is generated internally. DLISt Internal data from a programmable data list is used. ZERO | ONE Internal 0 and 1 data is used. PATTern A user-definable bit pattern with a maximum length of 64 bits is generated internally.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:UP:CELL<ST>:ENH:DCH:HSDPA:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.tdscdma.up.cell.enh.dch.hsdpa.data.get(cell = repcap.Cell.Default) \n
		The command determines the data source for the HSDPA/HSUPA channels. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| ZERO| ONE| PATTern PNxx PRBS data as per CCITT with period lengths between 29-1 and 223-1 is generated internally. DLISt Internal data from a programmable data list is used. ZERO | ONE Internal 0 and 1 data is used. PATTern A user-definable bit pattern with a maximum length of 64 bits is generated internally."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:UP:CELL{cell_cmd_val}:ENH:DCH:HSDPA:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
