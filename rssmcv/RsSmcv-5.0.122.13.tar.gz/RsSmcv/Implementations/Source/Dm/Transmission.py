from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transmission:
	"""Transmission commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transmission", core, parent)

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.SfeBbType:
		"""SCPI: [SOURce]:DM:TRANsmission:[STANdard] \n
		Snippet: value: enums.SfeBbType = driver.source.dm.transmission.get_standard() \n
		No command help available \n
			:return: standard: No help available
		"""
		response = self._core.io.query_str('SOURce:DM:TRANsmission:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.SfeBbType)

	def set_standard(self, standard: enums.SfeBbType) -> None:
		"""SCPI: [SOURce]:DM:TRANsmission:[STANdard] \n
		Snippet: driver.source.dm.transmission.set_standard(standard = enums.SfeBbType.AM) \n
		No command help available \n
			:param standard: No help available
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.SfeBbType)
		self._core.io.write(f'SOURce:DM:TRANsmission:STANdard {param}')
