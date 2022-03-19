from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 10 total commands, 8 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def bbConf(self):
		"""bbConf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbConf'):
			from .BbConf import BbConf
			self._bbConf = BbConf(self._core, self._cmd_group)
		return self._bbConf

	@property
	def bwRef(self):
		"""bwRef commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwRef'):
			from .BwRef import BwRef
			self._bwRef = BwRef(self._core, self._cmd_group)
		return self._bwRef

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def s120K(self):
		"""s120K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s120K'):
			from .S120K import S120K
			self._s120K = S120K(self._core, self._cmd_group)
		return self._s120K

	@property
	def s15K(self):
		"""s15K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s15K'):
			from .S15K import S15K
			self._s15K = S15K(self._core, self._cmd_group)
		return self._s15K

	@property
	def s240K(self):
		"""s240K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s240K'):
			from .S240K import S240K
			self._s240K = S240K(self._core, self._cmd_group)
		return self._s240K

	@property
	def s30K(self):
		"""s30K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s30K'):
			from .S30K import S30K
			self._s30K = S30K(self._core, self._cmd_group)
		return self._s30K

	@property
	def s60K(self):
		"""s60K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s60K'):
			from .S60K import S60K
			self._s60K = S60K(self._core, self._cmd_group)
		return self._s60K

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PowerModeAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:POWer:MODE \n
		Snippet: value: enums.PowerModeAll = driver.source.bb.nr5G.output.power.get_mode() \n
		Sets how the first output is leveled. \n
			:return: power_mode: AVG | ACTvsf| PSDConst AVG Average RMS power ACTvsf Average power in the active subframes PSDConst The absolute power of a particular allocation is set by multiplying the configured power spectral density (PSD) with the bandwidth of the particular allocation. Burst The 'Burst' mode is a special case of the “Constant PSD” mode in the sense that it computes automatically a reference bandwidth based on the chosen allocation.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:OUTPut:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowerModeAll)

	def set_mode(self, power_mode: enums.PowerModeAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:POWer:MODE \n
		Snippet: driver.source.bb.nr5G.output.power.set_mode(power_mode = enums.PowerModeAll.ACTvsf) \n
		Sets how the first output is leveled. \n
			:param power_mode: AVG | ACTvsf| PSDConst AVG Average RMS power ACTvsf Average power in the active subframes PSDConst The absolute power of a particular allocation is set by multiplying the configured power spectral density (PSD) with the bandwidth of the particular allocation. Burst The 'Burst' mode is a special case of the “Constant PSD” mode in the sense that it computes automatically a reference bandwidth based on the chosen allocation.
		"""
		param = Conversions.enum_scalar_to_str(power_mode, enums.PowerModeAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:OUTPut:POWer:MODE {param}')

	def get_rsbw(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:POWer:RSBW \n
		Snippet: value: float = driver.source.bb.nr5G.output.power.get_rsbw() \n
		Sets the reference bandwidth used by the leveling of the output signal at the first output. \n
			:return: ref_system_bw: float Range: 15E3 to 400E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:OUTPut:POWer:RSBW?')
		return Conversions.str_to_float(response)

	def set_rsbw(self, ref_system_bw: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:POWer:RSBW \n
		Snippet: driver.source.bb.nr5G.output.power.set_rsbw(ref_system_bw = 1.0) \n
		Sets the reference bandwidth used by the leveling of the output signal at the first output. \n
			:param ref_system_bw: float Range: 15E3 to 400E6
		"""
		param = Conversions.decimal_value_to_str(ref_system_bw)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:OUTPut:POWer:RSBW {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
