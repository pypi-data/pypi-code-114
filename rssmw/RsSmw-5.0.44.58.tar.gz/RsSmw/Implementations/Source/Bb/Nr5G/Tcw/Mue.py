from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mue:
	"""Mue commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mue", core, parent)

	def get_tsrs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:MUE:TSRS \n
		Snippet: value: bool = driver.source.bb.nr5G.tcw.mue.get_tsrs() \n
		Turns transmission of the sounding reference signal for 3GPP test cases on and off. \n
			:return: transmit_srs: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:MUE:TSRS?')
		return Conversions.str_to_bool(response)

	def set_tsrs(self, transmit_srs: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:MUE:TSRS \n
		Snippet: driver.source.bb.nr5G.tcw.mue.set_tsrs(transmit_srs = False) \n
		Turns transmission of the sounding reference signal for 3GPP test cases on and off. \n
			:param transmit_srs: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(transmit_srs)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:MUE:TSRS {param}')
