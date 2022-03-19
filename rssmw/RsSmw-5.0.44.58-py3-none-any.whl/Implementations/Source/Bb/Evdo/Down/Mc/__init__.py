from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mc:
	"""Mc commands group definition. 7 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mc", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	# noinspection PyTypeChecker
	def get_bclass(self) -> enums.EvdoBandClass:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:BCLass \n
		Snippet: value: enums.EvdoBandClass = driver.source.bb.evdo.down.mc.get_bclass() \n
		Selects the band class for operation, as defined in 3GPP2 C.S0057-E. BC17 is supported in downlink only. \n
			:return: band_class: BC0| BC1| BC2| BC3| BC4| BC5| BC6| BC7| BC8| BC9| BC10| BC11| BC12| BC13| BC14| BC15| BC16| BC17| BC18| BC19| BC20| BC21
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:DOWN:MC:BCLass?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoBandClass)

	def set_bclass(self, band_class: enums.EvdoBandClass) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:BCLass \n
		Snippet: driver.source.bb.evdo.down.mc.set_bclass(band_class = enums.EvdoBandClass.BC0) \n
		Selects the band class for operation, as defined in 3GPP2 C.S0057-E. BC17 is supported in downlink only. \n
			:param band_class: BC0| BC1| BC2| BC3| BC4| BC5| BC6| BC7| BC8| BC9| BC10| BC11| BC12| BC13| BC14| BC15| BC16| BC17| BC18| BC19| BC20| BC21
		"""
		param = Conversions.enum_scalar_to_str(band_class, enums.EvdoBandClass)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:DOWN:MC:BCLass {param}')

	def get_cdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:CDELay \n
		Snippet: value: float = driver.source.bb.evdo.down.mc.get_cdelay() \n
		Sets a delay to each active carrier. \n
			:return: carrier_delay: float Range: 0 to 10E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:DOWN:MC:CDELay?')
		return Conversions.str_to_float(response)

	def set_cdelay(self, carrier_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:CDELay \n
		Snippet: driver.source.bb.evdo.down.mc.set_cdelay(carrier_delay = 1.0) \n
		Sets a delay to each active carrier. \n
			:param carrier_delay: float Range: 0 to 10E-6
		"""
		param = Conversions.decimal_value_to_str(carrier_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:DOWN:MC:CDELay {param}')

	def get_cfrequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:CFRequency \n
		Snippet: value: int = driver.source.bb.evdo.down.mc.get_cfrequency() \n
		Queries the center frequency of the band resulting from the set active carriers. \n
			:return: center_frequency: integer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:DOWN:MC:CFRequency?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:STATe \n
		Snippet: value: bool = driver.source.bb.evdo.down.mc.get_state() \n
		Enables or disables multi-carrier operation. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:DOWN:MC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:STATe \n
		Snippet: driver.source.bb.evdo.down.mc.set_state(state = False) \n
		Enables or disables multi-carrier operation. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:DOWN:MC:STATe {param}')

	def clone(self) -> 'Mc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
