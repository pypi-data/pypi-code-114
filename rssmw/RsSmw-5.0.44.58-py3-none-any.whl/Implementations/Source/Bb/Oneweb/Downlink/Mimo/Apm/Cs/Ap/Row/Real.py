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

	def set(self, ant_port_map_dat: float, antennaPortNull=repcap.AntennaPortNull.Default, row=repcap.Row.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:MIMO:APM:CS:AP<DIR0>:ROW<ST0>:REAL \n
		Snippet: driver.source.bb.oneweb.downlink.mimo.apm.cs.ap.row.real.set(ant_port_map_dat = 1.0, antennaPortNull = repcap.AntennaPortNull.Default, row = repcap.Row.Default) \n
		Define the mapping of the antenna ports to the physical antennas. \n
			:param ant_port_map_dat: 0| 1 (for AP = 0 to 3) ; float (for AP = 4 | 6 | 15 to 46) The mapping of the first four APs AP0|1|2|3 depends on the system configuration as follows: With method RsSmw.Sconfiguration.Baseband.sourceSEParate exactly one single AP can be mapped to a BB. With method RsSmw.Sconfiguration.Baseband.sourceCOUPled|CPENtity none or exactly one single AP can be mapped to a BB. To map an AP, use the command SOURce1:BB:ONEWeb:DL:MIMO:APM:CS:AP0|1|2|3:ROW0|1|2|3:REAL 1. The corresponding ...:CS:AP0|1|2|3:ROW0|1|2|3:IMAG command has no effect. The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 360
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(ant_port_map_dat)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:MIMO:APM:CS:AP{antennaPortNull_cmd_val}:ROW{row_cmd_val}:REAL {param}')

	def get(self, antennaPortNull=repcap.AntennaPortNull.Default, row=repcap.Row.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:MIMO:APM:CS:AP<DIR0>:ROW<ST0>:REAL \n
		Snippet: value: float = driver.source.bb.oneweb.downlink.mimo.apm.cs.ap.row.real.get(antennaPortNull = repcap.AntennaPortNull.Default, row = repcap.Row.Default) \n
		Define the mapping of the antenna ports to the physical antennas. \n
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:return: ant_port_map_dat: 0| 1 (for AP = 0 to 3) ; float (for AP = 4 | 6 | 15 to 46) The mapping of the first four APs AP0|1|2|3 depends on the system configuration as follows: With method RsSmw.Sconfiguration.Baseband.sourceSEParate exactly one single AP can be mapped to a BB. With method RsSmw.Sconfiguration.Baseband.sourceCOUPled|CPENtity none or exactly one single AP can be mapped to a BB. To map an AP, use the command SOURce1:BB:ONEWeb:DL:MIMO:APM:CS:AP0|1|2|3:ROW0|1|2|3:REAL 1. The corresponding ...:CS:AP0|1|2|3:ROW0|1|2|3:IMAG command has no effect. The REAL (Magnitude) and IMAGinary (Phase) values are interdependent. Their value ranges change depending on each other and so that the resulting complex value is as follows: |REAL+j*IMAGinary| ≤ 1 Otherwise, the values are normalized to Magnitude = 1. Range: -1 to 360"""
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:MIMO:APM:CS:AP{antennaPortNull_cmd_val}:ROW{row_cmd_val}:REAL?')
		return Conversions.str_to_float(response)
