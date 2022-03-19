from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Anetwork:
	"""Anetwork commands group definition. 14 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anetwork", core, parent)

	@property
	def cchannel(self):
		"""cchannel commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_cchannel'):
			from .Cchannel import Cchannel
			self._cchannel = Cchannel(self._core, self._cmd_group)
		return self._cchannel

	@property
	def pchannel(self):
		"""pchannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pchannel'):
			from .Pchannel import Pchannel
			self._pchannel = Pchannel(self._core, self._cmd_group)
		return self._pchannel

	@property
	def rab(self):
		"""rab commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_rab'):
			from .Rab import Rab
			self._rab = Rab(self._core, self._cmd_group)
		return self._rab

	def get_cp_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CPMode \n
		Snippet: value: bool = driver.source.bb.evdo.anetwork.get_cp_mode() \n
		Enables or disables a special mode within the 1xEV-DO generator. Note: During the special mode, all other parameters do
		not affect the signal output. \n
			:return: cp_mode: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:CPMode?')
		return Conversions.str_to_bool(response)

	def set_cp_mode(self, cp_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CPMode \n
		Snippet: driver.source.bb.evdo.anetwork.set_cp_mode(cp_mode = False) \n
		Enables or disables a special mode within the 1xEV-DO generator. Note: During the special mode, all other parameters do
		not affect the signal output. \n
			:param cp_mode: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(cp_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:CPMode {param}')

	def get_ou_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:OUCount \n
		Snippet: value: int = driver.source.bb.evdo.anetwork.get_ou_count() \n
		Sets the number of additional users (beyond the four defined users) that appear in the MAC Channel. \n
			:return: ou_count: integer Range: 0 to 55 for physical layer subtype 0&1) , 0 to 110 for physical layer subtype 2, 0 to 360 for physical layer subtype 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:OUCount?')
		return Conversions.str_to_int(response)

	def set_ou_count(self, ou_count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:OUCount \n
		Snippet: driver.source.bb.evdo.anetwork.set_ou_count(ou_count = 1) \n
		Sets the number of additional users (beyond the four defined users) that appear in the MAC Channel. \n
			:param ou_count: integer Range: 0 to 55 for physical layer subtype 0&1) , 0 to 110 for physical layer subtype 2, 0 to 360 for physical layer subtype 3
		"""
		param = Conversions.decimal_value_to_str(ou_count)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:OUCount {param}')

	# noinspection PyTypeChecker
	def get_sub_type(self) -> enums.EvdoLayerDn:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:SUBType \n
		Snippet: value: enums.EvdoLayerDn = driver.source.bb.evdo.anetwork.get_sub_type() \n
		Selects the physical layer subtype. Note: The physical layer subtype settings can be queried per user. \n
			:return: sub_type: S1| S2| S3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:SUBType?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoLayerDn)

	def set_sub_type(self, sub_type: enums.EvdoLayerDn) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:SUBType \n
		Snippet: driver.source.bb.evdo.anetwork.set_sub_type(sub_type = enums.EvdoLayerDn.S1) \n
		Selects the physical layer subtype. Note: The physical layer subtype settings can be queried per user. \n
			:param sub_type: S1| S2| S3
		"""
		param = Conversions.enum_scalar_to_str(sub_type, enums.EvdoLayerDn)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:SUBType {param}')

	def clone(self) -> 'Anetwork':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Anetwork(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
