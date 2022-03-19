from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Predefined:
	"""Predefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("predefined", core, parent)

	def set(self, predefined_env: enums.ObscModelVertObst, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:VOBS:PREDefined \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.vobs.predefined.set(predefined_env = enums.ObscModelVertObst.URB1, vehicle = repcap.Vehicle.Default) \n
		Loads a predefined environment configuration. You can load a user-defined setting or a predefined settings that simulate
		two urban canyon environments. \n
			:param predefined_env: USER| URB1| URB2 USER User-defined environment configuration URB1|URB2 Urban canyon environment configuration
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(predefined_env, enums.ObscModelVertObst)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:VOBS:PREDefined {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.ObscModelVertObst:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:VOBS:PREDefined \n
		Snippet: value: enums.ObscModelVertObst = driver.source.bb.gnss.receiver.v.environment.vobs.predefined.get(vehicle = repcap.Vehicle.Default) \n
		Loads a predefined environment configuration. You can load a user-defined setting or a predefined settings that simulate
		two urban canyon environments. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: predefined_env: USER| URB1| URB2 USER User-defined environment configuration URB1|URB2 Urban canyon environment configuration"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:VOBS:PREDefined?')
		return Conversions.str_to_scalar_enum(response, enums.ObscModelVertObst)
