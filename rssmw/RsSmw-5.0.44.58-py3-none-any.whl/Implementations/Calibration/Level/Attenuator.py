from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuator:
	"""Attenuator commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuator", core, parent)

	# noinspection PyTypeChecker
	def get_amplifier(self) -> enums.NumbersI:
		"""SCPI: CALibration<HW>:LEVel:ATTenuator:AMPLifier \n
		Snippet: value: enums.NumbersI = driver.calibration.level.attenuator.get_amplifier() \n
		No command help available \n
			:return: att_amplifier: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:ATTenuator:AMPLifier?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersI)

	def set_amplifier(self, att_amplifier: enums.NumbersI) -> None:
		"""SCPI: CALibration<HW>:LEVel:ATTenuator:AMPLifier \n
		Snippet: driver.calibration.level.attenuator.set_amplifier(att_amplifier = enums.NumbersI._0) \n
		No command help available \n
			:param att_amplifier: No help available
		"""
		param = Conversions.enum_scalar_to_str(att_amplifier, enums.NumbersI)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:ATTenuator:AMPLifier {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.CalPowAttMode:
		"""SCPI: CALibration<HW>:LEVel:ATTenuator:MODE \n
		Snippet: value: enums.CalPowAttMode = driver.calibration.level.attenuator.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:ATTenuator:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CalPowAttMode)

	def get_stage(self) -> int:
		"""SCPI: CALibration<HW>:LEVel:ATTenuator:STAGe \n
		Snippet: value: int = driver.calibration.level.attenuator.get_stage() \n
		No command help available \n
			:return: stage: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:ATTenuator:STAGe?')
		return Conversions.str_to_int(response)

	def set_stage(self, stage: int) -> None:
		"""SCPI: CALibration<HW>:LEVel:ATTenuator:STAGe \n
		Snippet: driver.calibration.level.attenuator.set_stage(stage = 1) \n
		No command help available \n
			:param stage: No help available
		"""
		param = Conversions.decimal_value_to_str(stage)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:ATTenuator:STAGe {param}')
