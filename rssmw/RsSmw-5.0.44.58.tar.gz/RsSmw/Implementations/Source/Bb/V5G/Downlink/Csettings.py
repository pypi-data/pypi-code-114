from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csettings:
	"""Csettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csettings", core, parent)

	def get_ra_rnti(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSETtings:RARNti \n
		Snippet: value: int = driver.source.bb.v5G.downlink.csettings.get_ra_rnti() \n
		No command help available \n
			:return: ra_rnti: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:CSETtings:RARNti?')
		return Conversions.str_to_int(response)

	def set_ra_rnti(self, ra_rnti: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSETtings:RARNti \n
		Snippet: driver.source.bb.v5G.downlink.csettings.set_ra_rnti(ra_rnti = 1) \n
		No command help available \n
			:param ra_rnti: No help available
		"""
		param = Conversions.decimal_value_to_str(ra_rnti)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CSETtings:RARNti {param}')
