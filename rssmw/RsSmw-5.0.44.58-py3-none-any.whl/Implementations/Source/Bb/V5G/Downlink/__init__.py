from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 338 total commands, 22 Subgroups, 15 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def apm(self):
		"""apm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apm'):
			from .Apm import Apm
			self._apm = Apm(self._core, self._cmd_group)
		return self._apm

	@property
	def ca(self):
		"""ca commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ca'):
			from .Ca import Ca
			self._ca = Ca(self._core, self._cmd_group)
		return self._ca

	@property
	def conf(self):
		"""conf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conf'):
			from .Conf import Conf
			self._conf = Conf(self._core, self._cmd_group)
		return self._conf

	@property
	def csettings(self):
		"""csettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csettings'):
			from .Csettings import Csettings
			self._csettings = Csettings(self._core, self._cmd_group)
		return self._csettings

	@property
	def csis(self):
		"""csis commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csis'):
			from .Csis import Csis
			self._csis = Csis(self._core, self._cmd_group)
		return self._csis

	@property
	def drs(self):
		"""drs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_drs'):
			from .Drs import Drs
			self._drs = Drs(self._core, self._cmd_group)
		return self._drs

	@property
	def dumd(self):
		"""dumd commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_dumd'):
			from .Dumd import Dumd
			self._dumd = Dumd(self._core, self._cmd_group)
		return self._dumd

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	@property
	def pbch(self):
		"""pbch commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_pbch'):
			from .Pbch import Pbch
			self._pbch = Pbch(self._core, self._cmd_group)
		return self._pbch

	@property
	def pdsch(self):
		"""pdsch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._cmd_group)
		return self._pdsch

	@property
	def phich(self):
		"""phich commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_phich'):
			from .Phich import Phich
			self._phich = Phich(self._core, self._cmd_group)
		return self._phich

	@property
	def prss(self):
		"""prss commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_prss'):
			from .Prss import Prss
			self._prss = Prss(self._core, self._cmd_group)
		return self._prss

	@property
	def refsig(self):
		"""refsig commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_refsig'):
			from .Refsig import Refsig
			self._refsig = Refsig(self._core, self._cmd_group)
		return self._refsig

	@property
	def rstFrame(self):
		"""rstFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rstFrame'):
			from .RstFrame import RstFrame
			self._rstFrame = RstFrame(self._core, self._cmd_group)
		return self._rstFrame

	@property
	def signals(self):
		"""signals commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signals'):
			from .Signals import Signals
			self._signals = Signals(self._core, self._cmd_group)
		return self._signals

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 12 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def user(self):
		"""user commands group. 23 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	@property
	def view(self):
		"""view commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_view'):
			from .View import View
			self._view = View(self._core, self._cmd_group)
		return self._view

	@property
	def xpdcch(self):
		"""xpdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xpdcch'):
			from .Xpdcch import Xpdcch
			self._xpdcch = Xpdcch(self._core, self._cmd_group)
		return self._xpdcch

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	@property
	def plci(self):
		"""plci commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_plci'):
			from .Plci import Plci
			self._plci = Plci(self._core, self._cmd_group)
		return self._plci

	@property
	def subf(self):
		"""subf commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_subf'):
			from .Subf import Subf
			self._subf = Subf(self._core, self._cmd_group)
		return self._subf

	# noinspection PyTypeChecker
	def get_bur(self) -> enums.BehUnsSubFrames:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:BUR \n
		Snippet: value: enums.BehUnsSubFrames = driver.source.bb.v5G.downlink.get_bur() \n
		No command help available \n
			:return: bur: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:BUR?')
		return Conversions.str_to_scalar_enum(response, enums.BehUnsSubFrames)

	def set_bur(self, bur: enums.BehUnsSubFrames) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:BUR \n
		Snippet: driver.source.bb.v5G.downlink.set_bur(bur = enums.BehUnsSubFrames.DTX) \n
		No command help available \n
			:param bur: No help available
		"""
		param = Conversions.enum_scalar_to_str(bur, enums.BehUnsSubFrames)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:BUR {param}')

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.ChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:BW \n
		Snippet: value: enums.ChannelBandwidth = driver.source.bb.v5G.downlink.get_bw() \n
		No command help available \n
			:return: bw: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:BW?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidth)

	def set_bw(self, bw: enums.ChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:BW \n
		Snippet: driver.source.bb.v5G.downlink.set_bw(bw = enums.ChannelBandwidth.BW0_20) \n
		No command help available \n
			:param bw: No help available
		"""
		param = Conversions.enum_scalar_to_str(bw, enums.ChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:BW {param}')

	def get_con_sub_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CONSubframes \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_con_sub_frames() \n
		Sets the number of configurable subframes. \n
			:return: con_sub_frames: integer Range: 1 to 40
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:CONSubframes?')
		return Conversions.str_to_int(response)

	def set_con_sub_frames(self, con_sub_frames: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CONSubframes \n
		Snippet: driver.source.bb.v5G.downlink.set_con_sub_frames(con_sub_frames = 1) \n
		Sets the number of configurable subframes. \n
			:param con_sub_frames: integer Range: 1 to 40
		"""
		param = Conversions.decimal_value_to_str(con_sub_frames)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CONSubframes {param}')

	# noinspection PyTypeChecker
	def get_cpc(self) -> enums.CyclicPrefixGs:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CPC \n
		Snippet: value: enums.CyclicPrefixGs = driver.source.bb.v5G.downlink.get_cpc() \n
		No command help available \n
			:return: cyclic_prefix: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:CPC?')
		return Conversions.str_to_scalar_enum(response, enums.CyclicPrefixGs)

	def set_cpc(self, cyclic_prefix: enums.CyclicPrefixGs) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CPC \n
		Snippet: driver.source.bb.v5G.downlink.set_cpc(cyclic_prefix = enums.CyclicPrefixGs.EXTended) \n
		No command help available \n
			:param cyclic_prefix: No help available
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.CyclicPrefixGs)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CPC {param}')

	def get_fft(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:FFT \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_fft() \n
		No command help available \n
			:return: fft: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:FFT?')
		return Conversions.str_to_int(response)

	def set_fft(self, fft: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:FFT \n
		Snippet: driver.source.bb.v5G.downlink.set_fft(fft = 1) \n
		No command help available \n
			:param fft: No help available
		"""
		param = Conversions.decimal_value_to_str(fft)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:FFT {param}')

	def get_lgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:LGS \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_lgs() \n
		No command help available \n
			:return: lgs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:LGS?')
		return Conversions.str_to_int(response)

	def get_no_rb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:NORB \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_no_rb() \n
		No command help available \n
			:return: no_rb: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:NORB?')
		return Conversions.str_to_int(response)

	def set_no_rb(self, no_rb: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:NORB \n
		Snippet: driver.source.bb.v5G.downlink.set_no_rb(no_rb = 1) \n
		No command help available \n
			:param no_rb: No help available
		"""
		param = Conversions.decimal_value_to_str(no_rb)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:NORB {param}')

	def get_occ_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:OCCBandwidth \n
		Snippet: value: float = driver.source.bb.v5G.downlink.get_occ_bandwidth() \n
		No command help available \n
			:return: occup_bandwidth: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:OCCBandwidth?')
		return Conversions.str_to_float(response)

	def get_occ_subcarriers(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:OCCSubcarriers \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_occ_subcarriers() \n
		No command help available \n
			:return: occup_subcarr: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:OCCSubcarriers?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_pum(self) -> enums.PwrUpdMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PUM \n
		Snippet: value: enums.PwrUpdMode = driver.source.bb.v5G.downlink.get_pum() \n
		No command help available \n
			:return: power_update_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PUM?')
		return Conversions.str_to_scalar_enum(response, enums.PwrUpdMode)

	def set_pum(self, power_update_mode: enums.PwrUpdMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PUM \n
		Snippet: driver.source.bb.v5G.downlink.set_pum(power_update_mode = enums.PwrUpdMode.CONTinuous) \n
		No command help available \n
			:param power_update_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(power_update_mode, enums.PwrUpdMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PUM {param}')

	# noinspection PyTypeChecker
	def get_rbm(self) -> enums.OneWebResBlckMap:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:RBM \n
		Snippet: value: enums.OneWebResBlckMap = driver.source.bb.v5G.downlink.get_rbm() \n
		No command help available \n
			:return: res_block_map: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:RBM?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebResBlckMap)

	def set_rbm(self, res_block_map: enums.OneWebResBlckMap) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:RBM \n
		Snippet: driver.source.bb.v5G.downlink.set_rbm(res_block_map = enums.OneWebResBlckMap.V80) \n
		No command help available \n
			:param res_block_map: No help available
		"""
		param = Conversions.enum_scalar_to_str(res_block_map, enums.OneWebResBlckMap)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:RBM {param}')

	def get_rgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:RGS \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_rgs() \n
		No command help available \n
			:return: rgs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:RGS?')
		return Conversions.str_to_int(response)

	def get_sf_selection(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SFSelection \n
		Snippet: value: int = driver.source.bb.v5G.downlink.get_sf_selection() \n
		No command help available \n
			:return: sub_frame_sel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SFSelection?')
		return Conversions.str_to_int(response)

	def set_sf_selection(self, sub_frame_sel: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SFSelection \n
		Snippet: driver.source.bb.v5G.downlink.set_sf_selection(sub_frame_sel = 1) \n
		No command help available \n
			:param sub_frame_sel: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_frame_sel)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SFSelection {param}')

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SRATe \n
		Snippet: value: float = driver.source.bb.v5G.downlink.get_symbol_rate() \n
		No command help available \n
			:return: sample_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SRATe?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_ulcpc(self) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:ULCPc \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.v5G.downlink.get_ulcpc() \n
		No command help available \n
			:return: gs_cpc_opp_dir: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:ULCPc?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)

	def set_ulcpc(self, gs_cpc_opp_dir: enums.EuTraDuration) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:ULCPc \n
		Snippet: driver.source.bb.v5G.downlink.set_ulcpc(gs_cpc_opp_dir = enums.EuTraDuration.EXTended) \n
		No command help available \n
			:param gs_cpc_opp_dir: No help available
		"""
		param = Conversions.enum_scalar_to_str(gs_cpc_opp_dir, enums.EuTraDuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:ULCPc {param}')

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
