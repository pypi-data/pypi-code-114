from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Height:
	"""Height commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("height", core, parent)

	def set(self, heigth: float, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:RPL:ROFFset:HEIGht \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.rpl.roffset.height.set(heigth = 1.0, vehicle = repcap.Vehicle.Default) \n
		Sets the receiver height offset, i.e. the antenna altitude relative to the ground. \n
			:param heigth: float Range: 0 to 500
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.decimal_value_to_str(heigth)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:RPL:ROFFset:HEIGht {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:RPL:ROFFset:HEIGht \n
		Snippet: value: float = driver.source.bb.gnss.receiver.v.environment.rpl.roffset.height.get(vehicle = repcap.Vehicle.Default) \n
		Sets the receiver height offset, i.e. the antenna altitude relative to the ground. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: heigth: float Range: 0 to 500"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:RPL:ROFFset:HEIGht?')
		return Conversions.str_to_float(response)
