from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data: enums.V5GdlDataSourceUser, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:DATA \n
		Snippet: driver.source.bb.v5G.downlink.subf.alloc.data.set(data = enums.V5GdlDataSourceUser.DLISt, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the data source for the selected allocation. \n
			:param data: MIB| XPDCch USERx Assign a user to the xPDSCH allocation. Specify the data source of the user via: [:SOURcehw]:BB:V5G:DL:USERch:DATA MIB (Result parameter) Indicates that the xPBCH transmits master information blocks. XPDCch (Result parameter) Indicates the connection type xPDCCH.
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.V5GdlDataSourceUser)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.V5GdlDataSourceUser:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:DATA \n
		Snippet: value: enums.V5GdlDataSourceUser = driver.source.bb.v5G.downlink.subf.alloc.data.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the data source for the selected allocation. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: data: MIB| XPDCch USERx Assign a user to the xPDSCH allocation. Specify the data source of the user via: [:SOURcehw]:BB:V5G:DL:USERch:DATA MIB (Result parameter) Indicates that the xPBCH transmits master information blocks. XPDCch (Result parameter) Indicates the connection type xPDCCH."""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.V5GdlDataSourceUser)
