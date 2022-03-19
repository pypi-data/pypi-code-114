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
		"""SCPI: [SOURce<HW>]:BB:C2K:TRIGger:EXTernal:SYNChronize:OUTPut \n
		Snippet: value: bool = driver.source.bb.c2K.trigger.external.synchronize.get_output() \n
		Enables signal output synchronous to the trigger event. \n
			:return: output: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:TRIGger:EXTernal:SYNChronize:OUTPut?')
		return Conversions.str_to_bool(response)

	def set_output(self, output: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:TRIGger:EXTernal:SYNChronize:OUTPut \n
		Snippet: driver.source.bb.c2K.trigger.external.synchronize.set_output(output = False) \n
		Enables signal output synchronous to the trigger event. \n
			:param output: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(output)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:TRIGger:EXTernal:SYNChronize:OUTPut {param}')
