from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PfpFactor:
	"""PfpFactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pfpFactor", core, parent)

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PFPFactor \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.pfpFactor.get(frameBlock = repcap.FrameBlock.Default) \n
		Queries the pre-FEC padding factor. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: pre_fec_padding: integer Range: 0 to 3"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PFPFactor?')
		return Conversions.str_to_int(response)
