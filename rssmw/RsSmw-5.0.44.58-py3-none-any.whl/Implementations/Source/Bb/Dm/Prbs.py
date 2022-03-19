from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prbs:
	"""Prbs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prbs", core, parent)

	# noinspection PyTypeChecker
	def get_length(self) -> enums.DmDataPrbs:
		"""SCPI: [SOURce<HW>]:BB:DM:PRBS:[LENGth] \n
		Snippet: value: enums.DmDataPrbs = driver.source.bb.dm.prbs.get_length() \n
		Defines the length of the pseudo-random sequence in accordance with the following equation: Length = (2^Length) - 1 \n
			:return: length: 9| 11| 15| 16| 20| 21| 23| PN9| PN11| PN15| PN16| PN20| PN21| PN23
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRBS:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.DmDataPrbs)

	def set_length(self, length: enums.DmDataPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRBS:[LENGth] \n
		Snippet: driver.source.bb.dm.prbs.set_length(length = enums.DmDataPrbs._11) \n
		Defines the length of the pseudo-random sequence in accordance with the following equation: Length = (2^Length) - 1 \n
			:param length: 9| 11| 15| 16| 20| 21| 23| PN9| PN11| PN15| PN16| PN20| PN21| PN23
		"""
		param = Conversions.enum_scalar_to_str(length, enums.DmDataPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRBS:LENGth {param}')
