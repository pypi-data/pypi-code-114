from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaRound:
	"""TaRound commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taRound", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TARound:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.taRound.get_state() \n
		Asctivates/deactivates turnaround. \n
			:return: ta_round: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:TARound:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, ta_round: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TARound:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.taRound.set_state(ta_round = False) \n
		Asctivates/deactivates turnaround. \n
			:param ta_round: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(ta_round)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:TARound:STATe {param}')
