from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def get_hostname(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:[COMMon]:HOSTname \n
		Snippet: value: str = driver.system.communicate.bb.network.common.get_hostname() \n
		Sets an individual hostname for the R&S SMW. Note:We recommend that you do not change the hostname to avoid problems with
		the network connection. If you change the hostname, be sure to use a unique name. This is a password-protected function.
		Unlock the protection level 1 to access it, see method RsSmw.System.Protect.State.set. \n
			:return: hostname: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:COMMon:HOSTname?')
		return trim_str_response(response)

	def set_hostname(self, hostname: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:[COMMon]:HOSTname \n
		Snippet: driver.system.communicate.bb.network.common.set_hostname(hostname = '1') \n
		Sets an individual hostname for the R&S SMW. Note:We recommend that you do not change the hostname to avoid problems with
		the network connection. If you change the hostname, be sure to use a unique name. This is a password-protected function.
		Unlock the protection level 1 to access it, see method RsSmw.System.Protect.State.set. \n
			:param hostname: string
		"""
		param = Conversions.value_to_quoted_str(hostname)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:COMMon:HOSTname {param}')

	def get_workgroup(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:[COMMon]:WORKgroup \n
		Snippet: value: str = driver.system.communicate.bb.network.common.get_workgroup() \n
		No command help available \n
			:return: workgroup: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:NETWork:COMMon:WORKgroup?')
		return trim_str_response(response)

	def set_workgroup(self, workgroup: str) -> None:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:NETWork:[COMMon]:WORKgroup \n
		Snippet: driver.system.communicate.bb.network.common.set_workgroup(workgroup = '1') \n
		No command help available \n
			:param workgroup: No help available
		"""
		param = Conversions.value_to_quoted_str(workgroup)
		self._core.io.write(f'SYSTem:COMMunicate:BB<HwInstance>:NETWork:COMMon:WORKgroup {param}')
