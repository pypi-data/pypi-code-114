from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfOff:
	"""RfOff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfOff", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PowAttRfOffMode:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:RFOFf:MODE \n
		Snippet: value: enums.PowAttRfOffMode = driver.source.power.attenuation.rfOff.get_mode() \n
		Selects the state the attenuator is to assume if the RF signal is switched off. \n
			:return: mode: UNCHanged| FATTenuation FATTenuation The step attenuator switches to maximum attenuation when RF is off. Note: This setting overrides the RF level modes method RsSmw.Output.amodeFIXed|MANual. UNCHanged Freezes the current setting to keep the output impedance constant during RF off.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ATTenuation:RFOFf:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowAttRfOffMode)

	def set_mode(self, mode: enums.PowAttRfOffMode) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:RFOFf:MODE \n
		Snippet: driver.source.power.attenuation.rfOff.set_mode(mode = enums.PowAttRfOffMode.FATTenuation) \n
		Selects the state the attenuator is to assume if the RF signal is switched off. \n
			:param mode: UNCHanged| FATTenuation FATTenuation The step attenuator switches to maximum attenuation when RF is off. Note: This setting overrides the RF level modes method RsSmw.Output.amodeFIXed|MANual. UNCHanged Freezes the current setting to keep the output impedance constant during RF off.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowAttRfOffMode)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ATTenuation:RFOFf:MODE {param}')
