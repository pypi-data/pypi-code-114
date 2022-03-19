from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	# noinspection PyTypeChecker
	def get(self, digitalIq=repcap.DigitalIq.Default) -> enums.SampRateFifoStatus:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:SRATe:FIFO:[STATus] \n
		Snippet: value: enums.SampRateFifoStatus = driver.source.iq.output.digital.fader.symbolRate.fifo.status.get(digitalIq = repcap.DigitalIq.Default) \n
		No command help available \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:return: status: No help available"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:SRATe:FIFO:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.SampRateFifoStatus)
