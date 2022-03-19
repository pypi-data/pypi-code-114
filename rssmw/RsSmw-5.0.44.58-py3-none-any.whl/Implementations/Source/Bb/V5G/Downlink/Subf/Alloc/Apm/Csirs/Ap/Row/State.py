from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:APM:CSIRs:AP<GR0>:ROW<USER>:STATe \n
		Snippet: driver.source.bb.v5G.downlink.subf.alloc.apm.csirs.ap.row.state.set(state = False, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, rowNull = repcap.RowNull.Default) \n
		Specifies, which antenna ports are used for CSI-RS. \n
			:param state: 1| ON| 0| OFF
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.bool_to_str(state)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:APM:CSIRs:AP{antennaPortNull_cmd_val}:ROW{rowNull_cmd_val}:STATe {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, rowNull=repcap.RowNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:APM:CSIRs:AP<GR0>:ROW<USER>:STATe \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.subf.alloc.apm.csirs.ap.row.state.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, rowNull = repcap.RowNull.Default) \n
		Specifies, which antenna ports are used for CSI-RS. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: state: 1| ON| 0| OFF"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:APM:CSIRs:AP{antennaPortNull_cmd_val}:ROW{rowNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
