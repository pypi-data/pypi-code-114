from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qcomponent:
	"""Qcomponent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qcomponent", core, parent)

	def set(self, qpart: float, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:IQOutput<CH>:LEAKage:Q \n
		Snippet: driver.source.bb.impairment.iqOutput.leakage.qcomponent.set(qpart = 1.0, iqConnector = repcap.IqConnector.Default) \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:param qpart: float Range: -10 to 10
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IqOutput')
		"""
		param = Conversions.decimal_value_to_str(qpart)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:BB:IMPairment:IQOutput{iqConnector_cmd_val}:LEAKage:Q {param}')

	def get(self, iqConnector=repcap.IqConnector.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:IQOutput<CH>:LEAKage:Q \n
		Snippet: value: float = driver.source.bb.impairment.iqOutput.leakage.qcomponent.get(iqConnector = repcap.IqConnector.Default) \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IqOutput')
			:return: qpart: No help available"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:IQOutput{iqConnector_cmd_val}:LEAKage:Q?')
		return Conversions.str_to_float(response)
