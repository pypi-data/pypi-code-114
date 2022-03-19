from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsPy:
	"""IsPy commands group definition. 17 total commands, 0 Subgroups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isPy", core, parent)

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:BAND \n
		Snippet: value: enums.Band = driver.source.bb.nr5G.tcw.isPy.get_band() \n
		Set the frequency band (n1 to n86) for the interfering signal. \n
			:return: band: N1| N2| N3| N5| N7| N8| N12| N20| N25| N28| N34| N38| N39| N40| N41| N50| N51| N66| N70| N71| N74| N75| N76| N77| N78| N79| N80| N81| N82| N83| N84| N86
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:BAND \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_band(band = enums.Band.N1) \n
		Set the frequency band (n1 to n86) for the interfering signal. \n
			:param band: N1| N2| N3| N5| N7| N8| N12| N20| N25| N28| N34| N38| N39| N40| N41| N50| N51| N66| N70| N71| N74| N75| N76| N77| N78| N79| N80| N81| N82| N83| N84| N86
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:BAND {param}')

	# noinspection PyTypeChecker
	def get_chbw(self) -> enums.Nr5Gcbw:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:CHBW \n
		Snippet: value: enums.Nr5Gcbw = driver.source.bb.nr5G.tcw.isPy.get_chbw() \n
		Queries the channel bandwidth of the interfering signal. \n
			:return: isch_bw: BW5| BW10| BW15| BW20| BW25| BW30| BW40| BW50| BW60| BW70| BW80| BW90| BW100| BW200| BW400
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:CHBW?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5Gcbw)

	def get_clid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:CLID \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_clid() \n
		Sets the cell ID of the interfering signal. \n
			:return: is_cell_id: integer Range: 0 to 1007
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:CLID?')
		return Conversions.str_to_int(response)

	def set_clid(self, is_cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:CLID \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_clid(is_cell_id = 1) \n
		Sets the cell ID of the interfering signal. \n
			:param is_cell_id: integer Range: 0 to 1007
		"""
		param = Conversions.decimal_value_to_str(is_cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:CLID {param}')

	def get_distance(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:DISTance \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_distance() \n
		Sets the distance between the test object and test antenna injecting the interferer signal. \n
			:return: distance: integer Range: 1 to 300
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:DISTance?')
		return Conversions.str_to_int(response)

	def set_distance(self, distance: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:DISTance \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_distance(distance = 1) \n
		Sets the distance between the test object and test antenna injecting the interferer signal. \n
			:param distance: integer Range: 1 to 300
		"""
		param = Conversions.decimal_value_to_str(distance)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:DISTance {param}')

	# noinspection PyTypeChecker
	def get_duplex(self) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:DUPLex \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.nr5G.tcw.isPy.get_duplex() \n
		The duplexing mechanism used for the interfering signal can be switched between FDD and TDD. \n
			:return: is_duplexing: FDD| TDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:DUPLex?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)

	def set_duplex(self, is_duplexing: enums.EutraDuplexMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:DUPLex \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_duplex(is_duplexing = enums.EutraDuplexMode.FDD) \n
		The duplexing mechanism used for the interfering signal can be switched between FDD and TDD. \n
			:param is_duplexing: FDD| TDD
		"""
		param = Conversions.enum_scalar_to_str(is_duplexing, enums.EutraDuplexMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:DUPLex {param}')

	# noinspection PyTypeChecker
	def get_fr_shift(self) -> enums.FreqShift:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:FRSHift \n
		Snippet: value: enums.FreqShift = driver.source.bb.nr5G.tcw.isPy.get_fr_shift() \n
		Sets the parameter 'Frequency Shift m' for the interfering signal. With this setting, the allocated RB can be offset to a
		different center frequency. \n
			:return: is_freq_shift: FS0| FS1| FS2| FS3| FS4| FS9| FS14| FS19| FS24| FS29| FS54| FS79| FS99
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:FRSHift?')
		return Conversions.str_to_scalar_enum(response, enums.FreqShift)

	def set_fr_shift(self, is_freq_shift: enums.FreqShift) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:FRSHift \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_fr_shift(is_freq_shift = enums.FreqShift.FS0) \n
		Sets the parameter 'Frequency Shift m' for the interfering signal. With this setting, the allocated RB can be offset to a
		different center frequency. \n
			:param is_freq_shift: FS0| FS1| FS2| FS3| FS4| FS9| FS14| FS19| FS24| FS29| FS54| FS79| FS99
		"""
		param = Conversions.enum_scalar_to_str(is_freq_shift, enums.FreqShift)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:FRSHift {param}')

	# noinspection PyTypeChecker
	def get_if_type(self) -> enums.InterfererTypeNr:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:IFTYpe \n
		Snippet: value: enums.InterfererTypeNr = driver.source.bb.nr5G.tcw.isPy.get_if_type() \n
		Selects the type of the interfering signal. The second interfering signal is always a CW signal. \n
			:return: interferer_type_1: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:IFTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.InterfererTypeNr)

	def set_if_type(self, interferer_type_1: enums.InterfererTypeNr) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:IFTYpe \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_if_type(interferer_type_1 = enums.InterfererTypeNr.CW) \n
		Selects the type of the interfering signal. The second interfering signal is always a CW signal. \n
			:param interferer_type_1: CW
		"""
		param = Conversions.enum_scalar_to_str(interferer_type_1, enums.InterfererTypeNr)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:IFTYpe {param}')

	def get_nrblock(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:NRBLock \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_nrblock() \n
		Queries the No. of resource blocks of the interfering signal. \n
			:return: is_num_rb: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:NRBLock?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_ofn(self) -> enums.OffsetFactorN:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:OFN \n
		Snippet: value: enums.OffsetFactorN = driver.source.bb.nr5G.tcw.isPy.get_ofn() \n
		Set the offset factor for the interfering signal. \n
			:return: offset_factor_n: OFN_1| OFN_2| OFN_3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:OFN?')
		return Conversions.str_to_scalar_enum(response, enums.OffsetFactorN)

	def set_ofn(self, offset_factor_n: enums.OffsetFactorN) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:OFN \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_ofn(offset_factor_n = enums.OffsetFactorN.OFN_1) \n
		Set the offset factor for the interfering signal. \n
			:param offset_factor_n: OFN_1| OFN_2| OFN_3
		"""
		param = Conversions.enum_scalar_to_str(offset_factor_n, enums.OffsetFactorN)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:OFN {param}')

	def get_plevel(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:PLEVel \n
		Snippet: value: float = driver.source.bb.nr5G.tcw.isPy.get_plevel() \n
		Queries the power level of the interfering signal. \n
			:return: is_pow_level: float Range: -145 to 20, Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:PLEVel?')
		return Conversions.str_to_float(response)

	def get_rbc_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:RBCFrequency \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_rbc_frequency() \n
		Queries the center frequency of the interfering signal. \n
			:return: is_rb_center_freq: integer Range: 100e+03 to 6e+09, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:RBCFrequency?')
		return Conversions.str_to_int(response)

	def get_rb_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:RBOFfset \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_rb_offset() \n
		Sets the RB offset of the interfering signal. \n
			:return: is_rb_offset: integer Range: 0 to 273
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:RBOFfset?')
		return Conversions.str_to_int(response)

	def set_rb_offset(self, is_rb_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:RBOFfset \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_rb_offset(is_rb_offset = 1) \n
		Sets the RB offset of the interfering signal. \n
			:param is_rb_offset: integer Range: 0 to 273
		"""
		param = Conversions.decimal_value_to_str(is_rb_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:RBOFfset {param}')

	def get_rf_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:RFFRequency \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_rf_frequency() \n
		Queries the center frequency of the interfering signal 1 and 2. \n
			:return: is_rf_freq: integer Range: 100e+03 to 6e+09, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:RFFRequency?')
		return Conversions.str_to_int(response)

	def set_rf_frequency(self, is_rf_freq: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:RFFRequency \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_rf_frequency(is_rf_freq = 1) \n
		Queries the center frequency of the interfering signal 1 and 2. \n
			:param is_rf_freq: integer Range: 100e+03 to 6e+09, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(is_rf_freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:RFFRequency {param}')

	# noinspection PyTypeChecker
	def get_sc_spacing(self) -> enums.Numerology:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:SCSPacing \n
		Snippet: value: enums.Numerology = driver.source.bb.nr5G.tcw.isPy.get_sc_spacing() \n
		Queries the sub-carrier spacing for the interfering signal. \n
			:return: is_scs: N15| N30| N60| X60| N120| N240| N480| N960 N15, N30, N60, N120, N240, N480, N960 Normal cyclic prefix, value in kHz E60 Extended cyclic prefix, 60 kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.Numerology)

	# noinspection PyTypeChecker
	def get_tmodel(self) -> enums.TestModel:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:TMODel \n
		Snippet: value: enums.TestModel = driver.source.bb.nr5G.tcw.isPy.get_tmodel() \n
		Shows the test model set for the test case. The NR-TMs for FR1 are defined in TS 38.141-1 section 4.9.2. \n
			:return: test_model: TM1_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:TMODel?')
		return Conversions.str_to_scalar_enum(response, enums.TestModel)

	# noinspection PyTypeChecker
	def get_trequire(self) -> enums.TestRequire:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:TREQuire \n
		Snippet: value: enums.TestRequire = driver.source.bb.nr5G.tcw.isPy.get_trequire() \n
		Selects whether the standard out-of-band blocking requirements test is performed (BLPE) or the optional blocking scenario,
		when the BS is co-located with another BS in a different operating band (COBS) . \n
			:return: is_test_require: BLPE| COBS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:TREQuire?')
		return Conversions.str_to_scalar_enum(response, enums.TestRequire)

	def set_trequire(self, is_test_require: enums.TestRequire) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:TREQuire \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_trequire(is_test_require = enums.TestRequire.BLPE) \n
		Selects whether the standard out-of-band blocking requirements test is performed (BLPE) or the optional blocking scenario,
		when the BS is co-located with another BS in a different operating band (COBS) . \n
			:param is_test_require: BLPE| COBS
		"""
		param = Conversions.enum_scalar_to_str(is_test_require, enums.TestRequire)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:TREQuire {param}')

	def get_ue_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:UEID \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.isPy.get_ue_id() \n
		Sets the UE ID/n_RNTI for the interfering signal. \n
			:return: isu_eid: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS:UEID?')
		return Conversions.str_to_int(response)

	def set_ue_id(self, isu_eid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS:UEID \n
		Snippet: driver.source.bb.nr5G.tcw.isPy.set_ue_id(isu_eid = 1) \n
		Sets the UE ID/n_RNTI for the interfering signal. \n
			:param isu_eid: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(isu_eid)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:IS:UEID {param}')
