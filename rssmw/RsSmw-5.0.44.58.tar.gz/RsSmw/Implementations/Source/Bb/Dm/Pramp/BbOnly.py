from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbOnly:
	"""BbOnly commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbOnly", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DM:PRAMp:BBONly:[STATe] \n
		Snippet: value: bool = driver.source.bb.dm.pramp.bbOnly.get_state() \n
		Enables power ramping in the baseband only or mixed power ramping in the baseband and the RF section. The ON setting is
		mandatory if, with power ramping active, only the baseband signal is output (I/Q outputs) . In case of two-path
		instruments, the ON setting is also mandatory if a baseband signal is applied to both paths. Only then can a signal with
		a defined, predictable level be output. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:PRAMp:BBONly:STATe?')
		return Conversions.str_to_bool(response)
