from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Guard:
	"""Guard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("guard", core, parent)

	# noinspection PyTypeChecker
	def get_interval(self) -> enums.Dvbt2FramingGuardInterval:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:GUARd:INTerval \n
		Snippet: value: enums.Dvbt2FramingGuardInterval = driver.source.bb.t2Dvb.guard.get_interval() \n
		Sets the guard interval length. \n
			:return: guard_interval: G1_4| G1_8| G1_16| G1_32| G1128| G19128| G19256
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:GUARd:INTerval?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2FramingGuardInterval)

	def set_interval(self, guard_interval: enums.Dvbt2FramingGuardInterval) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:GUARd:INTerval \n
		Snippet: driver.source.bb.t2Dvb.guard.set_interval(guard_interval = enums.Dvbt2FramingGuardInterval.G1_16) \n
		Sets the guard interval length. \n
			:param guard_interval: G1_4| G1_8| G1_16| G1_32| G1128| G19128| G19256
		"""
		param = Conversions.enum_scalar_to_str(guard_interval, enums.Dvbt2FramingGuardInterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:GUARd:INTerval {param}')
