from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zero:
	"""Zero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zero", core, parent)

	def set(self, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:ZERO \n
		Snippet: driver.sense.power.zero.set(channel = repcap.Channel.Default) \n
		Performs zeroing of the sensor. Zeroing is required after warm-up, i.e. after connecting the sensor. Note: Switch off or
		disconnect the RF power source from the sensor before zeroing.
			INTRO_CMD_HELP: We recommend that you zero in regular intervals (at least once a day) , if: \n
			- The temperature has varied more than about 5 °C.
			- The sensor has been replaced.
			- You want to measure very low power. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:ZERO')

	def set_with_opc(self, channel=repcap.Channel.Default, opc_timeout_ms: int = -1) -> None:
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		"""SCPI: SENSe<CH>:[POWer]:ZERO \n
		Snippet: driver.sense.power.zero.set_with_opc(channel = repcap.Channel.Default) \n
		Performs zeroing of the sensor. Zeroing is required after warm-up, i.e. after connecting the sensor. Note: Switch off or
		disconnect the RF power source from the sensor before zeroing.
			INTRO_CMD_HELP: We recommend that you zero in regular intervals (at least once a day) , if: \n
			- The temperature has varied more than about 5 °C.
			- The sensor has been replaced.
			- You want to measure very low power. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe{channel_cmd_val}:POWer:ZERO', opc_timeout_ms)
