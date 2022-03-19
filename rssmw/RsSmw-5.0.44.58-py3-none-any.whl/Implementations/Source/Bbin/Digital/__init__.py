from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Digital:
	"""Digital commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("digital", core, parent)

	@property
	def asetting(self):
		"""asetting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asetting'):
			from .Asetting import Asetting
			self._asetting = Asetting(self._core, self._cmd_group)
		return self._asetting

	# noinspection PyTypeChecker
	def get_interface(self) -> enums.BbinInterfaceMode:
		"""SCPI: [SOURce<HW>]:BBIN:DIGital:INTerface \n
		Snippet: value: enums.BbinInterfaceMode = driver.source.bbin.digital.get_interface() \n
		Selects the input connector at that the signal is fed. \n
			:return: bbin_dig_interface: DIGital| HSDin | DIGital| HSDin DIN DIG I/Q HSDin HS DIG I/Q
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:DIGital:INTerface?')
		return Conversions.str_to_scalar_enum(response, enums.BbinInterfaceMode)

	def set_interface(self, bbin_dig_interface: enums.BbinInterfaceMode) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:DIGital:INTerface \n
		Snippet: driver.source.bbin.digital.set_interface(bbin_dig_interface = enums.BbinInterfaceMode.DIGital) \n
		Selects the input connector at that the signal is fed. \n
			:param bbin_dig_interface: DIGital| HSDin | DIGital| HSDin DIN DIG I/Q HSDin HS DIG I/Q
		"""
		param = Conversions.enum_scalar_to_str(bbin_dig_interface, enums.BbinInterfaceMode)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:DIGital:INTerface {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.BbinDigInpSour:
		"""SCPI: [SOURce<HW>]:BBIN:DIGital:SOURce \n
		Snippet: value: enums.BbinDigInpSour = driver.source.bbin.digital.get_source() \n
		Defines the connector used as an external signal source. \n
			:return: dig_inp_source: CODER1 | FADER1| FADER2| CODER2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:DIGital:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BbinDigInpSour)

	def set_source(self, dig_inp_source: enums.BbinDigInpSour) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:DIGital:SOURce \n
		Snippet: driver.source.bbin.digital.set_source(dig_inp_source = enums.BbinDigInpSour.CODER1) \n
		Defines the connector used as an external signal source. \n
			:param dig_inp_source: CODER1 | FADER1| FADER2| CODER2
		"""
		param = Conversions.enum_scalar_to_str(dig_inp_source, enums.BbinDigInpSour)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:DIGital:SOURce {param}')

	def clone(self) -> 'Digital':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Digital(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
