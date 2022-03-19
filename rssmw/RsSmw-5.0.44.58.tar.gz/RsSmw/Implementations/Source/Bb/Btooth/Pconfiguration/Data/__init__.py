from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 5 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def dpattern(self):
		"""dpattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpattern'):
			from .Dpattern import Dpattern
			self._dpattern = Dpattern(self._core, self._cmd_group)
		return self._dpattern

	@property
	def vdPattern(self):
		"""vdPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vdPattern'):
			from .VdPattern import VdPattern
			self._vdPattern = VdPattern(self._core, self._cmd_group)
		return self._vdPattern

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.btooth.pconfiguration.data.get_dselection() \n
		The command selects data list file. \n
			:return: dselection: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DATA:DSELection \n
		Snippet: driver.source.bb.btooth.pconfiguration.data.set_dselection(dselection = '1') \n
		The command selects data list file. \n
			:param dselection: string
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DATA:DSELection {param}')

	def get_vd_selection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DATA:VDSElection \n
		Snippet: value: str = driver.source.bb.btooth.pconfiguration.data.get_vd_selection() \n
		Selects the data list for voice data. \n
			:return: vd_selection: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DATA:VDSElection?')
		return trim_str_response(response)

	def set_vd_selection(self, vd_selection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DATA:VDSElection \n
		Snippet: driver.source.bb.btooth.pconfiguration.data.set_vd_selection(vd_selection = '1') \n
		Selects the data list for voice data. \n
			:param vd_selection: string
		"""
		param = Conversions.value_to_quoted_str(vd_selection)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DATA:VDSElection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DataSourceB:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DATA \n
		Snippet: value: enums.DataSourceB = driver.source.bb.btooth.pconfiguration.data.get_value() \n
		Selects the data source used for the payload. \n
			:return: data: ALL0| ALL1| PATTern| PN09| PN11| PN15| PN16| PN20| PN21| PN23| DLISt
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceB)

	def set_value(self, data: enums.DataSourceB) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DATA \n
		Snippet: driver.source.bb.btooth.pconfiguration.data.set_value(data = enums.DataSourceB.ALL0) \n
		Selects the data source used for the payload. \n
			:param data: ALL0| ALL1| PATTern| PN09| PN11| PN15| PN16| PN20| PN21| PN23| DLISt
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceB)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DATA {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
