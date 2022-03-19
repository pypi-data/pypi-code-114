from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5G:
	"""Nr5G commands group definition. 1281 total commands, 27 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	@property
	def analyzer(self):
		"""analyzer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_analyzer'):
			from .Analyzer import Analyzer
			self._analyzer = Analyzer(self._core, self._cmd_group)
		return self._analyzer

	@property
	def cbwx(self):
		"""cbwx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbwx'):
			from .Cbwx import Cbwx
			self._cbwx = Cbwx(self._core, self._cmd_group)
		return self._cbwx

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def feature(self):
		"""feature commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_feature'):
			from .Feature import Feature
			self._feature = Feature(self._core, self._cmd_group)
		return self._feature

	@property
	def fmode(self):
		"""fmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmode'):
			from .Fmode import Fmode
			self._fmode = Fmode(self._core, self._cmd_group)
		return self._fmode

	@property
	def hfb(self):
		"""hfb commands group. 0 Sub-classes, 12 commands."""
		if not hasattr(self, '_hfb'):
			from .Hfb import Hfb
			self._hfb = Hfb(self._core, self._cmd_group)
		return self._hfb

	@property
	def k145(self):
		"""k145 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k145'):
			from .K145 import K145
			self._k145 = K145(self._core, self._cmd_group)
		return self._k145

	@property
	def k148(self):
		"""k148 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k148'):
			from .K148 import K148
			self._k148 = K148(self._core, self._cmd_group)
		return self._k148

	@property
	def k171(self):
		"""k171 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k171'):
			from .K171 import K171
			self._k171 = K171(self._core, self._cmd_group)
		return self._k171

	@property
	def k175(self):
		"""k175 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k175'):
			from .K175 import K175
			self._k175 = K175(self._core, self._cmd_group)
		return self._k175

	@property
	def k548(self):
		"""k548 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k548'):
			from .K548 import K548
			self._k548 = K548(self._core, self._cmd_group)
		return self._k548

	@property
	def k81(self):
		"""k81 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k81'):
			from .K81 import K81
			self._k81 = K81(self._core, self._cmd_group)
		return self._k81

	@property
	def logGen(self):
		"""logGen commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_logGen'):
			from .LogGen import LogGen
			self._logGen = LogGen(self._core, self._cmd_group)
		return self._logGen

	@property
	def node(self):
		"""node commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_node'):
			from .Node import Node
			self._node = Node(self._core, self._cmd_group)
		return self._node

	@property
	def nsmod(self):
		"""nsmod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsmod'):
			from .Nsmod import Nsmod
			self._nsmod = Nsmod(self._core, self._cmd_group)
		return self._nsmod

	@property
	def output(self):
		"""output commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def qckset(self):
		"""qckset commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_qckset'):
			from .Qckset import Qckset
			self._qckset = Qckset(self._core, self._cmd_group)
		return self._qckset

	@property
	def sanity(self):
		"""sanity commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sanity'):
			from .Sanity import Sanity
			self._sanity = Sanity(self._core, self._cmd_group)
		return self._sanity

	@property
	def scheduling(self):
		"""scheduling commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_scheduling'):
			from .Scheduling import Scheduling
			self._scheduling = Scheduling(self._core, self._cmd_group)
		return self._scheduling

	@property
	def setting(self):
		"""setting commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def tcw(self):
		"""tcw commands group. 11 Sub-classes, 14 commands."""
		if not hasattr(self, '_tcw'):
			from .Tcw import Tcw
			self._tcw = Tcw(self._core, self._cmd_group)
		return self._tcw

	@property
	def tdWind(self):
		"""tdWind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdWind'):
			from .TdWind import TdWind
			self._tdWind = TdWind(self._core, self._cmd_group)
		return self._tdWind

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def ubwp(self):
		"""ubwp commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ubwp'):
			from .Ubwp import Ubwp
			self._ubwp = Ubwp(self._core, self._cmd_group)
		return self._ubwp

	@property
	def uplane(self):
		"""uplane commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplane'):
			from .Uplane import Uplane
			self._uplane = Uplane(self._core, self._cmd_group)
		return self._uplane

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_link(self) -> enums.LinkDir2:
		"""SCPI: [SOURce<HW>]:BB:NR5G:LINK \n
		Snippet: value: enums.LinkDir2 = driver.source.bb.nr5G.get_link() \n
		Selects the transmission direction. \n
			:return: link_dir: DOWN | UP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.LinkDir2)

	def set_link(self, link_dir: enums.LinkDir2) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:LINK \n
		Snippet: driver.source.bb.nr5G.set_link(link_dir = enums.LinkDir2.DOWN) \n
		Selects the transmission direction. \n
			:param link_dir: DOWN | UP
		"""
		param = Conversions.enum_scalar_to_str(link_dir, enums.LinkDir2)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:LINK {param}')

	# noinspection PyTypeChecker
	def get_map_coord(self) -> enums.CoordMapMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:MAPCoord \n
		Snippet: value: enums.CoordMapMode = driver.source.bb.nr5G.get_map_coord() \n
		No command help available \n
			:return: coord_map_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:MAPCoord?')
		return Conversions.str_to_scalar_enum(response, enums.CoordMapMode)

	def set_map_coord(self, coord_map_mode: enums.CoordMapMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:MAPCoord \n
		Snippet: driver.source.bb.nr5G.set_map_coord(coord_map_mode = enums.CoordMapMode.CARTesian) \n
		No command help available \n
			:param coord_map_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(coord_map_mode, enums.CoordMapMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:MAPCoord {param}')

	def get_pl_version(self) -> str:
		"""SCPI: [SOURce]:BB:NR5G:PLVersion \n
		Snippet: value: str = driver.source.bb.nr5G.get_pl_version() \n
		Queries the installed version of the 5G New Radio application. \n
			:return: plugin_version: string
		"""
		response = self._core.io.query_str('SOURce:BB:NR5G:PLVersion?')
		return trim_str_response(response)

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:PRESet \n
		Snippet: driver.source.bb.nr5G.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:NR5G:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:PRESet \n
		Snippet: driver.source.bb.nr5G.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:NR5G:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:NR5G:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:STATe \n
		Snippet: driver.source.bb.nr5G.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce]:BB:NR5G:VERSion \n
		Snippet: value: str = driver.source.bb.nr5G.get_version() \n
		Queries the version of the 3GPP standard underlying the definitions. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SOURce:BB:NR5G:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Nr5G':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr5G(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
