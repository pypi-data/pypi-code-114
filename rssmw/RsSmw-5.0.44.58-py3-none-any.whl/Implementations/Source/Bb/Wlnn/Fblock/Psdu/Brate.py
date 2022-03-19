from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Brate:
	"""Brate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("brate", core, parent)

	def set(self, brate: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PSDU:BRATe \n
		Snippet: driver.source.bb.wlnn.fblock.psdu.brate.set(brate = 1, frameBlock = repcap.FrameBlock.Default) \n
		(available only for CCK and PBCC transport modes) Sets the PSDU bit rate. \n
			:param brate: integer Range: 0 to 22E6
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(brate)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PSDU:BRATe {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PSDU:BRATe \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.psdu.brate.get(frameBlock = repcap.FrameBlock.Default) \n
		(available only for CCK and PBCC transport modes) Sets the PSDU bit rate. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: brate: integer Range: 0 to 22E6"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PSDU:BRATe?')
		return Conversions.str_to_int(response)
