from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def get(self, subframe=repcap.Subframe.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:DURation \n
		Snippet: value: float = driver.source.bb.a3Tsc.subframe.duration.get(subframe = repcap.Subframe.Default) \n
		Queries the duration of the subframe. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: duration: float Range: 0 to 9999.999"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:DURation?')
		return Conversions.str_to_float(response)
