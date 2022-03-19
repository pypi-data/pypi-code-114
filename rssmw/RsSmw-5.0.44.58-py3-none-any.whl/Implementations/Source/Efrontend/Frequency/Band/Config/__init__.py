from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:BAND:CONFig:SELect \n
		Snippet: value: str = driver.source.efrontend.frequency.band.config.get_select() \n
		Loads the selected file from the default or the specified directory. Refer to 'Accessing Files in the Default or
		Specified Directory' for general information on file handling in the default and in a specific directory. \n
			:return: sel_band_config: string file name or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:FREQuency:BAND:CONFig:SELect?')
		return trim_str_response(response)

	def set_select(self, sel_band_config: str) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:FREQuency:BAND:CONFig:SELect \n
		Snippet: driver.source.efrontend.frequency.band.config.set_select(sel_band_config = '1') \n
		Loads the selected file from the default or the specified directory. Refer to 'Accessing Files in the Default or
		Specified Directory' for general information on file handling in the default and in a specific directory. \n
			:param sel_band_config: string file name or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(sel_band_config)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:FREQuency:BAND:CONFig:SELect {param}')

	def clone(self) -> 'Config':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Config(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
