from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shape:
	"""Shape commands group definition. 10 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shape", core, parent)

	@property
	def pulse(self):
		"""pulse commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pulse'):
			from .Pulse import Pulse
			self._pulse = Pulse(self._core, self._cmd_group)
		return self._pulse

	@property
	def trapeze(self):
		"""trapeze commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trapeze'):
			from .Trapeze import Trapeze
			self._trapeze = Trapeze(self._core, self._cmd_group)
		return self._trapeze

	@property
	def triangle(self):
		"""triangle commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_triangle'):
			from .Triangle import Triangle
			self._triangle = Triangle(self._core, self._cmd_group)
		return self._triangle

	def set(self, shape: enums.LfShapeBfAmily, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:SHAPe \n
		Snippet: driver.source.lfOutput.shape.set(shape = enums.LfShapeBfAmily.PULSe, lfOutput = repcap.LfOutput.Default) \n
		Selects the waveform shape of the LF signal. \n
			:param shape: SINE| SQUare| PULSe| TRIangle| TRAPeze
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.LfShapeBfAmily)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:SHAPe {param}')

	# noinspection PyTypeChecker
	def get(self, lfOutput=repcap.LfOutput.Default) -> enums.LfShapeBfAmily:
		"""SCPI: [SOURce<HW>]:LFOutput<CH>:SHAPe \n
		Snippet: value: enums.LfShapeBfAmily = driver.source.lfOutput.shape.get(lfOutput = repcap.LfOutput.Default) \n
		Selects the waveform shape of the LF signal. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: shape: SINE| SQUare| PULSe| TRIangle| TRAPeze"""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce<HwInstance>:LFOutput{lfOutput_cmd_val}:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.LfShapeBfAmily)

	def clone(self) -> 'Shape':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Shape(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
