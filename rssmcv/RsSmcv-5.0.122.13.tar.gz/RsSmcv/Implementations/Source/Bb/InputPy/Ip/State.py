from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, alias: bool, ipVersion=repcap.IpVersion.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:[STATe] \n
		Snippet: driver.source.bb.inputPy.ip.state.set(alias = False, ipVersion = repcap.IpVersion.Default) \n
		Activates/deactivates the 'IP Channel x' as IP input. Specify the current IP TS Channel with the command
		SOURce1:BB:DigStd:INPut:TSCHannel. DigStd stands for the IP TS Channel in the corresponding broadcast standard. \n
			:param alias: 1| ON| 0| OFF
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
		"""
		param = Conversions.bool_to_str(alias)
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:STATe {param}')

	def get(self, ipVersion=repcap.IpVersion.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:[STATe] \n
		Snippet: value: bool = driver.source.bb.inputPy.ip.state.get(ipVersion = repcap.IpVersion.Default) \n
		Activates/deactivates the 'IP Channel x' as IP input. Specify the current IP TS Channel with the command
		SOURce1:BB:DigStd:INPut:TSCHannel. DigStd stands for the IP TS Channel in the corresponding broadcast standard. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
			:return: alias: 1| ON| 0| OFF"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
