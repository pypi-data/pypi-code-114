from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:PHASe:OFFSet \n
		Snippet: value: float = driver.source.iq.doherty.phase.get_offset() \n
		Adds a phase offset. \n
			:return: attenuation: float Range: -999.99 to 999.99
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:PHASe:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, attenuation: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:PHASe:OFFSet \n
		Snippet: driver.source.iq.doherty.phase.set_offset(attenuation = 1.0) \n
		Adds a phase offset. \n
			:param attenuation: float Range: -999.99 to 999.99
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:PHASe:OFFSet {param}')
