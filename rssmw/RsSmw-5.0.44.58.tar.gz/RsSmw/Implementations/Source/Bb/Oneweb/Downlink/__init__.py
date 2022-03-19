from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 333 total commands, 19 Subgroups, 15 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

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
		"""csis commands group. 0 Sub-classes, 11 commands."""
		if not hasattr(self, '_csis'):
			from .Csis import Csis
			self._csis = Csis(self._core, self._cmd_group)
		return self._csis

	@property
	def dumd(self):
		"""dumd commands group. 1 Sub-classes, 5 commands."""
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
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._cmd_group)
		return self._pdcch

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
		"""prss commands group. 2 Sub-classes, 6 commands."""
		if not hasattr(self, '_prss'):
			from .Prss import Prss
			self._prss = Prss(self._core, self._cmd_group)
		return self._prss

	@property
	def refsig(self):
		"""refsig commands group. 0 Sub-classes, 10 commands."""
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
	def sync(self):
		"""sync commands group. 0 Sub-classes, 11 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def user(self):
		"""user commands group. 22 Sub-classes, 0 commands."""
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
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:BUR \n
		Snippet: value: enums.BehUnsSubFrames = driver.source.bb.oneweb.downlink.get_bur() \n
		No command help available \n
			:return: bur: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:BUR?')
		return Conversions.str_to_scalar_enum(response, enums.BehUnsSubFrames)

	def set_bur(self, bur: enums.BehUnsSubFrames) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:BUR \n
		Snippet: driver.source.bb.oneweb.downlink.set_bur(bur = enums.BehUnsSubFrames.DTX) \n
		No command help available \n
			:param bur: No help available
		"""
		param = Conversions.enum_scalar_to_str(bur, enums.BehUnsSubFrames)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:BUR {param}')

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.OneWebDlChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:BW \n
		Snippet: value: enums.OneWebDlChannelBandwidth = driver.source.bb.oneweb.downlink.get_bw() \n
		Queries the DL channel bandwidth. \n
			:return: bw: BW250_00
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:BW?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebDlChannelBandwidth)

	def get_con_sub_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CONSubframes \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_con_sub_frames() \n
		Sets the number of configurable subframes. \n
			:return: con_sub_frames: integer Range: 1 to 40
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CONSubframes?')
		return Conversions.str_to_int(response)

	def set_con_sub_frames(self, con_sub_frames: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CONSubframes \n
		Snippet: driver.source.bb.oneweb.downlink.set_con_sub_frames(con_sub_frames = 1) \n
		Sets the number of configurable subframes. \n
			:param con_sub_frames: integer Range: 1 to 40
		"""
		param = Conversions.decimal_value_to_str(con_sub_frames)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CONSubframes {param}')

	# noinspection PyTypeChecker
	def get_cpc(self) -> enums.OneWebCyclicPrefixGs:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CPC \n
		Snippet: value: enums.OneWebCyclicPrefixGs = driver.source.bb.oneweb.downlink.get_cpc() \n
		No command help available \n
			:return: cyclic_prefix: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CPC?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebCyclicPrefixGs)

	def get_fft(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:FFT \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_fft() \n
		No command help available \n
			:return: fft: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:FFT?')
		return Conversions.str_to_int(response)

	def get_lgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:LGS \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_lgs() \n
		No command help available \n
			:return: lgs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:LGS?')
		return Conversions.str_to_int(response)

	def get_no_rb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:NORB \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_no_rb() \n
		Queries the number of physical resource blocks per subframe. \n
			:return: no_rb: integer Range: 100 to 1152
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:NORB?')
		return Conversions.str_to_int(response)

	def get_occ_bandwidth(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:OCCBandwidth \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_occ_bandwidth() \n
		Queries the occupied bandwidth. \n
			:return: occup_bandwidth: integer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:OCCBandwidth?')
		return Conversions.str_to_int(response)

	def get_occ_subcarriers(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:OCCSubcarriers \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_occ_subcarriers() \n
		Queries the occupied subcarriers. \n
			:return: occup_subcarr: integer Range: 72 to 1321
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:OCCSubcarriers?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_pum(self) -> enums.PwrUpdMode:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PUM \n
		Snippet: value: enums.PwrUpdMode = driver.source.bb.oneweb.downlink.get_pum() \n
		No command help available \n
			:return: power_update_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PUM?')
		return Conversions.str_to_scalar_enum(response, enums.PwrUpdMode)

	def set_pum(self, power_update_mode: enums.PwrUpdMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:PUM \n
		Snippet: driver.source.bb.oneweb.downlink.set_pum(power_update_mode = enums.PwrUpdMode.CONTinuous) \n
		No command help available \n
			:param power_update_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(power_update_mode, enums.PwrUpdMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PUM {param}')

	# noinspection PyTypeChecker
	def get_rbm(self) -> enums.OneWebResBlckMap:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:RBM \n
		Snippet: value: enums.OneWebResBlckMap = driver.source.bb.oneweb.downlink.get_rbm() \n
		No command help available \n
			:return: res_block_map: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:RBM?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebResBlckMap)

	def set_rbm(self, res_block_map: enums.OneWebResBlckMap) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:RBM \n
		Snippet: driver.source.bb.oneweb.downlink.set_rbm(res_block_map = enums.OneWebResBlckMap.V80) \n
		No command help available \n
			:param res_block_map: No help available
		"""
		param = Conversions.enum_scalar_to_str(res_block_map, enums.OneWebResBlckMap)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:RBM {param}')

	def get_rgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:RGS \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_rgs() \n
		No command help available \n
			:return: rgs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:RGS?')
		return Conversions.str_to_int(response)

	def get_sf_selection(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:SFSelection \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.get_sf_selection() \n
		No command help available \n
			:return: sub_frame_sel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:SFSelection?')
		return Conversions.str_to_int(response)

	def set_sf_selection(self, sub_frame_sel: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:SFSelection \n
		Snippet: driver.source.bb.oneweb.downlink.set_sf_selection(sub_frame_sel = 1) \n
		No command help available \n
			:param sub_frame_sel: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_frame_sel)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:SFSelection {param}')

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:SRATe \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.get_symbol_rate() \n
		Queries the sampling rate. \n
			:return: sample_rate: float Range: 192E4 to 3072E4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:SRATe?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_ulcpc(self) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:ULCPc \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.oneweb.downlink.get_ulcpc() \n
		No command help available \n
			:return: gs_cpc_opp_dir: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:ULCPc?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)

	def set_ulcpc(self, gs_cpc_opp_dir: enums.EuTraDuration) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:ULCPc \n
		Snippet: driver.source.bb.oneweb.downlink.set_ulcpc(gs_cpc_opp_dir = enums.EuTraDuration.EXTended) \n
		No command help available \n
			:param gs_cpc_opp_dir: No help available
		"""
		param = Conversions.enum_scalar_to_str(gs_cpc_opp_dir, enums.EuTraDuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:ULCPc {param}')

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
