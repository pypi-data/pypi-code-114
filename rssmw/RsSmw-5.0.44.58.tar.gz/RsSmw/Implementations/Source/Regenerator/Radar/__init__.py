from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Radar:
	"""Radar commands group definition. 13 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("radar", core, parent)

	@property
	def analyzer(self):
		"""analyzer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_analyzer'):
			from .Analyzer import Analyzer
			self._analyzer = Analyzer(self._core, self._cmd_group)
		return self._analyzer

	@property
	def antenna(self):
		"""antenna commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def ota(self):
		"""ota commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ota'):
			from .Ota import Ota
			self._ota = Ota(self._core, self._cmd_group)
		return self._ota

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	# noinspection PyTypeChecker
	def get_tsetup(self) -> enums.RegRadarTestSetup:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:TSETup \n
		Snippet: value: enums.RegRadarTestSetup = driver.source.regenerator.radar.get_tsetup() \n
		Sets the test setup type. \n
			:return: test_setup: CONDucted| OTA
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:TSETup?')
		return Conversions.str_to_scalar_enum(response, enums.RegRadarTestSetup)

	def set_tsetup(self, test_setup: enums.RegRadarTestSetup) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:TSETup \n
		Snippet: driver.source.regenerator.radar.set_tsetup(test_setup = enums.RegRadarTestSetup.CONDucted) \n
		Sets the test setup type. \n
			:param test_setup: CONDucted| OTA
		"""
		param = Conversions.enum_scalar_to_str(test_setup, enums.RegRadarTestSetup)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:TSETup {param}')

	def clone(self) -> 'Radar':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Radar(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
