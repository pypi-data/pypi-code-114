from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	def set(self, user: enums.EutraPdcchCfg, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:USER \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.user.set(user = enums.EutraPdcchCfg.CCRNti, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Selects the User the DCI is dedicated to. The available DCI Formats depend on the value of this parameter. \n
			:param user: USER1| USER2| USER3| USER4| PRNTi| SIRNti| RARNti| NONE | U1E| U2E| U3E| UE4 | CCNRti
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.enum_scalar_to_str(user, enums.EutraPdcchCfg)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:USER {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> enums.EutraPdcchCfg:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:USER \n
		Snippet: value: enums.EutraPdcchCfg = driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.user.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Selects the User the DCI is dedicated to. The available DCI Formats depend on the value of this parameter. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: user: USER1| USER2| USER3| USER4| PRNTi| SIRNti| RARNti| NONE | U1E| U2E| U3E| UE4 | CCNRti"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:USER?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPdcchCfg)
