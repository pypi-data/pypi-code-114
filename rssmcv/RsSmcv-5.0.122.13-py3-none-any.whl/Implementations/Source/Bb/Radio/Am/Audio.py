from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Audio:
	"""Audio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audio", core, parent)

	def get_af(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:AUDio:AF \n
		Snippet: value: bool = driver.source.bb.radio.am.audio.get_af() \n
		Enables or disables the audio channel. \n
			:return: audio: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:AUDio:AF?')
		return Conversions.str_to_bool(response)

	def set_af(self, audio: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:AUDio:AF \n
		Snippet: driver.source.bb.radio.am.audio.set_af(audio = False) \n
		Enables or disables the audio channel. \n
			:param audio: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(audio)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:AUDio:AF {param}')
