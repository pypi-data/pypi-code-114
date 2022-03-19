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
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[PLCI]:CID \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.plci.get_cid() \n
		Sets the cell identity. \n
			:return: cell_id: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PLCI:CID?')
		return Conversions.str_to_int(response)

	def set_cid(self, cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[PLCI]:CID \n
		Snippet: driver.source.bb.oneweb.downlink.plci.set_cid(cell_id = 1) \n
		Sets the cell identity. \n
			:param cell_id: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PLCI:CID {param}')

	def get_cid_group(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[PLCI]:CIDGroup \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.plci.get_cid_group() \n
		No command help available \n
			:return: cell_id_group: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PLCI:CIDGroup?')
		return Conversions.str_to_int(response)

	def set_cid_group(self, cell_id_group: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[PLCI]:CIDGroup \n
		Snippet: driver.source.bb.oneweb.downlink.plci.set_cid_group(cell_id_group = 1) \n
		No command help available \n
			:param cell_id_group: No help available
		"""
		param = Conversions.decimal_value_to_str(cell_id_group)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PLCI:CIDGroup {param}')

	def get_plid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[PLCI]:PLID \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.plci.get_plid() \n
		No command help available \n
			:return: phys_lay_id: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:DL:PLCI:PLID?')
		return Conversions.str_to_int(response)

	def set_plid(self, phys_lay_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[PLCI]:PLID \n
		Snippet: driver.source.bb.oneweb.downlink.plci.set_plid(phys_lay_id = 1) \n
		No command help available \n
			:param phys_lay_id: No help available
		"""
		param = Conversions.decimal_value_to_str(phys_lay_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:PLCI:PLID {param}')
