from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	# noinspection PyTypeChecker
	def get_coupling(self) -> enums.AcDc:
		"""SCPI: [SOURce<HW>]:AM:EXTernal:COUPling \n
		Snippet: value: enums.AcDc = driver.source.am.external.get_coupling() \n
		No command help available \n
			:return: coupling: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:EXTernal:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.AcDc)

	def set_coupling(self, coupling: enums.AcDc) -> None:
		"""SCPI: [SOURce<HW>]:AM:EXTernal:COUPling \n
		Snippet: driver.source.am.external.set_coupling(coupling = enums.AcDc.AC) \n
		No command help available \n
			:param coupling: No help available
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.AcDc)
		self._core.io.write(f'SOURce<HwInstance>:AM:EXTernal:COUPling {param}')
