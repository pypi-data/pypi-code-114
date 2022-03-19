from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ostreams:
	"""Ostreams commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ostreams", core, parent)

	@property
	def output(self):
		"""output commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	def get_conflict(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:CONFlict \n
		Snippet: value: bool = driver.source.bb.gnss.ostreams.get_conflict() \n
		Indicates stream-specific and general signal generation conflicts in the GNSS output streams configuration. \n
			:return: conflict_status: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:OSTReams:CONFlict?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_count(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:COUNt \n
		Snippet: value: enums.NumberA = driver.source.bb.gnss.ostreams.get_count() \n
		Sets the number of GNSS streams. \n
			:return: output_streams: 1| 2| 3| 4 Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:OSTReams:COUNt?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_count(self, output_streams: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:COUNt \n
		Snippet: driver.source.bb.gnss.ostreams.set_count(output_streams = enums.NumberA._1) \n
		Sets the number of GNSS streams. \n
			:param output_streams: 1| 2| 3| 4 Range: 1 to 4
		"""
		param = Conversions.enum_scalar_to_str(output_streams, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:OSTReams:COUNt {param}')

	def get_lock(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:LOCK \n
		Snippet: value: bool = driver.source.bb.gnss.ostreams.get_lock() \n
		Locks the output streams mapping configuration. \n
			:return: lock_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:OSTReams:LOCK?')
		return Conversions.str_to_bool(response)

	def set_lock(self, lock_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OSTReams:LOCK \n
		Snippet: driver.source.bb.gnss.ostreams.set_lock(lock_state = False) \n
		Locks the output streams mapping configuration. \n
			:param lock_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(lock_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:OSTReams:LOCK {param}')

	def clone(self) -> 'Ostreams':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ostreams(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
