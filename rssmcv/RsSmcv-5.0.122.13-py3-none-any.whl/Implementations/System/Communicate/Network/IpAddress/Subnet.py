from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subnet:
	"""Subnet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subnet", core, parent)

	def get_mask(self) -> str:
		"""SCPI: SYSTem:COMMunicate:NETWork:[IPADdress]:SUBNet:MASK \n
		Snippet: value: str = driver.system.communicate.network.ipAddress.subnet.get_mask() \n
		Sets the subnet mask. \n
			:return: mask: string
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK?')
		return trim_str_response(response)

	def set_mask(self, mask: str) -> None:
		"""SCPI: SYSTem:COMMunicate:NETWork:[IPADdress]:SUBNet:MASK \n
		Snippet: driver.system.communicate.network.ipAddress.subnet.set_mask(mask = '1') \n
		Sets the subnet mask. \n
			:param mask: string
		"""
		param = Conversions.value_to_quoted_str(mask)
		self._core.io.write(f'SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK {param}')
