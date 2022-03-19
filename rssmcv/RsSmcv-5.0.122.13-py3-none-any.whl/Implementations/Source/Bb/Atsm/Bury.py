from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bury:
	"""Bury commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bury", core, parent)

	# noinspection PyTypeChecker
	def get_ratio(self) -> enums.AtscmhBuryRatio:
		"""SCPI: [SOURce<HW>]:BB:ATSM:BURY:RATio \n
		Snippet: value: enums.AtscmhBuryRatio = driver.source.bb.atsm.bury.get_ratio() \n
		Sets the power with that the watermark is added to the payload signal. \n
			:return: market_id: DB21| DB24| DB27| DB30| DB33| DB36| DB39 DBxx Bury ration value 'xx' in decibel.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:BURY:RATio?')
		return Conversions.str_to_scalar_enum(response, enums.AtscmhBuryRatio)

	def set_ratio(self, market_id: enums.AtscmhBuryRatio) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:BURY:RATio \n
		Snippet: driver.source.bb.atsm.bury.set_ratio(market_id = enums.AtscmhBuryRatio.DB21) \n
		Sets the power with that the watermark is added to the payload signal. \n
			:param market_id: DB21| DB24| DB27| DB30| DB33| DB36| DB39 DBxx Bury ration value 'xx' in decibel.
		"""
		param = Conversions.enum_scalar_to_str(market_id, enums.AtscmhBuryRatio)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:BURY:RATio {param}')
