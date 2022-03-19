from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Opu:
	"""Opu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("opu", core, parent)

	# noinspection PyTypeChecker
	def get_use(self) -> enums.CalPowOpuMode:
		"""SCPI: CALibration<HW>:LEVel:OPU:USE \n
		Snippet: value: enums.CalPowOpuMode = driver.calibration.level.opu.get_use() \n
		No command help available \n
			:return: opu_mode: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:OPU:USE?')
		return Conversions.str_to_scalar_enum(response, enums.CalPowOpuMode)

	def set_use(self, opu_mode: enums.CalPowOpuMode) -> None:
		"""SCPI: CALibration<HW>:LEVel:OPU:USE \n
		Snippet: driver.calibration.level.opu.set_use(opu_mode = enums.CalPowOpuMode.AUTO) \n
		No command help available \n
			:param opu_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(opu_mode, enums.CalPowOpuMode)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:OPU:USE {param}')
