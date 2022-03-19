from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	def set(self, signal: enums.OutpConnBbSignal, tmConnector=repcap.TmConnector.Default) -> None:
		"""SCPI: OUTPut<HW>:TM<CH>:SIGNal \n
		Snippet: driver.output.tm.signal.set(signal = enums.OutpConnBbSignal.BGATA, tmConnector = repcap.TmConnector.Default) \n
		Determines the control signal that is output at the selected connector. To define the connector direction, use the
		command method RsSmw.Output.Tm.Direction.set. \n
			:param signal: MARKA1| MARKA2| MARKA3| SCLA| LATTA| BGATA| HOPA| CWMODA| TRIGA| MARKB1| MARKB2| MARKB3| SCLB| LATTB| BGATB| HOPB| CWMODB| TRIGB| MARKC1| MARKC2| MARKC3| SCLC| LATTC| BGATC| HOPC| CWMODC| TRIGC| MARKD1| MARKD2| MARKD3| SCLD| LATTD| BGATD| HOPD| CWMODD| TRIGD MARKA1|MARKC1|MARKA2|MARKC2|(MARKA3|MARKC3) = Baseband A/C Marker 1/2/(3) SCLA|SCLB|SCLC|SCLD = Symbol Clock A/B/C/D Option: R&S SMW-B10 LATTA|LATTB|LATTC|LATTD = Lev Att A/B/C/D BGATA|BGATB|BGATC|BGATD = Burst Gate A/B/C/D HOPA|HOPB|HOPC|HOPD = HOP A/B/C/D CWMODA|CWMODB|CWMODC|CWMODD = CW/Mod A/B/C/D TRIGA|TRIGB|TRIGC|TRIGD = Triggered A The character A/B/C/D in the parameter value indicates the baseband the signal is related to.
			:param tmConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tm')
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.OutpConnBbSignal)
		tmConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(tmConnector, repcap.TmConnector)
		self._core.io.write(f'OUTPut<HwInstance>:TM{tmConnector_cmd_val}:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self, tmConnector=repcap.TmConnector.Default) -> enums.OutpConnBbSignal:
		"""SCPI: OUTPut<HW>:TM<CH>:SIGNal \n
		Snippet: value: enums.OutpConnBbSignal = driver.output.tm.signal.get(tmConnector = repcap.TmConnector.Default) \n
		Determines the control signal that is output at the selected connector. To define the connector direction, use the
		command method RsSmw.Output.Tm.Direction.set. \n
			:param tmConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tm')
			:return: signal: MARKA1| MARKA2| MARKA3| SCLA| LATTA| BGATA| HOPA| CWMODA| TRIGA| MARKB1| MARKB2| MARKB3| SCLB| LATTB| BGATB| HOPB| CWMODB| TRIGB| MARKC1| MARKC2| MARKC3| SCLC| LATTC| BGATC| HOPC| CWMODC| TRIGC| MARKD1| MARKD2| MARKD3| SCLD| LATTD| BGATD| HOPD| CWMODD| TRIGD MARKA1|MARKC1|MARKA2|MARKC2|(MARKA3|MARKC3) = Baseband A/C Marker 1/2/(3) SCLA|SCLB|SCLC|SCLD = Symbol Clock A/B/C/D Option: R&S SMW-B10 LATTA|LATTB|LATTC|LATTD = Lev Att A/B/C/D BGATA|BGATB|BGATC|BGATD = Burst Gate A/B/C/D HOPA|HOPB|HOPC|HOPD = HOP A/B/C/D CWMODA|CWMODB|CWMODC|CWMODD = CW/Mod A/B/C/D TRIGA|TRIGB|TRIGC|TRIGD = Triggered A The character A/B/C/D in the parameter value indicates the baseband the signal is related to."""
		tmConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(tmConnector, repcap.TmConnector)
		response = self._core.io.query_str(f'OUTPut<HwInstance>:TM{tmConnector_cmd_val}:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.OutpConnBbSignal)
