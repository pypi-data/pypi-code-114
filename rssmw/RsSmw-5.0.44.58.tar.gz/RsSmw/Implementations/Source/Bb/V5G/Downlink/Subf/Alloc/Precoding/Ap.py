from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ap:
	"""Ap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ap", core, parent)

	def set(self, antenna_ports: enums.V5GbfaNtSet, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:PRECoding:AP \n
		Snippet: driver.source.bb.v5G.downlink.subf.alloc.precoding.ap.set(antenna_ports = enums.V5GbfaNtSet.AP0, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the antenna port or the pair of antenna ports used by the particular allocation in particular subframe. \n
			:param antenna_ports: AP8_9| AP10_11| AP8_12| AP9_13| AP10_14| AP11_15| AP107_109| AP0| AP1| AP2| AP3| AP4| AP5| AP6| AP7| AP8| AP9| AP10| AP11| AP12| AP13| AP14| AP15| AP107| AP109| AP0_1| AP2_3| AP4_5| AP6_7| AP12_13| AP14_15
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(antenna_ports, enums.V5GbfaNtSet)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PRECoding:AP {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.V5GbfaNtSet:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:PRECoding:AP \n
		Snippet: value: enums.V5GbfaNtSet = driver.source.bb.v5G.downlink.subf.alloc.precoding.ap.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the antenna port or the pair of antenna ports used by the particular allocation in particular subframe. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: antenna_ports: AP8_9| AP10_11| AP8_12| AP9_13| AP10_14| AP11_15| AP107_109| AP0| AP1| AP2| AP3| AP4| AP5| AP6| AP7| AP8| AP9| AP10| AP11| AP12| AP13| AP14| AP15| AP107| AP109| AP0_1| AP2_3| AP4_5| AP6_7| AP12_13| AP14_15"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PRECoding:AP?')
		return Conversions.str_to_scalar_enum(response, enums.V5GbfaNtSet)
