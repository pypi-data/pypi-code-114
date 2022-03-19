from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LogFile:
	"""LogFile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logFile", core, parent)

	def get(self, frameBlock=repcap.FrameBlock.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:LOGFile \n
		Snippet: value: str = driver.source.bb.wlnn.fblock.logFile.get(frameBlock = repcap.FrameBlock.Default) \n
		Queries the fixed file path used for logging the contents of HE-SIG-A and HE-SIG-B fields,
		if [:SOURce<hw>]:BB:WLNN:FBLock<ch>:LOGGing is set to ON. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: log_file: string"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:LOGFile?')
		return trim_str_response(response)
