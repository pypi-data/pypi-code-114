from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.FreqStepMode, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:STEP:MODE \n
		Snippet: driver.source.iq.output.digital.fader.power.step.mode.set(mode = enums.FreqStepMode.DECimal, digitalIq = repcap.DigitalIq.Default) \n
		Defines the type of step size to vary the digital output power step-by-step. \n
			:param mode: DECimal| USER DECimal increases or decreases the level in steps of ten. USER increases or decreases the level in increments, determined with the command [:SOURce]:IQ:OUTPut:DIGital:FADerch:POWer:STEP[:INCRement].
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqStepMode)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:STEP:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, digitalIq=repcap.DigitalIq.Default) -> enums.FreqStepMode:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:STEP:MODE \n
		Snippet: value: enums.FreqStepMode = driver.source.iq.output.digital.fader.power.step.mode.get(digitalIq = repcap.DigitalIq.Default) \n
		Defines the type of step size to vary the digital output power step-by-step. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: mode: DECimal| USER DECimal increases or decreases the level in steps of ten. USER increases or decreases the level in increments, determined with the command [:SOURce]:IQ:OUTPut:DIGital:FADerch:POWer:STEP[:INCRement]."""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:STEP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqStepMode)
