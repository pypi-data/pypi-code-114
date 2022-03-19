from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sespace:
	"""Sespace commands group definition. 5 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sespace", core, parent)

	@property
	def chk(self):
		"""chk commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_chk'):
			from .Chk import Chk
			self._chk = Chk(self._core, self._cmd_group)
		return self._chk

	@property
	def max(self):
		"""max commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	@property
	def min(self):
		"""min commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_min'):
			from .Min import Min
			self._min = Min(self._core, self._cmd_group)
		return self._min

	def set(self, search_space: enums.EutraSearchSpace, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:SESPace \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.sespace.set(search_space = enums.EutraSearchSpace._0, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		If enabled, this parameter configures the PDCCH DCI to be transmitted within the common or UE-specific search space. \n
			:param search_space: OFF| AUTO| COMMon| UE| ON| 0| 1 COMMon|UE Common and UE-specific search spaces, as defined in the 3GPP specification OFF|AUTO For backwards compatibility only.
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.enum_scalar_to_str(search_space, enums.EutraSearchSpace)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:SESPace {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> enums.EutraSearchSpace:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:SESPace \n
		Snippet: value: enums.EutraSearchSpace = driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.sespace.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		If enabled, this parameter configures the PDCCH DCI to be transmitted within the common or UE-specific search space. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: search_space: OFF| AUTO| COMMon| UE| ON| 0| 1 COMMon|UE Common and UE-specific search spaces, as defined in the 3GPP specification OFF|AUTO For backwards compatibility only."""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:SESPace?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSearchSpace)

	def clone(self) -> 'Sespace':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sespace(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
