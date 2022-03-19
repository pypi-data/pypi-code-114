from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dm:
	"""Dm commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dm", core, parent)

	def get_filter_py(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:PROGress:MCODer:DM:FILTer \n
		Snippet: value: int = driver.source.bb.progress.mcoder.dm.get_filter_py() \n
		Queries the status of an applied offline filtering, like for example during the calculation of a waveform and a multi
		carrier waveform file. \n
			:return: filter_py: integer Indicates the task progress in percent Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PROGress:MCODer:DM:FILTer?')
		return Conversions.str_to_int(response)

	def get_sub(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:PROGress:MCODer:DM:SUB \n
		Snippet: value: int = driver.source.bb.progress.mcoder.dm.get_sub() \n
		No command help available \n
			:return: sub: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PROGress:MCODer:DM:SUB?')
		return Conversions.str_to_int(response)
