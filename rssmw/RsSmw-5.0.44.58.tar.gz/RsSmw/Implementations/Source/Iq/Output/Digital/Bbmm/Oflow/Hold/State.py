from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, iqConnector=repcap.IqConnector.Default) -> bool:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:OFLow:HOLD:STATe \n
		Snippet: value: bool = driver.source.iq.output.digital.bbmm.oflow.hold.state.get(iqConnector = repcap.IqConnector.Default) \n
		Queries an overload since last reset for evaluating the measurement. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: state: 1| ON| 0| OFF"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:OFLow:HOLD:STATe?')
		return Conversions.str_to_bool(response)
