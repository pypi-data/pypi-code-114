from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sstream:
	"""Sstream commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sstream", core, parent)

	def set(self, sstream: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SSTReam \n
		Snippet: driver.source.bb.wlnn.fblock.sstream.set(sstream = 1, frameBlock = repcap.FrameBlock.Default) \n
		Sets the number of the spatial streams. For physical mode LEGACY, only value 1 is valid. For Tx Mode 'HT-Duplicate', only
		value 1 is valid. In all other cases, the number of spatial streams depends on the number of antennas configured with
		command SOURce:BB:WLNN:ANTenna:MODE. \n
			:param sstream: integer Range: 1 to 8
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(sstream)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SSTReam {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SSTReam \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.sstream.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the number of the spatial streams. For physical mode LEGACY, only value 1 is valid. For Tx Mode 'HT-Duplicate', only
		value 1 is valid. In all other cases, the number of spatial streams depends on the number of antennas configured with
		command SOURce:BB:WLNN:ANTenna:MODE. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: sstream: integer Range: 1 to 8"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SSTReam?')
		return Conversions.str_to_int(response)
