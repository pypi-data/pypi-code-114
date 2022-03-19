from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mue:
	"""Mue commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mue", core, parent)

	def get_ovrb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:MUE:OVRB \n
		Snippet: value: int = driver.source.bb.eutra.tcw.mue.get_ovrb() \n
		Sets the number of RB the allocated RB(s) are shifted with. \n
			:return: offset_vrb: integer Range: 0 to 75
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:MUE:OVRB?')
		return Conversions.str_to_int(response)

	def set_ovrb(self, offset_vrb: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:MUE:OVRB \n
		Snippet: driver.source.bb.eutra.tcw.mue.set_ovrb(offset_vrb = 1) \n
		Sets the number of RB the allocated RB(s) are shifted with. \n
			:param offset_vrb: integer Range: 0 to 75
		"""
		param = Conversions.decimal_value_to_str(offset_vrb)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:MUE:OVRB {param}')

	def get_tsrs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:MUE:TSRS \n
		Snippet: value: bool = driver.source.bb.eutra.tcw.mue.get_tsrs() \n
		Enables/disables the transmission of the SRS. The SRS transmission is optional for this test case. \n
			:return: transmit_srs: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:MUE:TSRS?')
		return Conversions.str_to_bool(response)

	def set_tsrs(self, transmit_srs: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:MUE:TSRS \n
		Snippet: driver.source.bb.eutra.tcw.mue.set_tsrs(transmit_srs = False) \n
		Enables/disables the transmission of the SRS. The SRS transmission is optional for this test case. \n
			:param transmit_srs: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(transmit_srs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:MUE:TSRS {param}')

	def get_ue_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:MUE:UEID \n
		Snippet: value: int = driver.source.bb.eutra.tcw.mue.get_ue_id() \n
		Sets the UE ID/n_RNTI. \n
			:return: ue_idn_rnti: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:MUE:UEID?')
		return Conversions.str_to_int(response)

	def set_ue_id(self, ue_idn_rnti: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:MUE:UEID \n
		Snippet: driver.source.bb.eutra.tcw.mue.set_ue_id(ue_idn_rnti = 1) \n
		Sets the UE ID/n_RNTI. \n
			:param ue_idn_rnti: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ue_idn_rnti)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:MUE:UEID {param}')
