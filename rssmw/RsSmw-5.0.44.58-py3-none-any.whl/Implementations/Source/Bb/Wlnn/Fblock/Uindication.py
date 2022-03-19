from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uindication:
	"""Uindication commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uindication", core, parent)

	def set(self, uindication: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:UINDication \n
		Snippet: driver.source.bb.wlnn.fblock.uindication.set(uindication = False, frameBlock = repcap.FrameBlock.Default) \n
		Defines the currently generated user. In activated Multi User MIMO only, one user can be generated at a time.
		This parameter selects the generated one out of four available users. \n
			:param uindication: UIDX0| UIDX1| UIDX2| UIDX3
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(uindication)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:UINDication {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:UINDication \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.uindication.get(frameBlock = repcap.FrameBlock.Default) \n
		Defines the currently generated user. In activated Multi User MIMO only, one user can be generated at a time.
		This parameter selects the generated one out of four available users. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: uindication: No help available"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:UINDication?')
		return Conversions.str_to_bool(response)
