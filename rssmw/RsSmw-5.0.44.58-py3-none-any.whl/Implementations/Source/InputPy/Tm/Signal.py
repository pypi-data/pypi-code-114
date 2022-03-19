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

	def set(self, signal: enums.InpConnBbSignal, tmConnector=repcap.TmConnector.Default) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TM<CH>:SIGNal \n
		Snippet: driver.source.inputPy.tm.signal.set(signal = enums.InpConnBbSignal.CLOCk, tmConnector = repcap.TmConnector.Default) \n
		Determines the control signal that is input at the selected connector. To define the connector direction, use the command
		[:SOURce<hw>]:INPut:TM<ch>:DIRection. \n
			:param signal: TRIGger| CLOCk| FEEDback| DATA CLOCk is available only for TM1 DATA is available only for TM2 (default if custom digital modulation with external serial data is used) FEEDback is available only for TM3 (R&S SMW-B10) /TM2 (R&S SMW-B9)
			:param tmConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tm')
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.InpConnBbSignal)
		tmConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(tmConnector, repcap.TmConnector)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TM{tmConnector_cmd_val}:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self, tmConnector=repcap.TmConnector.Default) -> enums.InpConnBbSignal:
		"""SCPI: [SOURce<HW>]:INPut:TM<CH>:SIGNal \n
		Snippet: value: enums.InpConnBbSignal = driver.source.inputPy.tm.signal.get(tmConnector = repcap.TmConnector.Default) \n
		Determines the control signal that is input at the selected connector. To define the connector direction, use the command
		[:SOURce<hw>]:INPut:TM<ch>:DIRection. \n
			:param tmConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tm')
			:return: signal: TRIGger| CLOCk| FEEDback| DATA CLOCk is available only for TM1 DATA is available only for TM2 (default if custom digital modulation with external serial data is used) FEEDback is available only for TM3 (R&S SMW-B10) /TM2 (R&S SMW-B9)"""
		tmConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(tmConnector, repcap.TmConnector)
		response = self._core.io.query_str(f'SOURce<HwInstance>:INPut:TM{tmConnector_cmd_val}:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.InpConnBbSignal)
