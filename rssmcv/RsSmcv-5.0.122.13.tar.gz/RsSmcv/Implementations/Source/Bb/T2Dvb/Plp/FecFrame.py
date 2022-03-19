from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FecFrame:
	"""FecFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fecFrame", core, parent)

	def set(self, np_fec_frame: enums.BicmFecFrame, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:FECFrame \n
		Snippet: driver.source.bb.t2Dvb.plp.fecFrame.set(np_fec_frame = enums.BicmFecFrame.NORMal, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the FEC frame. \n
			:param np_fec_frame: NORMal| SHORt NORMal NLDPC = 64800 SHORt NLDPC = 16200
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(np_fec_frame, enums.BicmFecFrame)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:FECFrame {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.BicmFecFrame:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:FECFrame \n
		Snippet: value: enums.BicmFecFrame = driver.source.bb.t2Dvb.plp.fecFrame.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the FEC frame. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: np_fec_frame: NORMal| SHORt NORMal NLDPC = 64800 SHORt NLDPC = 16200"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:FECFrame?')
		return Conversions.str_to_scalar_enum(response, enums.BicmFecFrame)
