from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Depth:
	"""Depth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("depth", core, parent)

	def get_sum(self) -> float:
		"""SCPI: [SOURce<HW>]:AM:DEPTh:SUM \n
		Snippet: value: float = driver.source.am.depth.get_sum() \n
		Sets the total depth of the LF signal when using combined signal sources in amplitude modulation. \n
			:return: am_depth_sum: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AM:DEPTh:SUM?')
		return Conversions.str_to_float(response)

	def set_sum(self, am_depth_sum: float) -> None:
		"""SCPI: [SOURce<HW>]:AM:DEPTh:SUM \n
		Snippet: driver.source.am.depth.set_sum(am_depth_sum = 1.0) \n
		Sets the total depth of the LF signal when using combined signal sources in amplitude modulation. \n
			:param am_depth_sum: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(am_depth_sum)
		self._core.io.write(f'SOURce<HwInstance>:AM:DEPTh:SUM {param}')

	def set(self, depth: float, generatorIx=repcap.GeneratorIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:AM<CH>:[DEPTh] \n
		Snippet: driver.source.am.depth.set(depth = 1.0, generatorIx = repcap.GeneratorIx.Default) \n
		Sets the depth of the amplitude modulation in percent. \n
			:param depth: float Range: 0 to 100
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Am')
		"""
		param = Conversions.decimal_value_to_str(depth)
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		self._core.io.write(f'SOURce<HwInstance>:AM{generatorIx_cmd_val}:DEPTh {param}')

	def get(self, generatorIx=repcap.GeneratorIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:AM<CH>:[DEPTh] \n
		Snippet: value: float = driver.source.am.depth.get(generatorIx = repcap.GeneratorIx.Default) \n
		Sets the depth of the amplitude modulation in percent. \n
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Am')
			:return: depth: float Range: 0 to 100"""
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AM{generatorIx_cmd_val}:DEPTh?')
		return Conversions.str_to_float(response)
