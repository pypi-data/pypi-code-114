from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.ModTypeRmc:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RMC:MODulation \n
		Snippet: value: enums.ModTypeRmc = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.rmc.modulation.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Queries the modulation of the reference measurement channel (RMC) you have selected.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on use of RMCs ([:SOURce<hw>]:BB:NR5G:UBWP:USER<ch0>:CELL<st0>:DL:BWP<dir0>:RMC:STATe) .
			- Select a RMC ([:SOURce<hw>]:BB:NR5G:UBWP:USER<ch0>:CELL<st0>:DL:BWP<dir0>:RMC:ID) . \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: rmc_modulation: QPSK| QAM64| QAM256"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RMC:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModTypeRmc)
