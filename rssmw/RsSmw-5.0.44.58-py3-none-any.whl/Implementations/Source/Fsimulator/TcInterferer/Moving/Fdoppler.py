from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fdoppler:
	"""Fdoppler commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdoppler", core, parent)

	def get_actual(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:MOVing:FDOPpler:ACTual \n
		Snippet: value: float = driver.source.fsimulator.tcInterferer.moving.fdoppler.get_actual() \n
		Queries the actual Doppler shift. \n
			:return: act_doppler: float Range: -1600 to 1600
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:MOVing:FDOPpler:ACTual?')
		return Conversions.str_to_float(response)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:MOVing:FDOPpler \n
		Snippet: value: float = driver.source.fsimulator.tcInterferer.moving.fdoppler.get_value() \n
		Queries the Doppler frequency of the reference and moving path with 2 channel interferer fading. \n
			:return: fdoppler: float Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:MOVing:FDOPpler?')
		return Conversions.str_to_float(response)
