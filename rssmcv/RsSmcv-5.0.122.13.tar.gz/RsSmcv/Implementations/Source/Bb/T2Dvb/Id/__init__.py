from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	@property
	def txid(self):
		"""txid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txid'):
			from .Txid import Txid
			self._txid = Txid(self._core, self._cmd_group)
		return self._txid

	def get_cell(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:CELL \n
		Snippet: value: int = driver.source.bb.t2Dvb.id.get_cell() \n
		Sets the cell identification (ID) . \n
			:return: cell_id: integer 16-bit value in hexadecimal representation. Range: #H0 to #HFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:ID:CELL?')
		return Conversions.str_to_int(response)

	def set_cell(self, cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:CELL \n
		Snippet: driver.source.bb.t2Dvb.id.set_cell(cell_id = 1) \n
		Sets the cell identification (ID) . \n
			:param cell_id: integer 16-bit value in hexadecimal representation. Range: #H0 to #HFFFF
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:ID:CELL {param}')

	def get_network(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:NETWork \n
		Snippet: value: int = driver.source.bb.t2Dvb.id.get_network() \n
		Sets the network identification. \n
			:return: network_id: integer 16-bit value in hexadecimal representation. Range: #H0 to #HFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:ID:NETWork?')
		return Conversions.str_to_int(response)

	def set_network(self, network_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:NETWork \n
		Snippet: driver.source.bb.t2Dvb.id.set_network(network_id = 1) \n
		Sets the network identification. \n
			:param network_id: integer 16-bit value in hexadecimal representation. Range: #H0 to #HFFFF
		"""
		param = Conversions.decimal_value_to_str(network_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:ID:NETWork {param}')

	def get_t_2_system(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:T2SYstem \n
		Snippet: value: int = driver.source.bb.t2Dvb.id.get_t_2_system() \n
		Sets the T2 system identification. \n
			:return: t_2_system_id: integer 16-bit value in hexadecimal representation. Range: #H0 to #HFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:ID:T2SYstem?')
		return Conversions.str_to_int(response)

	def set_t_2_system(self, t_2_system_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:T2SYstem \n
		Snippet: driver.source.bb.t2Dvb.id.set_t_2_system(t_2_system_id = 1) \n
		Sets the T2 system identification. \n
			:param t_2_system_id: integer 16-bit value in hexadecimal representation. Range: #H0 to #HFFFF
		"""
		param = Conversions.decimal_value_to_str(t_2_system_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:ID:T2SYstem {param}')

	def clone(self) -> 'Id':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Id(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
