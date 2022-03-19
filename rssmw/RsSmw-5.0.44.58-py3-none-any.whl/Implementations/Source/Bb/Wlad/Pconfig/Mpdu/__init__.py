from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mpdu:
	"""Mpdu commands group definition. 5 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: MacPdu, default value after init: MacPdu.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpdu", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_macPdu_get', 'repcap_macPdu_set', repcap.MacPdu.Nr1)

	def repcap_macPdu_set(self, macPdu: repcap.MacPdu) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MacPdu.Default
		Default value after init: MacPdu.Nr1"""
		self._cmd_group.set_repcap_enum_value(macPdu)

	def repcap_macPdu_get(self) -> repcap.MacPdu:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def data(self):
		"""data commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU:COUNt \n
		Snippet: value: int = driver.source.bb.wlad.pconfig.mpdu.get_count() \n
		Sets the number of MPDUs in the frame. \n
			:return: count: integer Range: 1 to 64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU:COUNt \n
		Snippet: driver.source.bb.wlad.pconfig.mpdu.set_count(count = 1) \n
		Sets the number of MPDUs in the frame. \n
			:param count: integer Range: 1 to 64
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU:COUNt {param}')

	def clone(self) -> 'Mpdu':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mpdu(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
