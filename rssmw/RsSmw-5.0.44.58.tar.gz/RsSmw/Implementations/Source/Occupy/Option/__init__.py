from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Option:
	"""Option commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("option", core, parent)

	@property
	def renew(self):
		"""renew commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_renew'):
			from .Renew import Renew
			self._renew = Renew(self._core, self._cmd_group)
		return self._renew

	def set(self) -> None:
		"""SCPI: [SOURce]:OCCupy:OPTion \n
		Snippet: driver.source.occupy.option.set() \n
		Occupies the selected option. You can determine the option string, the time period and the number of licenses for the
		occupancy. \n
		"""
		self._core.io.write(f'SOURce:OCCupy:OPTion')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce]:OCCupy:OPTion \n
		Snippet: driver.source.occupy.option.set_with_opc() \n
		Occupies the selected option. You can determine the option string, the time period and the number of licenses for the
		occupancy. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:OCCupy:OPTion', opc_timeout_ms)

	def get_catalog(self) -> str:
		"""SCPI: [SOURce]:OCCupy:OPTion:CATalog \n
		Snippet: value: str = driver.source.occupy.option.get_catalog() \n
		Queries the availability of borrowable licenses on all license servers accessible for the R&S SMW. \n
			:return: occ_licenses_cat: string Comma-separated list of strings for available options.
		"""
		response = self._core.io.query_str('SOURce:OCCupy:OPTion:CATalog?')
		return trim_str_response(response)

	def clone(self) -> 'Option':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Option(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
