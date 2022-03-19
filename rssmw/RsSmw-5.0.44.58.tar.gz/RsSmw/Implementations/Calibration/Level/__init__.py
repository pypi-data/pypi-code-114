from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 10 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def attenuator(self):
		"""attenuator commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_attenuator'):
			from .Attenuator import Attenuator
			self._attenuator = Attenuator(self._core, self._cmd_group)
		return self._attenuator

	@property
	def haccuracy(self):
		"""haccuracy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_haccuracy'):
			from .Haccuracy import Haccuracy
			self._haccuracy = Haccuracy(self._core, self._cmd_group)
		return self._haccuracy

	@property
	def opu(self):
		"""opu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_opu'):
			from .Opu import Opu
			self._opu = Opu(self._core, self._cmd_group)
		return self._opu

	@property
	def measure(self):
		"""measure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measure'):
			from .Measure import Measure
			self._measure = Measure(self._core, self._cmd_group)
		return self._measure

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.CalPowBandwidth:
		"""SCPI: CALibration<HW>:LEVel:BWIDth \n
		Snippet: value: enums.CalPowBandwidth = driver.calibration.level.get_bandwidth() \n
		No command help available \n
			:return: bandwidth: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.CalPowBandwidth)

	def set_bandwidth(self, bandwidth: enums.CalPowBandwidth) -> None:
		"""SCPI: CALibration<HW>:LEVel:BWIDth \n
		Snippet: driver.calibration.level.set_bandwidth(bandwidth = enums.CalPowBandwidth.AUTO) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.CalPowBandwidth)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:BWIDth {param}')

	# noinspection PyTypeChecker
	def get_det_att(self) -> enums.DetAtt:
		"""SCPI: CALibration<HW>:LEVel:DETatt \n
		Snippet: value: enums.DetAtt = driver.calibration.level.get_det_att() \n
		No command help available \n
			:return: det_att: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:DETatt?')
		return Conversions.str_to_scalar_enum(response, enums.DetAtt)

	def set_det_att(self, det_att: enums.DetAtt) -> None:
		"""SCPI: CALibration<HW>:LEVel:DETatt \n
		Snippet: driver.calibration.level.set_det_att(det_att = enums.DetAtt.HIGH) \n
		No command help available \n
			:param det_att: No help available
		"""
		param = Conversions.enum_scalar_to_str(det_att, enums.DetAtt)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:DETatt {param}')

	def get_local(self) -> bool:
		"""SCPI: CALibration<HW>:LEVel:LOCal \n
		Snippet: value: bool = driver.calibration.level.get_local() \n
		No command help available \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:LOCal?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_state(self) -> enums.StateExtended:
		"""SCPI: CALibration<HW>:LEVel:STATe \n
		Snippet: value: enums.StateExtended = driver.calibration.level.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.StateExtended)

	def set_state(self, state: enums.StateExtended) -> None:
		"""SCPI: CALibration<HW>:LEVel:STATe \n
		Snippet: driver.calibration.level.set_state(state = enums.StateExtended._0) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.StateExtended)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:STATe {param}')

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
