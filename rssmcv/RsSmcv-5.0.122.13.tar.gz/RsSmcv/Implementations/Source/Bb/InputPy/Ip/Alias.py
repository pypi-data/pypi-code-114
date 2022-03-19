from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alias:
	"""Alias commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alias", core, parent)

	def set(self, alias: str, ipVersion=repcap.IpVersion.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:ALIas \n
		Snippet: driver.source.bb.inputPy.ip.alias.set(alias = '1', ipVersion = repcap.IpVersion.Default) \n
		Specifies an alias, i.e. name for the IP connection. \n
			:param alias: string
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
		"""
		param = Conversions.value_to_quoted_str(alias)
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		self._core.io.write(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:ALIas {param}')

	def get(self, ipVersion=repcap.IpVersion.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:INPut:IP<CH>:ALIas \n
		Snippet: value: str = driver.source.bb.inputPy.ip.alias.get(ipVersion = repcap.IpVersion.Default) \n
		Specifies an alias, i.e. name for the IP connection. \n
			:param ipVersion: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Ip')
			:return: alias: string"""
		ipVersion_cmd_val = self._cmd_group.get_repcap_cmd_value(ipVersion, repcap.IpVersion)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:INPut:IP{ipVersion_cmd_val}:ALIas?')
		return trim_str_response(response)
