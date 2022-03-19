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
		"""SCPI: [SOURce<HW>]:BB:OFDM:TRIGger:EXTernal:SYNChronize:OUTPut \n
		Snippet: value: bool = driver.source.bb.ofdm.trigger.external.synchronize.get_output() \n
		Enables signal output synchronous to the trigger event. \n
			:return: trig_sync_outp_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:TRIGger:EXTernal:SYNChronize:OUTPut?')
		return Conversions.str_to_bool(response)

	def set_output(self, trig_sync_outp_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:TRIGger:EXTernal:SYNChronize:OUTPut \n
		Snippet: driver.source.bb.ofdm.trigger.external.synchronize.set_output(trig_sync_outp_state = False) \n
		Enables signal output synchronous to the trigger event. \n
			:param trig_sync_outp_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(trig_sync_outp_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:TRIGger:EXTernal:SYNChronize:OUTPut {param}')
