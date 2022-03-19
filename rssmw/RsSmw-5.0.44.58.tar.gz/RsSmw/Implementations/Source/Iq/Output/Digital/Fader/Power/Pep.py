from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pep:
	"""Pep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pep", core, parent)

	def set(self, pep: float, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:PEP \n
		Snippet: driver.source.iq.output.digital.fader.power.pep.set(pep = 1.0, digitalIq = repcap.DigitalIq.Default) \n
		Enters the peak level of the output signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:param pep: float Range: -80 to 0
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.decimal_value_to_str(pep)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:PEP {param}')

	def get(self, digitalIq=repcap.DigitalIq.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:PEP \n
		Snippet: value: float = driver.source.iq.output.digital.fader.power.pep.get(digitalIq = repcap.DigitalIq.Default) \n
		Enters the peak level of the output signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: pep: float Range: -80 to 0"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:PEP?')
		return Conversions.str_to_float(response)
