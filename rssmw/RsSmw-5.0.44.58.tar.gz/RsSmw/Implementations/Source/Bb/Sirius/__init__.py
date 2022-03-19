from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sirius:
	"""Sirius commands group definition. 82 total commands, 5 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sirius", core, parent)

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def satellite(self):
		"""satellite commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_satellite'):
			from .Satellite import Satellite
			self._satellite = Satellite(self._core, self._cmd_group)
		return self._satellite

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def terrestrial(self):
		"""terrestrial commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_terrestrial'):
			from .Terrestrial import Terrestrial
			self._terrestrial = Terrestrial(self._core, self._cmd_group)
		return self._terrestrial

	@property
	def trigger(self):
		"""trigger commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	# noinspection PyTypeChecker
	def get_player(self) -> enums.SiriusLayer:
		"""SCPI: [SOURce<HW>]:BB:SIRius:PLAYer \n
		Snippet: value: enums.SiriusLayer = driver.source.bb.sirius.get_player() \n
		No command help available \n
			:return: player: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:PLAYer?')
		return Conversions.str_to_scalar_enum(response, enums.SiriusLayer)

	def set_player(self, player: enums.SiriusLayer) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:PLAYer \n
		Snippet: driver.source.bb.sirius.set_player(player = enums.SiriusLayer.LEGacy) \n
		No command help available \n
			:param player: No help available
		"""
		param = Conversions.enum_scalar_to_str(player, enums.SiriusLayer)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:PLAYer {param}')

	# noinspection PyTypeChecker
	def get_pl_transmission(self) -> enums.SiriusPhysLayer:
		"""SCPI: [SOURce<HW>]:BB:SIRius:PLTRansmission \n
		Snippet: value: enums.SiriusPhysLayer = driver.source.bb.sirius.get_pl_transmission() \n
		No command help available \n
			:return: pl_transmission: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:PLTRansmission?')
		return Conversions.str_to_scalar_enum(response, enums.SiriusPhysLayer)

	def set_pl_transmission(self, pl_transmission: enums.SiriusPhysLayer) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:PLTRansmission \n
		Snippet: driver.source.bb.sirius.set_pl_transmission(pl_transmission = enums.SiriusPhysLayer.SAT1) \n
		No command help available \n
			:param pl_transmission: No help available
		"""
		param = Conversions.enum_scalar_to_str(pl_transmission, enums.SiriusPhysLayer)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:PLTRansmission {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:PRESet \n
		Snippet: driver.source.bb.sirius.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:PRESet \n
		Snippet: driver.source.bb.sirius.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:SIRius:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:SIRius:STATe \n
		Snippet: value: bool = driver.source.bb.sirius.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:STATe \n
		Snippet: driver.source.bb.sirius.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:SIRius:VERSion \n
		Snippet: value: str = driver.source.bb.sirius.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'Sirius':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sirius(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
