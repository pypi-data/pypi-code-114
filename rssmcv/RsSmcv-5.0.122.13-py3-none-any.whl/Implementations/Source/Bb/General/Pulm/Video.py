from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Video:
	"""Video commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("video", core, parent)

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormalInverted:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:VIDeo:POLarity \n
		Snippet: value: enums.NormalInverted = driver.source.bb.general.pulm.video.get_polarity() \n
		Sets the video polarity. \n
			:return: puls_video_pol: NORMal| INVerted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:VIDeo:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)

	def set_polarity(self, puls_video_pol: enums.NormalInverted) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:VIDeo:POLarity \n
		Snippet: driver.source.bb.general.pulm.video.set_polarity(puls_video_pol = enums.NormalInverted.INVerted) \n
		Sets the video polarity. \n
			:param puls_video_pol: NORMal| INVerted
		"""
		param = Conversions.enum_scalar_to_str(puls_video_pol, enums.NormalInverted)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:VIDeo:POLarity {param}')
