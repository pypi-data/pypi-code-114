from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def get_hostname(self) -> str:
		"""SCPI: SYSTem:COMMunicate:BB<HW>:QSFP:NETWork:[COMMon]:HOSTname \n
		Snippet: value: str = driver.system.communicate.bb.qsfp.network.common.get_hostname() \n
		No command help available \n
			:return: hostname: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:BB<HwInstance>:QSFP:NETWork:COMMon:HOSTname?')
		return trim_str_response(response)
