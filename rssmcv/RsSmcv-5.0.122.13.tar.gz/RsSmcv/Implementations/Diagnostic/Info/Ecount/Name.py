from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def get(self, errorCount=repcap.ErrorCount.Default) -> str:
		"""SCPI: DIAGnostic:INFO:ECOunt<CH>:NAME \n
		Snippet: value: str = driver.diagnostic.info.ecount.name.get(errorCount = repcap.ErrorCount.Default) \n
		No command help available \n
			:param errorCount: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ecount')
			:return: ecount: No help available"""
		errorCount_cmd_val = self._cmd_group.get_repcap_cmd_value(errorCount, repcap.ErrorCount)
		response = self._core.io.query_str(f'DIAGnostic:INFO:ECOunt{errorCount_cmd_val}:NAME?')
		return trim_str_response(response)
