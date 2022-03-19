from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.GsmSymbRateMode:
		"""SCPI: [SOURce<HW>]:BB:GSM:SRATe:MODE \n
		Snippet: value: enums.GsmSymbRateMode = driver.source.bb.gsm.symbolRate.get_mode() \n
		Set the symbol rate mode, i.e. determines whether normal bursts (NB) or higher symbol rate bursts (HB) are generated. \n
			:return: mode: NSRate| HSRate
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:SRATe:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.GsmSymbRateMode)

	def set_mode(self, mode: enums.GsmSymbRateMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:SRATe:MODE \n
		Snippet: driver.source.bb.gsm.symbolRate.set_mode(mode = enums.GsmSymbRateMode.HSRate) \n
		Set the symbol rate mode, i.e. determines whether normal bursts (NB) or higher symbol rate bursts (HB) are generated. \n
			:param mode: NSRate| HSRate
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.GsmSymbRateMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:SRATe:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:SRATe \n
		Snippet: value: float = driver.source.bb.gsm.symbolRate.get_value() \n
		Sets the symbol clock. Possible units are Hz, kHz, MHz, Sym/s, kSym/s, MSym/s. \n
			:return: srate: float Range: 400 to 15000000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:SRATe?')
		return Conversions.str_to_float(response)

	def set_value(self, srate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:SRATe \n
		Snippet: driver.source.bb.gsm.symbolRate.set_value(srate = 1.0) \n
		Sets the symbol clock. Possible units are Hz, kHz, MHz, Sym/s, kSym/s, MSym/s. \n
			:param srate: float Range: 400 to 15000000
		"""
		param = Conversions.decimal_value_to_str(srate)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:SRATe {param}')
