from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sonce:
	"""Sonce commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sonce", core, parent)

	def set(self, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:[SENSor<CH>]:[POWer]:SONCe \n
		Snippet: driver.source.correction.cset.data.sensor.power.sonce.set(channel = repcap.Channel.Default) \n
		Fills the selected user correction table with the level values measured by the power sensor for the given frequencies. To
		select the used power sensor set the suffix in key word SENSe. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
		"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:CSET:DATA:SENSor{channel_cmd_val}:POWer:SONCe')

	def set_with_opc(self, channel=repcap.Channel.Default, opc_timeout_ms: int = -1) -> None:
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:[SENSor<CH>]:[POWer]:SONCe \n
		Snippet: driver.source.correction.cset.data.sensor.power.sonce.set_with_opc(channel = repcap.Channel.Default) \n
		Fills the selected user correction table with the level values measured by the power sensor for the given frequencies. To
		select the used power sensor set the suffix in key word SENSe. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sensor')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:CSET:DATA:SENSor{channel_cmd_val}:POWer:SONCe', opc_timeout_ms)
