from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eratio:
	"""Eratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eratio", core, parent)

	def set(self, state: bool, twoStreams=repcap.TwoStreams.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:ERATio \n
		Snippet: driver.source.bb.esequencer.stream.eratio.set(state = False, twoStreams = repcap.TwoStreams.Default) \n
		No command help available \n
			:param state: No help available
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.bool_to_str(state)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:ERATio {param}')

	def get(self, twoStreams=repcap.TwoStreams.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:ERATio \n
		Snippet: value: bool = driver.source.bb.esequencer.stream.eratio.get(twoStreams = repcap.TwoStreams.Default) \n
		No command help available \n
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: state: No help available"""
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:ERATio?')
		return Conversions.str_to_bool(response)
