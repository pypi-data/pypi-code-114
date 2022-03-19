from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

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

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.btooth.econfiguration.pconfiguration.data.get_dselection() \n
		Specifies data list file. The setting is relevant for [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:DATADLISt \n
			:return: dselection: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DSELection \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.data.set_dselection(dselection = '1') \n
		Specifies data list file. The setting is relevant for [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:DATADLISt \n
			:param dselection: string
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DataSourceB:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA \n
		Snippet: value: enums.DataSourceB = driver.source.bb.btooth.econfiguration.pconfiguration.data.get_value() \n
		Selects the pattern source used for the payload. \n
			:return: data: ALL0| ALL1| PATTern| PN09| PN11| PN15| PN16| PN20| PN21| PN23| DLISt ALL0 / ALL1 All 0 or all 1 pattern PATTern User-defined pattern. The pattern can be specified via: [:SOURcehw]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DPATtern PNxx Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9, 11, 15, 16, 20, 21, or 23. DLISt Internal data list is used. The data list can be specified via: [:SOURcehw]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DSELection
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceB)

	def set_value(self, data: enums.DataSourceB) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.data.set_value(data = enums.DataSourceB.ALL0) \n
		Selects the pattern source used for the payload. \n
			:param data: ALL0| ALL1| PATTern| PN09| PN11| PN15| PN16| PN20| PN21| PN23| DLISt ALL0 / ALL1 All 0 or all 1 pattern PATTern User-defined pattern. The pattern can be specified via: [:SOURcehw]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DPATtern PNxx Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9, 11, 15, 16, 20, 21, or 23. DLISt Internal data list is used. The data list can be specified via: [:SOURcehw]:BB:BTOoth:ECONfiguration:PCONfiguration:DATA:DSELection
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceB)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DATA {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
