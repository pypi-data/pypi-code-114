from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Device:
	"""Device commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("device", core, parent)

	# noinspection PyTypeChecker
	def get_language(self) -> enums.HardCopyImageFormat:
		"""SCPI: HCOPy:DEVice:LANGuage \n
		Snippet: value: enums.HardCopyImageFormat = driver.hardCopy.device.get_language() \n
		Selects the graphic format for the hard copy. You can use both commands alternatively. \n
			:return: language: BMP| JPG| XPM| PNG
		"""
		response = self._core.io.query_str('HCOPy:DEVice:LANGuage?')
		return Conversions.str_to_scalar_enum(response, enums.HardCopyImageFormat)

	def set_language(self, language: enums.HardCopyImageFormat) -> None:
		"""SCPI: HCOPy:DEVice:LANGuage \n
		Snippet: driver.hardCopy.device.set_language(language = enums.HardCopyImageFormat.BMP) \n
		Selects the graphic format for the hard copy. You can use both commands alternatively. \n
			:param language: BMP| JPG| XPM| PNG
		"""
		param = Conversions.enum_scalar_to_str(language, enums.HardCopyImageFormat)
		self._core.io.write(f'HCOPy:DEVice:LANGuage {param}')
