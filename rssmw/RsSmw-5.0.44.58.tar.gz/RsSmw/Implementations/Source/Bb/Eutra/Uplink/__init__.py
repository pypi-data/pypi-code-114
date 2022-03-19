from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 446 total commands, 15 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def apMap(self):
		"""apMap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apMap'):
			from .ApMap import ApMap
			self._apMap = ApMap(self._core, self._cmd_group)
		return self._apMap

	@property
	def ca(self):
		"""ca commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ca'):
			from .Ca import Ca
			self._ca = Ca(self._core, self._cmd_group)
		return self._ca

	@property
	def emtc(self):
		"""emtc commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_emtc'):
			from .Emtc import Emtc
			self._emtc = Emtc(self._core, self._cmd_group)
		return self._emtc

	@property
	def niot(self):
		"""niot commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import Niot
			self._niot = Niot(self._core, self._cmd_group)
		return self._niot

	@property
	def prach(self):
		"""prach commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 10 commands."""
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
		"""rtfb commands group. 0 Sub-classes, 16 commands."""
		if not hasattr(self, '_rtfb'):
			from .Rtfb import Rtfb
			self._rtfb = Rtfb(self._core, self._cmd_group)
		return self._rtfb

	@property
	def ue(self):
		"""ue commands group. 17 Sub-classes, 0 commands."""
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

	@property
	def subf(self):
		"""subf commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_subf'):
			from .Subf import Subf
			self._subf = Subf(self._core, self._cmd_group)
		return self._subf

	# noinspection PyTypeChecker
	def get_bw(self) -> enums.ChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:BW \n
		Snippet: value: enums.ChannelBandwidth = driver.source.bb.eutra.uplink.get_bw() \n
		Sets the UL channel bandwidth. \n
			:return: bandwidth: BW1_40| BW3_00| BW5_00| BW10_00| BW15_00| BW20_00 | BW0_20 | USER
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:BW?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidth)

	def set_bw(self, bandwidth: enums.ChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:BW \n
		Snippet: driver.source.bb.eutra.uplink.set_bw(bandwidth = enums.ChannelBandwidth.BW0_20) \n
		Sets the UL channel bandwidth. \n
			:param bandwidth: BW1_40| BW3_00| BW5_00| BW10_00| BW15_00| BW20_00 | BW0_20 | USER
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.ChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:BW {param}')

	def get_con_sub_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CONSubframes \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_con_sub_frames() \n
		No command help available \n
			:return: conf_subframes: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:CONSubframes?')
		return Conversions.str_to_int(response)

	def set_con_sub_frames(self, conf_subframes: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CONSubframes \n
		Snippet: driver.source.bb.eutra.uplink.set_con_sub_frames(conf_subframes = 1) \n
		No command help available \n
			:param conf_subframes: No help available
		"""
		param = Conversions.decimal_value_to_str(conf_subframes)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:CONSubframes {param}')

	# noinspection PyTypeChecker
	def get_cpc(self) -> enums.CyclicPrefixGs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CPC \n
		Snippet: value: enums.CyclicPrefixGs = driver.source.bb.eutra.uplink.get_cpc() \n
		Sets the cyclic prefix length for all subframes. \n
			:return: cyclic_prefix: NORMal| EXTended | USER
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:CPC?')
		return Conversions.str_to_scalar_enum(response, enums.CyclicPrefixGs)

	def set_cpc(self, cyclic_prefix: enums.CyclicPrefixGs) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CPC \n
		Snippet: driver.source.bb.eutra.uplink.set_cpc(cyclic_prefix = enums.CyclicPrefixGs.EXTended) \n
		Sets the cyclic prefix length for all subframes. \n
			:param cyclic_prefix: NORMal| EXTended | USER
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.CyclicPrefixGs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:CPC {param}')

	# noinspection PyTypeChecker
	def get_dl_cpc(self) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:DLCPc \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.eutra.uplink.get_dl_cpc() \n
		In TDD mode, determines the cyclic prefix for the appropriate opposite direction. \n
			:return: gs_cpc_opp_dir: NORMal| EXTended
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:DLCPc?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)

	def set_dl_cpc(self, gs_cpc_opp_dir: enums.EuTraDuration) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:DLCPc \n
		Snippet: driver.source.bb.eutra.uplink.set_dl_cpc(gs_cpc_opp_dir = enums.EuTraDuration.EXTended) \n
		In TDD mode, determines the cyclic prefix for the appropriate opposite direction. \n
			:param gs_cpc_opp_dir: NORMal| EXTended
		"""
		param = Conversions.enum_scalar_to_str(gs_cpc_opp_dir, enums.EuTraDuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:DLCPc {param}')

	def get_fft(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:FFT \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_fft() \n
		Sets the FFT (Fast Fourier Transformation) size. The available values depend on the selected number of resource blocks
		per slot. \n
			:return: fft_size: integer Range: 64 to 2048
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:FFT?')
		return Conversions.str_to_int(response)

	def set_fft(self, fft_size: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:FFT \n
		Snippet: driver.source.bb.eutra.uplink.set_fft(fft_size = 1) \n
		Sets the FFT (Fast Fourier Transformation) size. The available values depend on the selected number of resource blocks
		per slot. \n
			:param fft_size: integer Range: 64 to 2048
		"""
		param = Conversions.decimal_value_to_str(fft_size)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:FFT {param}')

	def get_lgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:LGS \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_lgs() \n
		Queries the number of left guard subcarriers. The value is set automatically according to the selected number of resource
		blocks per slot. \n
			:return: lg_sub_carr: integer Range: 28 to 364
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:LGS?')
		return Conversions.str_to_int(response)

	def get_no_rb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:NORB \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_no_rb() \n
		Selects the number of physical resource blocks per slot. \n
			:return: num_res_blocks: integer Range: 6 to 110
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:NORB?')
		return Conversions.str_to_int(response)

	def set_no_rb(self, num_res_blocks: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:NORB \n
		Snippet: driver.source.bb.eutra.uplink.set_no_rb(num_res_blocks = 1) \n
		Selects the number of physical resource blocks per slot. \n
			:param num_res_blocks: integer Range: 6 to 110
		"""
		param = Conversions.decimal_value_to_str(num_res_blocks)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:NORB {param}')

	def get_occ_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:OCCBandwidth \n
		Snippet: value: float = driver.source.bb.eutra.uplink.get_occ_bandwidth() \n
		Queries the occupied bandwidth. This value is set automatically according to the selected number of resource blocks per
		slot. \n
			:return: occ_bandwidth: float Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:OCCBandwidth?')
		return Conversions.str_to_float(response)

	def get_occ_subcarriers(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:OCCSubcarriers \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_occ_subcarriers() \n
		Queries the occupied subcarriers. The value is set automatically according to the selected number of resource blocks per
		slot. \n
			:return: occ_subcarriers: integer Range: 72 to 1320
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:OCCSubcarriers?')
		return Conversions.str_to_int(response)

	def get_rgs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RGS \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_rgs() \n
		Queries the number of right guard subcarriers. The value is set automatically according to the selected number of
		resource blocks per slot. \n
			:return: rg_sub_carr: integer Range: 35 to 601
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RGS?')
		return Conversions.str_to_int(response)

	def get_sf_selection(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:SFSelection \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_sf_selection() \n
		No command help available \n
			:return: sub_frame_sel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:SFSelection?')
		return Conversions.str_to_int(response)

	def set_sf_selection(self, sub_frame_sel: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:SFSelection \n
		Snippet: driver.source.bb.eutra.uplink.set_sf_selection(sub_frame_sel = 1) \n
		No command help available \n
			:param sub_frame_sel: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_frame_sel)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:SFSelection {param}')

	def get_soffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:SOFFset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.get_soffset() \n
		Set the start SFN value. \n
			:return: sfn_offset: integer Range: 0 to 4095, Unit: Frames
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, sfn_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:SOFFset \n
		Snippet: driver.source.bb.eutra.uplink.set_soffset(sfn_offset = 1) \n
		Set the start SFN value. \n
			:param sfn_offset: integer Range: 0 to 4095, Unit: Frames
		"""
		param = Conversions.decimal_value_to_str(sfn_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:SOFFset {param}')

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:SRATe \n
		Snippet: value: float = driver.source.bb.eutra.uplink.get_symbol_rate() \n
		Queries the sampling rate. \n
			:return: samp_rate: float Range: 192E4 to 3072E4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
