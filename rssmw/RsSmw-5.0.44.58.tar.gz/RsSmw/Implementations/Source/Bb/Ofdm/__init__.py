from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ofdm:
	"""Ofdm commands group definition. 101 total commands, 15 Subgroups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofdm", core, parent)

	@property
	def alloc(self):
		"""alloc commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_alloc'):
			from .Alloc import Alloc
			self._alloc = Alloc(self._core, self._cmd_group)
		return self._alloc

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def cpLength(self):
		"""cpLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpLength'):
			from .CpLength import CpLength
			self._cpLength = CpLength(self._core, self._cmd_group)
		return self._cpLength

	@property
	def dfts(self):
		"""dfts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfts'):
			from .Dfts import Dfts
			self._dfts = Dfts(self._core, self._cmd_group)
		return self._dfts

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def fofdm(self):
		"""fofdm commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fofdm'):
			from .Fofdm import Fofdm
			self._fofdm = Fofdm(self._core, self._cmd_group)
		return self._fofdm

	@property
	def gfdm(self):
		"""gfdm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gfdm'):
			from .Gfdm import Gfdm
			self._gfdm = Gfdm(self._core, self._cmd_group)
		return self._gfdm

	@property
	def modPreset(self):
		"""modPreset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modPreset'):
			from .ModPreset import ModPreset
			self._modPreset = ModPreset(self._core, self._cmd_group)
		return self._modPreset

	@property
	def notch(self):
		"""notch commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import Notch
			self._notch = Notch(self._core, self._cmd_group)
		return self._notch

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
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
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def ufmc(self):
		"""ufmc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ufmc'):
			from .Ufmc import Ufmc
			self._ufmc = Ufmc(self._core, self._cmd_group)
		return self._ufmc

	@property
	def user(self):
		"""user commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	def get_acp_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ACPLength \n
		Snippet: value: int = driver.source.bb.ofdm.get_acp_length() \n
		For f-OFDM/OFDM, enables additional alternative CP. \n
			:return: cp_length: integer Range: 0 to 8192
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:ACPLength?')
		return Conversions.str_to_int(response)

	def set_acp_length(self, cp_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ACPLength \n
		Snippet: driver.source.bb.ofdm.set_acp_length(cp_length = 1) \n
		For f-OFDM/OFDM, enables additional alternative CP. \n
			:param cp_length: integer Range: 0 to 8192
		"""
		param = Conversions.decimal_value_to_str(cp_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ACPLength {param}')

	def get_acp_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ACPSymbols \n
		Snippet: value: int = driver.source.bb.ofdm.get_acp_symbols() \n
		For f-OFDM/OFDM, defines number of symbols on that the cyclic prefix/the alternative cyclic prefix is applied. \n
			:return: cp_symbols: integer Range: 0 to 8192
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:ACPSymbols?')
		return Conversions.str_to_int(response)

	def set_acp_symbols(self, cp_symbols: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ACPSymbols \n
		Snippet: driver.source.bb.ofdm.set_acp_symbols(cp_symbols = 1) \n
		For f-OFDM/OFDM, defines number of symbols on that the cyclic prefix/the alternative cyclic prefix is applied. \n
			:param cp_symbols: integer Range: 0 to 8192
		"""
		param = Conversions.decimal_value_to_str(cp_symbols)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ACPSymbols {param}')

	def get_bw_occupied(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:BWOCcupied \n
		Snippet: value: float = driver.source.bb.ofdm.get_bw_occupied() \n
		Queries the occupied bandwidth. \n
			:return: occ_bw: float Range: 0.001 to 1000, Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:BWOCcupied?')
		return Conversions.str_to_float(response)

	def get_cp_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CPSYmbols \n
		Snippet: value: int = driver.source.bb.ofdm.get_cp_symbols() \n
		For f-OFDM/OFDM, defines number of symbols on that the cyclic prefix/the alternative cyclic prefix is applied. \n
			:return: cp_symbols: integer Range: 0 to 8192
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CPSYmbols?')
		return Conversions.str_to_int(response)

	def set_cp_symbols(self, cp_symbols: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CPSYmbols \n
		Snippet: driver.source.bb.ofdm.set_cp_symbols(cp_symbols = 1) \n
		For f-OFDM/OFDM, defines number of symbols on that the cyclic prefix/the alternative cyclic prefix is applied. \n
			:param cp_symbols: integer Range: 0 to 8192
		"""
		param = Conversions.decimal_value_to_str(cp_symbols)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CPSYmbols {param}')

	def get_lguard(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:LGUard \n
		Snippet: value: int = driver.source.bb.ofdm.get_lguard() \n
		Queries the number of left guard subcarriers. \n
			:return: left_guard_sc: integer Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:LGUard?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.C5Gmod:
		"""SCPI: [SOURce<HW>]:BB:OFDM:MODulation \n
		Snippet: value: enums.C5Gmod = driver.source.bb.ofdm.get_modulation() \n
		Selects the modulation type. \n
			:return: mod_type: UFMC| FBMC| GFDM| FOFDm| OFDM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.C5Gmod)

	def set_modulation(self, mod_type: enums.C5Gmod) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:MODulation \n
		Snippet: driver.source.bb.ofdm.set_modulation(mod_type = enums.C5Gmod.FBMC) \n
		Selects the modulation type. \n
			:param mod_type: UFMC| FBMC| GFDM| FOFDm| OFDM
		"""
		param = Conversions.enum_scalar_to_str(mod_type, enums.C5Gmod)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:MODulation {param}')

	def get_nalloc(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NALLoc \n
		Snippet: value: int = driver.source.bb.ofdm.get_nalloc() \n
		Sets the number of scheduled allocations. \n
			:return: no_of_alloc: integer Range: 0 to 500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:NALLoc?')
		return Conversions.str_to_int(response)

	def set_nalloc(self, no_of_alloc: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NALLoc \n
		Snippet: driver.source.bb.ofdm.set_nalloc(no_of_alloc = 1) \n
		Sets the number of scheduled allocations. \n
			:param no_of_alloc: integer Range: 0 to 500
		"""
		param = Conversions.decimal_value_to_str(no_of_alloc)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:NALLoc {param}')

	def get_noccupied(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NOCCupied \n
		Snippet: value: int = driver.source.bb.ofdm.get_noccupied() \n
		Sets the number of occupied subcarriers. \n
			:return: num_occ_sc: integer Range: 1 to 13107
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:NOCCupied?')
		return Conversions.str_to_int(response)

	def set_noccupied(self, num_occ_sc: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NOCCupied \n
		Snippet: driver.source.bb.ofdm.set_noccupied(num_occ_sc = 1) \n
		Sets the number of occupied subcarriers. \n
			:param num_occ_sc: integer Range: 1 to 13107
		"""
		param = Conversions.decimal_value_to_str(num_occ_sc)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:NOCCupied {param}')

	def get_nsubcarriers(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NSUBcarriers \n
		Snippet: value: int = driver.source.bb.ofdm.get_nsubcarriers() \n
		Sets the number of available subcarriers. \n
			:return: no_of_sub_carr: integer Range: 64 to 16384
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:NSUBcarriers?')
		return Conversions.str_to_int(response)

	def set_nsubcarriers(self, no_of_sub_carr: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NSUBcarriers \n
		Snippet: driver.source.bb.ofdm.set_nsubcarriers(no_of_sub_carr = 1) \n
		Sets the number of available subcarriers. \n
			:param no_of_sub_carr: integer Range: 64 to 16384
		"""
		param = Conversions.decimal_value_to_str(no_of_sub_carr)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:NSUBcarriers {param}')

	def get_out_path(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:OFDM:OUTPath \n
		Snippet: value: str = driver.source.bb.ofdm.get_out_path() \n
		Specifies the output path and output file of the exported OFDM signal generation settings. By default, the output path
		/var/user/K114-Export and output file Exported_K114_settings_K96.xml is specified. See also Example 'Default
		'Exported_K114_settings_K96.xml' file'. \n
			:return: k_114_output_path: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:OUTPath?')
		return trim_str_response(response)

	def set_out_path(self, k_114_output_path: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:OUTPath \n
		Snippet: driver.source.bb.ofdm.set_out_path(k_114_output_path = '1') \n
		Specifies the output path and output file of the exported OFDM signal generation settings. By default, the output path
		/var/user/K114-Export and output file Exported_K114_settings_K96.xml is specified. See also Example 'Default
		'Exported_K114_settings_K96.xml' file'. \n
			:param k_114_output_path: string
		"""
		param = Conversions.value_to_quoted_str(k_114_output_path)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:OUTPath {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:PRESet \n
		Snippet: driver.source.bb.ofdm.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:OFDM:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:PRESet \n
		Snippet: driver.source.bb.ofdm.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:OFDM:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:OFDM:PRESet', opc_timeout_ms)

	def get_rguard(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:RGUard \n
		Snippet: value: int = driver.source.bb.ofdm.get_rguard() \n
		Queries the number of right guard subcarriers. \n
			:return: right_guard_sc: integer Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:RGUard?')
		return Conversions.str_to_int(response)

	def get_sampling(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:SAMPling \n
		Snippet: value: float = driver.source.bb.ofdm.get_sampling() \n
		Queries the sampling rate. \n
			:return: samp_rate: float Range: 0.001 to 1000, Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:SAMPling?')
		return Conversions.str_to_float(response)

	def get_sc_space(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:SCSPace \n
		Snippet: value: float = driver.source.bb.ofdm.get_sc_space() \n
		Sets the frequency distance between the carrier frequencies of the subcarriers. \n
			:return: sub_car_sp: float Range: 0.001 to 2, Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:SCSPace?')
		return Conversions.str_to_float(response)

	def set_sc_space(self, sub_car_sp: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:SCSPace \n
		Snippet: driver.source.bb.ofdm.set_sc_space(sub_car_sp = 1.0) \n
		Sets the frequency distance between the carrier frequencies of the subcarriers. \n
			:param sub_car_sp: float Range: 0.001 to 2, Unit: MHz
		"""
		param = Conversions.decimal_value_to_str(sub_car_sp)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:SCSPace {param}')

	def get_seq_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:SEQLength \n
		Snippet: value: int = driver.source.bb.ofdm.get_seq_length() \n
		Sets the sequence length of the signal in number of symbols. \n
			:return: seq_len: integer Range: 1 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:SEQLength?')
		return Conversions.str_to_int(response)

	def set_seq_length(self, seq_len: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:SEQLength \n
		Snippet: driver.source.bb.ofdm.set_seq_length(seq_len = 1) \n
		Sets the sequence length of the signal in number of symbols. \n
			:param seq_len: integer Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(seq_len)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:SEQLength {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:OFDM:STATe \n
		Snippet: value: bool = driver.source.bb.ofdm.get_state() \n
		Activates the standard. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:STATe \n
		Snippet: driver.source.bb.ofdm.set_state(state = False) \n
		Activates the standard. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:STATe {param}')

	def get_subcarriers(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:SUBCarriers \n
		Snippet: value: int = driver.source.bb.ofdm.get_subcarriers() \n
		Queries the number of subcarriers per subband. \n
			:return: subc_per_subband: integer Range: 1 to 16384
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:SUBCarriers?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Ofdm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ofdm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
