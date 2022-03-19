from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stuffing:
	"""Stuffing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stuffing", core, parent)

	def get(self, inputStream=repcap.InputStream.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:STUFfing \n
		Snippet: value: bool = driver.source.bb.dvbs2.isPy.stuffing.get(inputStream = repcap.InputStream.Default) \n
		Queries the stuffing state that is active. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: stuffing: 1| ON| 0| OFF"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:STUFfing?')
		return Conversions.str_to_bool(response)
