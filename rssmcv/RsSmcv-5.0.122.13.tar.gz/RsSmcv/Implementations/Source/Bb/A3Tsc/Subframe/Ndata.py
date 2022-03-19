from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ndata:
	"""Ndata commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndata", core, parent)

	def set(self, tot_num_data: int, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:NDATa \n
		Snippet: driver.source.bb.a3Tsc.subframe.ndata.set(tot_num_data = 1, subframe = repcap.Subframe.Default) \n
		Sets the number of data symbols per subframe, including the subframe boundary symbols, excluding the preamble OFDM
		symbols. \n
			:param tot_num_data: integer Range: 1 to 2048
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.decimal_value_to_str(tot_num_data)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:NDATa {param}')

	def get(self, subframe=repcap.Subframe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:NDATa \n
		Snippet: value: int = driver.source.bb.a3Tsc.subframe.ndata.get(subframe = repcap.Subframe.Default) \n
		Sets the number of data symbols per subframe, including the subframe boundary symbols, excluding the preamble OFDM
		symbols. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: tot_num_data: integer Range: 1 to 2048"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:NDATa?')
		return Conversions.str_to_int(response)
