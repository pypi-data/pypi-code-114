from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Skew:
	"""Skew commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("skew", core, parent)

	def set(self, skew: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:SKEW \n
		Snippet: driver.source.bb.impairment.rf.skew.set(skew = 1.0, path = repcap.Path.Default) \n
		Sets a delay between the Q vector and the I vector of the corresponding stream. \n
			:param skew: float Range: -500E-9 to 500E-9
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(skew)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce:BB:IMPairment:RF{path_cmd_val}:SKEW {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:RF<CH>:SKEW \n
		Snippet: value: float = driver.source.bb.impairment.rf.skew.get(path = repcap.Path.Default) \n
		Sets a delay between the Q vector and the I vector of the corresponding stream. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: skew: float Range: -500E-9 to 500E-9"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce:BB:IMPairment:RF{path_cmd_val}:SKEW?')
		return Conversions.str_to_float(response)
