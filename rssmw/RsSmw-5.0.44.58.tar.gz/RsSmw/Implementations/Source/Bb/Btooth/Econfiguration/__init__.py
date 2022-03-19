from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Econfiguration:
	"""Econfiguration commands group definition. 137 total commands, 4 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("econfiguration", core, parent)

	@property
	def actable(self):
		"""actable commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_actable'):
			from .Actable import Actable
			self._actable = Actable(self._core, self._cmd_group)
		return self._actable

	@property
	def dcTable(self):
		"""dcTable commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcTable'):
			from .DcTable import DcTable
			self._dcTable = DcTable(self._core, self._cmd_group)
		return self._dcTable

	@property
	def ltKey(self):
		"""ltKey commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ltKey'):
			from .LtKey import LtKey
			self._ltKey = LtKey(self._core, self._cmd_group)
		return self._ltKey

	@property
	def pconfiguration(self):
		"""pconfiguration commands group. 45 Sub-classes, 52 commands."""
		if not hasattr(self, '_pconfiguration'):
			from .Pconfiguration import Pconfiguration
			self._pconfiguration = Pconfiguration(self._core, self._cmd_group)
		return self._pconfiguration

	def get_ad_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:ADINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.get_ad_interval() \n
		Sets the time interval between two consecutive advertising events for packet type 'ADV_DIRECT_IND' and duty cycle high.
		Command sets the values in ms. Query returns values in s. \n
			:return: ad_interval: float Range: 1.05E-3 s to 3.75E-3 s , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:ADINterval?')
		return Conversions.str_to_float(response)

	def set_ad_interval(self, ad_interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:ADINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.set_ad_interval(ad_interval = 1.0) \n
		Sets the time interval between two consecutive advertising events for packet type 'ADV_DIRECT_IND' and duty cycle high.
		Command sets the values in ms. Query returns values in s. \n
			:param ad_interval: float Range: 1.05E-3 s to 3.75E-3 s , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(ad_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:ADINterval {param}')

	def get_ae_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:AEDelay \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.get_ae_delay() \n
		Sets a time delay between the start times of two consecutive advertising events. The value is added to the advertising
		event interval. Command sets the values in ms. Query returns values in s. \n
			:return: ae_delay: float Range: 0 s to 10E-3 s , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:AEDelay?')
		return Conversions.str_to_float(response)

	def set_ae_delay(self, ae_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:AEDelay \n
		Snippet: driver.source.bb.btooth.econfiguration.set_ae_delay(ae_delay = 1.0) \n
		Sets a time delay between the start times of two consecutive advertising events. The value is added to the advertising
		event interval. Command sets the values in ms. Query returns values in s. \n
			:param ae_delay: float Range: 0 s to 10E-3 s , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(ae_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:AEDelay {param}')

	def get_ae_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:AEINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.get_ae_interval() \n
		Sets the time interval between two consecutive advertising events, with regard to the starting points. Command sets the
		values in ms. Query returns values in s. \n
			:return: ae_interval: float Range: 5E-3 s to depends on oversampling , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:AEINterval?')
		return Conversions.str_to_float(response)

	def set_ae_interval(self, ae_interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:AEINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.set_ae_interval(ae_interval = 1.0) \n
		Sets the time interval between two consecutive advertising events, with regard to the starting points. Command sets the
		values in ms. Query returns values in s. \n
			:param ae_interval: float Range: 5E-3 s to depends on oversampling , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(ae_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:AEINterval {param}')

	def get_ap_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:APINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.get_ap_interval() \n
		Sets the time interval between packets starting points of two consecutive packets in the advertising channel. \n
			:return: ap_interval: float Range: 1.3E-3 to 28E-3, Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:APINterval?')
		return Conversions.str_to_float(response)

	def set_ap_interval(self, ap_interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:APINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.set_ap_interval(ap_interval = 1.0) \n
		Sets the time interval between packets starting points of two consecutive packets in the advertising channel. \n
			:param ap_interval: float Range: 1.3E-3 to 28E-3, Unit: ms
		"""
		param = Conversions.decimal_value_to_str(ap_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:APINterval {param}')

	# noinspection PyTypeChecker
	def get_lc_mode(self) -> enums.BtoLlCnctMod:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:LCMode \n
		Snippet: value: enums.BtoLlCnctMod = driver.source.bb.btooth.econfiguration.get_lc_mode() \n
		Selects the link layer connection mode. In order to provide safe transmission of payload data, the data in the packet can
		be encrypted. If activated, the payload data follows MIC (Message authentication Code) . \n
			:return: lc_mode: UENC| ENC UENC Payload data is transmitted without encoding. ENC The link layer connection runs in encrypted mode.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:LCMode?')
		return Conversions.str_to_scalar_enum(response, enums.BtoLlCnctMod)

	def set_lc_mode(self, lc_mode: enums.BtoLlCnctMod) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:LCMode \n
		Snippet: driver.source.bb.btooth.econfiguration.set_lc_mode(lc_mode = enums.BtoLlCnctMod.ENC) \n
		Selects the link layer connection mode. In order to provide safe transmission of payload data, the data in the packet can
		be encrypted. If activated, the payload data follows MIC (Message authentication Code) . \n
			:param lc_mode: UENC| ENC UENC Payload data is transmitted without encoding. ENC The link layer connection runs in encrypted mode.
		"""
		param = Conversions.enum_scalar_to_str(lc_mode, enums.BtoLlCnctMod)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:LCMode {param}')

	def get_pnumber(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PNUMber \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.get_pnumber() \n
		Sets the number of Tx packets per event. Each connection contains at least one data channel packet. The maximum number of
		packets per event is determined by the duration of the connection event interval. \n
			:return: pnumber: integer Range: 1 to depends on connection event interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PNUMber?')
		return Conversions.str_to_int(response)

	def set_pnumber(self, pnumber: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PNUMber \n
		Snippet: driver.source.bb.btooth.econfiguration.set_pnumber(pnumber = 1) \n
		Sets the number of Tx packets per event. Each connection contains at least one data channel packet. The maximum number of
		packets per event is determined by the duration of the connection event interval. \n
			:param pnumber: integer Range: 1 to depends on connection event interval
		"""
		param = Conversions.decimal_value_to_str(pnumber)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PNUMber {param}')

	def get_sdci(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:SDCI \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.get_sdci() \n
		Queries the number of the first active data channel. \n
			:return: selected_channel: integer Range: 0 to 36
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:SDCI?')
		return Conversions.str_to_int(response)

	def get_sinterval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:SINTerval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.get_sinterval() \n
		Sets the time interval between the starting points of two consecutive windows during which the scanner is operating in an
		advertising channel. Command sets the values in ms. Query returns values in s. \n
			:return: sinterval: float Range: 10E-3 s to depends on oversampling and the number of advertsing channel table states , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:SINTerval?')
		return Conversions.str_to_float(response)

	def set_sinterval(self, sinterval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:SINTerval \n
		Snippet: driver.source.bb.btooth.econfiguration.set_sinterval(sinterval = 1.0) \n
		Sets the time interval between the starting points of two consecutive windows during which the scanner is operating in an
		advertising channel. Command sets the values in ms. Query returns values in s. \n
			:param sinterval: float Range: 10E-3 s to depends on oversampling and the number of advertsing channel table states , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(sinterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:SINTerval {param}')

	def get_swindow(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:SWINdow \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.get_swindow() \n
		Sets the length of the window during which the scanner is operating in the advertising channel. Note that the scan window
		is less or equal to the value of the scan interval. Command sets the values in ms. Query returns values in s. \n
			:return: swindow: float Range: 10E-3 s to 10240E-3 s , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:SWINdow?')
		return Conversions.str_to_float(response)

	def set_swindow(self, swindow: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:SWINdow \n
		Snippet: driver.source.bb.btooth.econfiguration.set_swindow(swindow = 1.0) \n
		Sets the length of the window during which the scanner is operating in the advertising channel. Note that the scan window
		is less or equal to the value of the scan interval. Command sets the values in ms. Query returns values in s. \n
			:param swindow: float Range: 10E-3 s to 10240E-3 s , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(swindow)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:SWINdow {param}')

	def get_wo_info(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:WOINfo \n
		Snippet: value: str = driver.source.bb.btooth.econfiguration.get_wo_info() \n
		Requires data event and advertising frame configuration with the packet type CONNECT_IND. Queries the start point of the
		transmit window. \n
			:return: wo_info: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:WOINfo?')
		return trim_str_response(response)

	def get_ws_info(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:WSINfo \n
		Snippet: value: str = driver.source.bb.btooth.econfiguration.get_ws_info() \n
		Requires data event and advertising frame configuration with the packet type CONNECT_IND. Queries the size of the
		transmit window, regarding to the start point. \n
			:return: ws_info: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:WSINfo?')
		return trim_str_response(response)

	def clone(self) -> 'Econfiguration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Econfiguration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
