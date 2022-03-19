from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coordinates:
	"""Coordinates commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coordinates", core, parent)

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.PositionFormat:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:BEIDou:COORdinates:FORMat \n
		Snippet: value: enums.PositionFormat = driver.source.bb.gnss.adGeneration.beidou.coordinates.get_format_py() \n
		Sets the format in which the coordinates of the reference location are set. \n
			:return: position_format: DMS| DECimal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:BEIDou:COORdinates:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PositionFormat)

	def set_format_py(self, position_format: enums.PositionFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:BEIDou:COORdinates:FORMat \n
		Snippet: driver.source.bb.gnss.adGeneration.beidou.coordinates.set_format_py(position_format = enums.PositionFormat.DECimal) \n
		Sets the format in which the coordinates of the reference location are set. \n
			:param position_format: DMS| DECimal
		"""
		param = Conversions.enum_scalar_to_str(position_format, enums.PositionFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:BEIDou:COORdinates:FORMat {param}')
