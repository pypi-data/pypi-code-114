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

	def set(self, signal: enums.InpOutpConnGlbMapSignb, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce]:INPut:USER<CH>:SIGNal \n
		Snippet: driver.source.inputPy.user.signal.set(signal = enums.InpOutpConnGlbMapSignb.CLOCK1, userIx = repcap.UserIx.Default) \n
		Determines the control signal that is input at the selected connector. To define the connector direction, use the command
		[:SOURce]:INPut:USER<ch>:DIRection. \n
			:param signal: TRIG1| NSEGM1| INST| TS| ETI| SDIF| PPS TRIG1 Global trigger input signal available at 'User 1/2' connector NSEGM1 Input global next segment for triggering of multi-segment waveform files. The signal is available at 'User 1/2' connector. INST Internal instrument trigger signal available at 'User 1/2' connector. TS Transport stream (TS) input signal available at 'User 1' connector only ETI Ensemble transport interface input signal compatible with DAB/T-DMB ETSI standard. The signal is available at 'User 1' connector only. SDIF S/PDIF input signal available at 'User 1' connector only PPS 1PPS (one pulse per second) input signal available at 'User 2' connector only
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.InpOutpConnGlbMapSignb)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce:INPut:USER{userIx_cmd_val}:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.InpOutpConnGlbMapSignb:
		"""SCPI: [SOURce]:INPut:USER<CH>:SIGNal \n
		Snippet: value: enums.InpOutpConnGlbMapSignb = driver.source.inputPy.user.signal.get(userIx = repcap.UserIx.Default) \n
		Determines the control signal that is input at the selected connector. To define the connector direction, use the command
		[:SOURce]:INPut:USER<ch>:DIRection. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: signal: TRIG1| NSEGM1| INST| TS| ETI| SDIF| PPS TRIG1 Global trigger input signal available at 'User 1/2' connector NSEGM1 Input global next segment for triggering of multi-segment waveform files. The signal is available at 'User 1/2' connector. INST Internal instrument trigger signal available at 'User 1/2' connector. TS Transport stream (TS) input signal available at 'User 1' connector only ETI Ensemble transport interface input signal compatible with DAB/T-DMB ETSI standard. The signal is available at 'User 1' connector only. SDIF S/PDIF input signal available at 'User 1' connector only PPS 1PPS (one pulse per second) input signal available at 'User 2' connector only"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce:INPut:USER{userIx_cmd_val}:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.InpOutpConnGlbMapSignb)
