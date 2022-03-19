from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlength:
	"""Dlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlength", core, parent)

	# noinspection PyTypeChecker
	def get_select(self) -> enums.HrpUwbDeltaLength:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DLENgth:SELect \n
		Snippet: value: enums.HrpUwbDeltaLength = driver.source.bb.huwb.fconfig.dlength.get_select() \n
		No command help available \n
			:return: delta_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:DLENgth:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbDeltaLength)

	def set_select(self, delta_length: enums.HrpUwbDeltaLength) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DLENgth:SELect \n
		Snippet: driver.source.bb.huwb.fconfig.dlength.set_select(delta_length = enums.HrpUwbDeltaLength.DL_16) \n
		No command help available \n
			:param delta_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(delta_length, enums.HrpUwbDeltaLength)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:DLENgth:SELect {param}')
