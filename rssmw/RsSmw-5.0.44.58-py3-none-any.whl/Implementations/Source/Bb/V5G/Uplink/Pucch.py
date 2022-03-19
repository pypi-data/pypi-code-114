from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pucch:
	"""Pucch commands group definition. 8 total commands, 0 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	def get_de_shift(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:DESHift \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_de_shift() \n
		No command help available \n
			:return: delta_shift: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:DESHift?')
		return Conversions.str_to_int(response)

	def set_de_shift(self, delta_shift: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:DESHift \n
		Snippet: driver.source.bb.v5G.uplink.pucch.set_de_shift(delta_shift = 1) \n
		No command help available \n
			:param delta_shift: No help available
		"""
		param = Conversions.decimal_value_to_str(delta_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUCCh:DESHift {param}')

	def get_n_1_cs(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N1CS \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_n_1_cs() \n
		No command help available \n
			:return: n_1_cs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:N1CS?')
		return Conversions.str_to_int(response)

	def set_n_1_cs(self, n_1_cs: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N1CS \n
		Snippet: driver.source.bb.v5G.uplink.pucch.set_n_1_cs(n_1_cs = 1) \n
		No command help available \n
			:param n_1_cs: No help available
		"""
		param = Conversions.decimal_value_to_str(n_1_cs)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUCCh:N1CS {param}')

	def get_n_1_e_max(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N1EMax \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_n_1_e_max() \n
		No command help available \n
			:return: n_1_e_max: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:N1EMax?')
		return Conversions.str_to_int(response)

	def get_n_1_n_max(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N1NMax \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_n_1_n_max() \n
		No command help available \n
			:return: n_1_norm_cp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:N1NMax?')
		return Conversions.str_to_int(response)

	def get_n_2_max(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N2Max \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_n_2_max() \n
		No command help available \n
			:return: n_2_max: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:N2Max?')
		return Conversions.str_to_int(response)

	def get_n_2_rb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N2RB \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_n_2_rb() \n
		No command help available \n
			:return: n_2_rb: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:N2RB?')
		return Conversions.str_to_int(response)

	def set_n_2_rb(self, n_2_rb: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N2RB \n
		Snippet: driver.source.bb.v5G.uplink.pucch.set_n_2_rb(n_2_rb = 1) \n
		No command help available \n
			:param n_2_rb: No help available
		"""
		param = Conversions.decimal_value_to_str(n_2_rb)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUCCh:N2RB {param}')

	def get_n_3_max(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:N3Max \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_n_3_max() \n
		No command help available \n
			:return: n_3_max: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:N3Max?')
		return Conversions.str_to_int(response)

	def get_no_rb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:NORB \n
		Snippet: value: int = driver.source.bb.v5G.uplink.pucch.get_no_rb() \n
		No command help available \n
			:return: rb_count: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PUCCh:NORB?')
		return Conversions.str_to_int(response)

	def set_no_rb(self, rb_count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PUCCh:NORB \n
		Snippet: driver.source.bb.v5G.uplink.pucch.set_no_rb(rb_count = 1) \n
		No command help available \n
			:param rb_count: No help available
		"""
		param = Conversions.decimal_value_to_str(rb_count)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PUCCh:NORB {param}')
