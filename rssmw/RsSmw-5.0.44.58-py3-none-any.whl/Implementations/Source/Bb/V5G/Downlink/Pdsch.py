from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	def get_pb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PDSCh:PB \n
		Snippet: value: int = driver.source.bb.v5G.downlink.pdsch.get_pb() \n
		No command help available \n
			:return: pb: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PDSCh:PB?')
		return Conversions.str_to_int(response)

	def set_pb(self, pb: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PDSCh:PB \n
		Snippet: driver.source.bb.v5G.downlink.pdsch.set_pb(pb = 1) \n
		No command help available \n
			:param pb: No help available
		"""
		param = Conversions.decimal_value_to_str(pb)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PDSCh:PB {param}')

	def get_ratba(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PDSCh:RATBa \n
		Snippet: value: float = driver.source.bb.v5G.downlink.pdsch.get_ratba() \n
		No command help available \n
			:return: ratio_pb_pa: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:PDSCh:RATBa?')
		return Conversions.str_to_float(response)

	def set_ratba(self, ratio_pb_pa: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PDSCh:RATBa \n
		Snippet: driver.source.bb.v5G.downlink.pdsch.set_ratba(ratio_pb_pa = 1.0) \n
		No command help available \n
			:param ratio_pb_pa: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio_pb_pa)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:PDSCh:RATBa {param}')
