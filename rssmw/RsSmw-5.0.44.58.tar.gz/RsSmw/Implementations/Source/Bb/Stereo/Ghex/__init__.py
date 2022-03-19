from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ghex:
	"""Ghex commands group definition. 6 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ghex", core, parent)

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:CATalog \n
		Snippet: value: List[str] = driver.source.bb.stereo.ghex.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:GHEX:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, load: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:LOAD \n
		Snippet: driver.source.bb.stereo.ghex.load(load = '1') \n
		No command help available \n
			:param load: No help available
		"""
		param = Conversions.value_to_quoted_str(load)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GHEX:LOAD {param}')

	def get_no_entries(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:NOENtries \n
		Snippet: value: int = driver.source.bb.stereo.ghex.get_no_entries() \n
		No command help available \n
			:return: no_entries: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:STEReo:GHEX:NOENtries?')
		return Conversions.str_to_int(response)

	def set_no_entries(self, no_entries: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:NOENtries \n
		Snippet: driver.source.bb.stereo.ghex.set_no_entries(no_entries = 1) \n
		No command help available \n
			:param no_entries: No help available
		"""
		param = Conversions.decimal_value_to_str(no_entries)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GHEX:NOENtries {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:PRESet \n
		Snippet: driver.source.bb.stereo.ghex.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GHEX:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:PRESet \n
		Snippet: driver.source.bb.stereo.ghex.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:STEReo:GHEX:PRESet', opc_timeout_ms)

	def set_store(self, store: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GHEX:STORe \n
		Snippet: driver.source.bb.stereo.ghex.set_store(store = '1') \n
		No command help available \n
			:param store: No help available
		"""
		param = Conversions.value_to_quoted_str(store)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GHEX:STORe {param}')

	def clone(self) -> 'Ghex':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ghex(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
