from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 227 total commands, 12 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def ca(self):
		"""ca commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ca'):
			from .Ca import Ca
			self._ca = Ca(self._core, self._cmd_group)
		return self._ca

	@property
	def prach(self):
		"""prach commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def refsig(self):
		"""refsig commands group. 2 Sub-classes, 4 commands."""
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
	def rtfb(self):
		"""rtfb commands group. 0 Sub-classes, 15 commands."""
		if not hasattr(self, '_rtfb'):
			from .Rtfb import Rtfb
			self._rtfb = Rtfb(self._core, self._cmd_group)
		return self._rtfb

	@property
	def subf(self):
		"""subf commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_subf'):
			from .Subf import Subf
			self._subf = Subf(self._core, self._cmd_group)
		return self._subf

	@property
	def ue(self):
		"""ue commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import Ue
			self._ue = Ue(self._core, self._cmd_group)
		return self._ue

	@property
	def view(self):
		"""view commands group. 0 Sub-classes, 4 commands."""
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

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.ChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:BW \n
		Snippet: value: enums.ChannelBandwidth = driver.source.bb.v5G.uplink.get_bw() \n
		No command help available \n
			:return: bandwidth: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:BW?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidth)

	def set_bw(self, bandwidth: enums.ChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:BW \n
		Snippet: driver.source.bb.v5G.uplink.set_bw(bandwidth = enums.ChannelBandwidth.BW0_20) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.ChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:BW {param}')

	def get_con_sub_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:CONSubframes \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_con_sub_frames() \n
		No command help available \n
			:return: conf_subframes: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:CONSubframes?')
		return Conversions.str_to_int(response)

	def set_con_sub_frames(self, conf_subframes: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:CONSubframes \n
		Snippet: driver.source.bb.v5G.uplink.set_con_sub_frames(conf_subframes = 1) \n
		No command help available \n
			:param conf_subframes: No help available
		"""
		param = Conversions.decimal_value_to_str(conf_subframes)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:CONSubframes {param}')

	# noinspection PyTypeChecker
	def get_cpc(self) -> enums.CyclicPrefixGs:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:CPC \n
		Snippet: value: enums.CyclicPrefixGs = driver.source.bb.v5G.uplink.get_cpc() \n
		No command help available \n
			:return: cyclic_prefix: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:CPC?')
		return Conversions.str_to_scalar_enum(response, enums.CyclicPrefixGs)

	def set_cpc(self, cyclic_prefix: enums.CyclicPrefixGs) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:CPC \n
		Snippet: driver.source.bb.v5G.uplink.set_cpc(cyclic_prefix = enums.CyclicPrefixGs.EXTended) \n
		No command help available \n
			:param cyclic_prefix: No help available
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.CyclicPrefixGs)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:CPC {param}')

	# noinspection PyTypeChecker
	def get_dl_cpc(self) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:DLCPc \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.v5G.uplink.get_dl_cpc() \n
		No command help available \n
			:return: gs_cpc_opp_dir: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:DLCPc?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)

	def set_dl_cpc(self, gs_cpc_opp_dir: enums.EuTraDuration) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:DLCPc \n
		Snippet: driver.source.bb.v5G.uplink.set_dl_cpc(gs_cpc_opp_dir = enums.EuTraDuration.EXTended) \n
		No command help available \n
			:param gs_cpc_opp_dir: No help available
		"""
		param = Conversions.enum_scalar_to_str(gs_cpc_opp_dir, enums.EuTraDuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:DLCPc {param}')

	def get_fft(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:FFT \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_fft() \n
		No command help available \n
			:return: fft_size: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:FFT?')
		return Conversions.str_to_int(response)

	def set_fft(self, fft_size: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:FFT \n
		Snippet: driver.source.bb.v5G.uplink.set_fft(fft_size = 1) \n
		No command help available \n
			:param fft_size: No help available
		"""
		param = Conversions.decimal_value_to_str(fft_size)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:FFT {param}')

	def get_lgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:LGS \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_lgs() \n
		No command help available \n
			:return: lg_sub_carr: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:LGS?')
		return Conversions.str_to_int(response)

	def get_no_rb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:NORB \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_no_rb() \n
		No command help available \n
			:return: num_res_blocks: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:NORB?')
		return Conversions.str_to_int(response)

	def set_no_rb(self, num_res_blocks: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:NORB \n
		Snippet: driver.source.bb.v5G.uplink.set_no_rb(num_res_blocks = 1) \n
		No command help available \n
			:param num_res_blocks: No help available
		"""
		param = Conversions.decimal_value_to_str(num_res_blocks)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:NORB {param}')

	def get_occ_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:OCCBandwidth \n
		Snippet: value: float = driver.source.bb.v5G.uplink.get_occ_bandwidth() \n
		No command help available \n
			:return: occ_bandwidth: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:OCCBandwidth?')
		return Conversions.str_to_float(response)

	def get_occ_subcarriers(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:OCCSubcarriers \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_occ_subcarriers() \n
		No command help available \n
			:return: occ_subcarriers: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:OCCSubcarriers?')
		return Conversions.str_to_int(response)

	def get_rgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:RGS \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_rgs() \n
		No command help available \n
			:return: rg_sub_carr: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:RGS?')
		return Conversions.str_to_int(response)

	def get_sf_selection(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SFSelection \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_sf_selection() \n
		No command help available \n
			:return: sub_frame_sel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:SFSelection?')
		return Conversions.str_to_int(response)

	def set_sf_selection(self, sub_frame_sel: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SFSelection \n
		Snippet: driver.source.bb.v5G.uplink.set_sf_selection(sub_frame_sel = 1) \n
		No command help available \n
			:param sub_frame_sel: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_frame_sel)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:SFSelection {param}')

	def get_soffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SOFFset \n
		Snippet: value: int = driver.source.bb.v5G.uplink.get_soffset() \n
		No command help available \n
			:return: sfn_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, sfn_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SOFFset \n
		Snippet: driver.source.bb.v5G.uplink.set_soffset(sfn_offset = 1) \n
		No command help available \n
			:param sfn_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(sfn_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:SOFFset {param}')

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SRATe \n
		Snippet: value: float = driver.source.bb.v5G.uplink.get_symbol_rate() \n
		No command help available \n
			:return: samp_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
