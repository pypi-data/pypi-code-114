from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfAlignment:
	"""RfAlignment commands group definition. 12 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfAlignment", core, parent)

	@property
	def calibrated(self):
		"""calibrated commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_calibrated'):
			from .Calibrated import Calibrated
			self._calibrated = Calibrated(self._core, self._cmd_group)
		return self._calibrated

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def fresponse(self):
		"""fresponse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fresponse'):
			from .Fresponse import Fresponse
			self._fresponse = Fresponse(self._core, self._cmd_group)
		return self._fresponse

	@property
	def rfInfo(self):
		"""rfInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfInfo'):
			from .RfInfo import RfInfo
			self._rfInfo = RfInfo(self._core, self._cmd_group)
		return self._rfInfo

	def get_dattenuation(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:DATTenuation \n
		Snippet: value: float = driver.source.rfAlignment.get_dattenuation() \n
		Queries the applied digital attenuation. \n
			:return: attenuation: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:DATTenuation?')
		return Conversions.str_to_float(response)

	def get_directory(self) -> str:
		"""SCPI: SOURce<HW>:RFALignment:DIRectory \n
		Snippet: value: str = driver.source.rfAlignment.get_directory() \n
		No command help available \n
			:return: directory: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:DIRectory?')
		return trim_str_response(response)

	def get_foffset(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:FOFFset \n
		Snippet: value: float = driver.source.rfAlignment.get_foffset() \n
		Queries the applied baseband frequency offset. \n
			:return: bb_freq_offset: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:FOFFset?')
		return Conversions.str_to_float(response)

	def get_state(self) -> bool:
		"""SCPI: SOURce<HW>:RFALignment:STATe \n
		Snippet: value: bool = driver.source.rfAlignment.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SOURce<HW>:RFALignment:STATe \n
		Snippet: driver.source.rfAlignment.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:RFALignment:STATe {param}')

	def clone(self) -> 'RfAlignment':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfAlignment(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
