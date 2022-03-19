from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, select: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:CORRection:SPDevice:SELect \n
		Snippet: driver.sense.power.correction.spDevice.select.set(select = 1.0, channel = repcap.Channel.Default) \n
		Several S-parameter tables can be stored in a sensor. The command selects a loaded data set for S-parameter correction
		for the corresponding sensor. \n
			:param select: float
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.decimal_value_to_str(select)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:CORRection:SPDevice:SELect {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: SENSe<CH>:[POWer]:CORRection:SPDevice:SELect \n
		Snippet: value: float = driver.sense.power.correction.spDevice.select.get(channel = repcap.Channel.Default) \n
		Several S-parameter tables can be stored in a sensor. The command selects a loaded data set for S-parameter correction
		for the corresponding sensor. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: select: float"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:CORRection:SPDevice:SELect?')
		return Conversions.str_to_float(response)
