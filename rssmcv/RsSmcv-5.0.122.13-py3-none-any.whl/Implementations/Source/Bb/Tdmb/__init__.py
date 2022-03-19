from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdmb:
	"""Tdmb commands group definition. 34 total commands, 9 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdmb", core, parent)

	@property
	def dataRate(self):
		"""dataRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dataRate'):
			from .DataRate import DataRate
			self._dataRate = DataRate(self._core, self._cmd_group)
		return self._dataRate

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def prbs(self):
		"""prbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbs'):
			from .Prbs import Prbs
			self._prbs = Prbs(self._core, self._cmd_group)
		return self._prbs

	@property
	def protection(self):
		"""protection commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_protection'):
			from .Protection import Protection
			self._protection = Protection(self._core, self._cmd_group)
		return self._protection

	@property
	def scid(self):
		"""scid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scid'):
			from .Scid import Scid
			self._scid = Scid(self._core, self._cmd_group)
		return self._scid

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def tii(self):
		"""tii commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tii'):
			from .Tii import Tii
			self._tii = Tii(self._core, self._cmd_group)
		return self._tii

	@property
	def special(self):
		"""special commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_special'):
			from .Special import Special
			self._special = Special(self._core, self._cmd_group)
		return self._special

	# noinspection PyTypeChecker
	def get_eti_input(self) -> enums.TdmbInputSignalEtiSignal:
		"""SCPI: [SOURce<HW>]:BB:TDMB:ETIinput \n
		Snippet: value: enums.TdmbInputSignalEtiSignal = driver.source.bb.tdmb.get_eti_input() \n
		Displays whether a valid ETI signal is present and the signal type. \n
			:return: eti_signal: INValid| ENI| E559| E537
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:ETIinput?')
		return Conversions.str_to_scalar_enum(response, enums.TdmbInputSignalEtiSignal)

	def get_mid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:MID \n
		Snippet: value: int = driver.source.bb.tdmb.get_mid() \n
		Displays the DAB mode identity. A mode identity of 0 corresponds to an invalid ETI signal. \n
			:return: mode_identity: integer Range: 0 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:MID?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_net(self) -> enums.EnetworkMode:
		"""SCPI: [SOURce<HW>]:BB:TDMB:NET \n
		Snippet: value: enums.EnetworkMode = driver.source.bb.tdmb.get_net() \n
		Sets the network mode. \n
			:return: network_mode: MFN| SFN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:NET?')
		return Conversions.str_to_scalar_enum(response, enums.EnetworkMode)

	def set_net(self, network_mode: enums.EnetworkMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:NET \n
		Snippet: driver.source.bb.tdmb.set_net(network_mode = enums.EnetworkMode.MFN) \n
		Sets the network mode. \n
			:param network_mode: MFN| SFN
		"""
		param = Conversions.enum_scalar_to_str(network_mode, enums.EnetworkMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:NET {param}')

	def get_nst(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TDMB:NST \n
		Snippet: value: int = driver.source.bb.tdmb.get_nst() \n
		Displays the number of streams (NST) contained in the ETI signal. \n
			:return: num_of_streams: integer Range: 0 to 64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:NST?')
		return Conversions.str_to_int(response)

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:PRESet \n
		Snippet: driver.source.bb.tdmb.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:TDMB:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:PRESet \n
		Snippet: driver.source.bb.tdmb.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:TDMB:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:TDMB:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.CodingInputSignalSource:
		"""SCPI: [SOURce<HW>]:BB:TDMB:SOURce \n
		Snippet: value: enums.CodingInputSignalSource = driver.source.bb.tdmb.get_source() \n
		Sets the modulation source for the input signal. \n
			:return: tdmb_source: EXTernal| TSPLayer| TESTsignal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalSource)

	def set_source(self, tdmb_source: enums.CodingInputSignalSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:SOURce \n
		Snippet: driver.source.bb.tdmb.set_source(tdmb_source = enums.CodingInputSignalSource.EXTernal) \n
		Sets the modulation source for the input signal. \n
			:param tdmb_source: EXTernal| TSPLayer| TESTsignal
		"""
		param = Conversions.enum_scalar_to_str(tdmb_source, enums.CodingInputSignalSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDMB:STATe \n
		Snippet: value: bool = driver.source.bb.tdmb.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:STATe \n
		Snippet: driver.source.bb.tdmb.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:STATe {param}')

	def clone(self) -> 'Tdmb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tdmb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
