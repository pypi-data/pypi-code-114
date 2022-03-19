from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ts25141:
	"""Ts25141 commands group definition. 55 total commands, 8 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ts25141", core, parent)

	@property
	def awgn(self):
		"""awgn commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import Awgn
			self._awgn = Awgn(self._core, self._cmd_group)
		return self._awgn

	@property
	def bsSignal(self):
		"""bsSignal commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bsSignal'):
			from .BsSignal import BsSignal
			self._bsSignal = BsSignal(self._core, self._cmd_group)
		return self._bsSignal

	@property
	def fsimulator(self):
		"""fsimulator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsimulator'):
			from .Fsimulator import Fsimulator
			self._fsimulator = Fsimulator(self._core, self._cmd_group)
		return self._fsimulator

	@property
	def ifRignal(self):
		"""ifRignal commands group. 3 Sub-classes, 6 commands."""
		if not hasattr(self, '_ifRignal'):
			from .IfRignal import IfRignal
			self._ifRignal = IfRignal(self._core, self._cmd_group)
		return self._ifRignal

	@property
	def scode(self):
		"""scode commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scode'):
			from .Scode import Scode
			self._scode = Scode(self._core, self._cmd_group)
		return self._scode

	@property
	def tcase(self):
		"""tcase commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcase'):
			from .Tcase import Tcase
			self._tcase = Tcase(self._core, self._cmd_group)
		return self._tcase

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def wsignal(self):
		"""wsignal commands group. 5 Sub-classes, 6 commands."""
		if not hasattr(self, '_wsignal'):
			from .Wsignal import Wsignal
			self._wsignal = Wsignal(self._core, self._cmd_group)
		return self._wsignal

	# noinspection PyTypeChecker
	def get_bsp_class(self) -> enums.Ts25141BspOwClass:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:BSPClass \n
		Snippet: value: enums.Ts25141BspOwClass = driver.source.bb.w3Gpp.ts25141.get_bsp_class() \n
		Selects the base station power class. \n
			:return: bsp_class: WIDE| MEDium| LOCal
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:BSPClass?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141BspOwClass)

	def set_bsp_class(self, bsp_class: enums.Ts25141BspOwClass) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:BSPClass \n
		Snippet: driver.source.bb.w3Gpp.ts25141.set_bsp_class(bsp_class = enums.Ts25141BspOwClass.LOCal) \n
		Selects the base station power class. \n
			:param bsp_class: WIDE| MEDium| LOCal
		"""
		param = Conversions.enum_scalar_to_str(bsp_class, enums.Ts25141BspOwClass)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:BSPClass {param}')

	# noinspection PyTypeChecker
	def get_emode(self) -> enums.Ts25141EditMode:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:EMODe \n
		Snippet: value: enums.Ts25141EditMode = driver.source.bb.w3Gpp.ts25141.get_emode() \n
		Selects the edit mode for the configuration of the test cases. \n
			:return: emode: STANdard| USER STANdard Edit mode 'According to Standard'. Only settings in compliance with TS 25.141 are possible. All other parameters are preset. USER Edit mode 'User definable'. A wider range of settings is possible
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:EMODe?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141EditMode)

	def set_emode(self, emode: enums.Ts25141EditMode) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:EMODe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.set_emode(emode = enums.Ts25141EditMode.STANdard) \n
		Selects the edit mode for the configuration of the test cases. \n
			:param emode: STANdard| USER STANdard Edit mode 'According to Standard'. Only settings in compliance with TS 25.141 are possible. All other parameters are preset. USER Edit mode 'User definable'. A wider range of settings is possible
		"""
		param = Conversions.enum_scalar_to_str(emode, enums.Ts25141EditMode)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:EMODe {param}')

	# noinspection PyTypeChecker
	def get_route(self) -> enums.MappingType:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:ROUTe \n
		Snippet: value: enums.MappingType = driver.source.bb.w3Gpp.ts25141.get_route() \n
		Selects the signal routing for baseband A signal which in most test cases represents the wanted signal (exception test
		case 6.6) . The command is only available for two-path-instruments and only for test cases that do not use both paths
		anyway. \n
			:return: route: A| B
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:ROUTe?')
		return Conversions.str_to_scalar_enum(response, enums.MappingType)

	def set_route(self, route: enums.MappingType) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:ROUTe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.set_route(route = enums.MappingType.A) \n
		Selects the signal routing for baseband A signal which in most test cases represents the wanted signal (exception test
		case 6.6) . The command is only available for two-path-instruments and only for test cases that do not use both paths
		anyway. \n
			:param route: A| B
		"""
		param = Conversions.enum_scalar_to_str(route, enums.MappingType)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:ROUTe {param}')

	def get_rx_diversity(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:RXDiversity \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.get_rx_diversity() \n
		Sets the signal generator according to the base station diversity processing capability. The command is only available
		for two-path-instruments and only for test cases that do not use both paths anyway. \n
			:return: rx_diversity: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:RXDiversity?')
		return Conversions.str_to_bool(response)

	def set_rx_diversity(self, rx_diversity: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:RXDiversity \n
		Snippet: driver.source.bb.w3Gpp.ts25141.set_rx_diversity(rx_diversity = False) \n
		Sets the signal generator according to the base station diversity processing capability. The command is only available
		for two-path-instruments and only for test cases that do not use both paths anyway. \n
			:param rx_diversity: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(rx_diversity)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:RXDiversity {param}')

	def clone(self) -> 'Ts25141':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ts25141(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
