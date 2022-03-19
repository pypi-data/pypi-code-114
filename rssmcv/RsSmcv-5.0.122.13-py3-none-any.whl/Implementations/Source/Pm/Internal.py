from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Internal:
	"""Internal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("internal", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.AmSourceInt:
		"""SCPI: [SOURce<HW>]:PM:INTernal:SOURce \n
		Snippet: value: enums.AmSourceInt = driver.source.pm.internal.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PM:INTernal:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.AmSourceInt)

	def set_source(self, source: enums.AmSourceInt) -> None:
		"""SCPI: [SOURce<HW>]:PM:INTernal:SOURce \n
		Snippet: driver.source.pm.internal.set_source(source = enums.AmSourceInt.LF1) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.AmSourceInt)
		self._core.io.write(f'SOURce<HwInstance>:PM:INTernal:SOURce {param}')
