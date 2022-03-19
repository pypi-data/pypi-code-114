from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NePresent:
	"""NePresent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nePresent", core, parent)

	def set(self, ene_present: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BFConfiguration:ERP:NEPResent \n
		Snippet: driver.source.bb.wlnn.fblock.bfConfiguration.erp.nePresent.set(ene_present = False, frameBlock = repcap.FrameBlock.Default) \n
		Sets Non-ERP Present on. This is needed if there is a non-ERP MU associated to the AP. \n
			:param ene_present: 1| ON| 0| OFF
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(ene_present)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BFConfiguration:ERP:NEPResent {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BFConfiguration:ERP:NEPResent \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.bfConfiguration.erp.nePresent.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets Non-ERP Present on. This is needed if there is a non-ERP MU associated to the AP. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: ene_present: 1| ON| 0| OFF"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BFConfiguration:ERP:NEPResent?')
		return Conversions.str_to_bool(response)
