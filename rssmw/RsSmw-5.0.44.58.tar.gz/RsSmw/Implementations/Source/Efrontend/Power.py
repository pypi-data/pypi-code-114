from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_attenuation(self) -> float:
		"""SCPI: [SOURce<HW>]:EFRontend:POWer:ATTenuation \n
		Snippet: value: float = driver.source.efrontend.power.get_attenuation() \n
		Sets a fixed attenuation of the IF signal to the external frontend. \n
			:return: attenuation: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:POWer:ATTenuation?')
		return Conversions.str_to_float(response)

	def set_attenuation(self, attenuation: float) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:POWer:ATTenuation \n
		Snippet: driver.source.efrontend.power.set_attenuation(attenuation = 1.0) \n
		Sets a fixed attenuation of the IF signal to the external frontend. \n
			:param attenuation: float
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:POWer:ATTenuation {param}')
