from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Increment:
	"""Increment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("increment", core, parent)

	def set(self, ipart_increment: float, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:STEP:[INCRement] \n
		Snippet: driver.source.iq.output.digital.fader.power.step.increment.set(ipart_increment = 1.0, digitalIq = repcap.DigitalIq.Default) \n
		Sets the step width. Use this value to vary the digital I/Q output level step-by-step. \n
			:param ipart_increment: float Range: 0 to 80
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.decimal_value_to_str(ipart_increment)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:STEP:INCRement {param}')

	def get(self, digitalIq=repcap.DigitalIq.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:STEP:[INCRement] \n
		Snippet: value: float = driver.source.iq.output.digital.fader.power.step.increment.get(digitalIq = repcap.DigitalIq.Default) \n
		Sets the step width. Use this value to vary the digital I/Q output level step-by-step. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: ipart_increment: No help available"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:STEP:INCRement?')
		return Conversions.str_to_float(response)
