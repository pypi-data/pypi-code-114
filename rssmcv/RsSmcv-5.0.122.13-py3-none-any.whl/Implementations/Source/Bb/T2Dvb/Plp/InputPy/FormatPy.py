from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.Dvbt2PlpInputFormat, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:INPut:FORMat \n
		Snippet: driver.source.bb.t2Dvb.plp.inputPy.formatPy.set(format_py = enums.Dvbt2PlpInputFormat.GCS, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the input format of each PLP <num> for all input sources. \n
			:param format_py: GFPS| GCS| GSE| TS GFPS Generic fixed-length packetized stream GCS Generic continuous stream GSE Generic stream encapsulation TS Transport stream
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.Dvbt2PlpInputFormat)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:INPut:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Dvbt2PlpInputFormat:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:INPut:FORMat \n
		Snippet: value: enums.Dvbt2PlpInputFormat = driver.source.bb.t2Dvb.plp.inputPy.formatPy.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the input format of each PLP <num> for all input sources. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: format_py: GFPS| GCS| GSE| TS GFPS Generic fixed-length packetized stream GCS Generic continuous stream GSE Generic stream encapsulation TS Transport stream"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2PlpInputFormat)
