from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset_relative_t: enums.OffsetRelativeAll, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:OFFSet \n
		Snippet: driver.source.bb.nr5G.node.cell.offset.set(offset_relative_t = enums.OffsetRelativeAll.POINta, cellNull = repcap.CellNull.Nr0) \n
		Defines the reference point, relative to which the SS/PBCH is allocated in frequency domain. \n
			:param offset_relative_t: TXBW| POINta TXBW The frequency position of the SS/PBCH is set relative to the usable RBs that apply for the current numerology, i.e. to the start of the TxBWs. POINta The frequency position of the SS/PBCH is set relative to the position of point A.
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(offset_relative_t, enums.OffsetRelativeAll)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:OFFSet {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.OffsetRelativeAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:OFFSet \n
		Snippet: value: enums.OffsetRelativeAll = driver.source.bb.nr5G.node.cell.offset.get(cellNull = repcap.CellNull.Nr0) \n
		Defines the reference point, relative to which the SS/PBCH is allocated in frequency domain. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: offset_relative_t: TXBW| POINta TXBW The frequency position of the SS/PBCH is set relative to the usable RBs that apply for the current numerology, i.e. to the start of the TxBWs. POINta The frequency position of the SS/PBCH is set relative to the position of point A."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:OFFSet?')
		return Conversions.str_to_scalar_enum(response, enums.OffsetRelativeAll)
