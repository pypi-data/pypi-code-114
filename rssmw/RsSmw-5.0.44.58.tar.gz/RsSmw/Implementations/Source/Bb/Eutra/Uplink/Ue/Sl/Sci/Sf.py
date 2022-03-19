from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sf:
	"""Sf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sf", core, parent)

	def get(self, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:SF \n
		Snippet: value: str = driver.source.bb.eutra.uplink.ue.sl.sci.sf.get(userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Queries the subframe numbers of the subframes that can be used for SL transmission. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
			:return: sci_sf: string List of SF numbers, separated by commas"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:SF?')
		return trim_str_response(response)
