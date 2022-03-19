from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fa:
	"""Fa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fa", core, parent)

	# noinspection PyTypeChecker
	def get_fr_allocation(self) -> enums.LowHigh:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:FA:FRALlocation \n
		Snippet: value: enums.LowHigh = driver.source.bb.nr5G.tcw.fa.get_fr_allocation() \n
		Sets the frequency allocation to FR1 or FR2. \n
			:return: freq_alloc: LOW| HIGH
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:FA:FRALlocation?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_fr_allocation(self, freq_alloc: enums.LowHigh) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:FA:FRALlocation \n
		Snippet: driver.source.bb.nr5G.tcw.fa.set_fr_allocation(freq_alloc = enums.LowHigh.HIGH) \n
		Sets the frequency allocation to FR1 or FR2. \n
			:param freq_alloc: LOW| HIGH
		"""
		param = Conversions.enum_scalar_to_str(freq_alloc, enums.LowHigh)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:FA:FRALlocation {param}')
