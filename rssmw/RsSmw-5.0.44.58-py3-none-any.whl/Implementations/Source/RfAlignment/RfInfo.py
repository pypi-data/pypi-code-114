from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfInfo:
	"""RfInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfInfo", core, parent)

	def get(self, info_name: str) -> str:
		"""SCPI: SOURce<HW>:RFALignment:RFINfo \n
		Snippet: value: str = driver.source.rfAlignment.rfInfo.get(info_name = '1') \n
		No command help available \n
			:param info_name: No help available
			:return: value: No help available"""
		param = Conversions.value_to_quoted_str(info_name)
		response = self._core.io.query_str(f'SOURce<HwInstance>:RFALignment:RFINfo? {param}')
		return trim_str_response(response)
