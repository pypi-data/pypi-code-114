from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)

	def set(self, ecount: int, errorCount=repcap.ErrorCount.Default) -> None:
		"""SCPI: DIAGnostic:INFO:ECOunt<CH>:SET \n
		Snippet: driver.diagnostic.info.ecount.set.set(ecount = 1, errorCount = repcap.ErrorCount.Default) \n
		No command help available \n
			:param ecount: No help available
			:param errorCount: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ecount')
		"""
		param = Conversions.decimal_value_to_str(ecount)
		errorCount_cmd_val = self._cmd_group.get_repcap_cmd_value(errorCount, repcap.ErrorCount)
		self._core.io.write(f'DIAGnostic:INFO:ECOunt{errorCount_cmd_val}:SET {param}')
