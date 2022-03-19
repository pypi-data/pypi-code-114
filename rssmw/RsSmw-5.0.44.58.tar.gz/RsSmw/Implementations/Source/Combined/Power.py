from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_start(self) -> float:
		"""SCPI: [SOURce<HW>]:COMBined:POWer:STARt \n
		Snippet: value: float = driver.source.combined.power.get_start() \n
		Sets the start level value of the combined RF frequency / level sweep. See 'Correlating parameters in sweep mode'. \n
			:return: comb_pow_start: float Range: -245 to 120
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:COMBined:POWer:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, comb_pow_start: float) -> None:
		"""SCPI: [SOURce<HW>]:COMBined:POWer:STARt \n
		Snippet: driver.source.combined.power.set_start(comb_pow_start = 1.0) \n
		Sets the start level value of the combined RF frequency / level sweep. See 'Correlating parameters in sweep mode'. \n
			:param comb_pow_start: float Range: -245 to 120
		"""
		param = Conversions.decimal_value_to_str(comb_pow_start)
		self._core.io.write(f'SOURce<HwInstance>:COMBined:POWer:STARt {param}')

	def get_stop(self) -> float:
		"""SCPI: [SOURce<HW>]:COMBined:POWer:STOP \n
		Snippet: value: float = driver.source.combined.power.get_stop() \n
		Sets the stop level value of the combined RF frequency / level sweep. \n
			:return: comb_pow_stop: float Range: -245 to 120
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:COMBined:POWer:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, comb_pow_stop: float) -> None:
		"""SCPI: [SOURce<HW>]:COMBined:POWer:STOP \n
		Snippet: driver.source.combined.power.set_stop(comb_pow_stop = 1.0) \n
		Sets the stop level value of the combined RF frequency / level sweep. \n
			:param comb_pow_stop: float Range: -245 to 120
		"""
		param = Conversions.decimal_value_to_str(comb_pow_stop)
		self._core.io.write(f'SOURce<HwInstance>:COMBined:POWer:STOP {param}')
