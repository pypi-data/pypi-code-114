from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bootstrap:
	"""Bootstrap commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bootstrap", core, parent)

	# noinspection PyTypeChecker
	def get_eas(self) -> enums.Atsc30EmergencyAlertSignaling:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:BOOTstrap:EAS \n
		Snippet: value: enums.Atsc30EmergencyAlertSignaling = driver.source.bb.a3Tsc.special.bootstrap.get_eas() \n
		Sets the signaling for emergency alert. \n
			:return: eas: SET3| SET2| NOEMergency| SET1 | NOEMergency| SET1| SET2| SET3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SPECial:BOOTstrap:EAS?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30EmergencyAlertSignaling)

	def set_eas(self, eas: enums.Atsc30EmergencyAlertSignaling) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:BOOTstrap:EAS \n
		Snippet: driver.source.bb.a3Tsc.special.bootstrap.set_eas(eas = enums.Atsc30EmergencyAlertSignaling.NOEMergency) \n
		Sets the signaling for emergency alert. \n
			:param eas: SET3| SET2| NOEMergency| SET1 | NOEMergency| SET1| SET2| SET3
		"""
		param = Conversions.enum_scalar_to_str(eas, enums.Atsc30EmergencyAlertSignaling)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SPECial:BOOTstrap:EAS {param}')

	def get_minor(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:BOOTstrap:MINor \n
		Snippet: value: int = driver.source.bb.a3Tsc.special.bootstrap.get_minor() \n
		Sets the minor version number of the bootstrap. \n
			:return: minor_version: integer Range: 0 to 7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SPECial:BOOTstrap:MINor?')
		return Conversions.str_to_int(response)

	def set_minor(self, minor_version: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:BOOTstrap:MINor \n
		Snippet: driver.source.bb.a3Tsc.special.bootstrap.set_minor(minor_version = 1) \n
		Sets the minor version number of the bootstrap. \n
			:param minor_version: integer Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(minor_version)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SPECial:BOOTstrap:MINor {param}')
