from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbOffset:
	"""RbOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbOffset", core, parent)

	def set(self, content_type: float, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:[SUBF<ST0>]:ALLoc<CH0>:XPUCch:RBOFfset \n
		Snippet: driver.source.bb.v5G.uplink.subf.alloc.xpucch.rbOffset.set(content_type = 1.0, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the xPUCCH resource block offset within the subframe of the selected allocation. \n
			:param content_type: float Range: 0 to 90, Unit: slot
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(content_type)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPUCch:RBOFfset {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:[SUBF<ST0>]:ALLoc<CH0>:XPUCch:RBOFfset \n
		Snippet: value: float = driver.source.bb.v5G.uplink.subf.alloc.xpucch.rbOffset.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the xPUCCH resource block offset within the subframe of the selected allocation. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: content_type: float Range: 0 to 90, Unit: slot"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPUCch:RBOFfset?')
		return Conversions.str_to_float(response)
