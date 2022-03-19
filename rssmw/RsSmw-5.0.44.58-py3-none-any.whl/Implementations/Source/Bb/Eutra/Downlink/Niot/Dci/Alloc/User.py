from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	def set(self, user: enums.EutraEmtcPdcchCfg, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:USER \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.user.set(user = enums.EutraEmtcPdcchCfg.PRNTi, allocationNull = repcap.AllocationNull.Default) \n
		Selects the user the DCI is dedicated to. \n
			:param user: USER1| USER2| USER3| USER4| PRNTi| RARNti
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(user, enums.EutraEmtcPdcchCfg)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:USER {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraEmtcPdcchCfg:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:USER \n
		Snippet: value: enums.EutraEmtcPdcchCfg = driver.source.bb.eutra.downlink.niot.dci.alloc.user.get(allocationNull = repcap.AllocationNull.Default) \n
		Selects the user the DCI is dedicated to. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: user: USER1| USER2| USER3| USER4| PRNTi| RARNti"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:USER?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcPdcchCfg)
