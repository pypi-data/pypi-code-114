from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stl:
	"""Stl commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stl", core, parent)

	def get_preamble(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:STL:PREamble \n
		Snippet: value: bool = driver.source.bb.a3Tsc.special.stl.get_preamble() \n
		Sets how the preamble packet is supported. \n
			:return: pre_comp_mode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SPECial:STL:PREamble?')
		return Conversions.str_to_bool(response)

	def set_preamble(self, pre_comp_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:STL:PREamble \n
		Snippet: driver.source.bb.a3Tsc.special.stl.set_preamble(pre_comp_mode = False) \n
		Sets how the preamble packet is supported. \n
			:param pre_comp_mode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pre_comp_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SPECial:STL:PREamble {param}')

	def get_tmp(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:STL:TMP \n
		Snippet: value: bool = driver.source.bb.a3Tsc.special.stl.get_tmp() \n
		Sets how the time & management packet is supported. \n
			:return: tmp_comp_mode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SPECial:STL:TMP?')
		return Conversions.str_to_bool(response)

	def set_tmp(self, tmp_comp_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:STL:TMP \n
		Snippet: driver.source.bb.a3Tsc.special.stl.set_tmp(tmp_comp_mode = False) \n
		Sets how the time & management packet is supported. \n
			:param tmp_comp_mode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tmp_comp_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SPECial:STL:TMP {param}')
