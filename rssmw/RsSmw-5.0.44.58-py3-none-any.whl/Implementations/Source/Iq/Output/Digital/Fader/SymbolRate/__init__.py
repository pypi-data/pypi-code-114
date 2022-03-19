from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	@property
	def fifo(self):
		"""fifo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fifo'):
			from .Fifo import Fifo
			self._fifo = Fifo(self._core, self._cmd_group)
		return self._fifo

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	def set(self, srate: float, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:SRATe \n
		Snippet: driver.source.iq.output.digital.fader.symbolRate.set(srate = 1.0, digitalIq = repcap.DigitalIq.Default) \n
		Sets/queries the sample rate of the digital I/Q output signal. \n
			:param srate: float Range: 0.5E6 to depends on options, Unit: Hz The maximum value depends on the installed options as follows: R&S SMW-B10: max = 200E6 and depends on the connected receiving device R&S SMW-B9: max = 250E6 See also 'Supported digital interfaces depending on the system configuration'.
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.decimal_value_to_str(srate)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:SRATe {param}')

	def get(self, digitalIq=repcap.DigitalIq.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:SRATe \n
		Snippet: value: float = driver.source.iq.output.digital.fader.symbolRate.get(digitalIq = repcap.DigitalIq.Default) \n
		Sets/queries the sample rate of the digital I/Q output signal. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: srate: float Range: 0.5E6 to depends on options, Unit: Hz The maximum value depends on the installed options as follows: R&S SMW-B10: max = 200E6 and depends on the connected receiving device R&S SMW-B9: max = 250E6 See also 'Supported digital interfaces depending on the system configuration'."""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SymbolRate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SymbolRate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
