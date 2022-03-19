from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interface:
	"""Interface commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interface", core, parent)

	def set(self, bbout_interf_mode: enums.BbinInterfaceMode, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:INTerface \n
		Snippet: driver.source.iq.output.digital.fader.interface.set(bbout_interf_mode = enums.BbinInterfaceMode.DIGital, digitalIq = repcap.DigitalIq.Default) \n
		Selects the connector for output of the digital IQ signal. \n
			:param bbout_interf_mode: DIGital| HSDin DIGital DIG I/Q HSDin HS DIG I/Q
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		param = Conversions.enum_scalar_to_str(bbout_interf_mode, enums.BbinInterfaceMode)
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:INTerface {param}')

	# noinspection PyTypeChecker
	def get(self, digitalIq=repcap.DigitalIq.Default) -> enums.BbinInterfaceMode:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:INTerface \n
		Snippet: value: enums.BbinInterfaceMode = driver.source.iq.output.digital.fader.interface.get(digitalIq = repcap.DigitalIq.Default) \n
		Selects the connector for output of the digital IQ signal. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: bbout_interf_mode: DIGital| HSDin DIGital DIG I/Q HSDin HS DIG I/Q"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:INTerface?')
		return Conversions.str_to_scalar_enum(response, enums.BbinInterfaceMode)
