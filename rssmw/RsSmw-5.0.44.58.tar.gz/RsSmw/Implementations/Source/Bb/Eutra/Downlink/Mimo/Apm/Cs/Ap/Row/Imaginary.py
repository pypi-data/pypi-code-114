from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Imaginary:
	"""Imaginary commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imaginary", core, parent)

	def set(self, ant_port_map_dat: float, antennaPortNull=repcap.AntennaPortNull.Default, row=repcap.Row.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MIMO:APM:CS:AP<DIR0>:ROW<ST0>:IMAGinary \n
		Snippet: driver.source.bb.eutra.downlink.mimo.apm.cs.ap.row.imaginary.set(ant_port_map_dat = 1.0, antennaPortNull = repcap.AntennaPortNull.Default, row = repcap.Row.Default) \n
		Define the mapping of the antenna ports to the physical antennas. \n
			:param ant_port_map_dat: float The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 360
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(ant_port_map_dat)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MIMO:APM:CS:AP{antennaPortNull_cmd_val}:ROW{row_cmd_val}:IMAGinary {param}')

	def get(self, antennaPortNull=repcap.AntennaPortNull.Default, row=repcap.Row.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MIMO:APM:CS:AP<DIR0>:ROW<ST0>:IMAGinary \n
		Snippet: value: float = driver.source.bb.eutra.downlink.mimo.apm.cs.ap.row.imaginary.get(antennaPortNull = repcap.AntennaPortNull.Default, row = repcap.Row.Default) \n
		Define the mapping of the antenna ports to the physical antennas. \n
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:return: ant_port_map_dat: float The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 360"""
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MIMO:APM:CS:AP{antennaPortNull_cmd_val}:ROW{row_cmd_val}:IMAGinary?')
		return Conversions.str_to_float(response)
