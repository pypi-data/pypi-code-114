from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Self:
	"""Self commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("self", core, parent)

	def get_address(self) -> int:
		"""SCPI: SYSTem:COMMunicate:GPIB:[SELF]:ADDRess \n
		Snippet: value: int = driver.system.communicate.gpib.self.get_address() \n
		Sets the GPIB address. \n
			:return: address: integer Range: 0 to 30
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:GPIB:SELF:ADDRess?')
		return Conversions.str_to_int(response)

	def set_address(self, address: int) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB:[SELF]:ADDRess \n
		Snippet: driver.system.communicate.gpib.self.set_address(address = 1) \n
		Sets the GPIB address. \n
			:param address: integer Range: 0 to 30
		"""
		param = Conversions.decimal_value_to_str(address)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB:SELF:ADDRess {param}')
