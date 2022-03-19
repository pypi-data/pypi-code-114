from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drs:
	"""Drs commands group definition. 8 total commands, 0 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("drs", core, parent)

	def get_dseq_shift(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:DSEQshift \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.refsig.drs.get_dseq_shift() \n
		No command help available \n
			:return: delta_seq_shift: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:DSEQshift?')
		return Conversions.str_to_int(response)

	def set_dseq_shift(self, delta_seq_shift: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:DSEQshift \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_dseq_shift(delta_seq_shift = 1) \n
		No command help available \n
			:param delta_seq_shift: No help available
		"""
		param = Conversions.decimal_value_to_str(delta_seq_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:DSEQshift {param}')

	def get_ghopping(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:GHOPping \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.refsig.drs.get_ghopping() \n
		No command help available \n
			:return: group_hopping: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:GHOPping?')
		return Conversions.str_to_bool(response)

	def set_ghopping(self, group_hopping: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:GHOPping \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_ghopping(group_hopping = False) \n
		No command help available \n
			:param group_hopping: No help available
		"""
		param = Conversions.bool_to_str(group_hopping)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:GHOPping {param}')

	def get_stb_sequence(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:STBSequence \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.refsig.drs.get_stb_sequence() \n
		No command help available \n
			:return: six_tone_base_seq: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:STBSequence?')
		return Conversions.str_to_int(response)

	def set_stb_sequence(self, six_tone_base_seq: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:STBSequence \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_stb_sequence(six_tone_base_seq = 1) \n
		No command help available \n
			:param six_tone_base_seq: No help available
		"""
		param = Conversions.decimal_value_to_str(six_tone_base_seq)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:STBSequence {param}')

	def get_stc_shift(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:STCShift \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.refsig.drs.get_stc_shift() \n
		No command help available \n
			:return: six_tone_cyc_shift: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:STCShift?')
		return Conversions.str_to_int(response)

	def set_stc_shift(self, six_tone_cyc_shift: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:STCShift \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_stc_shift(six_tone_cyc_shift = 1) \n
		No command help available \n
			:param six_tone_cyc_shift: No help available
		"""
		param = Conversions.decimal_value_to_str(six_tone_cyc_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:STCShift {param}')

	def get_ttb_sequence(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:TTBSequence \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.refsig.drs.get_ttb_sequence() \n
		No command help available \n
			:return: three_tone_base_sq: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:TTBSequence?')
		return Conversions.str_to_int(response)

	def set_ttb_sequence(self, three_tone_base_sq: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:TTBSequence \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_ttb_sequence(three_tone_base_sq = 1) \n
		No command help available \n
			:param three_tone_base_sq: No help available
		"""
		param = Conversions.decimal_value_to_str(three_tone_base_sq)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:TTBSequence {param}')

	def get_ttc_shift(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:TTCShift \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.refsig.drs.get_ttc_shift() \n
		No command help available \n
			:return: three_tone_cyc_shi: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:TTCShift?')
		return Conversions.str_to_int(response)

	def set_ttc_shift(self, three_tone_cyc_shi: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:TTCShift \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_ttc_shift(three_tone_cyc_shi = 1) \n
		No command help available \n
			:param three_tone_cyc_shi: No help available
		"""
		param = Conversions.decimal_value_to_str(three_tone_cyc_shi)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:TTCShift {param}')

	def get_twb_sequence(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:TWBSequence \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.refsig.drs.get_twb_sequence() \n
		No command help available \n
			:return: twelfe_tone_base_s: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:TWBSequence?')
		return Conversions.str_to_int(response)

	def set_twb_sequence(self, twelfe_tone_base_s: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:TWBSequence \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_twb_sequence(twelfe_tone_base_s = 1) \n
		No command help available \n
			:param twelfe_tone_base_s: No help available
		"""
		param = Conversions.decimal_value_to_str(twelfe_tone_base_s)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:TWBSequence {param}')

	def get_use_base(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:USEBase \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.refsig.drs.get_use_base() \n
		No command help available \n
			:return: use_base_sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:USEBase?')
		return Conversions.str_to_bool(response)

	def set_use_base(self, use_base_sequence: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:REFSig:DRS:USEBase \n
		Snippet: driver.source.bb.oneweb.uplink.refsig.drs.set_use_base(use_base_sequence = False) \n
		No command help available \n
			:param use_base_sequence: No help available
		"""
		param = Conversions.bool_to_str(use_base_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:REFSig:DRS:USEBase {param}')
