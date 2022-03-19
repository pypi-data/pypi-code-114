from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Actual:
	"""Actual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("actual", core, parent)

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:PATH<CH>:FDOPpler:ACTual \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.path.fdoppler.actual.get(path = repcap.Path.Default) \n
		Queries the actuial Doppler frequency. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: act_doppler: float Range: -1600 to 1600"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:PATH{path_cmd_val}:FDOPpler:ACTual?')
		return Conversions.str_to_float(response)
