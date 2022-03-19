from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alpha:
	"""Alpha commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: AlphaNull, default value after init: AlphaNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpha", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_alphaNull_get', 'repcap_alphaNull_set', repcap.AlphaNull.Nr0)

	def repcap_alphaNull_set(self, alphaNull: repcap.AlphaNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AlphaNull.Default
		Default value after init: AlphaNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(alphaNull)

	def repcap_alphaNull_get(self) -> repcap.AlphaNull:
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

	def set(self, alpha: int, alphaNull=repcap.AlphaNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:QZSS:NMESsage:NAV:IONospheric:ALPHa<CH0> \n
		Snippet: driver.source.bb.gnss.atmospheric.qzss.nmessage.nav.ionospheric.alpha.set(alpha = 1, alphaNull = repcap.AlphaNull.Default) \n
		Sets the parameters alpha_0 to alpha_3 of the satellite's navigation message. \n
			:param alpha: integer Range: -128 to 127
			:param alphaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alpha')
		"""
		param = Conversions.decimal_value_to_str(alpha)
		alphaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(alphaNull, repcap.AlphaNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:QZSS:NMESsage:NAV:IONospheric:ALPHa{alphaNull_cmd_val} {param}')

	def get(self, alphaNull=repcap.AlphaNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:QZSS:NMESsage:NAV:IONospheric:ALPHa<CH0> \n
		Snippet: value: int = driver.source.bb.gnss.atmospheric.qzss.nmessage.nav.ionospheric.alpha.get(alphaNull = repcap.AlphaNull.Default) \n
		Sets the parameters alpha_0 to alpha_3 of the satellite's navigation message. \n
			:param alphaNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alpha')
			:return: alpha: integer Range: -128 to 127"""
		alphaNull_cmd_val = self._cmd_group.get_repcap_cmd_value(alphaNull, repcap.AlphaNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:QZSS:NMESsage:NAV:IONospheric:ALPHa{alphaNull_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Alpha':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alpha(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
