from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McbGroups:
	"""McbGroups commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcbGroups", core, parent)

	def set(self, dl_max_cbg_per_tb: enums.MaxCbgaLl, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:MCBGroups \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.mcbGroups.set(dl_max_cbg_per_tb = enums.MaxCbgaLl.DISabled, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Limits the number of code block groups per transport block. In 5G NR a huge TB (transport block) is split into multiple
		code blocks (CB) . Multiples CBs are grouped into one code block group (CBG) . The number of code blocks grouped into the
		CBG can be limited by the 'Max Code Block Groups Per Transport Block' setting. \n
			:param dl_max_cbg_per_tb: G2| G4| DISabled| G6| G8 G2 Limits the number of code block groups per transport block to 2. G4 Limits the number of code block groups per transport block to 4. G6 Limits the number of code block groups per transport block to 6. G8 Limits the number of code block groups per transport block to 8. DISabled Default value (also G0) , which disabled the limitation of code block groups per transport block.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(dl_max_cbg_per_tb, enums.MaxCbgaLl)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:MCBGroups {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.MaxCbgaLl:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:PDSCh:MCBGroups \n
		Snippet: value: enums.MaxCbgaLl = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.pdsch.mcbGroups.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Limits the number of code block groups per transport block. In 5G NR a huge TB (transport block) is split into multiple
		code blocks (CB) . Multiples CBs are grouped into one code block group (CBG) . The number of code blocks grouped into the
		CBG can be limited by the 'Max Code Block Groups Per Transport Block' setting. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: dl_max_cbg_per_tb: G2| G4| DISabled| G6| G8 G2 Limits the number of code block groups per transport block to 2. G4 Limits the number of code block groups per transport block to 4. G6 Limits the number of code block groups per transport block to 6. G8 Limits the number of code block groups per transport block to 8. DISabled Default value (also G0) , which disabled the limitation of code block groups per transport block."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:PDSCh:MCBGroups?')
		return Conversions.str_to_scalar_enum(response, enums.MaxCbgaLl)
