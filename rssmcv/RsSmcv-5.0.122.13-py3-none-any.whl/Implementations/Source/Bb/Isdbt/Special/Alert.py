from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alert:
	"""Alert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alert", core, parent)

	def get_broadcast(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:ALERt:[BROadcast] \n
		Snippet: value: bool = driver.source.bb.isdbt.special.alert.get_broadcast() \n
		Enables or disables the alert broadcasting flag in the data. \n
			:return: alert_bc_flag: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SPECial:ALERt:BROadcast?')
		return Conversions.str_to_bool(response)

	def set_broadcast(self, alert_bc_flag: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:ALERt:[BROadcast] \n
		Snippet: driver.source.bb.isdbt.special.alert.set_broadcast(alert_bc_flag = False) \n
		Enables or disables the alert broadcasting flag in the data. \n
			:param alert_bc_flag: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(alert_bc_flag)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SPECial:ALERt:BROadcast {param}')
