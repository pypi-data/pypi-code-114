from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def get_domain(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:DOMain \n
		Snippet: value: str = driver.system.communicate.network.common.get_domain() \n
		Determines the primary suffix of the network domain. \n
			:return: domain: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:COMMon:DOMain?')
		return trim_str_response(response)

	def set_domain(self, domain: str) -> None:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:DOMain \n
		Snippet: driver.system.communicate.network.common.set_domain(domain = '1') \n
		Determines the primary suffix of the network domain. \n
			:param domain: string
		"""
		param = Conversions.value_to_quoted_str(domain)
		self._core.io.write(f'SYSTem:COMMunicate:NETWork:COMMon:DOMain {param}')

	def get_hostname(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:HOSTname \n
		Snippet: value: str = driver.system.communicate.network.common.get_hostname() \n
		Sets an individual hostname for the vector signal generator. Note: We recommend that you do not change the hostname to
		avoid problems with the network connection. If you change the hostname, be sure to use a unique name.
		This is a password-protected function. Unlock the protection level 1 to access it. See method RsSmcv.System.Protect.State.
		set. \n
			:return: hostname: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:COMMon:HOSTname?')
		return trim_str_response(response)

	def set_hostname(self, hostname: str) -> None:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:HOSTname \n
		Snippet: driver.system.communicate.network.common.set_hostname(hostname = '1') \n
		Sets an individual hostname for the vector signal generator. Note: We recommend that you do not change the hostname to
		avoid problems with the network connection. If you change the hostname, be sure to use a unique name.
		This is a password-protected function. Unlock the protection level 1 to access it. See method RsSmcv.System.Protect.State.
		set. \n
			:param hostname: string
		"""
		param = Conversions.value_to_quoted_str(hostname)
		self._core.io.write(f'SYSTem:COMMunicate:NETWork:COMMon:HOSTname {param}')

	def get_workgroup(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:WORKgroup \n
		Snippet: value: str = driver.system.communicate.network.common.get_workgroup() \n
		Sets an individual workgroup name for the instrument. \n
			:return: workgroup: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:COMMon:WORKgroup?')
		return trim_str_response(response)

	def set_workgroup(self, workgroup: str) -> None:
		"""SCPI: SYSTem:COMMunicate:NETWork:[COMMon]:WORKgroup \n
		Snippet: driver.system.communicate.network.common.set_workgroup(workgroup = '1') \n
		Sets an individual workgroup name for the instrument. \n
			:param workgroup: string
		"""
		param = Conversions.value_to_quoted_str(workgroup)
		self._core.io.write(f'SYSTem:COMMunicate:NETWork:COMMon:WORKgroup {param}')
