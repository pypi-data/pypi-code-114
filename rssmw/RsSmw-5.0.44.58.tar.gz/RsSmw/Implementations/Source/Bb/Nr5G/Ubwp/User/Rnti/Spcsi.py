from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spcsi:
	"""Spcsi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spcsi", core, parent)

	def set(self, sp_csi_rnti: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:RNTI:SPCSi \n
		Snippet: driver.source.bb.nr5G.ubwp.user.rnti.spcsi.set(sp_csi_rnti = 1, userNull = repcap.UserNull.Default) \n
		Sets the SP-CSI-RNTI of the user. It is a unique UE identification used for semi-persistent CSI reporting on PUSCH. \n
			:param sp_csi_rnti: integer Range: 1 to 65519
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(sp_csi_rnti)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:RNTI:SPCSi {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:RNTI:SPCSi \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.rnti.spcsi.get(userNull = repcap.UserNull.Default) \n
		Sets the SP-CSI-RNTI of the user. It is a unique UE identification used for semi-persistent CSI reporting on PUSCH. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: sp_csi_rnti: integer Range: 1 to 65519"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:RNTI:SPCSi?')
		return Conversions.str_to_int(response)
