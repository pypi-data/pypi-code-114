from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:BB:STEReo:TRIGger:RMODe \n
		Snippet: value: enums.TrigRunMode = driver.source.bb.stereo.trigger.get_rmode() \n
		No command help available \n
			:return: rmode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:TRIGger:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	def set_rmode(self, rmode: enums.TrigRunMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:TRIGger:RMODe \n
		Snippet: driver.source.bb.stereo.trigger.set_rmode(rmode = enums.TrigRunMode.RUN) \n
		No command help available \n
			:param rmode: No help available
		"""
		param = Conversions.enum_scalar_to_str(rmode, enums.TrigRunMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:TRIGger:RMODe {param}')

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.ScheduleMode:
		"""SCPI: [SOURce<HW>]:BB:STEReo:[TRIGger]:SEQuence \n
		Snippet: value: enums.ScheduleMode = driver.source.bb.stereo.trigger.get_sequence() \n
		No command help available \n
			:return: sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:TRIGger:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.ScheduleMode)

	def set_sequence(self, sequence: enums.ScheduleMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:[TRIGger]:SEQuence \n
		Snippet: driver.source.bb.stereo.trigger.set_sequence(sequence = enums.ScheduleMode.AUTO) \n
		No command help available \n
			:param sequence: No help available
		"""
		param = Conversions.enum_scalar_to_str(sequence, enums.ScheduleMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:TRIGger:SEQuence {param}')
