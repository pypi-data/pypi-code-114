from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icomponent:
	"""Icomponent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icomponent", core, parent)

	def set(self, ipart: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:LEAKage:I \n
		Snippet: driver.source.bb.impairment.rf.leakage.icomponent.set(ipart = 1.0, path = repcap.Path.Default) \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:param ipart: float Range: -10 to 10
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(ipart)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce:BB:IMPairment:RF{path_cmd_val}:LEAKage:I {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:LEAKage:I \n
		Snippet: value: float = driver.source.bb.impairment.rf.leakage.icomponent.get(path = repcap.Path.Default) \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: ipart: No help available"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:RF{path_cmd_val}:LEAKage:I?')
		return Conversions.str_to_float(response)
