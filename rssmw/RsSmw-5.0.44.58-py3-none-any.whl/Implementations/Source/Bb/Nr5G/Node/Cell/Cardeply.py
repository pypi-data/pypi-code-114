from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cardeply:
	"""Cardeply commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cardeply", core, parent)

	def set(self, carrier_depl: enums.Nr5GcarDep, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:CARDeply \n
		Snippet: driver.source.bb.nr5G.node.cell.cardeply.set(carrier_depl = enums.Nr5GcarDep.BT36, cellNull = repcap.CellNull.Nr0) \n
		Selects one of the frequency ranges, specified for 5G NR transmission. \n
			:param carrier_depl: FR1LT3| FR1GT3| FR2
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(carrier_depl, enums.Nr5GcarDep)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:CARDeply {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.Nr5GcarDep:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:CARDeply \n
		Snippet: value: enums.Nr5GcarDep = driver.source.bb.nr5G.node.cell.cardeply.get(cellNull = repcap.CellNull.Nr0) \n
		Selects one of the frequency ranges, specified for 5G NR transmission. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: carrier_depl: FR1LT3| FR1GT3| FR2"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:CARDeply?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5GcarDep)
