from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ecount:
	"""Ecount commands group definition. 4 total commands, 3 Subgroups, 1 group commands
	Repeated Capability: ErrorCount, default value after init: ErrorCount.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ecount", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_errorCount_get', 'repcap_errorCount_set', repcap.ErrorCount.Nr1)

	def repcap_errorCount_set(self, errorCount: repcap.ErrorCount) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ErrorCount.Default
		Default value after init: ErrorCount.Nr1"""
		self._cmd_group.set_repcap_enum_value(errorCount)

	def repcap_errorCount_get(self) -> repcap.ErrorCount:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Set import Set
			self._set = Set(self._core, self._cmd_group)
		return self._set

	def get(self, errorCount=repcap.ErrorCount.Default) -> int:
		"""SCPI: DIAGnostic:INFO:ECOunt<CH> \n
		Snippet: value: int = driver.diagnostic.info.ecount.get(errorCount = repcap.ErrorCount.Default) \n
		No command help available \n
			:param errorCount: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ecount')
			:return: ecount: No help available"""
		errorCount_cmd_val = self._cmd_group.get_repcap_cmd_value(errorCount, repcap.ErrorCount)
		response = self._core.io.query_str(f'DIAGnostic:INFO:ECOunt{errorCount_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Ecount':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ecount(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
