from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 6 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def isPy(self):
		"""isPy commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_isPy'):
			from .IsPy import IsPy
			self._isPy = IsPy(self._core, self._cmd_group)
		return self._isPy

	# noinspection PyTypeChecker
	def get_cm_mode(self) -> enums.Dvbs2InputSignalCmMode:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[INPut]:CMMode \n
		Snippet: value: enums.Dvbs2InputSignalCmMode = driver.source.bb.dvbs2.inputPy.get_cm_mode() \n
		Sets the coding and modulation (CM) mode. \n
			:return: cm_mode: VCM| CCM| ACM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:INPut:CMMode?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbs2InputSignalCmMode)

	def set_cm_mode(self, cm_mode: enums.Dvbs2InputSignalCmMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[INPut]:CMMode \n
		Snippet: driver.source.bb.dvbs2.inputPy.set_cm_mode(cm_mode = enums.Dvbs2InputSignalCmMode.ACM) \n
		Sets the coding and modulation (CM) mode. \n
			:param cm_mode: VCM| CCM| ACM
		"""
		param = Conversions.enum_scalar_to_str(cm_mode, enums.Dvbs2InputSignalCmMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:INPut:CMMode {param}')

	def get_nis(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[INPut]:NIS \n
		Snippet: value: float = driver.source.bb.dvbs2.inputPy.get_nis() \n
		Sets the number of input streams. Maximum 8 input streams are possible. \n
			:return: num_inp_sig: float Range: 1 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:INPut:NIS?')
		return Conversions.str_to_float(response)

	def set_nis(self, num_inp_sig: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[INPut]:NIS \n
		Snippet: driver.source.bb.dvbs2.inputPy.set_nis(num_inp_sig = 1.0) \n
		Sets the number of input streams. Maximum 8 input streams are possible. \n
			:param num_inp_sig: float Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(num_inp_sig)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:INPut:NIS {param}')

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
