from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XmRadio:
	"""XmRadio commands group definition. 78 total commands, 5 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xmRadio", core, parent)

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def satellite(self):
		"""satellite commands group. 4 Sub-classes, 1 commands."""
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
		"""terrestrial commands group. 5 Sub-classes, 1 commands."""
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

	def get_fcounter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:FCOunter \n
		Snippet: value: int = driver.source.bb.xmRadio.get_fcounter() \n
		No command help available \n
			:return: fcounter: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:FCOunter?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_layer(self) -> enums.XmRadioPhysLayer:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:LAYer \n
		Snippet: value: enums.XmRadioPhysLayer = driver.source.bb.xmRadio.get_layer() \n
		No command help available \n
			:return: layer: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:LAYer?')
		return Conversions.str_to_scalar_enum(response, enums.XmRadioPhysLayer)

	def set_layer(self, layer: enums.XmRadioPhysLayer) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:LAYer \n
		Snippet: driver.source.bb.xmRadio.set_layer(layer = enums.XmRadioPhysLayer.SAT1A) \n
		No command help available \n
			:param layer: No help available
		"""
		param = Conversions.enum_scalar_to_str(layer, enums.XmRadioPhysLayer)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:LAYer {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:PRESet \n
		Snippet: driver.source.bb.xmRadio.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:PRESet \n
		Snippet: driver.source.bb.xmRadio.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:XMRadio:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:STATe \n
		Snippet: value: bool = driver.source.bb.xmRadio.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:STATe \n
		Snippet: driver.source.bb.xmRadio.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:STATe {param}')

	def get_version(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:VERSion \n
		Snippet: value: str = driver.source.bb.xmRadio.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:VERSion?')
		return trim_str_response(response)

	def clone(self) -> 'XmRadio':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = XmRadio(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
