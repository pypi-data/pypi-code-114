from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselection:
	"""Dselection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselection", core, parent)

	def set(self, dselection: str, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DATA:DSELection \n
		Snippet: driver.source.bb.wlnn.fblock.data.dselection.set(dselection = '1', frameBlock = repcap.FrameBlock.Default) \n
		Selects the data list for the DLISt data source selection. The lists are saved as files with the fixed file extensions *.
		dm_iqd in a directory of the user's choice. The directory applicable to the following commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name without the path and the file extension. \n
			:param dselection: string
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.value_to_quoted_str(dselection)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DATA:DSELection {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.wlnn.fblock.data.dselection.get(frameBlock = repcap.FrameBlock.Default) \n
		Selects the data list for the DLISt data source selection. The lists are saved as files with the fixed file extensions *.
		dm_iqd in a directory of the user's choice. The directory applicable to the following commands is defined with the
		command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, you only have to give the file
		name without the path and the file extension. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: dselection: string"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DATA:DSELection?')
		return trim_str_response(response)
