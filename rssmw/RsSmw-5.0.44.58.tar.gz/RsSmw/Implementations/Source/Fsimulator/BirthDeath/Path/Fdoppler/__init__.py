from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fdoppler:
	"""Fdoppler commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdoppler", core, parent)

	@property
	def actual(self):
		"""actual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_actual'):
			from .Actual import Actual
			self._actual = Actual(self._core, self._cmd_group)
		return self._actual

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:PATH<CH>:FDOPpler \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.path.fdoppler.get(path = repcap.Path.Default) \n
		Queries the resulting Doppler frequency with birth death propagation. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: fdoppler: float Range: 0 to 1000"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:PATH{path_cmd_val}:FDOPpler?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Fdoppler':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fdoppler(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
