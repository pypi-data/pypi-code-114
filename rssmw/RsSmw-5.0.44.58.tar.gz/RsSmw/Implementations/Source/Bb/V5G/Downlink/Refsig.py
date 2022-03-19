from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Refsig:
	"""Refsig commands group definition. 8 total commands, 0 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refsig", core, parent)

	def get_epre(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:EPRE \n
		Snippet: value: float = driver.source.bb.v5G.downlink.refsig.get_epre() \n
		No command help available \n
			:return: rel_to_level_displ: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:EPRE?')
		return Conversions.str_to_float(response)

	def get_fpower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:FPOWer \n
		Snippet: value: float = driver.source.bb.v5G.downlink.refsig.get_fpower() \n
		No command help available \n
			:return: first_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:FPOWer?')
		return Conversions.str_to_float(response)

	def set_fpower(self, first_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:FPOWer \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_fpower(first_power = 1.0) \n
		No command help available \n
			:param first_power: No help available
		"""
		param = Conversions.decimal_value_to_str(first_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:FPOWer {param}')

	# noinspection PyTypeChecker
	def get_fst_position(self) -> enums.FirstRefSymPos:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:FSTPosition \n
		Snippet: value: enums.FirstRefSymPos = driver.source.bb.v5G.downlink.refsig.get_fst_position() \n
		No command help available \n
			:return: first_position: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:FSTPosition?')
		return Conversions.str_to_scalar_enum(response, enums.FirstRefSymPos)

	def set_fst_position(self, first_position: enums.FirstRefSymPos) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:FSTPosition \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_fst_position(first_position = enums.FirstRefSymPos.SYM0) \n
		No command help available \n
			:param first_position: No help available
		"""
		param = Conversions.enum_scalar_to_str(first_position, enums.FirstRefSymPos)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:FSTPosition {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:POWer \n
		Snippet: value: float = driver.source.bb.v5G.downlink.refsig.get_power() \n
		No command help available \n
			:return: power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:POWer \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_power(power = 1.0) \n
		No command help available \n
			:param power: No help available
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:POWer {param}')

	def get_prs(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:PRS \n
		Snippet: value: str = driver.source.bb.v5G.downlink.refsig.get_prs() \n
		No command help available \n
			:return: prs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:PRS?')
		return trim_str_response(response)

	def set_prs(self, prs: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:PRS \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_prs(prs = '1') \n
		No command help available \n
			:param prs: No help available
		"""
		param = Conversions.value_to_quoted_str(prs)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:PRS {param}')

	def get_s_2_active(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:S2ACtive \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.refsig.get_s_2_active() \n
		No command help available \n
			:return: s_2_active: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:S2ACtive?')
		return Conversions.str_to_bool(response)

	def set_s_2_active(self, s_2_active: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:S2ACtive \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_s_2_active(s_2_active = False) \n
		No command help available \n
			:param s_2_active: No help available
		"""
		param = Conversions.bool_to_str(s_2_active)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:S2ACtive {param}')

	def get_sc_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:SCOFfset \n
		Snippet: value: int = driver.source.bb.v5G.downlink.refsig.get_sc_offset() \n
		No command help available \n
			:return: sub_carr_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:SCOFfset?')
		return Conversions.str_to_int(response)

	def set_sc_offset(self, sub_carr_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:SCOFfset \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_sc_offset(sub_carr_offset = 1) \n
		No command help available \n
			:param sub_carr_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_carr_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:SCOFfset {param}')

	def get_spower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:SPOWer \n
		Snippet: value: float = driver.source.bb.v5G.downlink.refsig.get_spower() \n
		No command help available \n
			:return: symbol_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:REFSig:SPOWer?')
		return Conversions.str_to_float(response)

	def set_spower(self, symbol_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:REFSig:SPOWer \n
		Snippet: driver.source.bb.v5G.downlink.refsig.set_spower(symbol_power = 1.0) \n
		No command help available \n
			:param symbol_power: No help available
		"""
		param = Conversions.decimal_value_to_str(symbol_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:REFSig:SPOWer {param}')
