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

	def set(self, ipart_increment: float, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:STEP:[INCRement] \n
		Snippet: driver.source.iq.output.digital.bbmm.power.step.increment.set(ipart_increment = 1.0, iqConnector = repcap.IqConnector.Default) \n
		Sets the step width. Use this value to vary the digital I/Q output level step-by-step. \n
			:param ipart_increment: float Range: 0 to 80
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.decimal_value_to_str(ipart_increment)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:STEP:INCRement {param}')

	def get(self, iqConnector=repcap.IqConnector.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:STEP:[INCRement] \n
		Snippet: value: float = driver.source.iq.output.digital.bbmm.power.step.increment.get(iqConnector = repcap.IqConnector.Default) \n
		Sets the step width. Use this value to vary the digital I/Q output level step-by-step. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: ipart_increment: No help available"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:STEP:INCRement?')
		return Conversions.str_to_float(response)
