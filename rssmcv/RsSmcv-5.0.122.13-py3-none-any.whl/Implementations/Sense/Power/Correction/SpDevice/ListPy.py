from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self, channel=repcap.Channel.Default) -> List[str]:
		"""SCPI: SENSe<CH>:[POWer]:CORRection:SPDevice:LIST \n
		Snippet: value: List[str] = driver.sense.power.correction.spDevice.listPy.get(channel = repcap.Channel.Default) \n
		Queries the list of the S-parameter data sets that have been loaded to the power sensor. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: list_py: string list"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:CORRection:SPDevice:LIST?')
		return Conversions.str_to_str_list(response)
