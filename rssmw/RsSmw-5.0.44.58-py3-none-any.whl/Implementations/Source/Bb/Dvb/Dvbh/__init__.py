from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbh:
	"""Dvbh commands group definition. 32 total commands, 6 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbh", core, parent)

	@property
	def iinterleaver(self):
		"""iinterleaver commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iinterleaver'):
			from .Iinterleaver import Iinterleaver
			self._iinterleaver = Iinterleaver(self._core, self._cmd_group)
		return self._iinterleaver

	@property
	def ofdm(self):
		"""ofdm commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import Ofdm
			self._ofdm = Ofdm(self._core, self._cmd_group)
		return self._ofdm

	@property
	def sample(self):
		"""sample commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sample'):
			from .Sample import Sample
			self._sample = Sample(self._core, self._cmd_group)
		return self._sample

	@property
	def tps(self):
		"""tps commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tps'):
			from .Tps import Tps
			self._tps = Tps(self._core, self._cmd_group)
		return self._tps

	@property
	def hp(self):
		"""hp commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_hp'):
			from .Hp import Hp
			self._hp = Hp(self._core, self._cmd_group)
		return self._hp

	@property
	def lp(self):
		"""lp commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_lp'):
			from .Lp import Lp
			self._lp = Lp(self._core, self._cmd_group)
		return self._lp

	def get_drate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:DRATe \n
		Snippet: value: float = driver.source.bb.dvb.dvbh.get_drate() \n
		Queries the data rate. \n
			:return: drate: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:DRATe?')
		return Conversions.str_to_float(response)

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:DURation \n
		Snippet: value: float = driver.source.bb.dvb.dvbh.get_duration() \n
		Queries the signal duration. \n
			:return: duration: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:DURation?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_hmode(self) -> enums.DvbHierarchyMode:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:HMODe \n
		Snippet: value: enums.DvbHierarchyMode = driver.source.bb.dvb.dvbh.get_hmode() \n
		Queries the mode for hierarchical coding, that is non-hierachical coding. The current firmware does not support
		hierarchical coding. \n
			:return: hmode: NHIerarchical Non-hierchical coding using high priority input only.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:HMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DvbHierarchyMode)

	def set_hmode(self, hmode: enums.DvbHierarchyMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:HMODe \n
		Snippet: driver.source.bb.dvb.dvbh.set_hmode(hmode = enums.DvbHierarchyMode.HIErarchical) \n
		Queries the mode for hierarchical coding, that is non-hierachical coding. The current firmware does not support
		hierarchical coding. \n
			:param hmode: NHIerarchical Non-hierchical coding using high priority input only.
		"""
		param = Conversions.enum_scalar_to_str(hmode, enums.DvbHierarchyMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:HMODe {param}')

	def get_sframes(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:SFRames \n
		Snippet: value: int = driver.source.bb.dvb.dvbh.get_sframes() \n
		Sets the number of super-frames to be transmitted. \n
			:return: sframes: integer Range: 1 to 1633 (dynamic)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBH:SFRames?')
		return Conversions.str_to_int(response)

	def set_sframes(self, sframes: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBH:SFRames \n
		Snippet: driver.source.bb.dvb.dvbh.set_sframes(sframes = 1) \n
		Sets the number of super-frames to be transmitted. \n
			:param sframes: integer Range: 1 to 1633 (dynamic)
		"""
		param = Conversions.decimal_value_to_str(sframes)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBH:SFRames {param}')

	def clone(self) -> 'Dvbh':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dvbh(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
