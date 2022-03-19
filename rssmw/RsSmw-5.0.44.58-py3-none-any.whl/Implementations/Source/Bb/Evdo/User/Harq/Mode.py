from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.EvdoHarqMode, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:HARQ:MODE \n
		Snippet: driver.source.bb.evdo.user.harq.mode.set(mode = enums.EvdoHarqMode.ACK, userIx = repcap.UserIx.Default) \n
		Enables or disables the H-ARQ Channel. The H-ARQ channel is used by the access network to transmit positive
		acknowledgement (ACK) or a negative acknowledgement (NAK) in response to a physical layer packet. Note: This parameter is
		enabled for Physical Layer Subtype 2 only. \n
			:param mode: OFF| ACK| NAK OFF Disables transmission of the H-ARQ channel. ACK Enables transmission of H-ARQ. The channel is transmitted with all bits set to ACK. NAK Enables transmission of H-ARQ. The channel is transmitted with all bits set to NAK
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EvdoHarqMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:HARQ:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EvdoHarqMode:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:HARQ:MODE \n
		Snippet: value: enums.EvdoHarqMode = driver.source.bb.evdo.user.harq.mode.get(userIx = repcap.UserIx.Default) \n
		Enables or disables the H-ARQ Channel. The H-ARQ channel is used by the access network to transmit positive
		acknowledgement (ACK) or a negative acknowledgement (NAK) in response to a physical layer packet. Note: This parameter is
		enabled for Physical Layer Subtype 2 only. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: mode: OFF| ACK| NAK OFF Disables transmission of the H-ARQ channel. ACK Enables transmission of H-ARQ. The channel is transmitted with all bits set to ACK. NAK Enables transmission of H-ARQ. The channel is transmitted with all bits set to NAK"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:HARQ:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoHarqMode)
