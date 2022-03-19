from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timc:
	"""Timc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timc", core, parent)

	# noinspection PyTypeChecker
	def get_nta_offset(self) -> enums.TimcNtAoffs:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TIMC:NTAoffset \n
		Snippet: value: enums.TimcNtAoffs = driver.source.bb.oneweb.timc.get_nta_offset() \n
		No command help available \n
			:return: nta_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TIMC:NTAoffset?')
		return Conversions.str_to_scalar_enum(response, enums.TimcNtAoffs)

	def set_nta_offset(self, nta_offset: enums.TimcNtAoffs) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TIMC:NTAoffset \n
		Snippet: driver.source.bb.oneweb.timc.set_nta_offset(nta_offset = enums.TimcNtAoffs._0) \n
		No command help available \n
			:param nta_offset: No help available
		"""
		param = Conversions.enum_scalar_to_str(nta_offset, enums.TimcNtAoffs)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TIMC:NTAoffset {param}')
