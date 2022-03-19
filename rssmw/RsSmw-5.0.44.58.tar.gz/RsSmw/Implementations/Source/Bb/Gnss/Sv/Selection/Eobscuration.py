from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eobscuration:
	"""Eobscuration commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eobscuration", core, parent)

	def get_angle(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:EOBScuration:ANGLe \n
		Snippet: value: float = driver.source.bb.gnss.sv.selection.eobscuration.get_angle() \n
		Sets the satellite's elevation mask angle. The angle is applied relative to the selected horizon. \n
			:return: elev_mask_angle: float Range: -10 to 90
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:EOBScuration:ANGLe?')
		return Conversions.str_to_float(response)

	def set_angle(self, elev_mask_angle: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:EOBScuration:ANGLe \n
		Snippet: driver.source.bb.gnss.sv.selection.eobscuration.set_angle(elev_mask_angle = 1.0) \n
		Sets the satellite's elevation mask angle. The angle is applied relative to the selected horizon. \n
			:param elev_mask_angle: float Range: -10 to 90
		"""
		param = Conversions.decimal_value_to_str(elev_mask_angle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:SELection:EOBScuration:ANGLe {param}')

	# noinspection PyTypeChecker
	def get_reference(self) -> enums.ElevMaskType:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:EOBScuration:REFerence \n
		Snippet: value: enums.ElevMaskType = driver.source.bb.gnss.sv.selection.eobscuration.get_reference() \n
		Selects how the behavior of earth obscuration is defined. \n
			:return: type_py: ETANgent| LHORizon
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:EOBScuration:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.ElevMaskType)

	def set_reference(self, type_py: enums.ElevMaskType) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:EOBScuration:REFerence \n
		Snippet: driver.source.bb.gnss.sv.selection.eobscuration.set_reference(type_py = enums.ElevMaskType.ETANgent) \n
		Selects how the behavior of earth obscuration is defined. \n
			:param type_py: ETANgent| LHORizon
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ElevMaskType)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:SELection:EOBScuration:REFerence {param}')
