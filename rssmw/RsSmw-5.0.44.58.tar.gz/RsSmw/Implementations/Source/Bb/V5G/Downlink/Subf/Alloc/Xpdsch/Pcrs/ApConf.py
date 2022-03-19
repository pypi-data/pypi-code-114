from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApConf:
	"""ApConf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apConf", core, parent)

	def set(self, ap_configuration: enums.ApConfAll, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:XPDSch:PCRS:APConf \n
		Snippet: driver.source.bb.v5G.downlink.subf.alloc.xpdsch.pcrs.apConf.set(ap_configuration = enums.ApConfAll.A00, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the antenna ports used by downlink phase compensation reference signal (PCRS) . \n
			:param ap_configuration: A00| A01| A10| A11 A00 DL PCRS not present A01 Antenna port 60 used A10 Antenna port 61 used A11 Antenna ports 60 and 61 used
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(ap_configuration, enums.ApConfAll)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPDSch:PCRS:APConf {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.ApConfAll:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ALLoc<CH0>:XPDSch:PCRS:APConf \n
		Snippet: value: enums.ApConfAll = driver.source.bb.v5G.downlink.subf.alloc.xpdsch.pcrs.apConf.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Specifies the antenna ports used by downlink phase compensation reference signal (PCRS) . \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: ap_configuration: A00| A01| A10| A11 A00 DL PCRS not present A01 Antenna port 60 used A10 Antenna port 61 used A11 Antenna ports 60 and 61 used"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:XPDSch:PCRS:APConf?')
		return Conversions.str_to_scalar_enum(response, enums.ApConfAll)
