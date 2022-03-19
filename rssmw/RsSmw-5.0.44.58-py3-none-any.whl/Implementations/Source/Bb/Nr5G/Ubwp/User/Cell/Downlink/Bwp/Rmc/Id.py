from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def set(self, rmc_id: enums.RmcIdAll, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RMC:ID \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.rmc.id.set(rmc_id = enums.RmcIdAll.F215, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		This command selects a reference measurement channel. The availability of RMCs depends on the subcarrier spacing of the
		bandwidth part you are configuring. \n
			:param rmc_id: FQ15| FQ30| FQ60| F615| F630| F660| F215| F230| F260| TQ15| TQ30| TQ60| T615| T630| T660| T215| T230| T260| TS38176_FR1A311| TS38176_FR1A312| TS38176_FR1A313| TS38176_FR1A314| TS38176_FR1A315| TS38176_FR2A311| TS38176_FR2A312| TS38176_FR2A313| TS38176_FR1A321| TS38176_FR2A321| TS38176_FR2A322| TS38176_FR1A331| FR2TQ60| FR2TQ120| FR2T660| FR2T6120| FR2T260| FR2T2120| TS38176_FR1A351| TS38176_FR1A352| TS38176_FR1A353| TS38176_FR1A354| TS38176_FR1A355| TS38176_FR1A356| TS38176_FR2A351| TS38176_FR2A352| TS38176_FR2A353 The logic of the labels is as follows: No prefix = 38.521 FR1 RMCs Prefix FR2 = 38.521 FR2 RMCs F / T = duplexing (FDD or TDD) Q / 6 / 2 = modulation (QPSK, 64QAM or 256 QAM) 15 / 30 / 60 = subcarrier spacing (15, 30 or 60 kHz) For example 'T615' corresponds to FR1 RMC with the name 'TS 38.521: A.3.3.3-1 (15 kHz) '. The RMCs from 38.176 are basically a shortened form of the names of the RMCs. For example 'TS38176_FR1A352' corresponds to RMC with the name 'TS 38.176: M-FR1-A3_5_2'.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(rmc_id, enums.RmcIdAll)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RMC:ID {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.RmcIdAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:BWP<DIR0>:RMC:ID \n
		Snippet: value: enums.RmcIdAll = driver.source.bb.nr5G.ubwp.user.cell.downlink.bwp.rmc.id.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		This command selects a reference measurement channel. The availability of RMCs depends on the subcarrier spacing of the
		bandwidth part you are configuring. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: rmc_id: FQ15| FQ30| FQ60| F615| F630| F660| F215| F230| F260| TQ15| TQ30| TQ60| T615| T630| T660| T215| T230| T260| TS38176_FR1A311| TS38176_FR1A312| TS38176_FR1A313| TS38176_FR1A314| TS38176_FR1A315| TS38176_FR2A311| TS38176_FR2A312| TS38176_FR2A313| TS38176_FR1A321| TS38176_FR2A321| TS38176_FR2A322| TS38176_FR1A331| FR2TQ60| FR2TQ120| FR2T660| FR2T6120| FR2T260| FR2T2120| TS38176_FR1A351| TS38176_FR1A352| TS38176_FR1A353| TS38176_FR1A354| TS38176_FR1A355| TS38176_FR1A356| TS38176_FR2A351| TS38176_FR2A352| TS38176_FR2A353 The logic of the labels is as follows: No prefix = 38.521 FR1 RMCs Prefix FR2 = 38.521 FR2 RMCs F / T = duplexing (FDD or TDD) Q / 6 / 2 = modulation (QPSK, 64QAM or 256 QAM) 15 / 30 / 60 = subcarrier spacing (15, 30 or 60 kHz) For example 'T615' corresponds to FR1 RMC with the name 'TS 38.521: A.3.3.3-1 (15 kHz) '. The RMCs from 38.176 are basically a shortened form of the names of the RMCs. For example 'TS38176_FR1A352' corresponds to RMC with the name 'TS 38.176: M-FR1-A3_5_2'."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:BWP{bwPartNull_cmd_val}:RMC:ID?')
		return Conversions.str_to_scalar_enum(response, enums.RmcIdAll)
