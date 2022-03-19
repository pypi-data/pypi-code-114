from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mute:
	"""Mute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mute", core, parent)

	def get_bootstrap(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:MUTE:[BOOTstrap] \n
		Snippet: value: bool = driver.source.bb.a3Tsc.delay.mute.get_bootstrap() \n
		If enabled, replaces the bootstrap by a null signal (no output power) . \n
			:return: mute_bootstrap: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:DELay:MUTE:BOOTstrap?')
		return Conversions.str_to_bool(response)

	def set_bootstrap(self, mute_bootstrap: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:DELay:MUTE:[BOOTstrap] \n
		Snippet: driver.source.bb.a3Tsc.delay.mute.set_bootstrap(mute_bootstrap = False) \n
		If enabled, replaces the bootstrap by a null signal (no output power) . \n
			:param mute_bootstrap: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(mute_bootstrap)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:DELay:MUTE:BOOTstrap {param}')
