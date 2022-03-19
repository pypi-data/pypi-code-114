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
	def get_interval(self) -> enums.DvbtCodingGuardInterval:
		"""SCPI: [SOURce<HW>]:BB:DVBT:GUARd:INTerval \n
		Snippet: value: enums.DvbtCodingGuardInterval = driver.source.bb.dvbt.guard.get_interval() \n
		Sets the guard interval. The interval is expressed in fractions of the useful part of the OFDM symbol period Tu. \n
			:return: guard_int: G1_32| G1_16| G1| G1_| G1_8| G1_4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:GUARd:INTerval?')
		return Conversions.str_to_scalar_enum(response, enums.DvbtCodingGuardInterval)

	def set_interval(self, guard_int: enums.DvbtCodingGuardInterval) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:GUARd:INTerval \n
		Snippet: driver.source.bb.dvbt.guard.set_interval(guard_int = enums.DvbtCodingGuardInterval.G1) \n
		Sets the guard interval. The interval is expressed in fractions of the useful part of the OFDM symbol period Tu. \n
			:param guard_int: G1_32| G1_16| G1| G1_| G1_8| G1_4
		"""
		param = Conversions.enum_scalar_to_str(guard_int, enums.DvbtCodingGuardInterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:GUARd:INTerval {param}')
