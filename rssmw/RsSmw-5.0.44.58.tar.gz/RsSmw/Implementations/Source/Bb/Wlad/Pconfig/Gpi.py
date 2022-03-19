from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gpi:
	"""Gpi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gpi", core, parent)

	# noinspection PyTypeChecker
	def get_gp_index(self) -> enums.WlanadGrpPrIdx:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:GPI:GPINdex \n
		Snippet: value: enums.WlanadGrpPrIdx = driver.source.bb.wlad.pconfig.gpi.get_gp_index() \n
		No command help available \n
			:return: dgpi: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:GPI:GPINdex?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadGrpPrIdx)

	def set_gp_index(self, dgpi: enums.WlanadGrpPrIdx) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:GPI:GPINdex \n
		Snippet: driver.source.bb.wlad.pconfig.gpi.set_gp_index(dgpi = enums.WlanadGrpPrIdx.GPI0) \n
		No command help available \n
			:param dgpi: No help available
		"""
		param = Conversions.enum_scalar_to_str(dgpi, enums.WlanadGrpPrIdx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:GPI:GPINdex {param}')
