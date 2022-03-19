from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slist:
	"""Slist commands group definition. 7 total commands, 3 Subgroups, 3 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slist", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ports(self):
		"""ports commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import Ports
			self._ports = Ports(self._core, self._cmd_group)
		return self._ports

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_catalog(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:CATalog \n
		Snippet: value: str = driver.source.correction.fresponse.rf.user.slist.get_catalog() \n
		Queries the S-parameter files included in the current S-paramters list. \n
			:return: catalog: filename1,filename2,...filename10 Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:CATalog?')
		return trim_str_response(response)

	def clear(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.clear() \n
		Deletes all entries in the lists. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.clear_with_opc() \n
		Deletes all entries in the lists. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:CLEar', opc_timeout_ms)

	def get_size(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:SIZE \n
		Snippet: value: int = driver.source.correction.fresponse.rf.user.slist.get_size() \n
		Queries the number of files in the list. \n
			:return: freq_resp_rf_sli_si: integer Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:SIZE?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Slist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Slist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
