from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Til:
	"""Til commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("til", core, parent)

	def set(self, time_inter_mode: enums.Atsc30TimeInterleaverMode, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:TIL \n
		Snippet: driver.source.bb.a3Tsc.plp.til.til.set(time_inter_mode = enums.Atsc30TimeInterleaverMode.CTI, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the time interleaver mode. \n
			:param time_inter_mode: OFF| CTI| HTI
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(time_inter_mode, enums.Atsc30TimeInterleaverMode)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:TIL {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30TimeInterleaverMode:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TIL:TIL \n
		Snippet: value: enums.Atsc30TimeInterleaverMode = driver.source.bb.a3Tsc.plp.til.til.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the time interleaver mode. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: time_inter_mode: OFF| CTI| HTI"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TIL:TIL?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30TimeInterleaverMode)
