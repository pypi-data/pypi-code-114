from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Periodicity:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, drs_periodicity: enums.DsPeriod, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:PERiodicity \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.periodicity.set(drs_periodicity = enums.DsPeriod.P160, cellNull = repcap.CellNull.Default) \n
		Sets the DRS periodictity. \n
			:param drs_periodicity: P40| P80| P160
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(drs_periodicity, enums.DsPeriod)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:PERiodicity {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.DsPeriod:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:PERiodicity \n
		Snippet: value: enums.DsPeriod = driver.source.bb.eutra.downlink.drs.cell.periodicity.get(cellNull = repcap.CellNull.Default) \n
		Sets the DRS periodictity. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: drs_periodicity: P40| P80| P160"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:PERiodicity?')
		return Conversions.str_to_scalar_enum(response, enums.DsPeriod)
