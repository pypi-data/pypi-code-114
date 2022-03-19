from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:DATA:LENGth \n
		Snippet: driver.source.bb.wlnn.fblock.user.data.length.set(length = 1, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		The command enters the size of the data field in bytes. For Data Length = 0, no data field will be generated for the case
		of a sounding frame. The maximum data length depends on the physical mode: In LEGACY mode, the maximum value is 4061
		Bytes. In MIXED MODE and GREEN FIELD, the maximum value is 65495 Bytes. The data length is related to the number of data
		symbols. Whenever the data length changes, the number of data symbols is updated and vice versa. \n
			:param length: integer Range: 0 to Max
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(length)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:DATA:LENGth {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:DATA:LENGth \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.user.data.length.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		The command enters the size of the data field in bytes. For Data Length = 0, no data field will be generated for the case
		of a sounding frame. The maximum data length depends on the physical mode: In LEGACY mode, the maximum value is 4061
		Bytes. In MIXED MODE and GREEN FIELD, the maximum value is 65495 Bytes. The data length is related to the number of data
		symbols. Whenever the data length changes, the number of data symbols is updated and vice versa. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: length: integer Range: 0 to Max"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:DATA:LENGth?')
		return Conversions.str_to_int(response)
