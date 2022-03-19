from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def get(self, subframe=repcap.Subframe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:USED:[BANDwidth] \n
		Snippet: value: int = driver.source.bb.a3Tsc.subframe.used.bandwidth.get(subframe = repcap.Subframe.Default) \n
		Queries the used bandwidth per subframe. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: used_bw: integer Range: 0 to 9.9999999"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:USED:BANDwidth?')
		return Conversions.str_to_int(response)
