from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:OUTPut:LEVel \n
		Snippet: value: float = driver.source.iq.doherty.output.get_level() \n
		Queries the PEP and level values. \n
			:return: level: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:OUTPut:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:OUTPut:PEP \n
		Snippet: value: float = driver.source.iq.doherty.output.get_pep() \n
		Queries the PEP and level values. \n
			:return: pep: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:OUTPut:PEP?')
		return Conversions.str_to_float(response)
