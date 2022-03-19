from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nfc:
	"""Nfc commands group definition. 192 total commands, 10 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nfc", core, parent)

	@property
	def cblock(self):
		"""cblock commands group. 107 Sub-classes, 2 commands."""
		if not hasattr(self, '_cblock'):
			from .Cblock import Cblock
			self._cblock = Cblock(self._core, self._cmd_group)
		return self._cblock

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clipping'):
			from .Clipping import Clipping
			self._clipping = Clipping(self._core, self._cmd_group)
		return self._clipping

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def mset(self):
		"""mset commands group. 0 Sub-classes, 13 commands."""
		if not hasattr(self, '_mset'):
			from .Mset import Mset
			self._mset = Mset(self._core, self._cmd_group)
		return self._mset

	@property
	def pred(self):
		"""pred commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_pred'):
			from .Pred import Pred
			self._pred = Pred(self._core, self._cmd_group)
		return self._pred

	@property
	def sconfiguration(self):
		"""sconfiguration commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sconfiguration'):
			from .Sconfiguration import Sconfiguration
			self._sconfiguration = Sconfiguration(self._core, self._cmd_group)
		return self._sconfiguration

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def trigger(self):
		"""trigger commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def uaiSetting(self):
		"""uaiSetting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uaiSetting'):
			from .UaiSetting import UaiSetting
			self._uaiSetting = UaiSetting(self._core, self._cmd_group)
		return self._uaiSetting

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	def set_cc_block(self, cc_block: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CCBLock \n
		Snippet: driver.source.bb.nfc.set_cc_block(cc_block = 1) \n
		Copies a command block for later use. \n
			:param cc_block: integer Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(cc_block)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CCBLock {param}')

	def set_dc_block(self, dc_block: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:DCBLock \n
		Snippet: driver.source.bb.nfc.set_dc_block(dc_block = 1) \n
		Removes a command block from the command sequence. \n
			:param dc_block: integer Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(dc_block)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:DCBLock {param}')

	# noinspection PyTypeChecker
	def get_divisor(self) -> enums.NfcDivForMod:
		"""SCPI: [SOURce<HW>]:BB:NFC:DIVisor \n
		Snippet: value: enums.NfcDivForMod = driver.source.bb.nfc.get_divisor() \n
		Selects the divisor and thus the datarate for technology NFC-F. \n
			:return: div_for_mod: DIV2| DIV4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:DIVisor?')
		return Conversions.str_to_scalar_enum(response, enums.NfcDivForMod)

	def set_divisor(self, div_for_mod: enums.NfcDivForMod) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:DIVisor \n
		Snippet: driver.source.bb.nfc.set_divisor(div_for_mod = enums.NfcDivForMod.DIV2) \n
		Selects the divisor and thus the datarate for technology NFC-F. \n
			:param div_for_mod: DIV2| DIV4
		"""
		param = Conversions.enum_scalar_to_str(div_for_mod, enums.NfcDivForMod)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:DIVisor {param}')

	def get_dvoltage(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:DVOLtage \n
		Snippet: value: float = driver.source.bb.nfc.get_dvoltage() \n
		Sets the desired voltage in unmodulated signal parts. \n
			:return: dvoltage: float Range: 0.020 to 1.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:DVOLtage?')
		return Conversions.str_to_float(response)

	def set_dvoltage(self, dvoltage: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:DVOLtage \n
		Snippet: driver.source.bb.nfc.set_dvoltage(dvoltage = 1.0) \n
		Sets the desired voltage in unmodulated signal parts. \n
			:param dvoltage: float Range: 0.020 to 1.5
		"""
		param = Conversions.decimal_value_to_str(dvoltage)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:DVOLtage {param}')

	def set_ic_block(self, ic_block: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:ICBLock \n
		Snippet: driver.source.bb.nfc.set_ic_block(ic_block = 1) \n
		Inserts a default command block before the selected command block. The command block with this position must be existing,
		otherwise an error is returned. \n
			:param ic_block: integer Range: 1 to 99
		"""
		param = Conversions.decimal_value_to_str(ic_block)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:ICBLock {param}')

	def set_pc_block(self, pc_block: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:PCBLock \n
		Snippet: driver.source.bb.nfc.set_pc_block(pc_block = 1) \n
		Pastes a command block (which was copied before) at the given position into the command sequence. \n
			:param pc_block: integer Range: 1 to 99
		"""
		param = Conversions.decimal_value_to_str(pc_block)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:PCBLock {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:PRESet \n
		Snippet: driver.source.bb.nfc.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:NFC:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:PRESet \n
		Snippet: driver.source.bb.nfc.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command SOURce<hw>:BB:NFC:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:NFC:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:STATe \n
		Snippet: value: bool = driver.source.bb.nfc.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:STATe \n
		Snippet: driver.source.bb.nfc.set_state(state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:STATe {param}')

	# noinspection PyTypeChecker
	def get_technology(self) -> enums.NfcProtocolMode:
		"""SCPI: [SOURce<HW>]:BB:NFC:TECHnology \n
		Snippet: value: enums.NfcProtocolMode = driver.source.bb.nfc.get_technology() \n
		Selects the NFC/EMV technology. \n
			:return: protocol: NFCA| NFCB| NFCF| EMVA| EMVB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TECHnology?')
		return Conversions.str_to_scalar_enum(response, enums.NfcProtocolMode)

	def set_technology(self, protocol: enums.NfcProtocolMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TECHnology \n
		Snippet: driver.source.bb.nfc.set_technology(protocol = enums.NfcProtocolMode.EMVA) \n
		Selects the NFC/EMV technology. \n
			:param protocol: NFCA| NFCB| NFCF| EMVA| EMVB
		"""
		param = Conversions.enum_scalar_to_str(protocol, enums.NfcProtocolMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TECHnology {param}')

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.NfcTransMode:
		"""SCPI: [SOURce<HW>]:BB:NFC:TMODe \n
		Snippet: value: enums.NfcTransMode = driver.source.bb.nfc.get_tmode() \n
		Selects the transmission mode. \n
			:return: transmission: POLL| LISTen
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.NfcTransMode)

	def set_tmode(self, transmission: enums.NfcTransMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TMODe \n
		Snippet: driver.source.bb.nfc.set_tmode(transmission = enums.NfcTransMode.LISTen) \n
		Selects the transmission mode. \n
			:param transmission: POLL| LISTen
		"""
		param = Conversions.enum_scalar_to_str(transmission, enums.NfcTransMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TMODe {param}')

	def get_up_voltage(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:UPVoltage \n
		Snippet: value: int = driver.source.bb.nfc.get_up_voltage() \n
		Displays the ratio of the voltage in the unmodulated parts of the signal to its peak value. \n
			:return: up_voltage: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:UPVoltage?')
		return Conversions.str_to_int(response)

	def get_version(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NFC:VERSion \n
		Snippet: value: str = driver.source.bb.nfc.get_version() \n
		Queries the version of the NFC-Forum and EMVCo specifications used for the signal generation. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Nfc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nfc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
