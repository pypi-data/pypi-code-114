from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: NoisePoint, default value after init: NoisePoint.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_noisePoint_get', 'repcap_noisePoint_set', repcap.NoisePoint.Nr1)

	def repcap_noisePoint_set(self, noisePoint: repcap.NoisePoint) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to NoisePoint.Default
		Default value after init: NoisePoint.Nr1"""
		self._cmd_group.set_repcap_enum_value(noisePoint)

	def repcap_noisePoint_get(self) -> repcap.NoisePoint:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, frequency: float, noisePoint=repcap.NoisePoint.Default) -> None:
		"""SCPI: TEST:BB:GENerator:FREQuency<CH> \n
		Snippet: driver.test.bb.generator.frequency.set(frequency = 1.0, noisePoint = repcap.NoisePoint.Default) \n
		Sets the frequency of the test sine or constant I/Q test signal. \n
			:param frequency: float Range: -250E6 to 250E6
			:param noisePoint: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frequency')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		noisePoint_cmd_val = self._cmd_group.get_repcap_cmd_value(noisePoint, repcap.NoisePoint)
		self._core.io.write(f'TEST:BB:GENerator:FREQuency{noisePoint_cmd_val} {param}')

	def get(self, noisePoint=repcap.NoisePoint.Default) -> float:
		"""SCPI: TEST:BB:GENerator:FREQuency<CH> \n
		Snippet: value: float = driver.test.bb.generator.frequency.get(noisePoint = repcap.NoisePoint.Default) \n
		Sets the frequency of the test sine or constant I/Q test signal. \n
			:param noisePoint: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frequency')
			:return: frequency: float Range: -250E6 to 250E6"""
		noisePoint_cmd_val = self._cmd_group.get_repcap_cmd_value(noisePoint, repcap.NoisePoint)
		response = self._core.io.query_str(f'TEST:BB:GENerator:FREQuency{noisePoint_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
