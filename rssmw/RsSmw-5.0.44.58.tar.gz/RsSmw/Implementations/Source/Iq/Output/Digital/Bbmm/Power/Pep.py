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

	def set(self, pep: float, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:PEP \n
		Snippet: driver.source.iq.output.digital.bbmm.power.pep.set(pep = 1.0, iqConnector = repcap.IqConnector.Default) \n
		Enters the peak level of the output signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:param pep: float Range: -80 to 0
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.decimal_value_to_str(pep)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:PEP {param}')

	def get(self, iqConnector=repcap.IqConnector.Default) -> float:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:POWer:PEP \n
		Snippet: value: float = driver.source.iq.output.digital.bbmm.power.pep.get(iqConnector = repcap.IqConnector.Default) \n
		Enters the peak level of the output signal relative to full scale of 0.5 V (in terms of dB full scale) . \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: pep: float Range: -80 to 0"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:POWer:PEP?')
		return Conversions.str_to_float(response)
