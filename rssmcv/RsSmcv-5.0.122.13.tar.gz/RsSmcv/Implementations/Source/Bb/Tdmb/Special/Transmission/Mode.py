from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def get_select(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TRANsmission:MODE:SELECT \n
		Snippet: value: int = driver.source.bb.tdmb.special.transmission.mode.get_select() \n
		Selects the transmission mode.
		This setting takes effect, if special settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:return: mode_select: integer Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:SPECial:TRANsmission:MODE:SELECT?')
		return Conversions.str_to_int(response)

	def set_select(self, mode_select: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TRANsmission:MODE:SELECT \n
		Snippet: driver.source.bb.tdmb.special.transmission.mode.set_select(mode_select = 1) \n
		Selects the transmission mode.
		This setting takes effect, if special settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:param mode_select: integer Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(mode_select)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:SPECial:TRANsmission:MODE:SELECT {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.TdmbSpecialTransmissionMode:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TRANsmission:MODE \n
		Snippet: value: enums.TdmbSpecialTransmissionMode = driver.source.bb.tdmb.special.transmission.mode.get_value() \n
		Sets the transmission mode.
		This setting takes effect, if special settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:return: trans_mode: MID| MANual
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:SPECial:TRANsmission:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TdmbSpecialTransmissionMode)

	def set_value(self, trans_mode: enums.TdmbSpecialTransmissionMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:[SPECial]:TRANsmission:MODE \n
		Snippet: driver.source.bb.tdmb.special.transmission.mode.set_value(trans_mode = enums.TdmbSpecialTransmissionMode.MANual) \n
		Sets the transmission mode.
		This setting takes effect, if special settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:param trans_mode: MID| MANual
		"""
		param = Conversions.enum_scalar_to_str(trans_mode, enums.TdmbSpecialTransmissionMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:SPECial:TRANsmission:MODE {param}')
