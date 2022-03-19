from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:DRM:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.drm.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.drm.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: drm_cat: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, drm_delete: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:SETTing:DELete \n
		Snippet: driver.source.bb.drm.setting.delete(drm_delete = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.drm. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param drm_delete: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(drm_delete)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:SETTing:DELete {param}')

	def load(self, drm_recall: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:SETTing:LOAD \n
		Snippet: driver.source.bb.drm.setting.load(drm_recall = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.drm.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param drm_recall: 'DrmRecall' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(drm_recall)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:SETTing:LOAD {param}')

	def set_store(self, drm_save: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DRM:SETTing:STORe \n
		Snippet: driver.source.bb.drm.setting.set_store(drm_save = '1') \n
		Saves the current settings into the selected file; the file extension (*.drm) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param drm_save: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(drm_save)
		self._core.io.write(f'SOURce<HwInstance>:BB:DRM:SETTing:STORe {param}')
