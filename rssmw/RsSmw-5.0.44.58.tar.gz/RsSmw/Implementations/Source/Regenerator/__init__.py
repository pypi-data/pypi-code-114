from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Regenerator:
	"""Regenerator commands group definition. 78 total commands, 7 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("regenerator", core, parent)

	@property
	def diagram(self):
		"""diagram commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_diagram'):
			from .Diagram import Diagram
			self._diagram = Diagram(self._core, self._cmd_group)
		return self._diagram

	@property
	def object(self):
		"""object commands group. 15 Sub-classes, 2 commands."""
		if not hasattr(self, '_object'):
			from .Object import Object
			self._object = Object(self._core, self._cmd_group)
		return self._object

	@property
	def radar(self):
		"""radar commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_radar'):
			from .Radar import Radar
			self._radar = Radar(self._core, self._cmd_group)
		return self._radar

	@property
	def restart(self):
		"""restart commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	@property
	def simulation(self):
		"""simulation commands group. 5 Sub-classes, 6 commands."""
		if not hasattr(self, '_simulation'):
			from .Simulation import Simulation
			self._simulation = Simulation(self._core, self._cmd_group)
		return self._simulation

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_test'):
			from .Test import Test
			self._test = Test(self._core, self._cmd_group)
		return self._test

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:REGenerator:CATalog \n
		Snippet: value: List[str] = driver.source.regenerator.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.reg.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: filenames: filename1,filename2,... Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:LOAD \n
		Snippet: driver.source.regenerator.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.reg.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: string file name or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:LOAD {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:PRESet \n
		Snippet: driver.source.regenerator.preset() \n
		Calls the default settings. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:PRESet \n
		Snippet: driver.source.regenerator.preset_with_opc() \n
		Calls the default settings. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:REGenerator:PRESet', opc_timeout_ms)

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:STORe \n
		Snippet: driver.source.regenerator.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.reg) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:STORe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:[STATe] \n
		Snippet: value: bool = driver.source.regenerator.get_state() \n
		Enables/disables the radar echo generation. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:[STATe] \n
		Snippet: driver.source.regenerator.set_state(state = False) \n
		Enables/disables the radar echo generation. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:STATe {param}')

	def clone(self) -> 'Regenerator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Regenerator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
