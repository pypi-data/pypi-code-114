from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qsfp:
	"""Qsfp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qsfp", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:QSFP:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.asequencing.qsfp.get_state() \n
		No command help available \n
			:return: qsfp_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:QSFP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qsfp_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:QSFP:STATe \n
		Snippet: driver.source.bb.esequencer.asequencing.qsfp.set_state(qsfp_state = False) \n
		No command help available \n
			:param qsfp_state: No help available
		"""
		param = Conversions.bool_to_str(qsfp_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:QSFP:STATe {param}')
