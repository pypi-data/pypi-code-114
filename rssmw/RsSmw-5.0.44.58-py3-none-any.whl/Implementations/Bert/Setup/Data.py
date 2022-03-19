from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormalInverted:
		"""SCPI: BERT:SETup:DATA:[POLarity] \n
		Snippet: value: enums.NormalInverted = driver.bert.setup.data.get_polarity() \n
		Sets the polarity of the feedback data bits. \n
			:return: polarity: NORMal| INVerted NORMal High level represents a logic 1, low level a logic 0. INVerted Low level represents a logic 1, high level a logic 0.
		"""
		response = self._core.io.query_str('BERT:SETup:DATA:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)

	def set_polarity(self, polarity: enums.NormalInverted) -> None:
		"""SCPI: BERT:SETup:DATA:[POLarity] \n
		Snippet: driver.bert.setup.data.set_polarity(polarity = enums.NormalInverted.INVerted) \n
		Sets the polarity of the feedback data bits. \n
			:param polarity: NORMal| INVerted NORMal High level represents a logic 1, low level a logic 0. INVerted Low level represents a logic 1, high level a logic 0.
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.NormalInverted)
		self._core.io.write(f'BERT:SETup:DATA:POLarity {param}')
