from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbols:
	"""Symbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbols", core, parent)

	def set(self, symbols: int, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:DATA:SYMBols \n
		Snippet: driver.source.bb.wlnn.fblock.user.data.symbols.set(symbols = 1, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the number of data symbols per frame block. If the number of OFDM data symbols is changed, the generator calculates
		the data field length as a function of the set PPDU bit rate and displays it at Data Length. \n
			:param symbols: integer Range: 1 to Max
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(symbols)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:DATA:SYMBols {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:DATA:SYMBols \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.user.data.symbols.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the number of data symbols per frame block. If the number of OFDM data symbols is changed, the generator calculates
		the data field length as a function of the set PPDU bit rate and displays it at Data Length. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: symbols: integer Range: 1 to Max"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:DATA:SYMBols?')
		return Conversions.str_to_int(response)
