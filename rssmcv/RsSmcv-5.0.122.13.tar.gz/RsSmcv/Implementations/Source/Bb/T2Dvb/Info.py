from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 12 total commands, 0 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	def get_dp(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:DP \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_dp() \n
		Queries the maximum possible number of PLP data cells in the T2 frame. \n
			:return: dplp: integer Range: 0 to 1E7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:DP?')
		return Conversions.str_to_int(response)

	def get_dp_used(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:DPUSed \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_dp_used() \n
		Queries the current number of PLP data cells in the T2 frame. \n
			:return: dplp_used: integer Range: 0 to 1E7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:DPUSed?')
		return Conversions.str_to_int(response)

	def get_posbits(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:POSBits \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_posbits() \n
		Queries the L1-post signaling length in bits. \n
			:return: l_1_post_sig_bits: integer Range: 0 to 262175
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:POSBits?')
		return Conversions.str_to_int(response)

	def get_poscells(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:POSCells \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_poscells() \n
		Queries the L1-post signaling length in cells. \n
			:return: l_1_post_sig_cells: integer Range: 0 to 262143
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:POSCells?')
		return Conversions.str_to_int(response)

	def get_prebits(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:PREBits \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_prebits() \n
		Queries the L1-pre signaling length in bits. \n
			:return: l_1_pre_sig_bits: integer Range: 0 to 200
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:PREBits?')
		return Conversions.str_to_int(response)

	def get_precells(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:PRECells \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_precells() \n
		Queries the L1-pre signaling length in cells. \n
			:return: l_1_pre_sig_cells: integer Range: 0 to 1840
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:PRECells?')
		return Conversions.str_to_int(response)

	def get_tf(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:TF \n
		Snippet: value: float = driver.source.bb.t2Dvb.info.get_tf() \n
		Queries the T2 frame duration. \n
			:return: t_2_frame_duration: float Range: 0 to 0.999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:TF?')
		return Conversions.str_to_float(response)

	def get_tfef(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:TFEF \n
		Snippet: value: int = driver.source.bb.t2Dvb.info.get_tfef() \n
		Queries the future extension frame duration. \n
			:return: fef_dur: integer Range: 0 to 9.999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:TFEF?')
		return Conversions.str_to_int(response)

	def get_tp_1(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:TP1 \n
		Snippet: value: float = driver.source.bb.t2Dvb.info.get_tp_1() \n
		Queries the P1 symbol duration. \n
			:return: p_1_symbol_dur: float Range: 0 to 0.001000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:TP1?')
		return Conversions.str_to_float(response)

	def get_tp_2(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:TP2 \n
		Snippet: value: float = driver.source.bb.t2Dvb.info.get_tp_2() \n
		Queries the P2 and data symbol duration. \n
			:return: ofdm_symbol_dur: float Range: 0 to 0.010000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:TP2?')
		return Conversions.str_to_float(response)

	def get_ts(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:TS \n
		Snippet: value: float = driver.source.bb.t2Dvb.info.get_ts() \n
		Queries the P2 and data symbol duration. \n
			:return: ofdm_symbol_dur: float Range: 0 to 0.010000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:TS?')
		return Conversions.str_to_float(response)

	def get_tsf(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INFO:TSF \n
		Snippet: value: float = driver.source.bb.t2Dvb.info.get_tsf() \n
		Queries the super frame duration. \n
			:return: super_frame_duration: float Range: 0 to 999.999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INFO:TSF?')
		return Conversions.str_to_float(response)
