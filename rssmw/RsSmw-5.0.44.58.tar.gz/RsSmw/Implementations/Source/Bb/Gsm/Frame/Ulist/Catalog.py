from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, frameIx=repcap.FrameIx.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GSM:FRAMe<DI>:ULISt:CATalog \n
		Snippet: value: List[str] = driver.source.bb.gsm.frame.ulist.catalog.get(frameIx = repcap.FrameIx.Default) \n
		This command reads out the files with user defined frame settings in the default directory. The default directory is set
		using command method RsSmw.MassMemory.currentDirectory. Only files with the file extension *.gsm_fu and *.gsm_hfu are
		listed. \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:return: catalog: string"""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:ULISt:CATalog?')
		return Conversions.str_to_str_list(response)
