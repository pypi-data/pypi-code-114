from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xpdcch:
	"""Xpdcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xpdcch", core, parent)

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:XPDCch:RATBa \n
		Snippet: value: float = driver.source.bb.v5G.downlink.xpdcch.get_ratba() \n
		No command help available \n
			:return: ratio_pb_ba: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:XPDCch:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_ba: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:XPDCch:RATBa \n
		Snippet: driver.source.bb.v5G.downlink.xpdcch.set_ratba(ratio_pb_ba = 1.0) \n
		No command help available \n
			:param ratio_pb_ba: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_ba)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:XPDCch:RATBa {param}')
