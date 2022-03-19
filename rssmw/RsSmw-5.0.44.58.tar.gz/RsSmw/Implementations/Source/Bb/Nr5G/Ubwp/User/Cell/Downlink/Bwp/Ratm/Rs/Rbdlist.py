from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.Utilities import trim_str_response
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbdlist:
	"""Rbdlist commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbdlist", core, parent)

	def set(self, rate_rb_patt_dlist: str, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default, rateSettingNull=repcap.RateSettingNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RATM:RS<GR0>:RBDList \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.ratm.rs.rbdlist.set(rate_rb_patt_dlist = '1', userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default, rateSettingNull = repcap.RateSettingNull.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param rate_rb_patt_dlist: string Filename incl. file extension or complete file path
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:param rateSettingNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rs')
		"""
		param = Conversions.value_to_quoted_str(rate_rb_patt_dlist)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		rateSettingNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rateSettingNull, repcap.RateSettingNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RATM:RS{rateSettingNull_cmd_val}:RBDList {param}')

	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default, rateSettingNull=repcap.RateSettingNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RATM:RS<GR0>:RBDList \n
		Snippet: value: str = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.ratm.rs.rbdlist.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default, rateSettingNull = repcap.RateSettingNull.Default) \n
		Selects an existing data list file from the default directory or from the specific directory. Refer to 'Accessing Files
		in the Default or Specified Directory' for general information on file handling in the default and in a specific
		directory. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:param rateSettingNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Rs')
			:return: rate_rb_patt_dlist: string Filename incl. file extension or complete file path"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		rateSettingNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rateSettingNull, repcap.RateSettingNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RATM:RS{rateSettingNull_cmd_val}:RBDList?')
		return trim_str_response(response)
