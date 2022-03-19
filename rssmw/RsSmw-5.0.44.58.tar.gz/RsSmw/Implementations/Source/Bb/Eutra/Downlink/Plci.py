from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plci:
	"""Plci commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plci", core, parent)

	def get_cid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[PLCI]:CID \n
		Snippet: value: int = driver.source.bb.eutra.downlink.plci.get_cid() \n
		Sets the cell identity. \n
			:return: cell_id: integer Range: 0 to 503
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PLCI:CID?')
		return Conversions.str_to_int(response)

	def set_cid(self, cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[PLCI]:CID \n
		Snippet: driver.source.bb.eutra.downlink.plci.set_cid(cell_id = 1) \n
		Sets the cell identity. \n
			:param cell_id: integer Range: 0 to 503
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PLCI:CID {param}')

	def get_cid_group(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[PLCI]:CIDGroup \n
		Snippet: value: int = driver.source.bb.eutra.downlink.plci.get_cid_group() \n
		Sets the ID of the physical cell identity group. \n
			:return: cell_id_group: integer Range: 0 to 167
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PLCI:CIDGroup?')
		return Conversions.str_to_int(response)

	def set_cid_group(self, cell_id_group: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[PLCI]:CIDGroup \n
		Snippet: driver.source.bb.eutra.downlink.plci.set_cid_group(cell_id_group = 1) \n
		Sets the ID of the physical cell identity group. \n
			:param cell_id_group: integer Range: 0 to 167
		"""
		param = Conversions.decimal_value_to_str(cell_id_group)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PLCI:CIDGroup {param}')

	def get_plid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[PLCI]:PLID \n
		Snippet: value: int = driver.source.bb.eutra.downlink.plci.get_plid() \n
		Sets the identity of the physical layer within the selected physical cell identity group, set with the command
		[:SOURce<hw>]:BB:EUTRa:DL[:PLCI]:CIDGroup. \n
			:return: phys_lay_id: integer Range: 0 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PLCI:PLID?')
		return Conversions.str_to_int(response)

	def set_plid(self, phys_lay_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[PLCI]:PLID \n
		Snippet: driver.source.bb.eutra.downlink.plci.set_plid(phys_lay_id = 1) \n
		Sets the identity of the physical layer within the selected physical cell identity group, set with the command
		[:SOURce<hw>]:BB:EUTRa:DL[:PLCI]:CIDGroup. \n
			:param phys_lay_id: integer Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(phys_lay_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PLCI:PLID {param}')
