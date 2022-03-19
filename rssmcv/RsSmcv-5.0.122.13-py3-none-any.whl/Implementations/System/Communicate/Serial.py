from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Serial:
	"""Serial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("serial", core, parent)

	# noinspection PyTypeChecker
	def get_sbits(self) -> enums.Count:
		"""SCPI: SYSTem:COMMunicate:SERial:SBITs \n
		Snippet: value: enums.Count = driver.system.communicate.serial.get_sbits() \n
		No command help available \n
			:return: sbits: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:SERial:SBITs?')
		return Conversions.str_to_scalar_enum(response, enums.Count)

	def set_sbits(self, sbits: enums.Count) -> None:
		"""SCPI: SYSTem:COMMunicate:SERial:SBITs \n
		Snippet: driver.system.communicate.serial.set_sbits(sbits = enums.Count._1) \n
		No command help available \n
			:param sbits: No help available
		"""
		param = Conversions.enum_scalar_to_str(sbits, enums.Count)
		self._core.io.write(f'SYSTem:COMMunicate:SERial:SBITs {param}')
