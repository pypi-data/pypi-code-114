from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def get_hostname(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:COMMon:HOSTname \n
		Snippet: value: str = driver.system.communicate.bcIp.network.common.get_hostname() \n
		Sets an individual hostname for the vector signal generator. Note:We recommend that you do not change the hostname to
		avoid problems with the network connection. If you change the hostname, be sure to use a unique name. \n
			:return: hostname: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BCIP:NETWork:COMMon:HOSTname?')
		return trim_str_response(response)

	def set_hostname(self, hostname: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BCIP:NETWork:COMMon:HOSTname \n
		Snippet: driver.system.communicate.bcIp.network.common.set_hostname(hostname = '1') \n
		Sets an individual hostname for the vector signal generator. Note:We recommend that you do not change the hostname to
		avoid problems with the network connection. If you change the hostname, be sure to use a unique name. \n
			:param hostname: string
		"""
		param = Conversions.value_to_quoted_str(hostname)
		self._core.io.write(f'SYSTem:COMMunicate:BCIP:NETWork:COMMon:HOSTname {param}')
