from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def get_logarithmic(self) -> float:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:STEP:[LOGarithmic] \n
		Snippet: value: float = driver.source.sweep.power.step.get_logarithmic() \n
		Sets a logarithmically determined step size for the RF level sweep. The level is increased by a logarithmically
		calculated fraction of the current level. See 'Correlating parameters in sweep mode'. \n
			:return: logarithmic: float The unit dB is mandatory. Range: 0.01 to 139 dB, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:STEP:LOGarithmic?')
		return Conversions.str_to_float(response)

	def set_logarithmic(self, logarithmic: float) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:STEP:[LOGarithmic] \n
		Snippet: driver.source.sweep.power.step.set_logarithmic(logarithmic = 1.0) \n
		Sets a logarithmically determined step size for the RF level sweep. The level is increased by a logarithmically
		calculated fraction of the current level. See 'Correlating parameters in sweep mode'. \n
			:param logarithmic: float The unit dB is mandatory. Range: 0.01 to 139 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(logarithmic)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:STEP:LOGarithmic {param}')
