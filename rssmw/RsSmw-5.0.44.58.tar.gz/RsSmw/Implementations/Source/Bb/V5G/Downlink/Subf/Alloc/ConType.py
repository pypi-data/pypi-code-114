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

	def set(self, con_type: enums.V5GdlContentType, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:CONType \n
		Snippet: driver.source.bb.v5G.downlink.subf.alloc.conType.set(con_type = enums.V5GdlContentType.CSI, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the connection type for the selected allocation. xPBCH can be configured in subframe 0 or 25 only. All other
		content types can be configured in the remaining subframes only. \n
			:param con_type: XPDSch| XPBCh| XPDCch| CSI
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(con_type, enums.V5GdlContentType)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CONType {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.V5GdlContentType:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:CONType \n
		Snippet: value: enums.V5GdlContentType = driver.source.bb.v5G.downlink.subf.alloc.conType.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the connection type for the selected allocation. xPBCH can be configured in subframe 0 or 25 only. All other
		content types can be configured in the remaining subframes only. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: con_type: XPDSch| XPBCh| XPDCch| CSI"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CONType?')
		return Conversions.str_to_scalar_enum(response, enums.V5GdlContentType)
