from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hopping", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadHoppMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:HOPPing:MODE \n
		Snippet: value: enums.FadHoppMode = driver.source.fsimulator.hopping.get_mode() \n
		This is a password-protected function. Unlock the protection level 1 to access it. See method RsSmw.System.Protect.State.
		set. Activates frequency hopping and determines how fading is resumed after a frequency hop. Note: Activate list mode and
		load the frequency table befor activating frequency hopping. \n
			:return: mode: OFF| IBANd| OOBand OFF Frequency hopping is deactivated. IBANd Activates an in-band frequency hopping. OOBand Activates an out of band frequency hopping.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HOPPing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadHoppMode)

	def set_mode(self, mode: enums.FadHoppMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HOPPing:MODE \n
		Snippet: driver.source.fsimulator.hopping.set_mode(mode = enums.FadHoppMode.IBANd) \n
		This is a password-protected function. Unlock the protection level 1 to access it. See method RsSmw.System.Protect.State.
		set. Activates frequency hopping and determines how fading is resumed after a frequency hop. Note: Activate list mode and
		load the frequency table befor activating frequency hopping. \n
			:param mode: OFF| IBANd| OOBand OFF Frequency hopping is deactivated. IBANd Activates an in-band frequency hopping. OOBand Activates an out of band frequency hopping.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadHoppMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HOPPing:MODE {param}')
