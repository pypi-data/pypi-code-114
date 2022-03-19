from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Grps:
	"""Grps commands group definition. 55 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("grps", core, parent)

	@property
	def agPreset(self):
		"""agPreset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agPreset'):
			from .AgPreset import AgPreset
			self._agPreset = AgPreset(self._core, self._cmd_group)
		return self._agPreset

	@property
	def cmns(self):
		"""cmns commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cmns'):
			from .Cmns import Cmns
			self._cmns = Cmns(self._core, self._cmd_group)
		return self._cmns

	@property
	def gt(self):
		"""gt commands group. 30 Sub-classes, 0 commands."""
		if not hasattr(self, '_gt'):
			from .Gt import Gt
			self._gt = Gt(self._core, self._cmd_group)
		return self._gt

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:PRESet \n
		Snippet: driver.source.bb.stereo.grps.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:PRESet \n
		Snippet: driver.source.bb.stereo.grps.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:STEReo:GRPS:PRESet', opc_timeout_ms)

	def set_store(self, store: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:STORe \n
		Snippet: driver.source.bb.stereo.grps.set_store(store = '1') \n
		No command help available \n
			:param store: No help available
		"""
		param = Conversions.value_to_quoted_str(store)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:STORe {param}')

	def clone(self) -> 'Grps':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Grps(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
