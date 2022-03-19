from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:EFRontend:CONNection:STATe \n
		Snippet: value: bool = driver.source.efrontend.connection.get_state() \n
		Queries the state of the connection between R&S SMW and external frontend. \n
			:return: conn_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:CONNection:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, conn_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:CONNection:STATe \n
		Snippet: driver.source.efrontend.connection.set_state(conn_state = False) \n
		Queries the state of the connection between R&S SMW and external frontend. \n
			:param conn_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(conn_state)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:CONNection:STATe {param}')
