from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncfg:
	"""Ncfg commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncfg", core, parent)

	def set(self, number_of_configs: enums.EutraCsiRsNumCfg, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:NCFG \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.ncfg.set(number_of_configs = enums.EutraCsiRsNumCfg._1, cellNull = repcap.CellNull.Default) \n
		Sets the number of CSI-RS configurations. \n
			:param number_of_configs: 1| 2| 3| 4| 5| 7
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(number_of_configs, enums.EutraCsiRsNumCfg)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:NCFG {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.EutraCsiRsNumCfg:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:NCFG \n
		Snippet: value: enums.EutraCsiRsNumCfg = driver.source.bb.eutra.downlink.csis.cell.ncfg.get(cellNull = repcap.CellNull.Default) \n
		Sets the number of CSI-RS configurations. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: number_of_configs: 1| 2| 3| 4| 5| 7"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:NCFG?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCsiRsNumCfg)
