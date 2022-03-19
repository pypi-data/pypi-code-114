from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfr:
	"""Cfr commands group definition. 14 total commands, 2 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfr", core, parent)

	@property
	def measure(self):
		"""measure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measure'):
			from .Measure import Measure
			self._measure = Measure(self._core, self._cmd_group)
		return self._measure

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_algorithm(self) -> enums.CfrAlgo:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:ALGorithm \n
		Snippet: value: enums.CfrAlgo = driver.source.bb.arbitrary.cfr.get_algorithm() \n
		Displays the algorithm used for the crest factor reduction. The 'Clipping and filtering' algorithm performs a hard
		clipping. It is followed by a low pass filtering of the result in an iterative manner until the target crest factor is
		reached. You can define the settings of the filter that is used for the calculation. \n
			:return: arb_cfr_algorithm: CLFiltering
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:ALGorithm?')
		return Conversions.str_to_scalar_enum(response, enums.CfrAlgo)

	def set_algorithm(self, arb_cfr_algorithm: enums.CfrAlgo) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:ALGorithm \n
		Snippet: driver.source.bb.arbitrary.cfr.set_algorithm(arb_cfr_algorithm = enums.CfrAlgo.CLFiltering) \n
		Displays the algorithm used for the crest factor reduction. The 'Clipping and filtering' algorithm performs a hard
		clipping. It is followed by a low pass filtering of the result in an iterative manner until the target crest factor is
		reached. You can define the settings of the filter that is used for the calculation. \n
			:param arb_cfr_algorithm: CLFiltering
		"""
		param = Conversions.enum_scalar_to_str(arb_cfr_algorithm, enums.CfrAlgo)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:ALGorithm {param}')

	def get_cspacing(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:CSPacing \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_cspacing() \n
		Sets the channel spacing, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to SIMPle. \n
			:return: arb_cfr_chan_spac: float Range: 0 to depends on the sample rate of the loaded file
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:CSPacing?')
		return Conversions.str_to_float(response)

	def set_cspacing(self, arb_cfr_chan_spac: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:CSPacing \n
		Snippet: driver.source.bb.arbitrary.cfr.set_cspacing(arb_cfr_chan_spac = 1.0) \n
		Sets the channel spacing, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to SIMPle. \n
			:param arb_cfr_chan_spac: float Range: 0 to depends on the sample rate of the loaded file
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_chan_spac)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:CSPacing {param}')

	def get_dcfdelta(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:DCFDelta \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_dcfdelta() \n
		Sets the value difference by which you want to change your crest factor. \n
			:return: arb_cfr_dcf_delta: float Range: -20 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:DCFDelta?')
		return Conversions.str_to_float(response)

	def set_dcfdelta(self, arb_cfr_dcf_delta: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:DCFDelta \n
		Snippet: driver.source.bb.arbitrary.cfr.set_dcfdelta(arb_cfr_dcf_delta = 1.0) \n
		Sets the value difference by which you want to change your crest factor. \n
			:param arb_cfr_dcf_delta: float Range: -20 to 0
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_dcf_delta)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:DCFDelta {param}')

	# noinspection PyTypeChecker
	def get_filter_py(self) -> enums.CfrFiltMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:FILTer \n
		Snippet: value: enums.CfrFiltMode = driver.source.bb.arbitrary.cfr.get_filter_py() \n
		Selects which filter mode is used for the filtering. \n
			:return: arb_cfr_filter_mod: SIMPle| ENHanced
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.CfrFiltMode)

	def set_filter_py(self, arb_cfr_filter_mod: enums.CfrFiltMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:FILTer \n
		Snippet: driver.source.bb.arbitrary.cfr.set_filter_py(arb_cfr_filter_mod = enums.CfrFiltMode.ENHanced) \n
		Selects which filter mode is used for the filtering. \n
			:param arb_cfr_filter_mod: SIMPle| ENHanced
		"""
		param = Conversions.enum_scalar_to_str(arb_cfr_filter_mod, enums.CfrFiltMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:FILTer {param}')

	def get_forder(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:FORDer \n
		Snippet: value: int = driver.source.bb.arbitrary.cfr.get_forder() \n
		Sets the maximum filter order, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to ENHanced. \n
			:return: arb_cfr_max_file_order: integer Range: 0 to 300
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:FORDer?')
		return Conversions.str_to_int(response)

	def set_forder(self, arb_cfr_max_file_order: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:FORDer \n
		Snippet: driver.source.bb.arbitrary.cfr.set_forder(arb_cfr_max_file_order = 1) \n
		Sets the maximum filter order, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to ENHanced. \n
			:param arb_cfr_max_file_order: integer Range: 0 to 300
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_max_file_order)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:FORDer {param}')

	def get_iterations(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:ITERations \n
		Snippet: value: int = driver.source.bb.arbitrary.cfr.get_iterations() \n
		Sets the number of iterations that are used for calculating the resulting crest factor. The iteration process is stopped
		when the desired crest factor delta is achieved by 0.1 dB. \n
			:return: arb_cfr_max_iter: integer Range: 1 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:ITERations?')
		return Conversions.str_to_int(response)

	def set_iterations(self, arb_cfr_max_iter: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:ITERations \n
		Snippet: driver.source.bb.arbitrary.cfr.set_iterations(arb_cfr_max_iter = 1) \n
		Sets the number of iterations that are used for calculating the resulting crest factor. The iteration process is stopped
		when the desired crest factor delta is achieved by 0.1 dB. \n
			:param arb_cfr_max_iter: integer Range: 1 to 10
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_max_iter)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:ITERations {param}')

	def get_oc_factor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:OCFactor \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_oc_factor() \n
		Queries the original crest factor of the waveform after the calculation of the resulting crest factor is completed. The
		original crest factor is calculated as an average over the whole waveform, including any idle periods that might be
		present in TDD waveforms. \n
			:return: arb_cfro_crest_factor: float Range: 1 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:OCFactor?')
		return Conversions.str_to_float(response)

	def get_pfreq(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:PFReq \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_pfreq() \n
		Sets the passband frequency, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to ENHanced. Frequency components lower than
		the passband frequency are passed through unfiltered. \n
			:return: arb_cfr_pass_band_freq: float Range: 0 to depends on the sample rate of the loaded file
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:PFReq?')
		return Conversions.str_to_float(response)

	def set_pfreq(self, arb_cfr_pass_band_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:PFReq \n
		Snippet: driver.source.bb.arbitrary.cfr.set_pfreq(arb_cfr_pass_band_freq = 1.0) \n
		Sets the passband frequency, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to ENHanced. Frequency components lower than
		the passband frequency are passed through unfiltered. \n
			:param arb_cfr_pass_band_freq: float Range: 0 to depends on the sample rate of the loaded file
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_pass_band_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:PFReq {param}')

	def get_rc_factor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:RCFactor \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_rc_factor() \n
		Queries the resulting crest factor of the waveform after the calculations are completed. The resulting crest factor is
		calculated as an average over the whole waveform, including any idle periods that might be present in TDD waveforms. \n
			:return: arb_cfr_res_crest_factor: float Range: 1 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:RCFactor?')
		return Conversions.str_to_float(response)

	def get_sbandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:SBANdwidth \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_sbandwidth() \n
		Sets the signal bandwidth, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to SIMPle. The value of the signal bandwidth
		should not be higher than the channel spacing ([:SOURce<hw>]:BB:ARBitrary:CFR:CSPacing) . \n
			:return: arb_cfr_signal_bw: float Range: 0 to depends on the sample rate of the loaded file
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:SBANdwidth?')
		return Conversions.str_to_float(response)

	def set_sbandwidth(self, arb_cfr_signal_bw: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:SBANdwidth \n
		Snippet: driver.source.bb.arbitrary.cfr.set_sbandwidth(arb_cfr_signal_bw = 1.0) \n
		Sets the signal bandwidth, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to SIMPle. The value of the signal bandwidth
		should not be higher than the channel spacing ([:SOURce<hw>]:BB:ARBitrary:CFR:CSPacing) . \n
			:param arb_cfr_signal_bw: float Range: 0 to depends on the sample rate of the loaded file
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_signal_bw)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:SBANdwidth {param}')

	def get_sfreq(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:SFReq \n
		Snippet: value: float = driver.source.bb.arbitrary.cfr.get_sfreq() \n
		Sets the stopband frequency of the filter, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to ENHanced.
		Frequency components higher than the stopband frequency are filtered out by the lowpass filter. \n
			:return: arb_cfr_stop_band_freq: float Range: 0 to depends on the sample rate of the loaded file
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:SFReq?')
		return Conversions.str_to_float(response)

	def set_sfreq(self, arb_cfr_stop_band_freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:SFReq \n
		Snippet: driver.source.bb.arbitrary.cfr.set_sfreq(arb_cfr_stop_band_freq = 1.0) \n
		Sets the stopband frequency of the filter, if [:SOURce<hw>]:BB:ARBitrary:CFR:FILTer is set to ENHanced.
		Frequency components higher than the stopband frequency are filtered out by the lowpass filter. \n
			:param arb_cfr_stop_band_freq: float Range: 0 to depends on the sample rate of the loaded file
		"""
		param = Conversions.decimal_value_to_str(arb_cfr_stop_band_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:SFReq {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:[STATe] \n
		Snippet: value: bool = driver.source.bb.arbitrary.cfr.get_state() \n
		Enables the crest factor reduction calculation. \n
			:return: arb_cfr_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arb_cfr_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:[STATe] \n
		Snippet: driver.source.bb.arbitrary.cfr.set_state(arb_cfr_state = False) \n
		Enables the crest factor reduction calculation. \n
			:param arb_cfr_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(arb_cfr_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CFR:STATe {param}')

	def clone(self) -> 'Cfr':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cfr(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
