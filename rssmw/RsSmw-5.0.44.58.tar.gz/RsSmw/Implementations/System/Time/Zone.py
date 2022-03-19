from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zone:
	"""Zone commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zone", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: SYSTem:TIME:ZONE:CATalog \n
		Snippet: value: List[str] = driver.system.time.zone.get_catalog() \n
		Querys the list of available timezones. \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SYSTem:TIME:ZONE:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: SYSTem:TIME:ZONE \n
		Snippet: value: str = driver.system.time.zone.get_value() \n
		Sets the timezone. You can query the list of the available timezones with method RsSmw.System.Time.Zone.catalog. \n
			:return: time_zone: string
		"""
		response = self._core.io.query_str('SYSTem:TIME:ZONE?')
		return trim_str_response(response)

	def set_value(self, time_zone: str) -> None:
		"""SCPI: SYSTem:TIME:ZONE \n
		Snippet: driver.system.time.zone.set_value(time_zone = '1') \n
		Sets the timezone. You can query the list of the available timezones with method RsSmw.System.Time.Zone.catalog. \n
			:param time_zone: string
		"""
		param = Conversions.value_to_quoted_str(time_zone)
		self._core.io.write(f'SYSTem:TIME:ZONE {param}')
