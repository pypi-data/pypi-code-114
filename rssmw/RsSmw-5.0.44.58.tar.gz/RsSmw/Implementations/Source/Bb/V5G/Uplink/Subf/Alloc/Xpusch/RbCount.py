from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbCount:
	"""RbCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbCount", core, parent)

	def set(self, xpusch_rb_cnt_set_1: float, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SUBF<ST0>:ALLoc<CH0>:XPUSch:RBCount \n
		Snippet: driver.source.bb.v5G.uplink.subf.alloc.xpusch.rbCount.set(xpusch_rb_cnt_set_1 = 1.0, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the size of the selected xPUSCH allocation in resource blocks per slot. \n
			:param xpusch_rb_cnt_set_1: float Range: 4 to 100
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(xpusch_rb_cnt_set_1)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPUSch:RBCount {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:SUBF<ST0>:ALLoc<CH0>:XPUSch:RBCount \n
		Snippet: value: float = driver.source.bb.v5G.uplink.subf.alloc.xpusch.rbCount.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the size of the selected xPUSCH allocation in resource blocks per slot. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: xpusch_rb_cnt_set_1: float Range: 4 to 100"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPUSch:RBCount?')
		return Conversions.str_to_float(response)
