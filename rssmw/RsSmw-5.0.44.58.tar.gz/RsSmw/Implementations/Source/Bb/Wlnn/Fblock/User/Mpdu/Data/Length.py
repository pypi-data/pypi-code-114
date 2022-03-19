from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default, macPdu=repcap.MacPdu.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:MPDU<ST>:DATA:LENGth \n
		Snippet: driver.source.bb.wlnn.fblock.user.mpdu.data.length.set(length = 1, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default, macPdu = repcap.MacPdu.Default) \n
		Determines the size of the data field in bytes. \n
			:param length: integer Range: 0 to 16384
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
		"""
		param = Conversions.decimal_value_to_str(length)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:MPDU{macPdu_cmd_val}:DATA:LENGth {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default, macPdu=repcap.MacPdu.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:MPDU<ST>:DATA:LENGth \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.user.mpdu.data.length.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default, macPdu = repcap.MacPdu.Default) \n
		Determines the size of the data field in bytes. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
			:return: length: integer Range: 0 to 16384"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:MPDU{macPdu_cmd_val}:DATA:LENGth?')
		return Conversions.str_to_int(response)
