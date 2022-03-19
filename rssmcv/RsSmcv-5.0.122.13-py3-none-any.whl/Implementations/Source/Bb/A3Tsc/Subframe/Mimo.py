from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mimo:
	"""Mimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	def get(self, subframe=repcap.Subframe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:MIMO \n
		Snippet: value: bool = driver.source.bb.a3Tsc.subframe.mimo.get(subframe = repcap.Subframe.Default) \n
		Displays whether multiple inputs and multiple outputs (MIMO) are used. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: mimo: OFF| ON| 1| 0 | 0| 1| OFF| ON"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:MIMO?')
		return Conversions.str_to_bool(response)
