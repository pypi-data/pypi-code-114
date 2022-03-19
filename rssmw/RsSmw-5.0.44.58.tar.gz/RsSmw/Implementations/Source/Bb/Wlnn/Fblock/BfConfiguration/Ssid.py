from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssid:
	"""Ssid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssid", core, parent)

	def set(self, ssid: str, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BFConfiguration:SSID \n
		Snippet: driver.source.bb.wlnn.fblock.bfConfiguration.ssid.set(ssid = '1', frameBlock = repcap.FrameBlock.Default) \n
		Specifies the desired SSID or the wildcard SSID. \n
			:param ssid: string Range: 0 char to 32 char
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.value_to_quoted_str(ssid)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BFConfiguration:SSID {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BFConfiguration:SSID \n
		Snippet: value: str = driver.source.bb.wlnn.fblock.bfConfiguration.ssid.get(frameBlock = repcap.FrameBlock.Default) \n
		Specifies the desired SSID or the wildcard SSID. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: ssid: string Range: 0 char to 32 char"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BFConfiguration:SSID?')
		return trim_str_response(response)
