from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Information:
	"""Information commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("information", core, parent)

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_test'):
			from .Test import Test
			self._test = Test(self._core, self._cmd_group)
		return self._test

	def get_scpi(self) -> str:
		"""SCPI: SYSTem:INFormation:SCPI \n
		Snippet: value: str = driver.system.information.get_scpi() \n
		Inserts system information in recorded SCPI command lists, for example information on a missing command. \n
			:return: info_string: string
		"""
		response = self._core.io.query_str('SYSTem:INFormation:SCPI?')
		return trim_str_response(response)

	def set_scpi(self, info_string: str) -> None:
		"""SCPI: SYSTem:INFormation:SCPI \n
		Snippet: driver.system.information.set_scpi(info_string = '1') \n
		Inserts system information in recorded SCPI command lists, for example information on a missing command. \n
			:param info_string: string
		"""
		param = Conversions.value_to_quoted_str(info_string)
		self._core.io.write(f'SYSTem:INFormation:SCPI {param}')

	def get_sr(self) -> str:
		"""SCPI: SYSTem:INFormation:SR \n
		Snippet: value: str = driver.system.information.get_sr() \n
		No command help available \n
			:return: sr_info: No help available
		"""
		response = self._core.io.query_str('SYSTem:INFormation:SR?')
		return trim_str_response(response)

	def set_sr(self, sr_info: str) -> None:
		"""SCPI: SYSTem:INFormation:SR \n
		Snippet: driver.system.information.set_sr(sr_info = '1') \n
		No command help available \n
			:param sr_info: No help available
		"""
		param = Conversions.value_to_quoted_str(sr_info)
		self._core.io.write(f'SYSTem:INFormation:SR {param}')

	def clone(self) -> 'Information':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Information(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
