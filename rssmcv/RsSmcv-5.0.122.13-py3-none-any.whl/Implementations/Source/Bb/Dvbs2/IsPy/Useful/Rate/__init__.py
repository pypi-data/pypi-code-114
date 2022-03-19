from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	@property
	def max(self):
		"""max commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	def set(self, useful_data_rate: float, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:USEFul:[RaTE] \n
		Snippet: driver.source.bb.dvbs2.isPy.useful.rate.set(useful_data_rate = 1.0, inputStream = repcap.InputStream.Default) \n
		Queries the data rate of useful data ruseful of the external transport stream. The data rate is measured at the input of
		the installed input interface. \n
			:param useful_data_rate: float Range: 0 to 999999999
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.decimal_value_to_str(useful_data_rate)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:USEFul:RaTE {param}')

	def get(self, inputStream=repcap.InputStream.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:USEFul:[RaTE] \n
		Snippet: value: float = driver.source.bb.dvbs2.isPy.useful.rate.get(inputStream = repcap.InputStream.Default) \n
		Queries the data rate of useful data ruseful of the external transport stream. The data rate is measured at the input of
		the installed input interface. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: useful_data_rate: float Range: 0 to 999999999"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:USEFul:RaTE?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Rate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
