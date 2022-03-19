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
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSETtings:RARNti \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.csettings.get_ra_rnti() \n
		Sets the random-access response identity RA-RNTI. The value selected here determines the value of the parameter
		'UE_ID/n_RNTI' in case a RA_RNTI 'User' is selected. \n
			:return: ra_rnti: integer Range: 1 to 60
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:CSETtings:RARNti?')
		return Conversions.str_to_int(response)

	def set_ra_rnti(self, ra_rnti: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:CSETtings:RARNti \n
		Snippet: driver.source.bb.oneweb.downlink.csettings.set_ra_rnti(ra_rnti = 1) \n
		Sets the random-access response identity RA-RNTI. The value selected here determines the value of the parameter
		'UE_ID/n_RNTI' in case a RA_RNTI 'User' is selected. \n
			:param ra_rnti: integer Range: 1 to 60
		"""
		param = Conversions.decimal_value_to_str(ra_rnti)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:CSETtings:RARNti {param}')
