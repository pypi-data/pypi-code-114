from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	# noinspection PyTypeChecker
	def get_interleaver(self) -> enums.DtmbCodingTimeInterleaver:
		"""SCPI: [SOURce<HW>]:BB:DTMB:TIME:[INTerleaver] \n
		Snippet: value: enums.DtmbCodingTimeInterleaver = driver.source.bb.dtmb.time.get_interleaver() \n
		Defines the depth of the basic delay. \n
			:return: dtmb_time_int: OFF| I240| I720 I240|I720 Basic delay of 240/720 symbols OFF Disables/bridges the time interleaver.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:TIME:INTerleaver?')
		return Conversions.str_to_scalar_enum(response, enums.DtmbCodingTimeInterleaver)

	def set_interleaver(self, dtmb_time_int: enums.DtmbCodingTimeInterleaver) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:TIME:[INTerleaver] \n
		Snippet: driver.source.bb.dtmb.time.set_interleaver(dtmb_time_int = enums.DtmbCodingTimeInterleaver.I240) \n
		Defines the depth of the basic delay. \n
			:param dtmb_time_int: OFF| I240| I720 I240|I720 Basic delay of 240/720 symbols OFF Disables/bridges the time interleaver.
		"""
		param = Conversions.enum_scalar_to_str(dtmb_time_int, enums.DtmbCodingTimeInterleaver)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:TIME:INTerleaver {param}')
