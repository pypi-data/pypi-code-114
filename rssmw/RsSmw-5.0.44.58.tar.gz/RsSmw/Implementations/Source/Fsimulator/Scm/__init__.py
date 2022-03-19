from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scm:
	"""Scm commands group definition. 53 total commands, 5 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scm", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def d3Mode(self):
		"""d3Mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_d3Mode'):
			from .D3Mode import D3Mode
			self._d3Mode = D3Mode(self._core, self._cmd_group)
		return self._d3Mode

	@property
	def los(self):
		"""los commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_los'):
			from .Los import Los
			self._los = Los(self._core, self._cmd_group)
		return self._los

	@property
	def polarization(self):
		"""polarization commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_polarization'):
			from .Polarization import Polarization
			self._polarization = Polarization(self._core, self._cmd_group)
		return self._polarization

	@property
	def tap(self):
		"""tap commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tap'):
			from .Tap import Tap
			self._tap = Tap(self._core, self._cmd_group)
		return self._tap

	def get_dot(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:DOT \n
		Snippet: value: float = driver.source.fsimulator.scm.get_dot() \n
		Sets the direction of travel of the mobile station. \n
			:return: dir_of_travel: float Range: 0 to 359.9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:DOT?')
		return Conversions.str_to_float(response)

	def set_dot(self, dir_of_travel: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:DOT \n
		Snippet: driver.source.fsimulator.scm.set_dot(dir_of_travel = 1.0) \n
		Sets the direction of travel of the mobile station. \n
			:param dir_of_travel: float Range: 0 to 359.9
		"""
		param = Conversions.decimal_value_to_str(dir_of_travel)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:DOT {param}')

	def get_phi(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:PHI \n
		Snippet: value: float = driver.source.fsimulator.scm.get_phi() \n
		Sets the travel azimuth angle. \n
			:return: scm_phi: float Range: 0 to 359.9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:PHI?')
		return Conversions.str_to_float(response)

	def set_phi(self, scm_phi: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:PHI \n
		Snippet: driver.source.fsimulator.scm.set_phi(scm_phi = 1.0) \n
		Sets the travel azimuth angle. \n
			:param scm_phi: float Range: 0 to 359.9
		"""
		param = Conversions.decimal_value_to_str(scm_phi)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:PHI {param}')

	def get_sigma(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:SIGMa \n
		Snippet: value: float = driver.source.fsimulator.scm.get_sigma() \n
		Sets the lognormal shadow fading standard deviation, applied as a common parameter to the paths. \n
			:return: sigma: float Range: 0 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:SIGMa?')
		return Conversions.str_to_float(response)

	def set_sigma(self, sigma: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:SIGMa \n
		Snippet: driver.source.fsimulator.scm.set_sigma(sigma = 1.0) \n
		Sets the lognormal shadow fading standard deviation, applied as a common parameter to the paths. \n
			:param sigma: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(sigma)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:SIGMa {param}')

	def get_speed(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:SPEed \n
		Snippet: value: float = driver.source.fsimulator.scm.get_speed() \n
		Sets the speed of the mobile station. \n
			:return: speed: float Range: 0 to 27778
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:SPEed?')
		return Conversions.str_to_float(response)

	def set_speed(self, speed: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:SPEed \n
		Snippet: driver.source.fsimulator.scm.set_speed(speed = 1.0) \n
		Sets the speed of the mobile station. \n
			:param speed: float Range: 0 to 27778
		"""
		param = Conversions.decimal_value_to_str(speed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:SPEed {param}')

	def get_theta(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:THETa \n
		Snippet: value: float = driver.source.fsimulator.scm.get_theta() \n
		Sets the elevation angle. \n
			:return: scm_theta: float Range: 0 to 179.9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:THETa?')
		return Conversions.str_to_float(response)

	def set_theta(self, scm_theta: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:THETa \n
		Snippet: driver.source.fsimulator.scm.set_theta(scm_theta = 1.0) \n
		Sets the elevation angle. \n
			:param scm_theta: float Range: 0 to 179.9
		"""
		param = Conversions.decimal_value_to_str(scm_theta)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:THETa {param}')

	def clone(self) -> 'Scm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
