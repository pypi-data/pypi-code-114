from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def rfOff(self):
		"""rfOff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfOff'):
			from .RfOff import RfOff
			self._rfOff = RfOff(self._core, self._cmd_group)
		return self._rfOff

	def get_mlrange(self) -> str:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:MLRange \n
		Snippet: value: str = driver.source.roscillator.external.get_mlrange() \n
		Queries the minimum locking range for the selected external reference frequency. Depending on the RF hardware version,
		and the installed options, the minimum locking range vaies. For more information, see data sheet. \n
			:return: min_lock_range: string
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:MLRange?')
		return trim_str_response(response)

	def get_ns_bandwidth(self) -> str:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:NSBandwidth \n
		Snippet: value: str = driver.source.roscillator.external.get_ns_bandwidth() \n
		Queries the nominal synchronization bandwidth for the selected external reference frequency and synchronization bandwidth. \n
			:return: nom_bandwidth: string
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:NSBandwidth?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_sbandwidth(self) -> enums.FilterWidth:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:SBANdwidth \n
		Snippet: value: enums.FilterWidth = driver.source.roscillator.external.get_sbandwidth() \n
		Selects the synchronization bandwidth for the external reference signal. Depending on the RF hardware version, and the
		installed options, the synchronizsation bandwidth varies. For more information, see data sheet. \n
			:return: sbandwidth: WIDE| NARRow NARRow The synchronization bandwidth is 1 Hz. WIDE Uses the widest possible synchronization bandwidth.
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:SBANdwidth?')
		return Conversions.str_to_scalar_enum(response, enums.FilterWidth)

	def set_sbandwidth(self, sbandwidth: enums.FilterWidth) -> None:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:SBANdwidth \n
		Snippet: driver.source.roscillator.external.set_sbandwidth(sbandwidth = enums.FilterWidth.NARRow) \n
		Selects the synchronization bandwidth for the external reference signal. Depending on the RF hardware version, and the
		installed options, the synchronizsation bandwidth varies. For more information, see data sheet. \n
			:param sbandwidth: WIDE| NARRow NARRow The synchronization bandwidth is 1 Hz. WIDE Uses the widest possible synchronization bandwidth.
		"""
		param = Conversions.enum_scalar_to_str(sbandwidth, enums.FilterWidth)
		self._core.io.write(f'SOURce:ROSCillator:EXTernal:SBANdwidth {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
