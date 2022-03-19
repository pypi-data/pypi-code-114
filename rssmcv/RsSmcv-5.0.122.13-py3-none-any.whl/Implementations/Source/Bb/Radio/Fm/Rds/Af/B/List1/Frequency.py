from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)
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

	def set(self, af_list_1_freq: float, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST1:FREQuency<CH> \n
		Snippet: driver.source.bb.radio.fm.rds.af.b.list1.frequency.set(af_list_1_freq = 1.0, index = repcap.Index.Default) \n
		Sets an alternative frequency of a list in AF method B. \n
			:param af_list_1_freq: float Range: 87.6 to 107.9, Unit: MHz
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frequency')
		"""
		param = Conversions.decimal_value_to_str(af_list_1_freq)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST1:FREQuency{index_cmd_val} {param}')

	def get(self, index=repcap.Index.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:AF:B:LIST1:FREQuency<CH> \n
		Snippet: value: float = driver.source.bb.radio.fm.rds.af.b.list1.frequency.get(index = repcap.Index.Default) \n
		Sets an alternative frequency of a list in AF method B. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frequency')
			:return: af_list_1_freq: No help available"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:RADio:FM:RDS:AF:B:LIST1:FREQuency{index_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
