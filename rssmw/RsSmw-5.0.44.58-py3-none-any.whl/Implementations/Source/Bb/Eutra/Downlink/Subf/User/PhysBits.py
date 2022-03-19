from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhysBits:
	"""PhysBits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("physBits", core, parent)

	def get(self, subframeNull=repcap.SubframeNull.Default, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:USER<CH>:PHYSbits \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.user.physBits.get(subframeNull = repcap.SubframeNull.Default, userIx = repcap.UserIx.Default) \n
		Queries the size of the selected allocation in bits and considering the subcarriers that are used for other signals or
		channels with higher priority. If a User 1...4 is selected for the 'Data Source' in the allocation table for the
		corresponding allocation, the value of the parameter 'Number of Physical Bits' is the sum of the 'Physical Bits' of all
		single allocations that belong to the same user in the selected subframe. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: physical_bits: integer Range: 0 to 100000"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:USER{userIx_cmd_val}:PHYSbits?')
		return Conversions.str_to_int(response)
