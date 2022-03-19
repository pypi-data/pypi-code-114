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

	def set(self, ant_port_map_data: float, userIx=repcap.UserIx.Default, layerNull=repcap.LayerNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, row=repcap.Row.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:APM:[LAYer<USER>]:AP<DIR0>:ROW<ST0>:IMAGinary \n
		Snippet: driver.source.bb.v5G.downlink.user.apm.layer.ap.row.imaginary.set(ant_port_map_data = 1.0, userIx = repcap.UserIx.Default, layerNull = repcap.LayerNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, row = repcap.Row.Default) \n
		Defines the mapping of the antenna ports to the physical antennas:
			INTRO_CMD_HELP: Selects the clock source: \n
			- Per user (1 to 4) ,
			- Per layer (1 to 2) ,
			- Per antenna port (8 to 15 and 60, 61, 107, 109) , and
			- Per row selecting baseband (0 to 7) .
		The command specifies imaginary / phase part. \n
			:param ant_port_map_data: float The REAL (magnitude) and IMAGinary (phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to magnitude = 1. Range: -1 to 360
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(ant_port_map_data)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:APM:LAYer{layerNull_cmd_val}:AP{antennaPortNull_cmd_val}:ROW{row_cmd_val}:IMAGinary {param}')

	def get(self, userIx=repcap.UserIx.Default, layerNull=repcap.LayerNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, row=repcap.Row.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:APM:[LAYer<USER>]:AP<DIR0>:ROW<ST0>:IMAGinary \n
		Snippet: value: float = driver.source.bb.v5G.downlink.user.apm.layer.ap.row.imaginary.get(userIx = repcap.UserIx.Default, layerNull = repcap.LayerNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, row = repcap.Row.Default) \n
		Defines the mapping of the antenna ports to the physical antennas:
			INTRO_CMD_HELP: Selects the clock source: \n
			- Per user (1 to 4) ,
			- Per layer (1 to 2) ,
			- Per antenna port (8 to 15 and 60, 61, 107, 109) , and
			- Per row selecting baseband (0 to 7) .
		The command specifies imaginary / phase part. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:return: ant_port_map_data: float The REAL (magnitude) and IMAGinary (phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to magnitude = 1. Range: -1 to 360"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:APM:LAYer{layerNull_cmd_val}:AP{antennaPortNull_cmd_val}:ROW{row_cmd_val}:IMAGinary?')
		return Conversions.str_to_float(response)
