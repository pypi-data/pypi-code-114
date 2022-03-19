from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:ULISt:CATalog \n
		Snippet: value: List[str] = driver.source.bb.gsm.frame.slot.subChannel.user.ulist.catalog.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		This command reads out the files with user defined slot settings in the default directory. The default directory is set
		using command method RsSmw.MassMemory.currentDirectory. Only files with the file extension *.gsm_slu and *.gsm_hslu are
		listed. \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: catalog: string"""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:ULISt:CATalog?')
		return Conversions.str_to_str_list(response)
