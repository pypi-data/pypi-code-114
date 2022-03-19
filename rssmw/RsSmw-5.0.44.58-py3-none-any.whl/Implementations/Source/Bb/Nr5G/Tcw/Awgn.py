from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Awgn:
	"""Awgn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	def get_plevel(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:AWGN:PLEVel \n
		Snippet: value: str = driver.source.bb.nr5G.tcw.awgn.get_plevel() \n
		Queries the AWGN power level. \n
			:return: awgn_pow_lev: string Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:AWGN:PLEVel?')
		return trim_str_response(response)
