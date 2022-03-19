from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Via:
	"""Via commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("via", core, parent)

	def set(self, via: enums.IqOutDispViaType, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:VIA \n
		Snippet: driver.source.iq.output.digital.fader.power.via.set(via = enums.IqOutDispViaType.LEVel, digitalIq = repcap.DigitalIq.Default) \n
		No command help available \n
			:param via: PEP| LEVel
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.enum_scalar_to_str(via, enums.IqOutDispViaType)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:VIA {param}')

	# noinspection PyTypeChecker
	def get(self, digitalIq=repcap.DigitalIq.Default) -> enums.IqOutDispViaType:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:POWer:VIA \n
		Snippet: value: enums.IqOutDispViaType = driver.source.iq.output.digital.fader.power.via.get(digitalIq = repcap.DigitalIq.Default) \n
		No command help available \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: via: PEP| LEVel"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:POWer:VIA?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutDispViaType)
