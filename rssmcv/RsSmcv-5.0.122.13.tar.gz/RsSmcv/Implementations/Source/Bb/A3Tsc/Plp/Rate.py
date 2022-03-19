from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def set(self, coderate: enums.Atsc30Coderate, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:RATE \n
		Snippet: driver.source.bb.a3Tsc.plp.rate.set(coderate = enums.Atsc30Coderate.R10_15, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the code rate. \n
			:param coderate: R2_15| R3_15| R4_15| R5_15| R6_15| R7_15| R8_15| R9_15| R10_15| R11_15| R12_15| R13_15
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(coderate, enums.Atsc30Coderate)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:RATE {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30Coderate:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:RATE \n
		Snippet: value: enums.Atsc30Coderate = driver.source.bb.a3Tsc.plp.rate.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the code rate. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: coderate: R2_15| R3_15| R4_15| R5_15| R6_15| R7_15| R8_15| R9_15| R10_15| R11_15| R12_15| R13_15"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30Coderate)
