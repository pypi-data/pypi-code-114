from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.SlopeRiseFall:
		"""SCPI: BLER:SETup:CLOCk:[POLarity] \n
		Snippet: value: enums.SlopeRiseFall = driver.bler.setup.clock.get_polarity() \n
		No command help available \n
			:return: polarity: No help available
		"""
		response = self._core.io.query_str('BLER:SETup:CLOCk:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeRiseFall)

	def set_polarity(self, polarity: enums.SlopeRiseFall) -> None:
		"""SCPI: BLER:SETup:CLOCk:[POLarity] \n
		Snippet: driver.bler.setup.clock.set_polarity(polarity = enums.SlopeRiseFall.FALLing) \n
		No command help available \n
			:param polarity: No help available
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.SlopeRiseFall)
		self._core.io.write(f'BLER:SETup:CLOCk:POLarity {param}')
