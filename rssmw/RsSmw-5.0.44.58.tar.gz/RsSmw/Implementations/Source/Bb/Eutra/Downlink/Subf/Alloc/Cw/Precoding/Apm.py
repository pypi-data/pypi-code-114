from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apm:
	"""Apm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apm", core, parent)

	def set(self, ant_port_map: enums.BfapMapMode, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, codeword=repcap.Codeword.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ALLoc<CH0>:[CW<USER>]:PRECoding:APM \n
		Snippet: driver.source.bb.eutra.downlink.subf.alloc.cw.precoding.apm.set(ant_port_map = enums.BfapMapMode.CB, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, codeword = repcap.Codeword.Default) \n
		Sets the way that the logical antenna ports are mapped to the physical Tx-antennas. See 'DL antenna port mapping
		settings'. \n
			:param ant_port_map: CB| RCB| FW CB = codebook RCB = random codebook FW = fixed weights
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codeword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cw')
		"""
		param = Conversions.enum_scalar_to_str(ant_port_map, enums.BfapMapMode)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		codeword_cmd_val = self._cmd_group.get_repcap_cmd_value(codeword, repcap.Codeword)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CW{codeword_cmd_val}:PRECoding:APM {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, codeword=repcap.Codeword.Default) -> enums.BfapMapMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ALLoc<CH0>:[CW<USER>]:PRECoding:APM \n
		Snippet: value: enums.BfapMapMode = driver.source.bb.eutra.downlink.subf.alloc.cw.precoding.apm.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, codeword = repcap.Codeword.Default) \n
		Sets the way that the logical antenna ports are mapped to the physical Tx-antennas. See 'DL antenna port mapping
		settings'. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codeword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cw')
			:return: ant_port_map: CB| RCB| FW CB = codebook RCB = random codebook FW = fixed weights"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		codeword_cmd_val = self._cmd_group.get_repcap_cmd_value(codeword, repcap.Codeword)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CW{codeword_cmd_val}:PRECoding:APM?')
		return Conversions.str_to_scalar_enum(response, enums.BfapMapMode)
