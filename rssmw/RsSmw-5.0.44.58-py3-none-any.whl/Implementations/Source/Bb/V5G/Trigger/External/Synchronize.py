from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Synchronize:
	"""Synchronize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronize", core, parent)

	def get_output(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:EXTernal:SYNChronize:OUTPut \n
		Snippet: value: bool = driver.source.bb.v5G.trigger.external.synchronize.get_output() \n
		Enables output of the signal synchronous to the external trigger event. \n
			:return: trig_sync_out: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:TRIGger:EXTernal:SYNChronize:OUTPut?')
		return Conversions.str_to_bool(response)

	def set_output(self, trig_sync_out: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:EXTernal:SYNChronize:OUTPut \n
		Snippet: driver.source.bb.v5G.trigger.external.synchronize.set_output(trig_sync_out = False) \n
		Enables output of the signal synchronous to the external trigger event. \n
			:param trig_sync_out: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(trig_sync_out)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:TRIGger:EXTernal:SYNChronize:OUTPut {param}')
