from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cosine:
	"""Cosine commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cosine", core, parent)

	def get_cofs(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLAD:FILTer:PARameter:COSine:COFS \n
		Snippet: value: float = driver.source.bb.wlad.filterPy.parameter.cosine.get_cofs() \n
		Sets the cut of frequency shift value for the cosine filter type. \n
			:return: cofs: float Range: -1 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:FILTer:PARameter:COSine:COFS?')
		return Conversions.str_to_float(response)

	def set_cofs(self, cofs: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:FILTer:PARameter:COSine:COFS \n
		Snippet: driver.source.bb.wlad.filterPy.parameter.cosine.set_cofs(cofs = 1.0) \n
		Sets the cut of frequency shift value for the cosine filter type. \n
			:param cofs: float Range: -1 to 1
		"""
		param = Conversions.decimal_value_to_str(cofs)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:FILTer:PARameter:COSine:COFS {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLAD:FILTer:PARameter:COSine \n
		Snippet: value: float = driver.source.bb.wlad.filterPy.parameter.cosine.get_value() \n
		Sets the roll-off factor for the cosine filter type. \n
			:return: cosine: float Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:FILTer:PARameter:COSine?')
		return Conversions.str_to_float(response)

	def set_value(self, cosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:FILTer:PARameter:COSine \n
		Snippet: driver.source.bb.wlad.filterPy.parameter.cosine.set_value(cosine = 1.0) \n
		Sets the roll-off factor for the cosine filter type. \n
			:param cosine: float Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(cosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:FILTer:PARameter:COSine {param}')
