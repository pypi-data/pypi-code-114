from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bootstrap:
	"""Bootstrap commands group definition. 12 total commands, 7 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bootstrap", core, parent)

	@property
	def basic(self):
		"""basic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_basic'):
			from .Basic import Basic
			self._basic = Basic(self._core, self._cmd_group)
		return self._basic

	@property
	def bsr(self):
		"""bsr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsr'):
			from .Bsr import Bsr
			self._bsr = Bsr(self._core, self._cmd_group)
		return self._bsr

	@property
	def fft(self):
		"""fft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import Fft
			self._fft = Fft(self._core, self._cmd_group)
		return self._fft

	@property
	def guard(self):
		"""guard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_guard'):
			from .Guard import Guard
			self._guard = Guard(self._core, self._cmd_group)
		return self._guard

	@property
	def pilot(self):
		"""pilot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pilot'):
			from .Pilot import Pilot
			self._pilot = Pilot(self._core, self._cmd_group)
		return self._pilot

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.Atsc30FrameInfoBandwidth:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:BANDwidth \n
		Snippet: value: enums.Atsc30FrameInfoBandwidth = driver.source.bb.a3Tsc.info.bootstrap.get_bandwidth() \n
		Queries the system bandwidth used for the post-bootstrap portion of the current physical layer frame. \n
			:return: frame_info_bw: BW_6| BW_7| BW_8| BW8G
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:BANDwidth?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30FrameInfoBandwidth)

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:DURation \n
		Snippet: value: float = driver.source.bb.a3Tsc.info.bootstrap.get_duration() \n
		Queries the duration of the bootstrap signal in ms. \n
			:return: duration: float Range: 2.000 to 2.000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:DURation?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_eas(self) -> enums.Atsc30EmergencyAlertSignaling:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:EAS \n
		Snippet: value: enums.Atsc30EmergencyAlertSignaling = driver.source.bb.a3Tsc.info.bootstrap.get_eas() \n
		Queries the signaling mode for emergency alert. \n
			:return: eas: NOEMergency| SET1| SET2| SET3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:EAS?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30EmergencyAlertSignaling)

	def get_major(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:MAJor \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.bootstrap.get_major() \n
		Queries the major version of the bootstrap. \n
			:return: major: integer Range: 0 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:MAJor?')
		return Conversions.str_to_int(response)

	def get_minor(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:BOOTstrap:MINor \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.bootstrap.get_minor() \n
		Queries the minor version of the bootstrap. \n
			:return: minor: integer Range: 0 to 7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:BOOTstrap:MINor?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Bootstrap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bootstrap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
