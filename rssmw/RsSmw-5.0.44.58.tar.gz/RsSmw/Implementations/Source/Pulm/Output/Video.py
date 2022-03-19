from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Video:
	"""Video commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("video", core, parent)

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormalInverted:
		"""SCPI: [SOURce<HW>]:PULM:OUTPut:VIDeo:POLarity \n
		Snippet: value: enums.NormalInverted = driver.source.pulm.output.video.get_polarity() \n
		Sets the polarity of the pulse video (modulating) signal, related to the RF (modulated) signal. \n
			:return: polarity: NORMal| INVerted NORMal the video signal follows the RF signal, that means it is high wihen RF signal is high and vice versa. INVerted the video signal follows in inverted mode.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:OUTPut:VIDeo:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)

	def set_polarity(self, polarity: enums.NormalInverted) -> None:
		"""SCPI: [SOURce<HW>]:PULM:OUTPut:VIDeo:POLarity \n
		Snippet: driver.source.pulm.output.video.set_polarity(polarity = enums.NormalInverted.INVerted) \n
		Sets the polarity of the pulse video (modulating) signal, related to the RF (modulated) signal. \n
			:param polarity: NORMal| INVerted NORMal the video signal follows the RF signal, that means it is high wihen RF signal is high and vice versa. INVerted the video signal follows in inverted mode.
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.NormalInverted)
		self._core.io.write(f'SOURce<HwInstance>:PULM:OUTPut:VIDeo:POLarity {param}')
