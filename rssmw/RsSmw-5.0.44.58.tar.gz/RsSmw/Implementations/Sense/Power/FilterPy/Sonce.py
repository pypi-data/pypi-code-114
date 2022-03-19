from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sonce:
	"""Sonce commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sonce", core, parent)

	def set(self, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:FILTer:SONCe \n
		Snippet: driver.sense.power.filterPy.sonce.set(channel = repcap.Channel.Default) \n
		Starts searching the optimum filter length for the current measurement conditions. You can check the result with command
		SENS1:POW:FILT:LENG:USER? in filter mode USER (method RsSmw.Sense.Power.FilterPy.TypePy.set) . \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:FILTer:SONCe')

	def set_with_opc(self, channel=repcap.Channel.Default, opc_timeout_ms: int = -1) -> None:
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		"""SCPI: SENSe<CH>:[POWer]:FILTer:SONCe \n
		Snippet: driver.sense.power.filterPy.sonce.set_with_opc(channel = repcap.Channel.Default) \n
		Starts searching the optimum filter length for the current measurement conditions. You can check the result with command
		SENS1:POW:FILT:LENG:USER? in filter mode USER (method RsSmw.Sense.Power.FilterPy.TypePy.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe{channel_cmd_val}:POWer:FILTer:SONCe', opc_timeout_ms)
