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
	def get(self, iqConnector=repcap.IqConnector.Default) -> enums.SampRateFifoStatus:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:SRATe:FIFO:[STATus] \n
		Snippet: value: enums.SampRateFifoStatus = driver.source.iq.output.digital.bbmm.symbolRate.fifo.status.get(iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: status: No help available"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:SRATe:FIFO:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.SampRateFifoStatus)
