from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Beta:
	"""Beta commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: BetaNull, default value after init: BetaNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("beta", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_betaNull_get', 'repcap_betaNull_set', repcap.BetaNull.Nr0)

	def repcap_betaNull_set(self, betaNull: repcap.BetaNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BetaNull.Default
		Default value after init: BetaNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(betaNull)

	def repcap_betaNull_get(self) -> repcap.BetaNull:
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

	def set(self, beta: int, betaNull=repcap.BetaNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:NAVic:IONospheric:BETA<CH0> \n
		Snippet: driver.source.bb.gnss.atmospheric.navic.ionospheric.beta.set(beta = 1, betaNull = repcap.BetaNull.Default) \n
		No command help available \n
			:param beta: No help available
			:param betaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Beta')
		"""
		param = Conversions.decimal_value_to_str(beta)
		betaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(betaNull, repcap.BetaNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:NAVic:IONospheric:BETA{betaNull_cmd_val} {param}')

	def get(self, betaNull=repcap.BetaNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:NAVic:IONospheric:BETA<CH0> \n
		Snippet: value: int = driver.source.bb.gnss.atmospheric.navic.ionospheric.beta.get(betaNull = repcap.BetaNull.Default) \n
		No command help available \n
			:param betaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Beta')
			:return: beta: No help available"""
		betaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(betaNull, repcap.BetaNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:NAVic:IONospheric:BETA{betaNull_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Beta':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Beta(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
