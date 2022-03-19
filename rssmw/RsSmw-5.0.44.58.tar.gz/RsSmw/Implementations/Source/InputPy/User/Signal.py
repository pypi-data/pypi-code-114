from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	def set(self, signal: enums.InpOutpConnGlbMapSign, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce]:INPut:USER<CH>:SIGNal \n
		Snippet: driver.source.inputPy.user.signal.set(signal = enums.InpOutpConnGlbMapSign.BERCLKIN, userIx = repcap.UserIx.Default) \n
		Determines the control signal that is input at the selected connector. To define the connector direction, use the command
		[:SOURce]:INPut:USER<ch>:DIRection. \n
			:param signal: TRIG1| TRIG2| CLOCK1| CLOCK2| NSEGM1| NSEGM2| NONE| FEEDback| IPULSA| IPULSB| ERRTA| ERRTB | BERDATIN| BERCLKIN| BERDATENIN| BERRESTIN | SYNCIN TRIG1|TRIG2 = Global Trigger 1/2 CLOCK1|CLOCK2 = Global Clock 1/2 NSEGM1|NSEGM2 = Global Next Segment 1/2 IPULSA|IPULSB = Pulse In A/B, available for USER4|5|6 FEEDback = Baseband Feedback, available for USER6 SYNCIN = Baseband Sync In BERDATIN|BERCLKIN|BERDATENIN|BERRESTIN = BER Data, Clock, Data Enable and Restart ERRTA|ERRTB = External restart trigger signals for REG
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.InpOutpConnGlbMapSign)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce:INPut:USER{userIx_cmd_val}:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.InpOutpConnGlbMapSign:
		"""SCPI: [SOURce]:INPut:USER<CH>:SIGNal \n
		Snippet: value: enums.InpOutpConnGlbMapSign = driver.source.inputPy.user.signal.get(userIx = repcap.UserIx.Default) \n
		Determines the control signal that is input at the selected connector. To define the connector direction, use the command
		[:SOURce]:INPut:USER<ch>:DIRection. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: signal: TRIG1| TRIG2| CLOCK1| CLOCK2| NSEGM1| NSEGM2| NONE| FEEDback| IPULSA| IPULSB| ERRTA| ERRTB | BERDATIN| BERCLKIN| BERDATENIN| BERRESTIN | SYNCIN TRIG1|TRIG2 = Global Trigger 1/2 CLOCK1|CLOCK2 = Global Clock 1/2 NSEGM1|NSEGM2 = Global Next Segment 1/2 IPULSA|IPULSB = Pulse In A/B, available for USER4|5|6 FEEDback = Baseband Feedback, available for USER6 SYNCIN = Baseband Sync In BERDATIN|BERCLKIN|BERDATENIN|BERRESTIN = BER Data, Clock, Data Enable and Restart ERRTA|ERRTB = External restart trigger signals for REG"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce:INPut:USER{userIx_cmd_val}:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.InpOutpConnGlbMapSign)
