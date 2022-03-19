from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConType:
	"""ConType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conType", core, parent)

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.V5GulContentType:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:[SUBF<ST0>]:ALLoc<CH0>:CONType \n
		Snippet: value: enums.V5GulContentType = driver.source.bb.v5G.uplink.subf.alloc.conType.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the content type for the selected allocation. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: content_type: XPUCch| XPUSch"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CONType?')
		return Conversions.str_to_scalar_enum(response, enums.V5GulContentType)
