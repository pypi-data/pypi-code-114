from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AntGain:
	"""AntGain commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antGain", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, antenna_gain: float, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfig:PCONfig:ANTGain<CH0> \n
		Snippet: driver.source.bb.btooth.econfig.pconfig.antGain.set(antenna_gain = 1.0, indexNull = repcap.IndexNull.Default) \n
		Specifies the gain of the antenna. You can specify the antenna gain infomation of up for four individual antennas for
		direction finding. \n
			:param antenna_gain: float Range: -10 to 10
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'AntGain')
		"""
		param = Conversions.decimal_value_to_str(antenna_gain)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfig:PCONfig:ANTGain{indexNull_cmd_val} {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfig:PCONfig:ANTGain<CH0> \n
		Snippet: value: float = driver.source.bb.btooth.econfig.pconfig.antGain.get(indexNull = repcap.IndexNull.Default) \n
		Specifies the gain of the antenna. You can specify the antenna gain infomation of up for four individual antennas for
		direction finding. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'AntGain')
			:return: antenna_gain: float Range: -10 to 10"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfig:PCONfig:ANTGain{indexNull_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AntGain':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AntGain(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
