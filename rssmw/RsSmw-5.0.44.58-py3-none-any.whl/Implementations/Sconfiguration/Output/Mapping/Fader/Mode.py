from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.SystConfOutpMapMatMode, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:FADer<CH>:MODE \n
		Snippet: driver.sconfiguration.output.mapping.fader.mode.set(mode = enums.SystConfOutpMapMatMode.ADD, digitalIq = repcap.DigitalIq.Default) \n
		Enables routing of multiple streams to the same output physical connector and defines the way the streams are internally
		processed. \n
			:param mode: SINGle| ADD| MULTiplex ADD enabled for the RF, I/Q OUT and BBMM outputs MULTiplex enabled for the BBMM outputs and method RsSmw.Sconfiguration.Output.modeDIGMux
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SystConfOutpMapMatMode)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:FADer{digitalIq_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, digitalIq=repcap.DigitalIq.Default) -> enums.SystConfOutpMapMatMode:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:FADer<CH>:MODE \n
		Snippet: value: enums.SystConfOutpMapMatMode = driver.sconfiguration.output.mapping.fader.mode.get(digitalIq = repcap.DigitalIq.Default) \n
		Enables routing of multiple streams to the same output physical connector and defines the way the streams are internally
		processed. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: mode: SINGle| ADD| MULTiplex ADD enabled for the RF, I/Q OUT and BBMM outputs MULTiplex enabled for the BBMM outputs and method RsSmw.Sconfiguration.Output.modeDIGMux"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SCONfiguration:OUTPut:MAPPing:FADer{digitalIq_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfOutpMapMatMode)
