from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsimulator:
	"""Fsimulator commands group definition. 724 total commands, 26 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsimulator", core, parent)

	@property
	def birthDeath(self):
		"""birthDeath commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_birthDeath'):
			from .BirthDeath import BirthDeath
			self._birthDeath = BirthDeath(self._core, self._cmd_group)
		return self._birthDeath

	@property
	def bypass(self):
		"""bypass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bypass'):
			from .Bypass import Bypass
			self._bypass = Bypass(self._core, self._cmd_group)
		return self._bypass

	@property
	def cdynamic(self):
		"""cdynamic commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_cdynamic'):
			from .Cdynamic import Cdynamic
			self._cdynamic = Cdynamic(self._core, self._cmd_group)
		return self._cdynamic

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def copy(self):
		"""copy commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_copy'):
			from .Copy import Copy
			self._copy = Copy(self._core, self._cmd_group)
		return self._copy

	@property
	def couple(self):
		"""couple commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_couple'):
			from .Couple import Couple
			self._couple = Couple(self._core, self._cmd_group)
		return self._couple

	@property
	def delPy(self):
		"""delPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_delPy'):
			from .DelPy import DelPy
			self._delPy = DelPy(self._core, self._cmd_group)
		return self._delPy

	@property
	def delay(self):
		"""delay commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def dsSimulation(self):
		"""dsSimulation commands group. 4 Sub-classes, 5 commands."""
		if not hasattr(self, '_dsSimulation'):
			from .DsSimulation import DsSimulation
			self._dsSimulation = DsSimulation(self._core, self._cmd_group)
		return self._dsSimulation

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def globale(self):
		"""globale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globale'):
			from .Globale import Globale
			self._globale = Globale(self._core, self._cmd_group)
		return self._globale

	@property
	def hopping(self):
		"""hopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopping'):
			from .Hopping import Hopping
			self._hopping = Hopping(self._core, self._cmd_group)
		return self._hopping

	@property
	def hsTrain(self):
		"""hsTrain commands group. 3 Sub-classes, 6 commands."""
		if not hasattr(self, '_hsTrain'):
			from .HsTrain import HsTrain
			self._hsTrain = HsTrain(self._core, self._cmd_group)
		return self._hsTrain

	@property
	def ignore(self):
		"""ignore commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ignore'):
			from .Ignore import Ignore
			self._ignore = Ignore(self._core, self._cmd_group)
		return self._ignore

	@property
	def iloss(self):
		"""iloss commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_iloss'):
			from .Iloss import Iloss
			self._iloss = Iloss(self._core, self._cmd_group)
		return self._iloss

	@property
	def mdelay(self):
		"""mdelay commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_mdelay'):
			from .Mdelay import Mdelay
			self._mdelay = Mdelay(self._core, self._cmd_group)
		return self._mdelay

	@property
	def mimo(self):
		"""mimo commands group. 6 Sub-classes, 6 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	@property
	def scm(self):
		"""scm commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_scm'):
			from .Scm import Scm
			self._scm = Scm(self._core, self._cmd_group)
		return self._scm

	@property
	def siso(self):
		"""siso commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siso'):
			from .Siso import Siso
			self._siso = Siso(self._core, self._cmd_group)
		return self._siso

	@property
	def speed(self):
		"""speed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_speed'):
			from .Speed import Speed
			self._speed = Speed(self._core, self._cmd_group)
		return self._speed

	@property
	def standard(self):
		"""standard commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import Standard
			self._standard = Standard(self._core, self._cmd_group)
		return self._standard

	@property
	def sum(self):
		"""sum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sum'):
			from .Sum import Sum
			self._sum = Sum(self._core, self._cmd_group)
		return self._sum

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	@property
	def tcInterferer(self):
		"""tcInterferer commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_tcInterferer'):
			from .TcInterferer import TcInterferer
			self._tcInterferer = TcInterferer(self._core, self._cmd_group)
		return self._tcInterferer

	@property
	def test(self):
		"""test commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_test'):
			from .Test import Test
			self._test = Test(self._core, self._cmd_group)
		return self._test

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce]:FSIMulator:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.fad.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: filenames: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:CATalog?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	def get_configuration(self) -> enums.FadType:
		"""SCPI: [SOURce<HW>]:FSIMulator:CONFiguration \n
		Snippet: value: enums.FadType = driver.source.fsimulator.get_configuration() \n
		Selects the fading configuration. To activate the selected fading configuration, use the command for switching the state. \n
			:return: configuration: STANdard| BIRThdeath| MDELay| TCInterferer| HSTRain| CDYNamic Defines the configuration: Standard delay, birth death propagation, moving propagation, two channel interferer, high-speed train and customized dynamic fading propagation.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:CONFiguration?')
		return Conversions.str_to_scalar_enum(response, enums.FadType)

	def set_configuration(self, configuration: enums.FadType) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CONFiguration \n
		Snippet: driver.source.fsimulator.set_configuration(configuration = enums.FadType.BIRThdeath) \n
		Selects the fading configuration. To activate the selected fading configuration, use the command for switching the state. \n
			:param configuration: STANdard| BIRThdeath| MDELay| TCInterferer| HSTRain| CDYNamic Defines the configuration: Standard delay, birth death propagation, moving propagation, two channel interferer, high-speed train and customized dynamic fading propagation.
		"""
		param = Conversions.enum_scalar_to_str(configuration, enums.FadType)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CONFiguration {param}')

	def get_cspeed(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:CSPeed \n
		Snippet: value: bool = driver.source.fsimulator.get_cspeed() \n
		Determines whether the same speed is set for all of the activated fading paths. \n
			:return: cspeed: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:CSPeed?')
		return Conversions.str_to_bool(response)

	def set_cspeed(self, cspeed: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CSPeed \n
		Snippet: driver.source.fsimulator.set_cspeed(cspeed = False) \n
		Determines whether the same speed is set for all of the activated fading paths. \n
			:param cspeed: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(cspeed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CSPeed {param}')

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce]:FSIMulator:DELETE \n
		Snippet: driver.source.fsimulator.delete(filename = '1') \n
		Deletes the specified file containing a fading setting from the default directory. The default directory is set with the
		command method RsSmw.MassMemory.currentDirectory. A path can also be specified. Only files with the file ending *.fad are
		deleted. Note: This command is only valid with DELETE in the long form as DEL is used as short form of header keyword
		DELay. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce:FSIMulator:DELETE {param}')

	# noinspection PyTypeChecker
	def get_kconstant(self) -> enums.FadKeepConst:
		"""SCPI: [SOURce<HW>]:FSIMulator:KCONstant \n
		Snippet: value: enums.FadKeepConst = driver.source.fsimulator.get_kconstant() \n
		Selects whether to keep the speed or the resulting Doppler shift constant in case of frequency changes. \n
			:return: kconstant: SPEed| DSHift
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:KCONstant?')
		return Conversions.str_to_scalar_enum(response, enums.FadKeepConst)

	def set_kconstant(self, kconstant: enums.FadKeepConst) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:KCONstant \n
		Snippet: driver.source.fsimulator.set_kconstant(kconstant = enums.FadKeepConst.DSHift) \n
		Selects whether to keep the speed or the resulting Doppler shift constant in case of frequency changes. \n
			:param kconstant: SPEed| DSHift
		"""
		param = Conversions.enum_scalar_to_str(kconstant, enums.FadKeepConst)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:KCONstant {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:LOAD \n
		Snippet: driver.source.fsimulator.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.fad.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:LOAD {param}')

	def get_plength(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:PLENgth \n
		Snippet: value: float = driver.source.fsimulator.get_plength() \n
		No command help available \n
			:return: fsim_path_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:PLENgth?')
		return Conversions.str_to_float(response)

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:PRESet \n
		Snippet: driver.source.fsimulator.preset() \n
		Sets the default settings (*RST values) for fading simulation. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:PRESet \n
		Snippet: driver.source.fsimulator.preset_with_opc() \n
		Sets the default settings (*RST values) for fading simulation. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_route(self) -> enums.FadConfPathOut:
		"""SCPI: [SOURce<HW>]:FSIMulator:ROUTe \n
		Snippet: value: enums.FadConfPathOut = driver.source.fsimulator.get_route() \n
		Selects on which baseband path the faded signal is output. The input signal of the fader is selected with command
		SOURce:BB:ROUTe. For one-path instruments this command is query only. It returns value FAA (Fader A always outputs the
		signal on baseband A) . Note: All MIMO configurations are enabled only in SCONfiguration:MODE ADVanced.
			Table Header: method RsSmw.Sconfiguration.mode / SCONfiguration:FADing <FadConfig> / [:SOURce<hw>]:FSIMulator:ROUTe \n
			- STANdard / FAAFBNone FAAFBB FAAFBA FABFBB FAABFBN FANFBAB FAABFBAB / FAMAXAB FAAFBB FAAFBA FABFBB FAMAXAB FBMAXAB FAABFBAB
			- ADVanced / MIMO1X2 MIMO1X3 MIMO1X4 MIMO2X2 MIMO2X3 MIMO2X4 MIMO3X1 MIMO3X2 MIMO3X3 MIMO3X4 MIMO4X1 MIMO4X2 MIMO4X3 MIMO4X4 MIMO1X8 MIMO8X1 MIMO2X8 MIMO8X2 MIMO2X1 MIMO4X8 MIMO8X4 / FA1A2BFB1A2BM12 FA1A2BFB1A2BM13 FA1A2BFB1A2BM14 FA1A2BFB1A2B|FA1A2BFB1A2BM22 FA1A2BFB1A2BM23 FA1A2BFB1A2BM24 FA1A2BFB1A2BM31 FA1A2BFB1A2BM32 FA1A2BFB1A2BM33 FA1A2BFB1A2BM34 FA1A2BFB1A2BM41 FA1A2BFB1A2BM42 FA1A2BFB1A2BM43 FA1A2BFB1A2BM44 FA1A2BFB1A2BM18 FA1A2BFB1A2BM81 FA1A2BFB1A2BM28 FA1A2BFB1A2BM82 FA1A2BFB1A2BM21 FA1A2BFB1A2BM48 FA1A2BFB1A2BM84
			- MIMO2X1X2 MIMO2X2X1 MIMO2X2X2 MIMO2X1X3 MIMO2X1X4 MIMO2X2X3 MIMO2X3X1 MIMO2X3X2 MIMO2X4X1 / FA1A2BFB1A2BM212 FA1A2BFB1A2BM221 FA1A2BFB1A2BM222 FA1A2BFB1A2BM213 FA1A2BFB1A2BM214 FA1A2BFB1A2BM223 FA1A2BFB1A2BM231 FA1A2BFB1A2BM232 FA1A2BFB1A2BM241
			- MIMO3X1X2 MIMO3X2X1 MIMO3X2X2 MIMO4X1X2 MIMO4X2X1 MIMO4X2X2 / FA1A2BFB1A2BM312 FA1A2BFB1A2BM321 FA1A2BFB1A2BM322 FA1A2BFB1A2BM412 FA1A2BFB1A2BM421 FA1A2BFB1A2BM422
			- SISO3X1X1 SISO4X1X1 SISO5X1X1 SISO6X1X1 SISO7X1X1 SISO8X1X1 / FAAFBB311 FAAFBB411 FAAFBB511 FAAFBB611 FAAFBB711 FAAFBB811
			- MIMO2X2X4 MIMO2X4X2 MIMO2X4X4 MIMO2X3X3 MIMO2X3X4 MIMO2X4X3 / FA1A2BFB1A2BM224 FA1A2BFB1A2BM242 FA1A2BFB1A2BM244 FA1A2BFB1A2BM233 FA1A2BFB1A2BM234 FA1A2BFB1A2BM243
			- MIMO8X8 / FA1A2BFB1A2BM88 \n
			:return: route: FAA| FAMAXAB| FAAFBA| FAAFBB| FABFBB| FBMAXAB| FAABFBAB| FA1A2BFB1A2B| FA1A2BFB1A2BM22| FA1A2BFB1A2BM24| FA1A2BFB1A2BM42| FA1A2BFB1A2BM23| FA1A2BFB1A2BM32| FA1A2BFB1A2BM12| FA1A2BFB1A2BM33| FA1A2BFB1A2BM34| FA1A2BFB1A2BM43| FA1A2BFB1A2BM44| FA1A2BFB1A2BM18| FA1A2BFB1A2BM81| FA1A2BFB1A2BM28| FA1A2BFB1A2BM82| FA1A2BFB1A2BM21| FA1A2BFB1A2BM212| FA1A2BFB1A2BM221| FA1A2BFB1A2BM222| FA1A2BFB1A2BM13| FA1A2BFB1A2BM31| FA1A2BFB1A2BM14| FA1A2BFB1A2BM41| FAMAXA| FA1A2BFB1A2BM224| FA1A2BFB1A2BM242| FA1A2BFB1A2BM48| FA1A2BFB1A2BM84| FA1A2BFB1A2BM88| FA1A2BFB1A2BM312| FA1A2BFB1A2BM321| FA1A2BFB1A2BM322| FA1A2BFB1A2BM412| FA1A2BFB1A2BM421| FA1A2BFB1A2BM422| FAAFBB311| FAAFBB411| FAAFBB511| FAAFBB611| FAAFBB711| FAAFBB811| FA1A2BFB1A2BM213| FA1A2BFB1A2BM214| FA1A2BFB1A2BM223| FA1A2BFB1A2BM231| FA1A2BFB1A2BM232| FA1A2BFB1A2BM241| FA1A2BFB1A2BM244| FA1A2BFB1A2BM233| FA1A2BFB1A2BM234| FA1A2BFB1A2BM243 FAA The faded modulation signal of fader A is placed on baseband path A. FAAFBB The faded modulation signal of fader A is placed on baseband path A and the faded modulation signal of fader B is placed on baseband path B. FAAFBA The faded modulation signal of fader A and B is placed on baseband path A. FABFBB The faded modulation signal of fader A and B is placed on baseband path B. FAABFBAB The faded modulation signal of fader A and B is placed on baseband paths A and B. FAMAXA The faded modulation signal of fader A is placed on baseband path A. FBMAXB The faded modulation signal of fader B is placed on baseband path B. FAMAXAB The faded modulation signal of fader A is placed on baseband paths A and B. FBMAXAB The faded modulation signal of fader B is placed on baseband paths A and B. FA1A2BFB1A2B|FA1A2BFB1A2BM22| ... |FAAFBB811 Sets a MIMO mode
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:ROUTe?')
		return Conversions.str_to_scalar_enum(response, enums.FadConfPathOut)

	def set_route(self, route: enums.FadConfPathOut) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:ROUTe \n
		Snippet: driver.source.fsimulator.set_route(route = enums.FadConfPathOut.FA1A2BFB1A2B) \n
		Selects on which baseband path the faded signal is output. The input signal of the fader is selected with command
		SOURce:BB:ROUTe. For one-path instruments this command is query only. It returns value FAA (Fader A always outputs the
		signal on baseband A) . Note: All MIMO configurations are enabled only in SCONfiguration:MODE ADVanced.
			Table Header: method RsSmw.Sconfiguration.mode / SCONfiguration:FADing <FadConfig> / [:SOURce<hw>]:FSIMulator:ROUTe \n
			- STANdard / FAAFBNone FAAFBB FAAFBA FABFBB FAABFBN FANFBAB FAABFBAB / FAMAXAB FAAFBB FAAFBA FABFBB FAMAXAB FBMAXAB FAABFBAB
			- ADVanced / MIMO1X2 MIMO1X3 MIMO1X4 MIMO2X2 MIMO2X3 MIMO2X4 MIMO3X1 MIMO3X2 MIMO3X3 MIMO3X4 MIMO4X1 MIMO4X2 MIMO4X3 MIMO4X4 MIMO1X8 MIMO8X1 MIMO2X8 MIMO8X2 MIMO2X1 MIMO4X8 MIMO8X4 / FA1A2BFB1A2BM12 FA1A2BFB1A2BM13 FA1A2BFB1A2BM14 FA1A2BFB1A2B|FA1A2BFB1A2BM22 FA1A2BFB1A2BM23 FA1A2BFB1A2BM24 FA1A2BFB1A2BM31 FA1A2BFB1A2BM32 FA1A2BFB1A2BM33 FA1A2BFB1A2BM34 FA1A2BFB1A2BM41 FA1A2BFB1A2BM42 FA1A2BFB1A2BM43 FA1A2BFB1A2BM44 FA1A2BFB1A2BM18 FA1A2BFB1A2BM81 FA1A2BFB1A2BM28 FA1A2BFB1A2BM82 FA1A2BFB1A2BM21 FA1A2BFB1A2BM48 FA1A2BFB1A2BM84
			- MIMO2X1X2 MIMO2X2X1 MIMO2X2X2 MIMO2X1X3 MIMO2X1X4 MIMO2X2X3 MIMO2X3X1 MIMO2X3X2 MIMO2X4X1 / FA1A2BFB1A2BM212 FA1A2BFB1A2BM221 FA1A2BFB1A2BM222 FA1A2BFB1A2BM213 FA1A2BFB1A2BM214 FA1A2BFB1A2BM223 FA1A2BFB1A2BM231 FA1A2BFB1A2BM232 FA1A2BFB1A2BM241
			- MIMO3X1X2 MIMO3X2X1 MIMO3X2X2 MIMO4X1X2 MIMO4X2X1 MIMO4X2X2 / FA1A2BFB1A2BM312 FA1A2BFB1A2BM321 FA1A2BFB1A2BM322 FA1A2BFB1A2BM412 FA1A2BFB1A2BM421 FA1A2BFB1A2BM422
			- SISO3X1X1 SISO4X1X1 SISO5X1X1 SISO6X1X1 SISO7X1X1 SISO8X1X1 / FAAFBB311 FAAFBB411 FAAFBB511 FAAFBB611 FAAFBB711 FAAFBB811
			- MIMO2X2X4 MIMO2X4X2 MIMO2X4X4 MIMO2X3X3 MIMO2X3X4 MIMO2X4X3 / FA1A2BFB1A2BM224 FA1A2BFB1A2BM242 FA1A2BFB1A2BM244 FA1A2BFB1A2BM233 FA1A2BFB1A2BM234 FA1A2BFB1A2BM243
			- MIMO8X8 / FA1A2BFB1A2BM88 \n
			:param route: FAA| FAMAXAB| FAAFBA| FAAFBB| FABFBB| FBMAXAB| FAABFBAB| FA1A2BFB1A2B| FA1A2BFB1A2BM22| FA1A2BFB1A2BM24| FA1A2BFB1A2BM42| FA1A2BFB1A2BM23| FA1A2BFB1A2BM32| FA1A2BFB1A2BM12| FA1A2BFB1A2BM33| FA1A2BFB1A2BM34| FA1A2BFB1A2BM43| FA1A2BFB1A2BM44| FA1A2BFB1A2BM18| FA1A2BFB1A2BM81| FA1A2BFB1A2BM28| FA1A2BFB1A2BM82| FA1A2BFB1A2BM21| FA1A2BFB1A2BM212| FA1A2BFB1A2BM221| FA1A2BFB1A2BM222| FA1A2BFB1A2BM13| FA1A2BFB1A2BM31| FA1A2BFB1A2BM14| FA1A2BFB1A2BM41| FAMAXA| FA1A2BFB1A2BM224| FA1A2BFB1A2BM242| FA1A2BFB1A2BM48| FA1A2BFB1A2BM84| FA1A2BFB1A2BM88| FA1A2BFB1A2BM312| FA1A2BFB1A2BM321| FA1A2BFB1A2BM322| FA1A2BFB1A2BM412| FA1A2BFB1A2BM421| FA1A2BFB1A2BM422| FAAFBB311| FAAFBB411| FAAFBB511| FAAFBB611| FAAFBB711| FAAFBB811| FA1A2BFB1A2BM213| FA1A2BFB1A2BM214| FA1A2BFB1A2BM223| FA1A2BFB1A2BM231| FA1A2BFB1A2BM232| FA1A2BFB1A2BM241| FA1A2BFB1A2BM244| FA1A2BFB1A2BM233| FA1A2BFB1A2BM234| FA1A2BFB1A2BM243 FAA The faded modulation signal of fader A is placed on baseband path A. FAAFBB The faded modulation signal of fader A is placed on baseband path A and the faded modulation signal of fader B is placed on baseband path B. FAAFBA The faded modulation signal of fader A and B is placed on baseband path A. FABFBB The faded modulation signal of fader A and B is placed on baseband path B. FAABFBAB The faded modulation signal of fader A and B is placed on baseband paths A and B. FAMAXA The faded modulation signal of fader A is placed on baseband path A. FBMAXB The faded modulation signal of fader B is placed on baseband path B. FAMAXAB The faded modulation signal of fader A is placed on baseband paths A and B. FBMAXAB The faded modulation signal of fader B is placed on baseband paths A and B. FA1A2BFB1A2B|FA1A2BFB1A2BM22| ... |FAAFBB811 Sets a MIMO mode
		"""
		param = Conversions.enum_scalar_to_str(route, enums.FadConfPathOut)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:ROUTe {param}')

	# noinspection PyTypeChecker
	def get_sdestination(self) -> enums.FadSignDest:
		"""SCPI: [SOURce<HW>]:FSIMulator:SDEStination \n
		Snippet: value: enums.FadSignDest = driver.source.fsimulator.get_sdestination() \n
		Defines the frequency to that the signal of the whole Fader block is dedicated. \n
			:return: sdestination: RF| BB RF The Doppler shift is calculated based on the actual RF frequency, that is dynamically estimated. To query the estimated dedicated frequency, use the command [:SOURcehw]:FSIMulator:FREQuency. To query the output connector, use the command [:SOURcehw]:FSIMulator:FREQuency:DETect?. BB Set the fader frequency manually by means of the command [:SOURcehw]:FSIMulator:FREQuency.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SDEStination?')
		return Conversions.str_to_scalar_enum(response, enums.FadSignDest)

	def set_sdestination(self, sdestination: enums.FadSignDest) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SDEStination \n
		Snippet: driver.source.fsimulator.set_sdestination(sdestination = enums.FadSignDest.BB) \n
		Defines the frequency to that the signal of the whole Fader block is dedicated. \n
			:param sdestination: RF| BB RF The Doppler shift is calculated based on the actual RF frequency, that is dynamically estimated. To query the estimated dedicated frequency, use the command [:SOURcehw]:FSIMulator:FREQuency. To query the output connector, use the command [:SOURcehw]:FSIMulator:FREQuency:DETect?. BB Set the fader frequency manually by means of the command [:SOURcehw]:FSIMulator:FREQuency.
		"""
		param = Conversions.enum_scalar_to_str(sdestination, enums.FadSignDest)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SDEStination {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:STORe \n
		Snippet: driver.source.fsimulator.set_store(filename = '1') \n
		Saves the current settings into the selected file; the file extension (*.fad) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:STORe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:[STATe] \n
		Snippet: value: bool = driver.source.fsimulator.get_state() \n
		Activates fading simulation. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:[STATe] \n
		Snippet: driver.source.fsimulator.set_state(state = False) \n
		Activates fading simulation. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:STATe {param}')

	def clone(self) -> 'Fsimulator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fsimulator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
