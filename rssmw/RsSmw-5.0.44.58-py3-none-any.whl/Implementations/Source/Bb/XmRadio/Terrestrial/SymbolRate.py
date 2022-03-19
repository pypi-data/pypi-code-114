from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get_variation(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:SRATe:VARiation \n
		Snippet: value: int = driver.source.bb.xmRadio.terrestrial.symbolRate.get_variation() \n
		No command help available \n
			:return: variation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:TERRestrial:SRATe:VARiation?')
		return Conversions.str_to_int(response)
