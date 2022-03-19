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
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:USER<CH>:PHYSbits \n
		Snippet: value: int = driver.source.bb.v5G.downlink.subf.user.physBits.get(subframeNull = repcap.SubframeNull.Default, userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: physical_bits: No help available"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:USER{userIx_cmd_val}:PHYSbits?')
		return Conversions.str_to_int(response)
