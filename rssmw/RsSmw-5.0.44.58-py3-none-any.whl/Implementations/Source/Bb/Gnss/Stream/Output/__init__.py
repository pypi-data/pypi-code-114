from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	@property
	def bbmm(self):
		"""bbmm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbmm'):
			from .Bbmm import Bbmm
			self._bbmm = Bbmm(self._core, self._cmd_group)
		return self._bbmm

	@property
	def rf(self):
		"""rf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rf'):
			from .Rf import Rf
			self._rf = Rf(self._core, self._cmd_group)
		return self._rf

	def set(self, output: enums.Output, stream=repcap.Stream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:OUTPut \n
		Snippet: driver.source.bb.gnss.stream.output.set(output = enums.Output.NONE, stream = repcap.Stream.Default) \n
		Sets the output connector to that the output GNSS signal is routed. \n
			:param output: RFA| RFB| NONE
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.enum_scalar_to_str(output, enums.Output)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:OUTPut {param}')

	# noinspection PyTypeChecker
	def get(self, stream=repcap.Stream.Default) -> enums.Output:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:OUTPut \n
		Snippet: value: enums.Output = driver.source.bb.gnss.stream.output.get(stream = repcap.Stream.Default) \n
		Sets the output connector to that the output GNSS signal is routed. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: output: RFA| RFB| NONE"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:OUTPut?')
		return Conversions.str_to_scalar_enum(response, enums.Output)

	def clone(self) -> 'Output':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Output(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
