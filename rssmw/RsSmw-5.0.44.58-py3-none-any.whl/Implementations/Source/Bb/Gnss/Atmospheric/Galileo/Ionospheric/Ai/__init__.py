from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ai:
	"""Ai commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: AiOrder, default value after init: AiOrder.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ai", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_aiOrder_get', 'repcap_aiOrder_set', repcap.AiOrder.Nr1)

	def repcap_aiOrder_set(self, aiOrder: repcap.AiOrder) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AiOrder.Default
		Default value after init: AiOrder.Nr1"""
		self._cmd_group.set_repcap_enum_value(aiOrder)

	def repcap_aiOrder_get(self) -> repcap.AiOrder:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def unscaled(self):
		"""unscaled commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unscaled'):
			from .Unscaled import Unscaled
			self._unscaled = Unscaled(self._core, self._cmd_group)
		return self._unscaled

	def set(self, ai: int, aiOrder=repcap.AiOrder.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:GALileo:IONospheric:AI<CH0> \n
		Snippet: driver.source.bb.gnss.atmospheric.galileo.ionospheric.ai.set(ai = 1, aiOrder = repcap.AiOrder.Default) \n
		No command help available \n
			:param ai: No help available
			:param aiOrder: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ai')
		"""
		param = Conversions.decimal_value_to_str(ai)
		aiOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(aiOrder, repcap.AiOrder)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:GALileo:IONospheric:AI{aiOrder_cmd_val} {param}')

	def get(self, aiOrder=repcap.AiOrder.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:GALileo:IONospheric:AI<CH0> \n
		Snippet: value: int = driver.source.bb.gnss.atmospheric.galileo.ionospheric.ai.get(aiOrder = repcap.AiOrder.Default) \n
		No command help available \n
			:param aiOrder: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ai')
			:return: ai: No help available"""
		aiOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(aiOrder, repcap.AiOrder)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:GALileo:IONospheric:AI{aiOrder_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Ai':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ai(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
