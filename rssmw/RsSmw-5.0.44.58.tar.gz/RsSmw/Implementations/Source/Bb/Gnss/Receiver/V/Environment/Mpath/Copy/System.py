from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	def set(self, system_source: enums.Hybrid, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:MPATh:COPY:SYSTem \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.mpath.copy.system.set(system_source = enums.Hybrid.BEIDou, vehicle = repcap.Vehicle.Default) \n
		Sets the GNSS system. If the copy to function is used, this setting refers to the target. \n
			:param system_source: GPS| GALileo| GLONass| BEIDou| QZSS| SBAS
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.enum_scalar_to_str(system_source, enums.Hybrid)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:MPATh:COPY:SYSTem {param}')

	# noinspection PyTypeChecker
	def get(self, vehicle=repcap.Vehicle.Default) -> enums.Hybrid:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:MPATh:COPY:SYSTem \n
		Snippet: value: enums.Hybrid = driver.source.bb.gnss.receiver.v.environment.mpath.copy.system.get(vehicle = repcap.Vehicle.Default) \n
		Sets the GNSS system. If the copy to function is used, this setting refers to the target. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: system_source: GPS| GALileo| GLONass| BEIDou| QZSS| SBAS"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:MPATh:COPY:SYSTem?')
		return Conversions.str_to_scalar_enum(response, enums.Hybrid)
