from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Real:
	"""Real commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("real", core, parent)

	def set(self, ant_port_map_data: float, userIx=repcap.UserIx.Default, layerNull=repcap.LayerNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, basebandNull=repcap.BasebandNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:APM:[LAYer<USER>]:AP<DIR0>:BB<ST0>:REAL \n
		Snippet: driver.source.bb.eutra.downlink.user.apm.layer.ap.bb.real.set(ant_port_map_data = 1.0, userIx = repcap.UserIx.Default, layerNull = repcap.LayerNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, basebandNull = repcap.BasebandNull.Default) \n
		Defines the mapping of the antenna ports to the physical antennas. \n
			:param ant_port_map_data: float The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 360
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param basebandNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bb')
		"""
		param = Conversions.decimal_value_to_str(ant_port_map_data)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		basebandNull_cmd_val = self._cmd_group.get_repcap_cmd_value(basebandNull, repcap.BasebandNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:APM:LAYer{layerNull_cmd_val}:AP{antennaPortNull_cmd_val}:BB{basebandNull_cmd_val}:REAL {param}')

	def get(self, userIx=repcap.UserIx.Default, layerNull=repcap.LayerNull.Default, antennaPortNull=repcap.AntennaPortNull.Default, basebandNull=repcap.BasebandNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:APM:[LAYer<USER>]:AP<DIR0>:BB<ST0>:REAL \n
		Snippet: value: float = driver.source.bb.eutra.downlink.user.apm.layer.ap.bb.real.get(userIx = repcap.UserIx.Default, layerNull = repcap.LayerNull.Default, antennaPortNull = repcap.AntennaPortNull.Default, basebandNull = repcap.BasebandNull.Default) \n
		Defines the mapping of the antenna ports to the physical antennas. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param basebandNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bb')
			:return: ant_port_map_data: float The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 360"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		basebandNull_cmd_val = self._cmd_group.get_repcap_cmd_value(basebandNull, repcap.BasebandNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:APM:LAYer{layerNull_cmd_val}:AP{antennaPortNull_cmd_val}:BB{basebandNull_cmd_val}:REAL?')
		return Conversions.str_to_float(response)
