from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 13 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	@property
	def mapping(self):
		"""mapping commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_mapping'):
			from .Mapping import Mapping
			self._mapping = Mapping(self._core, self._cmd_group)
		return self._mapping

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SystConfOutpMode:
		"""SCPI: SCONfiguration:OUTPut:MODE \n
		Snippet: value: enums.SystConfOutpMode = driver.sconfiguration.output.get_mode() \n
		Defines what kind of signal is generated and which output interfaces are enabled. \n
			:return: mode: DIGMux| DIGital| ALL | ANALog| HSDigital| HSALl ALL Output at the analog (RF and I/Q) and the digital DIG I/Q interfaces. DIGital | DIGMux Signal is output as single stream or multiplexed digital signal at the DIG I/Q interfaces. ANALog Output at the analog (RF and I/Q) interfaces. HSDigital Output at the interfaces HS DIG I/Q interfaces. HSALl Output at the analog (RF and I/Q) and the digital HS DIG I/Q interfaces.
		"""
		response = self._core.io.query_str('SCONfiguration:OUTPut:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfOutpMode)

	def set_mode(self, mode: enums.SystConfOutpMode) -> None:
		"""SCPI: SCONfiguration:OUTPut:MODE \n
		Snippet: driver.sconfiguration.output.set_mode(mode = enums.SystConfOutpMode.ALL) \n
		Defines what kind of signal is generated and which output interfaces are enabled. \n
			:param mode: DIGMux| DIGital| ALL | ANALog| HSDigital| HSALl ALL Output at the analog (RF and I/Q) and the digital DIG I/Q interfaces. DIGital | DIGMux Signal is output as single stream or multiplexed digital signal at the DIG I/Q interfaces. ANALog Output at the analog (RF and I/Q) interfaces. HSDigital Output at the interfaces HS DIG I/Q interfaces. HSALl Output at the analog (RF and I/Q) and the digital HS DIG I/Q interfaces.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SystConfOutpMode)
		self._core.io.write(f'SCONfiguration:OUTPut:MODE {param}')

	def clone(self) -> 'Output':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Output(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
