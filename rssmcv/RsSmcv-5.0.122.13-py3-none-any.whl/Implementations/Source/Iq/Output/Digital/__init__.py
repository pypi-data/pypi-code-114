from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Digital:
	"""Digital commands group definition. 23 total commands, 5 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("digital", core, parent)

	@property
	def bbmm(self):
		"""bbmm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbmm'):
			from .Bbmm import Bbmm
			self._bbmm = Bbmm(self._core, self._cmd_group)
		return self._bbmm

	@property
	def channel(self):
		"""channel commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def oflow(self):
		"""oflow commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_oflow'):
			from .Oflow import Oflow
			self._oflow = Oflow(self._core, self._cmd_group)
		return self._oflow

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def symbolRate(self):
		"""symbolRate commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	def get_cdevice(self) -> str:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:CDEVice \n
		Snippet: value: str = driver.source.iq.output.digital.get_cdevice() \n
		Queries information on the connected device. \n
			:return: cdevice: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:CDEVice?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_interface(self) -> enums.BbinInterfaceMode:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:INTerface \n
		Snippet: value: enums.BbinInterfaceMode = driver.source.iq.output.digital.get_interface() \n
		Queries the connector at that the signal is output. \n
			:return: bbout_interf_mode: HSDin HSDin Dig. IQ HS x
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:INTerface?')
		return Conversions.str_to_scalar_enum(response, enums.BbinInterfaceMode)

	def set_interface(self, bbout_interf_mode: enums.BbinInterfaceMode) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:INTerface \n
		Snippet: driver.source.iq.output.digital.set_interface(bbout_interf_mode = enums.BbinInterfaceMode.DIGital) \n
		Queries the connector at that the signal is output. \n
			:param bbout_interf_mode: HSDin HSDin Dig. IQ HS x
		"""
		param = Conversions.enum_scalar_to_str(bbout_interf_mode, enums.BbinInterfaceMode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:INTerface {param}')

	# noinspection PyTypeChecker
	def get_pon(self) -> enums.UnchOff:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:PON \n
		Snippet: value: enums.UnchOff = driver.source.iq.output.digital.get_pon() \n
		Sets the power-on state of the selected digital I/Q output. \n
			:return: pon: OFF| UNCHanged
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:PON?')
		return Conversions.str_to_scalar_enum(response, enums.UnchOff)

	def set_pon(self, pon: enums.UnchOff) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:PON \n
		Snippet: driver.source.iq.output.digital.set_pon(pon = enums.UnchOff.OFF) \n
		Sets the power-on state of the selected digital I/Q output. \n
			:param pon: OFF| UNCHanged
		"""
		param = Conversions.enum_scalar_to_str(pon, enums.UnchOff)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:PON {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:STATe \n
		Snippet: value: bool = driver.source.iq.output.digital.get_state() \n
		Activates the digital I/Q signal output. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:STATe \n
		Snippet: driver.source.iq.output.digital.set_state(state = False) \n
		Activates the digital I/Q signal output. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:STATe {param}')

	def clone(self) -> 'Digital':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Digital(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
