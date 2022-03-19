from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sue:
	"""Sue commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sue", core, parent)

	def get_tsrs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:SUE:TSRS \n
		Snippet: value: bool = driver.source.bb.nr5G.tcw.sue.get_tsrs() \n
		Turns transmission of the sounding reference signal for 3GPP test cases on and off. \n
			:return: sue_transmit_srs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:SUE:TSRS?')
		return Conversions.str_to_bool(response)

	def set_tsrs(self, sue_transmit_srs: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:SUE:TSRS \n
		Snippet: driver.source.bb.nr5G.tcw.sue.set_tsrs(sue_transmit_srs = False) \n
		Turns transmission of the sounding reference signal for 3GPP test cases on and off. \n
			:param sue_transmit_srs: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(sue_transmit_srs)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:SUE:TSRS {param}')
