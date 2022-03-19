from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tprs:
	"""Tprs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tprs", core, parent)

	def get(self, periodicity_tprs: int) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:PRSS:TPRS \n
		Snippet: value: int = driver.source.bb.v5G.downlink.prss.tprs.get(periodicity_tprs = 1) \n
		No command help available \n
			:param periodicity_tprs: No help available
			:return: periodicity_tprs: No help available"""
		param = Conversions.decimal_value_to_str(periodicity_tprs)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:PRSS:TPRS? {param}')
		return Conversions.str_to_int(response)
