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

	def set(self, coderate: enums.Dvbt2BicmCoderate, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:RATE \n
		Snippet: driver.source.bb.t2Dvb.plp.rate.set(coderate = enums.Dvbt2BicmCoderate.R1_2, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the code rate. \n
			:param coderate: R1_2| R3_5| R2_3| R3_4| R4_5| R5_6| R1_3| R2_5
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(coderate, enums.Dvbt2BicmCoderate)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:RATE {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Dvbt2BicmCoderate:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:RATE \n
		Snippet: value: enums.Dvbt2BicmCoderate = driver.source.bb.t2Dvb.plp.rate.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the code rate. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: coderate: R1_2| R3_5| R2_3| R3_4| R4_5| R5_6| R1_3| R2_5"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2BicmCoderate)
