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

	def set(self, mode: enums.FreqStepMode, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:STEP:MODE \n
		Snippet: driver.source.iq.output.digital.bbmm.power.step.mode.set(mode = enums.FreqStepMode.DECimal, iqConnector = repcap.IqConnector.Default) \n
		Defines the type of step size to vary the digital output power step-by-step. \n
			:param mode: DECimal| USER DECimal increases or decreases the level in steps of ten. USER increases or decreases the level in increments, determined with the command [:SOURce]:IQ:OUTPut:DIGital:FADerch:POWer:STEP[:INCRement].
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqStepMode)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:STEP:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, iqConnector=repcap.IqConnector.Default) -> enums.FreqStepMode:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:STEP:MODE \n
		Snippet: value: enums.FreqStepMode = driver.source.iq.output.digital.bbmm.power.step.mode.get(iqConnector = repcap.IqConnector.Default) \n
		Defines the type of step size to vary the digital output power step-by-step. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: mode: DECimal| USER DECimal increases or decreases the level in steps of ten. USER increases or decreases the level in increments, determined with the command [:SOURce]:IQ:OUTPut:DIGital:FADerch:POWer:STEP[:INCRement]."""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:STEP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqStepMode)
