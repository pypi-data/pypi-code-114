from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alp:
	"""Alp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alp", core, parent)

	def get_lmt(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:ALP:LMT \n
		Snippet: value: bool = driver.source.bb.a3Tsc.special.alp.get_lmt() \n
		Sets how the signaling is supported. \n
			:return: lmt_comp_mode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SPECial:ALP:LMT?')
		return Conversions.str_to_bool(response)

	def set_lmt(self, lmt_comp_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:ALP:LMT \n
		Snippet: driver.source.bb.a3Tsc.special.alp.set_lmt(lmt_comp_mode = False) \n
		Sets how the signaling is supported. \n
			:param lmt_comp_mode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(lmt_comp_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SPECial:ALP:LMT {param}')
