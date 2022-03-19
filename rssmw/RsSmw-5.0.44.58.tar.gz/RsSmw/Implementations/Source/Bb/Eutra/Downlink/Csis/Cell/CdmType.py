from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdmType:
	"""CdmType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdmType", core, parent)

	def set(self, cdm_type: enums.EutraCsiRsCdmType, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:CDMType \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.cdmType.set(cdm_type = enums.EutraCsiRsCdmType._2, cellNull = repcap.CellNull.Default) \n
		Sets the higher-level parameter CDMType that influence the antenna port mapping of the CSI-RS. \n
			:param cdm_type: 2| 4| 8
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(cdm_type, enums.EutraCsiRsCdmType)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:CDMType {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.EutraCsiRsCdmType:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:CDMType \n
		Snippet: value: enums.EutraCsiRsCdmType = driver.source.bb.eutra.downlink.csis.cell.cdmType.get(cellNull = repcap.CellNull.Default) \n
		Sets the higher-level parameter CDMType that influence the antenna port mapping of the CSI-RS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: cdm_type: 2| 4| 8"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:CDMType?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCsiRsCdmType)
