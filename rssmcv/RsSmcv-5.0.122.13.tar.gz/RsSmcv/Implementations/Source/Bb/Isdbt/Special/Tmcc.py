from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmcc:
	"""Tmcc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmcc", core, parent)

	# noinspection PyTypeChecker
	def get_next(self) -> enums.IsdbtSpecialTmcc:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:TMCC:NEXT \n
		Snippet: value: enums.IsdbtSpecialTmcc = driver.source.bb.isdbt.special.tmcc.get_next() \n
		Sets the next information bits. \n
			:return: mtcc_next: UNUSed| CURRent
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SPECial:TMCC:NEXT?')
		return Conversions.str_to_scalar_enum(response, enums.IsdbtSpecialTmcc)

	def set_next(self, mtcc_next: enums.IsdbtSpecialTmcc) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:[SPECial]:TMCC:NEXT \n
		Snippet: driver.source.bb.isdbt.special.tmcc.set_next(mtcc_next = enums.IsdbtSpecialTmcc.CURRent) \n
		Sets the next information bits. \n
			:param mtcc_next: UNUSed| CURRent
		"""
		param = Conversions.enum_scalar_to_str(mtcc_next, enums.IsdbtSpecialTmcc)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SPECial:TMCC:NEXT {param}')
