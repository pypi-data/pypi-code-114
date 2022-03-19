from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsPy:
	"""IsPy commands group definition. 4 total commands, 3 Subgroups, 1 group commands
	Repeated Capability: InputStream, default value after init: InputStream.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isPy", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_inputStream_get', 'repcap_inputStream_set', repcap.InputStream.Nr1)

	def repcap_inputStream_set(self, inputStream: repcap.InputStream) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to InputStream.Default
		Default value after init: InputStream.Nr1"""
		self._cmd_group.set_repcap_enum_value(inputStream)

	def repcap_inputStream_get(self) -> repcap.InputStream:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def tsChannel(self):
		"""tsChannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsChannel'):
			from .TsChannel import TsChannel
			self._tsChannel = TsChannel(self._core, self._cmd_group)
		return self._tsChannel

	@property
	def dataRate(self):
		"""dataRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dataRate'):
			from .DataRate import DataRate
			self._dataRate = DataRate(self._core, self._cmd_group)
		return self._dataRate

	def set(self, input_py: enums.CodingInputSignalInputA, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:INPut:[IS<CH>] \n
		Snippet: driver.source.bb.dvbs2.inputPy.isPy.set(input_py = enums.CodingInputSignalInputA.ASI1, inputStream = repcap.InputStream.Default) \n
		Sets the external input interface. \n
			:param input_py: TS| IP
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.CodingInputSignalInputA)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, inputStream=repcap.InputStream.Default) -> enums.CodingInputSignalInputA:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:INPut:[IS<CH>] \n
		Snippet: value: enums.CodingInputSignalInputA = driver.source.bb.dvbs2.inputPy.isPy.get(inputStream = repcap.InputStream.Default) \n
		Sets the external input interface. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: input_py: TS| IP"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputA)

	def clone(self) -> 'IsPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IsPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
