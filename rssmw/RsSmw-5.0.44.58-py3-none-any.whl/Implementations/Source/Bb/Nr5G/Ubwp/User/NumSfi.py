from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NumSfi:
	"""NumSfi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("numSfi", core, parent)

	def set(self, num_sfi_in_dci_20: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:NUMSfi \n
		Snippet: driver.source.bb.nr5G.ubwp.user.numSfi.set(num_sfi_in_dci_20 = 1, userNull = repcap.UserNull.Default) \n
		Sets how many slot format indicator (SFI) fields are transmitted in the DCI format 2_0. \n
			:param num_sfi_in_dci_20: integer Range: 1 to 16
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(num_sfi_in_dci_20)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:NUMSfi {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:NUMSfi \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.numSfi.get(userNull = repcap.UserNull.Default) \n
		Sets how many slot format indicator (SFI) fields are transmitted in the DCI format 2_0. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: num_sfi_in_dci_20: integer Range: 1 to 16"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:NUMSfi?')
		return Conversions.str_to_int(response)
