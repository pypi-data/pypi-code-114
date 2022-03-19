from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class First:
	"""First commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("first", core, parent)

	def set(self, sub_frame_first: int, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:SBS:FIRSt \n
		Snippet: driver.source.bb.a3Tsc.subframe.sbs.first.set(sub_frame_first = 1, subframe = repcap.Subframe.Default) \n
		Defines whether the first symbol of a subframe is a subframe boundary symbol. \n
			:param sub_frame_first: integer Range: 0 to 1
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.decimal_value_to_str(sub_frame_first)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:SBS:FIRSt {param}')

	def get(self, subframe=repcap.Subframe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:SBS:FIRSt \n
		Snippet: value: int = driver.source.bb.a3Tsc.subframe.sbs.first.get(subframe = repcap.Subframe.Default) \n
		Defines whether the first symbol of a subframe is a subframe boundary symbol. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: sub_frame_first: integer Range: 0 to 1"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:SBS:FIRSt?')
		return Conversions.str_to_int(response)
