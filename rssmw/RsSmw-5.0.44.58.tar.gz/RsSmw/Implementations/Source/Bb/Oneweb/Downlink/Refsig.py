from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Refsig:
	"""Refsig commands group definition. 10 total commands, 0 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refsig", core, parent)

	def get_epre(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:EPRE \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.refsig.get_epre() \n
		No command help available \n
			:return: rel_to_level_displ: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:EPRE?')
		return Conversions.str_to_float(response)

	def get_fpower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:FPOWer \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.refsig.get_fpower() \n
		No command help available \n
			:return: first_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:FPOWer?')
		return Conversions.str_to_float(response)

	def set_fpower(self, first_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:FPOWer \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_fpower(first_power = 1.0) \n
		No command help available \n
			:param first_power: No help available
		"""
		param = Conversions.decimal_value_to_str(first_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:FPOWer {param}')

	# noinspection PyTypeChecker
	def get_fst_position(self) -> enums.FirstRefSymPos:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:FSTPosition \n
		Snippet: value: enums.FirstRefSymPos = driver.source.bb.oneweb.downlink.refsig.get_fst_position() \n
		No command help available \n
			:return: first_position: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:FSTPosition?')
		return Conversions.str_to_scalar_enum(response, enums.FirstRefSymPos)

	def set_fst_position(self, first_position: enums.FirstRefSymPos) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:FSTPosition \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_fst_position(first_position = enums.FirstRefSymPos.SYM0) \n
		No command help available \n
			:param first_position: No help available
		"""
		param = Conversions.enum_scalar_to_str(first_position, enums.FirstRefSymPos)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:FSTPosition {param}')

	# noinspection PyTypeChecker
	def get_ort_sequence(self) -> enums.OneWebOrthSequ:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:ORTSequence \n
		Snippet: value: enums.OneWebOrthSequ = driver.source.bb.oneweb.downlink.refsig.get_ort_sequence() \n
		No command help available \n
			:return: orth_sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:ORTSequence?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebOrthSequ)

	def set_ort_sequence(self, orth_sequence: enums.OneWebOrthSequ) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:ORTSequence \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_ort_sequence(orth_sequence = enums.OneWebOrthSequ.ORS0) \n
		No command help available \n
			:param orth_sequence: No help available
		"""
		param = Conversions.enum_scalar_to_str(orth_sequence, enums.OneWebOrthSequ)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:ORTSequence {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:POWer \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.refsig.get_power() \n
		Queries the reference signal power. \n
			:return: power: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:POWer?')
		return Conversions.str_to_float(response)

	def get_prs(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:PRS \n
		Snippet: value: str = driver.source.bb.oneweb.downlink.refsig.get_prs() \n
		No command help available \n
			:return: prs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:PRS?')
		return trim_str_response(response)

	def set_prs(self, prs: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:PRS \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_prs(prs = '1') \n
		No command help available \n
			:param prs: No help available
		"""
		param = Conversions.value_to_quoted_str(prs)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:PRS {param}')

	def get_prsi(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:PRSI \n
		Snippet: value: str = driver.source.bb.oneweb.downlink.refsig.get_prsi() \n
		No command help available \n
			:return: prsi: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:PRSI?')
		return trim_str_response(response)

	def set_prsi(self, prsi: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:PRSI \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_prsi(prsi = '1') \n
		No command help available \n
			:param prsi: No help available
		"""
		param = Conversions.value_to_quoted_str(prsi)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:PRSI {param}')

	def get_s_2_active(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:S2ACtive \n
		Snippet: value: bool = driver.source.bb.oneweb.downlink.refsig.get_s_2_active() \n
		No command help available \n
			:return: s_2_active: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:S2ACtive?')
		return Conversions.str_to_bool(response)

	def set_s_2_active(self, s_2_active: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:S2ACtive \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_s_2_active(s_2_active = False) \n
		No command help available \n
			:param s_2_active: No help available
		"""
		param = Conversions.bool_to_str(s_2_active)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:S2ACtive {param}')

	def get_sc_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:SCOFfset \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.refsig.get_sc_offset() \n
		No command help available \n
			:return: sub_carr_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:SCOFfset?')
		return Conversions.str_to_int(response)

	def set_sc_offset(self, sub_carr_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:SCOFfset \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_sc_offset(sub_carr_offset = 1) \n
		No command help available \n
			:param sub_carr_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_carr_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:SCOFfset {param}')

	def get_shif_sequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:SHIFsequence \n
		Snippet: value: str = driver.source.bb.oneweb.downlink.refsig.get_shif_sequence() \n
		No command help available \n
			:return: shift_sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:SHIFsequence?')
		return trim_str_response(response)

	def set_shif_sequence(self, shift_sequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:REFSig:SHIFsequence \n
		Snippet: driver.source.bb.oneweb.downlink.refsig.set_shif_sequence(shift_sequence = '1') \n
		No command help available \n
			:param shift_sequence: No help available
		"""
		param = Conversions.value_to_quoted_str(shift_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:REFSig:SHIFsequence {param}')
