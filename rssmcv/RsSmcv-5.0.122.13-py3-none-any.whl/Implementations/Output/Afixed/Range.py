from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def get_lower(self) -> float:
		"""SCPI: OUTPut<HW>:AFIXed:RANGe:LOWer \n
		Snippet: value: float = driver.output.afixed.range.get_lower() \n
		Queries the settable minimum/maximum value in mode OUTPut:AMODe FIXed, i.e. when the attenuator is not being adjusted. \n
			:return: lower: float Unit: dBm
		"""
		response = self._core.io.query_str('OUTPut<HwInstance>:AFIXed:RANGe:LOWer?')
		return Conversions.str_to_float(response)

	def get_upper(self) -> float:
		"""SCPI: OUTPut<HW>:AFIXed:RANGe:UPPer \n
		Snippet: value: float = driver.output.afixed.range.get_upper() \n
		Queries the settable minimum/maximum value in mode OUTPut:AMODe FIXed, i.e. when the attenuator is not being adjusted. \n
			:return: upper: float Unit: dBm
		"""
		response = self._core.io.query_str('OUTPut<HwInstance>:AFIXed:RANGe:UPPer?')
		return Conversions.str_to_float(response)
