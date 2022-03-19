from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pon:
	"""Pon commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pon", core, parent)

	def set(self, pon: enums.UnchOff, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:PON \n
		Snippet: driver.source.iq.output.digital.fader.pon.set(pon = enums.UnchOff.OFF, digitalIq = repcap.DigitalIq.Default) \n
		Sets the power-on state of the selected digital I/Q output. \n
			:param pon: OFF| UNCHanged
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.enum_scalar_to_str(pon, enums.UnchOff)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:PON {param}')

	# noinspection PyTypeChecker
	def get(self, digitalIq=repcap.DigitalIq.Default) -> enums.UnchOff:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:PON \n
		Snippet: value: enums.UnchOff = driver.source.iq.output.digital.fader.pon.get(digitalIq = repcap.DigitalIq.Default) \n
		Sets the power-on state of the selected digital I/Q output. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: pon: OFF| UNCHanged"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:PON?')
		return Conversions.str_to_scalar_enum(response, enums.UnchOff)
