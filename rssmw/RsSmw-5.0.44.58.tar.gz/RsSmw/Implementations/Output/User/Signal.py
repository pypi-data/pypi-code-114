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

	def set(self, signal: enums.OutpConnGlbSignal, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: OUTPut<HW>:USER<CH>:SIGNal \n
		Snippet: driver.output.user.signal.set(signal = enums.OutpConnGlbSignal.BERCLKOUT, userIx = repcap.UserIx.Default) \n
		Sets the control signal that is output at the selected connector. To define the connector direction, use the command
		method RsSmw.Output.User.Direction.set. \n
			:param signal: MARKA1| MARKA2| MARKA3| MARKB1| MARKB2| MARKB3| MARKC1| MARKC2| MARKC3| MARKD1| MARKD2| MARKD3| SVALA| SVALB| OPULSA| OPULSB| SYNCA| VIDEOA| VIDEOB| SYNCB| NONE| RTRIGA| RTRIGB| SVALANegated| SVALBNegated| LOW| HIGH| MTRigger | SYNCOUT | BERRESTOUT| BERDATENOUT| BERCLKOUT| BERDATOUT MARKA|B|C|D1|2|3 = Baseband BB Marker 1/2/3 (available marker signals depend on the system configuration, see Table 'Mapping control signals to the USER x connectors') SVALA|SVALB = Signal Valid A/B, available for USER4|5|6 SVALANegated|SVALBNegated = Signal Valid A/B (negative) , available for USER4|5|6 OPULSA|OPULSB = Pulse Out A/B, available for USER4|5|6 SYNCA|SYNCB = Pulse Sync A/B, available for USER4|5|6 VIDEOA|VIDEOB = Pulse Video A/B, available for USER4|5|6 MTRigger = Manual Trigger, available for USER6 RTRIGA|RTRIGB = REG trigger A/B, available for USER4|5 BERRESTOUT|BERDATENOUT|BERCLKOUT|BERDATOUT = BERT TestGen Data, Clock, Data Enable and Restart SYNCOUT = Baseband Sync Out LOW|HIGH = Always 0/1 NONE = none
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.OutpConnGlbSignal)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'OUTPut<HwInstance>:USER{userIx_cmd_val}:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.OutpConnGlbSignal:
		"""SCPI: OUTPut<HW>:USER<CH>:SIGNal \n
		Snippet: value: enums.OutpConnGlbSignal = driver.output.user.signal.get(userIx = repcap.UserIx.Default) \n
		Sets the control signal that is output at the selected connector. To define the connector direction, use the command
		method RsSmw.Output.User.Direction.set. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: signal: MARKA1| MARKA2| MARKA3| MARKB1| MARKB2| MARKB3| MARKC1| MARKC2| MARKC3| MARKD1| MARKD2| MARKD3| SVALA| SVALB| OPULSA| OPULSB| SYNCA| VIDEOA| VIDEOB| SYNCB| NONE| RTRIGA| RTRIGB| SVALANegated| SVALBNegated| LOW| HIGH| MTRigger | SYNCOUT | BERRESTOUT| BERDATENOUT| BERCLKOUT| BERDATOUT MARKA|B|C|D1|2|3 = Baseband BB Marker 1/2/3 (available marker signals depend on the system configuration, see Table 'Mapping control signals to the USER x connectors') SVALA|SVALB = Signal Valid A/B, available for USER4|5|6 SVALANegated|SVALBNegated = Signal Valid A/B (negative) , available for USER4|5|6 OPULSA|OPULSB = Pulse Out A/B, available for USER4|5|6 SYNCA|SYNCB = Pulse Sync A/B, available for USER4|5|6 VIDEOA|VIDEOB = Pulse Video A/B, available for USER4|5|6 MTRigger = Manual Trigger, available for USER6 RTRIGA|RTRIGB = REG trigger A/B, available for USER4|5 BERRESTOUT|BERDATENOUT|BERCLKOUT|BERDATOUT = BERT TestGen Data, Clock, Data Enable and Restart SYNCOUT = Baseband Sync Out LOW|HIGH = Always 0/1 NONE = none"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'OUTPut<HwInstance>:USER{userIx_cmd_val}:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.OutpConnGlbSignal)
