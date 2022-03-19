from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssp:
	"""Ssp commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssp", core, parent)

	# noinspection PyTypeChecker
	def get_mpd_1(self) -> enums.EutraEmtcMpdcchNumRepetitions:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:MPD1 \n
		Snippet: value: enums.EutraEmtcMpdcchNumRepetitions = driver.source.bb.eutra.downlink.emtc.ssp.get_mpd_1() \n
		Sets the maximum number of MPDCCH repetitons for type 1 and type 2 common seach spaces. \n
			:return: max_rep_mpdcch_1: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:MPD1?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcMpdcchNumRepetitions)

	def set_mpd_1(self, max_rep_mpdcch_1: enums.EutraEmtcMpdcchNumRepetitions) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:MPD1 \n
		Snippet: driver.source.bb.eutra.downlink.emtc.ssp.set_mpd_1(max_rep_mpdcch_1 = enums.EutraEmtcMpdcchNumRepetitions._1) \n
		Sets the maximum number of MPDCCH repetitons for type 1 and type 2 common seach spaces. \n
			:param max_rep_mpdcch_1: 1| 2| 4| 8| 16| 32| 64| 128| 256
		"""
		param = Conversions.enum_scalar_to_str(max_rep_mpdcch_1, enums.EutraEmtcMpdcchNumRepetitions)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:MPD1 {param}')

	# noinspection PyTypeChecker
	def get_mpd_2(self) -> enums.EutraEmtcMpdcchNumRepetitions:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:MPD2 \n
		Snippet: value: enums.EutraEmtcMpdcchNumRepetitions = driver.source.bb.eutra.downlink.emtc.ssp.get_mpd_2() \n
		Sets the maximum number of MPDCCH repetitons for type 1 and type 2 common seach spaces. \n
			:return: max_rep_mpdcch_2: 1| 2| 4| 8| 16| 32| 64| 128| 256
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:MPD2?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcMpdcchNumRepetitions)

	def set_mpd_2(self, max_rep_mpdcch_2: enums.EutraEmtcMpdcchNumRepetitions) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:MPD2 \n
		Snippet: driver.source.bb.eutra.downlink.emtc.ssp.set_mpd_2(max_rep_mpdcch_2 = enums.EutraEmtcMpdcchNumRepetitions._1) \n
		Sets the maximum number of MPDCCH repetitons for type 1 and type 2 common seach spaces. \n
			:param max_rep_mpdcch_2: 1| 2| 4| 8| 16| 32| 64| 128| 256
		"""
		param = Conversions.enum_scalar_to_str(max_rep_mpdcch_2, enums.EutraEmtcMpdcchNumRepetitions)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:MPD2 {param}')

	# noinspection PyTypeChecker
	def get_pdsa(self) -> enums.EutraEmtcPdschNumRepetitions:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:PDSA \n
		Snippet: value: enums.EutraEmtcPdschNumRepetitions = driver.source.bb.eutra.downlink.emtc.ssp.get_pdsa() \n
		Sets the parameter pdsch-maxNumRepetitionCEmodeA that defines the PDSCH subframe assigment. \n
			:return: max_rep_pdscha: 16| 32| 64| NON| 192| 256| 384| 512| 786| 1024| 1536| 2048
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:PDSA?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcPdschNumRepetitions)

	def set_pdsa(self, max_rep_pdscha: enums.EutraEmtcPdschNumRepetitions) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:PDSA \n
		Snippet: driver.source.bb.eutra.downlink.emtc.ssp.set_pdsa(max_rep_pdscha = enums.EutraEmtcPdschNumRepetitions._1024) \n
		Sets the parameter pdsch-maxNumRepetitionCEmodeA that defines the PDSCH subframe assigment. \n
			:param max_rep_pdscha: 16| 32| 64| NON| 192| 256| 384| 512| 786| 1024| 1536| 2048
		"""
		param = Conversions.enum_scalar_to_str(max_rep_pdscha, enums.EutraEmtcPdschNumRepetitions)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:PDSA {param}')

	# noinspection PyTypeChecker
	def get_pdsb(self) -> enums.EutraEmtcPdschNumRepetitions:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:PDSB \n
		Snippet: value: enums.EutraEmtcPdschNumRepetitions = driver.source.bb.eutra.downlink.emtc.ssp.get_pdsb() \n
		Sets the parameter pdsch-maxNumRepetitionCEmodeB that defines the PDSCH subframe assigment. \n
			:return: max_rep_pdschb: 16| 32| 64| NON| 192| 256| 384| 512| 786| 1024| 1536| 2048
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:PDSB?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcPdschNumRepetitions)

	def set_pdsb(self, max_rep_pdschb: enums.EutraEmtcPdschNumRepetitions) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:PDSB \n
		Snippet: driver.source.bb.eutra.downlink.emtc.ssp.set_pdsb(max_rep_pdschb = enums.EutraEmtcPdschNumRepetitions._1024) \n
		Sets the parameter pdsch-maxNumRepetitionCEmodeB that defines the PDSCH subframe assigment. \n
			:param max_rep_pdschb: 16| 32| 64| NON| 192| 256| 384| 512| 786| 1024| 1536| 2048
		"""
		param = Conversions.enum_scalar_to_str(max_rep_pdschb, enums.EutraEmtcPdschNumRepetitions)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:PDSB {param}')

	# noinspection PyTypeChecker
	def get_stsf(self) -> enums.EutraEmtcMpdcchStartSf:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:STSF \n
		Snippet: value: enums.EutraEmtcMpdcchStartSf = driver.source.bb.eutra.downlink.emtc.ssp.get_stsf() \n
		Sets the start SF for the random access common search space. \n
			:return: sp_start_sf: S1| S1_5| S2| S2_5| S5| S8| S10| S20| S4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:STSF?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcMpdcchStartSf)

	def set_stsf(self, sp_start_sf: enums.EutraEmtcMpdcchStartSf) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:SSP:STSF \n
		Snippet: driver.source.bb.eutra.downlink.emtc.ssp.set_stsf(sp_start_sf = enums.EutraEmtcMpdcchStartSf.S1) \n
		Sets the start SF for the random access common search space. \n
			:param sp_start_sf: S1| S1_5| S2| S2_5| S5| S8| S10| S20| S4
		"""
		param = Conversions.enum_scalar_to_str(sp_start_sf, enums.EutraEmtcMpdcchStartSf)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:SSP:STSF {param}')
