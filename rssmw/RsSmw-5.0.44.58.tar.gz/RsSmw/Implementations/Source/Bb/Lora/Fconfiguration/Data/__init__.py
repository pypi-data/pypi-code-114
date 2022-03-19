from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


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
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.lora.fconfiguration.data.get_dselection() \n
		Selects an existing data list file from the default directory or from the specific directory. The data list is only used,
		if the data source DLIS is selected. \n
			:return: dselection: string Filename incl. file extension or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA:DSELection \n
		Snippet: driver.source.bb.lora.fconfiguration.data.set_dselection(dselection = '1') \n
		Selects an existing data list file from the default directory or from the specific directory. The data list is only used,
		if the data source DLIS is selected. \n
			:param dselection: string Filename incl. file extension or complete file path
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA:DSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.lora.fconfiguration.data.get_value() \n
		Sets the data source for the payload data in a LoRa frame. \n
			:return: data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt PNxx The pseudo-random sequence generator is used as the data source. There is a choice of different lengths of random sequence. DLISt A data list is used. The data list is selected with the aid of command SOURce:BB:LORA:DATA DLISt. ALL0 | ALL1 Internal 0 or 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined with the aid of command :SOURce:BB:LORA:DATA PATTern.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)

	def set_value(self, data: enums.DataSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA \n
		Snippet: driver.source.bb.lora.fconfiguration.data.set_value(data = enums.DataSourceA.DLISt) \n
		Sets the data source for the payload data in a LoRa frame. \n
			:param data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt PNxx The pseudo-random sequence generator is used as the data source. There is a choice of different lengths of random sequence. DLISt A data list is used. The data list is selected with the aid of command SOURce:BB:LORA:DATA DLISt. ALL0 | ALL1 Internal 0 or 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined with the aid of command :SOURce:BB:LORA:DATA PATTern.
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
