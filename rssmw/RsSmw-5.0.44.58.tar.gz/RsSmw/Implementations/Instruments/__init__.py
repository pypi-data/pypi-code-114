from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Instruments:
	"""Instruments commands group definition. 17 total commands, 6 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("instruments", core, parent)

	@property
	def active(self):
		"""active commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_active'):
			from .Active import Active
			self._active = Active(self._core, self._cmd_group)
		return self._active

	@property
	def eaccess(self):
		"""eaccess commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eaccess'):
			from .Eaccess import Eaccess
			self._eaccess = Eaccess(self._core, self._cmd_group)
		return self._eaccess

	@property
	def gpib(self):
		"""gpib commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_gpib'):
			from .Gpib import Gpib
			self._gpib = Gpib(self._core, self._cmd_group)
		return self._gpib

	@property
	def mapping(self):
		"""mapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mapping'):
			from .Mapping import Mapping
			self._mapping = Mapping(self._core, self._cmd_group)
		return self._mapping

	@property
	def remote(self):
		"""remote commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_remote'):
			from .Remote import Remote
			self._remote = Remote(self._core, self._cmd_group)
		return self._remote

	@property
	def scan(self):
		"""scan commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scan'):
			from .Scan import Scan
			self._scan = Scan(self._core, self._cmd_group)
		return self._scan

	def clear(self) -> None:
		"""SCPI: INSTruments:CLEar \n
		Snippet: driver.instruments.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'INSTruments:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INSTruments:CLEar \n
		Snippet: driver.instruments.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INSTruments:CLEar', opc_timeout_ms)

	def get_count(self) -> float:
		"""SCPI: INSTruments:COUNt \n
		Snippet: value: float = driver.instruments.get_count() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('INSTruments:COUNt?')
		return Conversions.str_to_float(response)

	def get_name(self) -> List[str]:
		"""SCPI: INSTruments:NAME \n
		Snippet: value: List[str] = driver.instruments.get_name() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('INSTruments:NAME?')
		return Conversions.str_to_str_list(response)

	def set_name(self, name: List[str]) -> None:
		"""SCPI: INSTruments:NAME \n
		Snippet: driver.instruments.set_name(name = ['1', '2', '3']) \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(name)
		self._core.io.write(f'INSTruments:NAME {param}')

	def get_serial(self) -> List[int]:
		"""SCPI: INSTruments:SERial \n
		Snippet: value: List[int] = driver.instruments.get_serial() \n
		No command help available \n
			:return: serial: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('INSTruments:SERial?')
		return response

	def set_serial(self, serial: List[int]) -> None:
		"""SCPI: INSTruments:SERial \n
		Snippet: driver.instruments.set_serial(serial = [1, 2, 3]) \n
		No command help available \n
			:param serial: No help available
		"""
		param = Conversions.list_to_csv_str(serial)
		self._core.io.write(f'INSTruments:SERial {param}')

	def get_type_py(self) -> str:
		"""SCPI: INSTruments:TYPE \n
		Snippet: value: str = driver.instruments.get_type_py() \n
		No command help available \n
			:return: type_py: No help available
		"""
		response = self._core.io.query_str('INSTruments:TYPE?')
		return trim_str_response(response)

	def set_type_py(self, type_py: str) -> None:
		"""SCPI: INSTruments:TYPE \n
		Snippet: driver.instruments.set_type_py(type_py = '1') \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.value_to_quoted_str(type_py)
		self._core.io.write(f'INSTruments:TYPE {param}')

	def clone(self) -> 'Instruments':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Instruments(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
