from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:STATe \n
		Snippet: driver.source.iq.output.digital.fader.state.set(state = False, digitalIq = repcap.DigitalIq.Default) \n
		Activates the digital I/Q signal output. \n
			:param state: 1| ON| 0| OFF
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.bool_to_str(state)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:STATe {param}')

	def get(self, digitalIq=repcap.DigitalIq.Default) -> bool:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:STATe \n
		Snippet: value: bool = driver.source.iq.output.digital.fader.state.get(digitalIq = repcap.DigitalIq.Default) \n
		Activates the digital I/Q signal output. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: state: 1| ON| 0| OFF"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
