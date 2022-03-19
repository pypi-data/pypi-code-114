from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shape:
	"""Shape commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shape", core, parent)

	@property
	def predefined(self):
		"""predefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_predefined'):
			from .Predefined import Predefined
			self._predefined = Predefined(self._core, self._cmd_group)
		return self._predefined

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:SHAPe:SELect \n
		Snippet: value: str = driver.source.noise.phasenoise.shape.get_select() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.fcf.
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and in a specific directory.
		Query the name of the predefined files with the command [:SOURce<hw>]:NOISe:PHASenoise:SHAPe:PREDefined:CATalog?. \n
			:return: phasenoise_sel: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:PHASenoise:SHAPe:SELect?')
		return trim_str_response(response)

	def set_select(self, phasenoise_sel: str) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:SHAPe:SELect \n
		Snippet: driver.source.noise.phasenoise.shape.set_select(phasenoise_sel = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.fcf.
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and in a specific directory.
		Query the name of the predefined files with the command [:SOURce<hw>]:NOISe:PHASenoise:SHAPe:PREDefined:CATalog?. \n
			:param phasenoise_sel: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(phasenoise_sel)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:PHASenoise:SHAPe:SELect {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:SHAPe:STORe \n
		Snippet: value: str = driver.source.noise.phasenoise.shape.get_store() \n
		Saves the current SSB profile settings into the selected file; the file extension (*.fcf) is assigned automatically.
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and in a specific directory. \n
			:return: phasenoise_store: 'filename' Filename or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:PHASenoise:SHAPe:STORe?')
		return trim_str_response(response)

	def set_store(self, phasenoise_store: str) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:SHAPe:STORe \n
		Snippet: driver.source.noise.phasenoise.shape.set_store(phasenoise_store = '1') \n
		Saves the current SSB profile settings into the selected file; the file extension (*.fcf) is assigned automatically.
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and in a specific directory. \n
			:param phasenoise_store: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(phasenoise_store)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:PHASenoise:SHAPe:STORe {param}')

	def clone(self) -> 'Shape':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Shape(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
