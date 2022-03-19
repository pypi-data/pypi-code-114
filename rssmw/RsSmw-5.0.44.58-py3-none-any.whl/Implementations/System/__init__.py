from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 201 total commands, 34 Subgroups, 30 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def beeper(self):
		"""beeper commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_beeper'):
			from .Beeper import Beeper
			self._beeper = Beeper(self._core, self._cmd_group)
		return self._beeper

	@property
	def bios(self):
		"""bios commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bios'):
			from .Bios import Bios
			self._bios = Bios(self._core, self._cmd_group)
		return self._bios

	@property
	def communicate(self):
		"""communicate commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .Communicate import Communicate
			self._communicate = Communicate(self._core, self._cmd_group)
		return self._communicate

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .Device import Device
			self._device = Device(self._core, self._cmd_group)
		return self._device

	@property
	def dexchange(self):
		"""dexchange commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_dexchange'):
			from .Dexchange import Dexchange
			self._dexchange = Dexchange(self._core, self._cmd_group)
		return self._dexchange

	@property
	def deviceFootprint(self):
		"""deviceFootprint commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_deviceFootprint'):
			from .DeviceFootprint import DeviceFootprint
			self._deviceFootprint = DeviceFootprint(self._core, self._cmd_group)
		return self._deviceFootprint

	@property
	def error(self):
		"""error commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_error'):
			from .Error import Error
			self._error = Error(self._core, self._cmd_group)
		return self._error

	@property
	def fpFpga(self):
		"""fpFpga commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpFpga'):
			from .FpFpga import FpFpga
			self._fpFpga = FpFpga(self._core, self._cmd_group)
		return self._fpFpga

	@property
	def fpreset(self):
		"""fpreset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpreset'):
			from .Fpreset import Fpreset
			self._fpreset = Fpreset(self._core, self._cmd_group)
		return self._fpreset

	@property
	def generic(self):
		"""generic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_generic'):
			from .Generic import Generic
			self._generic = Generic(self._core, self._cmd_group)
		return self._generic

	@property
	def help(self):
		"""help commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_help'):
			from .Help import Help
			self._help = Help(self._core, self._cmd_group)
		return self._help

	@property
	def identification(self):
		"""identification commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_identification'):
			from .Identification import Identification
			self._identification = Identification(self._core, self._cmd_group)
		return self._identification

	@property
	def information(self):
		"""information commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_information'):
			from .Information import Information
			self._information = Information(self._core, self._cmd_group)
		return self._information

	@property
	def linux(self):
		"""linux commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_linux'):
			from .Linux import Linux
			self._linux = Linux(self._core, self._cmd_group)
		return self._linux

	@property
	def lock(self):
		"""lock commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_lock'):
			from .Lock import Lock
			self._lock = Lock(self._core, self._cmd_group)
		return self._lock

	@property
	def massMemory(self):
		"""massMemory commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_massMemory'):
			from .MassMemory import MassMemory
			self._massMemory = MassMemory(self._core, self._cmd_group)
		return self._massMemory

	@property
	def ntp(self):
		"""ntp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ntp'):
			from .Ntp import Ntp
			self._ntp = Ntp(self._core, self._cmd_group)
		return self._ntp

	@property
	def option(self):
		"""option commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_option'):
			from .Option import Option
			self._option = Option(self._core, self._cmd_group)
		return self._option

	@property
	def package(self):
		"""package commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_package'):
			from .Package import Package
			self._package = Package(self._core, self._cmd_group)
		return self._package

	@property
	def pciFpga(self):
		"""pciFpga commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pciFpga'):
			from .PciFpga import PciFpga
			self._pciFpga = PciFpga(self._core, self._cmd_group)
		return self._pciFpga

	@property
	def profiling(self):
		"""profiling commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_profiling'):
			from .Profiling import Profiling
			self._profiling = Profiling(self._core, self._cmd_group)
		return self._profiling

	@property
	def protect(self):
		"""protect commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_protect'):
			from .Protect import Protect
			self._protect = Protect(self._core, self._cmd_group)
		return self._protect

	@property
	def reboot(self):
		"""reboot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reboot'):
			from .Reboot import Reboot
			self._reboot = Reboot(self._core, self._cmd_group)
		return self._reboot

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	@property
	def security(self):
		"""security commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_security'):
			from .Security import Security
			self._security = Security(self._core, self._cmd_group)
		return self._security

	@property
	def shutdown(self):
		"""shutdown commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shutdown'):
			from .Shutdown import Shutdown
			self._shutdown = Shutdown(self._core, self._cmd_group)
		return self._shutdown

	@property
	def specification(self):
		"""specification commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_specification'):
			from .Specification import Specification
			self._specification = Specification(self._core, self._cmd_group)
		return self._specification

	@property
	def srData(self):
		"""srData commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_srData'):
			from .SrData import SrData
			self._srData = SrData(self._core, self._cmd_group)
		return self._srData

	@property
	def srexec(self):
		"""srexec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srexec'):
			from .Srexec import Srexec
			self._srexec = Srexec(self._core, self._cmd_group)
		return self._srexec

	@property
	def srtime(self):
		"""srtime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_srtime'):
			from .Srtime import Srtime
			self._srtime = Srtime(self._core, self._cmd_group)
		return self._srtime

	@property
	def startup(self):
		"""startup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_startup'):
			from .Startup import Startup
			self._startup = Startup(self._core, self._cmd_group)
		return self._startup

	@property
	def time(self):
		"""time commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def undo(self):
		"""undo commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_undo'):
			from .Undo import Undo
			self._undo = Undo(self._core, self._cmd_group)
		return self._undo

	def set_crash(self, test_scpi_generic: float) -> None:
		"""SCPI: SYSTem:CRASh \n
		Snippet: driver.system.set_crash(test_scpi_generic = 1.0) \n
		No command help available \n
			:param test_scpi_generic: No help available
		"""
		param = Conversions.decimal_value_to_str(test_scpi_generic)
		self._core.io.write(f'SYSTem:CRASh {param}')

	def get_dfpr(self) -> str:
		"""SCPI: SYSTem:DFPR \n
		Snippet: value: str = driver.system.get_dfpr() \n
		Queries the device footprint of the instrument. The retrieved information is in machine-readable form suitable for
		automatic further processing. If you are obtaining technical support as described in 'Collecting information for
		technical support', this information is automatically retrieved and is part of the created *.tar.gz support file. \n
			:return: device_footprint: string Information on the instrument type, device identification and details on the installed FW version, hardware and software options.
		"""
		response = self._core.io.query_str('SYSTem:DFPR?')
		return trim_str_response(response)

	def get_did(self) -> str:
		"""SCPI: SYSTem:DID \n
		Snippet: value: str = driver.system.get_did() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:DID?')
		return trim_str_response(response)

	def get_dlock(self) -> bool:
		"""SCPI: SYSTem:DLOCk \n
		Snippet: value: bool = driver.system.get_dlock() \n
		Disables the manual operation via the display, including the front panel keyboard of the instrument and the LOCAL key. \n
			:return: disp_lock_stat: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SYSTem:DLOCk?')
		return Conversions.str_to_bool(response)

	def set_dlock(self, disp_lock_stat: bool) -> None:
		"""SCPI: SYSTem:DLOCk \n
		Snippet: driver.system.set_dlock(disp_lock_stat = False) \n
		Disables the manual operation via the display, including the front panel keyboard of the instrument and the LOCAL key. \n
			:param disp_lock_stat: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(disp_lock_stat)
		self._core.io.write(f'SYSTem:DLOCk {param}')

	def set_import_py(self, filename: str) -> None:
		"""SCPI: SYSTem:IMPort \n
		Snippet: driver.system.set_import_py(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SYSTem:IMPort {param}')

	def get_iresponse(self) -> str:
		"""SCPI: SYSTem:IRESponse \n
		Snippet: value: str = driver.system.get_iresponse() \n
		Defines the user defined identification string for *IDN. Note: While working in an emulation mode, the instrument's
		specific command set is disabled, i.e. the SCPI command method RsSmw.System.iresponse is discarded. \n
			:return: idn_response: string
		"""
		response = self._core.io.query_str('SYSTem:IRESponse?')
		return trim_str_response(response)

	def set_iresponse(self, idn_response: str) -> None:
		"""SCPI: SYSTem:IRESponse \n
		Snippet: driver.system.set_iresponse(idn_response = '1') \n
		Defines the user defined identification string for *IDN. Note: While working in an emulation mode, the instrument's
		specific command set is disabled, i.e. the SCPI command method RsSmw.System.iresponse is discarded. \n
			:param idn_response: string
		"""
		param = Conversions.value_to_quoted_str(idn_response)
		self._core.io.write(f'SYSTem:IRESponse {param}')

	def get_klock(self) -> bool:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: value: bool = driver.system.get_klock() \n
		Disables the front panel keyboard of the instrument including the LOCAL key. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SYSTem:KLOCk?')
		return Conversions.str_to_bool(response)

	def set_klock(self, state: bool) -> None:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: driver.system.set_klock(state = False) \n
		Disables the front panel keyboard of the instrument including the LOCAL key. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:KLOCk {param}')

	def get_language(self) -> str:
		"""SCPI: SYSTem:LANGuage \n
		Snippet: value: str = driver.system.get_language() \n
		Sets the remote control command set. \n
			:return: language: string
		"""
		response = self._core.io.query_str('SYSTem:LANGuage?')
		return trim_str_response(response)

	def set_language(self, language: str) -> None:
		"""SCPI: SYSTem:LANGuage \n
		Snippet: driver.system.set_language(language = '1') \n
		Sets the remote control command set. \n
			:param language: string
		"""
		param = Conversions.value_to_quoted_str(language)
		self._core.io.write(f'SYSTem:LANGuage {param}')

	def get_ninformation(self) -> str:
		"""SCPI: SYSTem:NINFormation \n
		Snippet: value: str = driver.system.get_ninformation() \n
		Queries the oldest information message ('Error History > Level > Info') in the error/event queue. \n
			:return: next_info: string
		"""
		response = self._core.io.query_str('SYSTem:NINFormation?')
		return trim_str_response(response)

	def get_oresponse(self) -> str:
		"""SCPI: SYSTem:ORESponse \n
		Snippet: value: str = driver.system.get_oresponse() \n
		Defines the user defined response string for *OPT. Note: While working in an emulation mode, the instrument's specific
		command set is disabled, i.e. the SCPI command method RsSmw.System.oresponse is discarded. \n
			:return: oresponse: string
		"""
		response = self._core.io.query_str('SYSTem:ORESponse?')
		return trim_str_response(response)

	def set_oresponse(self, oresponse: str) -> None:
		"""SCPI: SYSTem:ORESponse \n
		Snippet: driver.system.set_oresponse(oresponse = '1') \n
		Defines the user defined response string for *OPT. Note: While working in an emulation mode, the instrument's specific
		command set is disabled, i.e. the SCPI command method RsSmw.System.oresponse is discarded. \n
			:param oresponse: string
		"""
		param = Conversions.value_to_quoted_str(oresponse)
		self._core.io.write(f'SYSTem:ORESponse {param}')

	def get_osystem(self) -> str:
		"""SCPI: SYSTem:OSYStem \n
		Snippet: value: str = driver.system.get_osystem() \n
		Queries the operating system of the instrument. \n
			:return: oper_system: string
		"""
		response = self._core.io.query_str('SYSTem:OSYStem?')
		return trim_str_response(response)

	def preset(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:PRESet \n
		Snippet: driver.system.preset(pseudo_string = '1') \n
			INTRO_CMD_HELP: Triggers an instrument reset. It has the same effect as: \n
			- The [PRESET] key. However, the command does not close open GUI dialogs like the key does.
			- The *RST command
		For an overview of the settings affected by the preset function, see Table 'Key parameters affected by preset and
		factory preset' \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:PRESet {param}')

	def preset_all(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:PRESet:ALL {param}')

	def preset_base(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:PRESet:BASE {param}')

	def recall(self, path_name: str) -> None:
		"""SCPI: SYSTem:RCL \n
		Snippet: driver.system.recall(path_name = '1') \n
		Loads a file with previously saved R&S SMW settings. Loads the selected file with previously saved R&S SMW settings from
		the default or the specified directory. Loaded are files with extension *.savrcltxt. \n
			:param path_name: string
		"""
		param = Conversions.value_to_quoted_str(path_name)
		self._core.io.write(f'SYSTem:RCL {param}')

	def reset(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:RESet \n
		Snippet: driver.system.reset(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:RESet {param}')

	def reset_all(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:RESet:ALL {param}')

	def reset_base(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:RESet:BASE {param}')

	def save(self, path_name: str) -> None:
		"""SCPI: SYSTem:SAV \n
		Snippet: driver.system.save(path_name = '1') \n
		Saves the current R&S SMW settings into a file with defined filename and into a specified directory. The file extension
		(*.savrcltxt) is assigned automatically. \n
			:param path_name: string
		"""
		param = Conversions.value_to_quoted_str(path_name)
		self._core.io.write(f'SYSTem:SAV {param}')

	def get_simulation(self) -> bool:
		"""SCPI: SYSTem:SIMulation \n
		Snippet: value: bool = driver.system.get_simulation() \n
		No command help available \n
			:return: status: No help available
		"""
		response = self._core.io.query_str('SYSTem:SIMulation?')
		return Conversions.str_to_bool(response)

	def get_sr_cat(self) -> List[str]:
		"""SCPI: SYSTem:SRCat \n
		Snippet: value: List[str] = driver.system.get_sr_cat() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SYSTem:SRCat?')
		return Conversions.str_to_str_list(response)

	def set_srestore(self, data_set: int) -> None:
		"""SCPI: SYSTem:SREStore \n
		Snippet: driver.system.set_srestore(data_set = 1) \n
		No command help available \n
			:param data_set: No help available
		"""
		param = Conversions.decimal_value_to_str(data_set)
		self._core.io.write(f'SYSTem:SREStore {param}')

	# noinspection PyTypeChecker
	def get_sr_mode(self) -> enums.RecScpiCmdMode:
		"""SCPI: SYSTem:SRMode \n
		Snippet: value: enums.RecScpiCmdMode = driver.system.get_sr_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SYSTem:SRMode?')
		return Conversions.str_to_scalar_enum(response, enums.RecScpiCmdMode)

	def set_sr_mode(self, mode: enums.RecScpiCmdMode) -> None:
		"""SCPI: SYSTem:SRMode \n
		Snippet: driver.system.set_sr_mode(mode = enums.RecScpiCmdMode.AUTO) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RecScpiCmdMode)
		self._core.io.write(f'SYSTem:SRMode {param}')

	def get_sr_sel(self) -> str:
		"""SCPI: SYSTem:SRSel \n
		Snippet: value: str = driver.system.get_sr_sel() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SYSTem:SRSel?')
		return trim_str_response(response)

	def set_sr_sel(self, filename: str) -> None:
		"""SCPI: SYSTem:SRSel \n
		Snippet: driver.system.set_sr_sel(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SYSTem:SRSel {param}')

	def set_ssave(self, data_set: int) -> None:
		"""SCPI: SYSTem:SSAVe \n
		Snippet: driver.system.set_ssave(data_set = 1) \n
		No command help available \n
			:param data_set: No help available
		"""
		param = Conversions.decimal_value_to_str(data_set)
		self._core.io.write(f'SYSTem:SSAVe {param}')

	def get_tzone(self) -> str:
		"""SCPI: SYSTem:TZONe \n
		Snippet: value: str = driver.system.get_tzone() \n
		No command help available \n
			:return: pseudo_string: No help available
		"""
		response = self._core.io.query_str('SYSTem:TZONe?')
		return trim_str_response(response)

	def set_tzone(self, pseudo_string: str) -> None:
		"""SCPI: SYSTem:TZONe \n
		Snippet: driver.system.set_tzone(pseudo_string = '1') \n
		No command help available \n
			:param pseudo_string: No help available
		"""
		param = Conversions.value_to_quoted_str(pseudo_string)
		self._core.io.write(f'SYSTem:TZONe {param}')

	# noinspection PyTypeChecker
	def get_ulock(self) -> enums.DispKeybLockMode:
		"""SCPI: SYSTem:ULOCk \n
		Snippet: value: enums.DispKeybLockMode = driver.system.get_ulock() \n
		Locks or unlocks the user interface of the instrument. \n
			:return: mode: ENABled| DONLy| DISabled| TOFF| VNConly ENABled Unlocks the display, the touchscreen and all controls for the manual operation. DONLy Locks the touchscreen and controls for the manual operation of the instrument. The display shows the current settings. VNConly Locks the touchscreen and controls for the manual operation, and enables remote operation over VNC. The display shows the current settings. TOFF Locks the touchscreen for the manual operation of the instrument. The display shows the current settings. DISabled Locks the display, the touchscreen and all controls for the manual operation.
		"""
		response = self._core.io.query_str('SYSTem:ULOCk?')
		return Conversions.str_to_scalar_enum(response, enums.DispKeybLockMode)

	def set_ulock(self, mode: enums.DispKeybLockMode) -> None:
		"""SCPI: SYSTem:ULOCk \n
		Snippet: driver.system.set_ulock(mode = enums.DispKeybLockMode.DISabled) \n
		Locks or unlocks the user interface of the instrument. \n
			:param mode: ENABled| DONLy| DISabled| TOFF| VNConly ENABled Unlocks the display, the touchscreen and all controls for the manual operation. DONLy Locks the touchscreen and controls for the manual operation of the instrument. The display shows the current settings. VNConly Locks the touchscreen and controls for the manual operation, and enables remote operation over VNC. The display shows the current settings. TOFF Locks the touchscreen for the manual operation of the instrument. The display shows the current settings. DISabled Locks the display, the touchscreen and all controls for the manual operation.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DispKeybLockMode)
		self._core.io.write(f'SYSTem:ULOCk {param}')

	def get_up_time(self) -> str:
		"""SCPI: SYSTem:UPTime \n
		Snippet: value: str = driver.system.get_up_time() \n
		Queries the up time of the operating system. \n
			:return: up_time: 'ddd.hh:mm:ss'
		"""
		response = self._core.io.query_str('SYSTem:UPTime?')
		return trim_str_response(response)

	def get_version(self) -> str:
		"""SCPI: SYSTem:VERSion \n
		Snippet: value: str = driver.system.get_version() \n
		Queries the SCPI version the instrument's command set complies with. \n
			:return: version: string
		"""
		response = self._core.io.query_str('SYSTem:VERSion?')
		return trim_str_response(response)

	def set_wait(self, time_ms: int) -> None:
		"""SCPI: SYSTem:WAIT \n
		Snippet: driver.system.set_wait(time_ms = 1) \n
		Delays the execution of the subsequent remote command by the specified time. This function is useful, for example to
		execute an SCPI sequence automatically but with a defined time delay between some commands. See 'How to assign actions to
		the [USER] key'. \n
			:param time_ms: integer Wait time in ms Range: 0 to 10000
		"""
		param = Conversions.decimal_value_to_str(time_ms)
		self._core.io.write(f'SYSTem:WAIT {param}')

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
