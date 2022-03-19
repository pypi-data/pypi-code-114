from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FecType:
	"""FecType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fecType", core, parent)

	def set(self, fec_type: enums.Atsc30FecType, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:FECType \n
		Snippet: driver.source.bb.a3Tsc.plp.fecType.set(fec_type = enums.Atsc30FecType.B16K, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the forward error correction (FEC) used for encoding. The table below illustrates types and coding.
			Table Header: <FEC Type> / Outer code / Inner code \n
			- B16K / 16200 bits
			- B64K / BCH / 64800 bits LDPC
			- C16K / 16200 bits LDPC
			- C64K / CRC / 64800 bits LDPC
			- O16K / None / 16200 bits LDPC
			- O64K / None / 64800 bits LDPC \n
			:param fec_type: B16K| B64K| C16K| C64K| O16K| O64K
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(fec_type, enums.Atsc30FecType)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:FECType {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30FecType:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:FECType \n
		Snippet: value: enums.Atsc30FecType = driver.source.bb.a3Tsc.plp.fecType.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the forward error correction (FEC) used for encoding. The table below illustrates types and coding.
			Table Header: <FEC Type> / Outer code / Inner code \n
			- B16K / 16200 bits
			- B64K / BCH / 64800 bits LDPC
			- C16K / 16200 bits LDPC
			- C64K / CRC / 64800 bits LDPC
			- O16K / None / 16200 bits LDPC
			- O64K / None / 64800 bits LDPC \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: fec_type: B16K| B64K| C16K| C64K| O16K| O64K"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:FECType?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30FecType)
