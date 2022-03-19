from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ilength:
	"""Ilength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ilength", core, parent)

	def set(self, state: bool, vehicle=repcap.Vehicle.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:RPL:ILENgth \n
		Snippet: driver.source.bb.gnss.receiver.v.environment.rpl.ilength.set(state = False, vehicle = repcap.Vehicle.Default) \n
		If enabled, assumes roadside planes with infinite width. \n
			:param state: 1| ON| 0| OFF
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
		"""
		param = Conversions.bool_to_str(state)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:RPL:ILENgth {param}')

	def get(self, vehicle=repcap.Vehicle.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RECeiver:[V<ST>]:ENVironment:RPL:ILENgth \n
		Snippet: value: bool = driver.source.bb.gnss.receiver.v.environment.rpl.ilength.get(vehicle = repcap.Vehicle.Default) \n
		If enabled, assumes roadside planes with infinite width. \n
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:return: state: 1| ON| 0| OFF"""
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RECeiver:V{vehicle_cmd_val}:ENVironment:RPL:ILENgth?')
		return Conversions.str_to_bool(response)
