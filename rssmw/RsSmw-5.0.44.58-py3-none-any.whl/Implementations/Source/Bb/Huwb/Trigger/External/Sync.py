from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	def get_output(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:SYNC:OUTPut \n
		Snippet: value: bool = driver.source.bb.huwb.trigger.external.sync.get_output() \n
		Enables signal output synchronous to the trigger event. \n
			:return: output: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:SYNC:OUTPut?')
		return Conversions.str_to_bool(response)

	def set_output(self, output: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:SYNC:OUTPut \n
		Snippet: driver.source.bb.huwb.trigger.external.sync.set_output(output = False) \n
		Enables signal output synchronous to the trigger event. \n
			:param output: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(output)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:SYNC:OUTPut {param}')
