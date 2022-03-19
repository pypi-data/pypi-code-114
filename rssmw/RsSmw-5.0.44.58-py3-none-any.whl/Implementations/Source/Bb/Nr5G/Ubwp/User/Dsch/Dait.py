from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dait:
	"""Dait commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dait", core, parent)

	def set(self, nfi_total_dai_incl: bool, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:DAIT \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.dait.set(nfi_total_dai_incl = False, userNull = repcap.UserNull.Default) \n
		Configures the higher layer parameter nfi-TotalDAIIncluded as defined in 3GPP 38.331. \n
			:param nfi_total_dai_incl: 1| ON| 0| OFF
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(nfi_total_dai_incl)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:DAIT {param}')

	def get(self, userNull=repcap.UserNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:DAIT \n
		Snippet: value: bool = driver.source.bb.nr5G.ubwp.user.dsch.dait.get(userNull = repcap.UserNull.Default) \n
		Configures the higher layer parameter nfi-TotalDAIIncluded as defined in 3GPP 38.331. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: nfi_total_dai_incl: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:DAIT?')
		return Conversions.str_to_bool(response)
