from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Analog:
	"""Analog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("analog", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.IqOutMode:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:MODE \n
		Snippet: value: enums.IqOutMode = driver.source.iq.output.analog.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutMode)

	def set_mode(self, mode: enums.IqOutMode) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:MODE \n
		Snippet: driver.source.iq.output.analog.set_mode(mode = enums.IqOutMode.FIXed) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IqOutMode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:MODE {param}')
