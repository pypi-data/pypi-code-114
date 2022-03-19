from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DAB:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.dab.data.get_dselection() \n
		No command help available \n
			:return: dselection: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:DATA:DSELection \n
		Snippet: driver.source.bb.dab.data.set_dselection(dselection = '1') \n
		No command help available \n
			:param dselection: No help available
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:DATA:DSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DabDataSour:
		"""SCPI: [SOURce<HW>]:BB:DAB:DATA \n
		Snippet: value: enums.DabDataSour = driver.source.bb.dab.data.get_value() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DabDataSour)

	def set_value(self, data: enums.DabDataSour) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:DATA \n
		Snippet: driver.source.bb.dab.data.set_value(data = enums.DabDataSour.ALL0) \n
		No command help available \n
			:param data: No help available
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DabDataSour)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:DATA {param}')
