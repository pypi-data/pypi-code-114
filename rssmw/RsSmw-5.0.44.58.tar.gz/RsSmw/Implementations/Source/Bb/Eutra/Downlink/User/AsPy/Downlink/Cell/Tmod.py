from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmod:
	"""Tmod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmod", core, parent)

	def set(self, target_mod: enums.ModulationD, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:CELL<ST0>:TMOD \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.downlink.cell.tmod.set(target_mod = enums.ModulationD.QAM1024, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the target moduilation. \n
			:param target_mod: QPSK| QAM16| QAM64 | QAM256
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(target_mod, enums.ModulationD)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:TMOD {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> enums.ModulationD:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:CELL<ST0>:TMOD \n
		Snippet: value: enums.ModulationD = driver.source.bb.eutra.downlink.user.asPy.downlink.cell.tmod.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the target moduilation. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: target_mod: QPSK| QAM16| QAM64 | QAM256"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:CELL{cellNull_cmd_val}:TMOD?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationD)
