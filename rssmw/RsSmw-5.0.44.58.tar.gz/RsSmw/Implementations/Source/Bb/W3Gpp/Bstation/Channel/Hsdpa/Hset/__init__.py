from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hset:
	"""Hset commands group definition. 37 total commands, 29 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hset", core, parent)

	@property
	def acLength(self):
		"""acLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acLength'):
			from .AcLength import AcLength
			self._acLength = AcLength(self._core, self._cmd_group)
		return self._acLength

	@property
	def altModulation(self):
		"""altModulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_altModulation'):
			from .AltModulation import AltModulation
			self._altModulation = AltModulation(self._core, self._cmd_group)
		return self._altModulation

	@property
	def amode(self):
		"""amode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_amode'):
			from .Amode import Amode
			self._amode = Amode(self._core, self._cmd_group)
		return self._amode

	@property
	def bcbtti(self):
		"""bcbtti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bcbtti'):
			from .Bcbtti import Bcbtti
			self._bcbtti = Bcbtti(self._core, self._cmd_group)
		return self._bcbtti

	@property
	def bpayload(self):
		"""bpayload commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bpayload'):
			from .Bpayload import Bpayload
			self._bpayload = Bpayload(self._core, self._cmd_group)
		return self._bpayload

	@property
	def clength(self):
		"""clength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clength'):
			from .Clength import Clength
			self._clength = Clength(self._core, self._cmd_group)
		return self._clength

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import Crate
			self._crate = Crate(self._core, self._cmd_group)
		return self._crate

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def harq(self):
		"""harq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def hscCode(self):
		"""hscCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hscCode'):
			from .HscCode import HscCode
			self._hscCode = HscCode(self._core, self._cmd_group)
		return self._hscCode

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def naiBitrate(self):
		"""naiBitrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_naiBitrate'):
			from .NaiBitrate import NaiBitrate
			self._naiBitrate = NaiBitrate(self._core, self._cmd_group)
		return self._naiBitrate

	@property
	def predefined(self):
		"""predefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_predefined'):
			from .Predefined import Predefined
			self._predefined = Predefined(self._core, self._cmd_group)
		return self._predefined

	@property
	def pwPattern(self):
		"""pwPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwPattern'):
			from .PwPattern import PwPattern
			self._pwPattern = PwPattern(self._core, self._cmd_group)
		return self._pwPattern

	@property
	def rvpSequence(self):
		"""rvpSequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvpSequence'):
			from .RvpSequence import RvpSequence
			self._rvpSequence = RvpSequence(self._core, self._cmd_group)
		return self._rvpSequence

	@property
	def rvParameter(self):
		"""rvParameter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvParameter'):
			from .RvParameter import RvParameter
			self._rvParameter = RvParameter(self._core, self._cmd_group)
		return self._rvParameter

	@property
	def rvState(self):
		"""rvState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvState'):
			from .RvState import RvState
			self._rvState = RvState(self._core, self._cmd_group)
		return self._rvState

	@property
	def s64Qam(self):
		"""s64Qam commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_s64Qam'):
			from .S64Qam import S64Qam
			self._s64Qam = S64Qam(self._core, self._cmd_group)
		return self._s64Qam

	@property
	def scCode(self):
		"""scCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scCode'):
			from .ScCode import ScCode
			self._scCode = ScCode(self._core, self._cmd_group)
		return self._scCode

	@property
	def seed(self):
		"""seed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seed'):
			from .Seed import Seed
			self._seed = Seed(self._core, self._cmd_group)
		return self._seed

	@property
	def slength(self):
		"""slength commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import Slength
			self._slength = Slength(self._core, self._cmd_group)
		return self._slength

	@property
	def spattern(self):
		"""spattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spattern'):
			from .Spattern import Spattern
			self._spattern = Spattern(self._core, self._cmd_group)
		return self._spattern

	@property
	def staPattern(self):
		"""staPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_staPattern'):
			from .StaPattern import StaPattern
			self._staPattern = StaPattern(self._core, self._cmd_group)
		return self._staPattern

	@property
	def tbs(self):
		"""tbs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tbs'):
			from .Tbs import Tbs
			self._tbs = Tbs(self._core, self._cmd_group)
		return self._tbs

	@property
	def tpower(self):
		"""tpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpower'):
			from .Tpower import Tpower
			self._tpower = Tpower(self._core, self._cmd_group)
		return self._tpower

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def ueCategory(self):
		"""ueCategory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueCategory'):
			from .UeCategory import UeCategory
			self._ueCategory = UeCategory(self._core, self._cmd_group)
		return self._ueCategory

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeId
			self._ueId = UeId(self._core, self._cmd_group)
		return self._ueId

	@property
	def vibSize(self):
		"""vibSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vibSize'):
			from .VibSize import VibSize
			self._vibSize = VibSize(self._core, self._cmd_group)
		return self._vibSize

	def set(self, hset: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.set(hset = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		No command help available \n
			:param hset: No help available
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(hset)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		No command help available \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: hset: No help available"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET?')
		return Conversions.str_to_int(response)

	def preset(self, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel:HSDPa:HSET:PRESet \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.preset(baseStation = repcap.BaseStation.Default) \n
		Sets the default settings of the channel table for the HSDPA H-Set mode. Channels 12 to 17 are preset for HSDPA H-Set 1. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel:HSDPa:HSET:PRESet')

	def preset_with_opc(self, baseStation=repcap.BaseStation.Default, opc_timeout_ms: int = -1) -> None:
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel:HSDPa:HSET:PRESet \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.preset_with_opc(baseStation = repcap.BaseStation.Default) \n
		Sets the default settings of the channel table for the HSDPA H-Set mode. Channels 12 to 17 are preset for HSDPA H-Set 1. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel:HSDPa:HSET:PRESet', opc_timeout_ms)

	def clone(self) -> 'Hset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
