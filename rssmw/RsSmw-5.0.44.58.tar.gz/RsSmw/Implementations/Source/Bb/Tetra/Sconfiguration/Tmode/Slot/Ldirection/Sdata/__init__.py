from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sdata:
	"""Sdata commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdata", core, parent)

	@property
	def sdPattern(self):
		"""sdPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdPattern'):
			from .SdPattern import SdPattern
			self._sdPattern = SdPattern(self._core, self._cmd_group)
		return self._sdPattern

	@property
	def sdSelection(self):
		"""sdSelection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdSelection'):
			from .SdSelection import SdSelection
			self._sdSelection = SdSelection(self._core, self._cmd_group)
		return self._sdSelection

	def set(self, sdata: enums.DataSourceB, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:SDATa \n
		Snippet: driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.sdata.set(sdata = enums.DataSourceB.ALL0, testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Defines the data source for the DATA fields in the burst. \n
			:param sdata: PATTern| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| ALL0| ALL1| PN09 ALL0|ALL1| Internal 0 or 1 data is used. PATT Internal data is used. The bit pattern for the data is defined with the aid of command [:SOURcehw]:BB:TETRa:SCONfiguration:TMODedi:SLOTst:LDIRectionch:SDATa:SDPattern. PNxx The pseudo-random sequence generator is used as the data source. There is a choice of different lengths of random sequence. DLISt A data list is used. The data list is selected with the aid of command [:SOURcehw]:BB:TETRa:SCONfiguration:TMODedi:SLOTst:LDIRectionch:SDATa:SDSelection.
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
		"""
		param = Conversions.enum_scalar_to_str(sdata, enums.DataSourceB)
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:SDATa {param}')

	# noinspection PyTypeChecker
	def get(self, testMode=repcap.TestMode.Default, slot=repcap.Slot.Default, channel=repcap.Channel.Default) -> enums.DataSourceB:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:TMODe<DI>:SLOT<ST>:LDIRection<CH>:SDATa \n
		Snippet: value: enums.DataSourceB = driver.source.bb.tetra.sconfiguration.tmode.slot.ldirection.sdata.get(testMode = repcap.TestMode.Default, slot = repcap.Slot.Default, channel = repcap.Channel.Default) \n
		Defines the data source for the DATA fields in the burst. \n
			:param testMode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tmode')
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ldirection')
			:return: sdata: PATTern| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| ALL0| ALL1| PN09 ALL0|ALL1| Internal 0 or 1 data is used. PATT Internal data is used. The bit pattern for the data is defined with the aid of command [:SOURcehw]:BB:TETRa:SCONfiguration:TMODedi:SLOTst:LDIRectionch:SDATa:SDPattern. PNxx The pseudo-random sequence generator is used as the data source. There is a choice of different lengths of random sequence. DLISt A data list is used. The data list is selected with the aid of command [:SOURcehw]:BB:TETRa:SCONfiguration:TMODedi:SLOTst:LDIRectionch:SDATa:SDSelection."""
		testMode_cmd_val = self._cmd_group.get_repcap_cmd_value(testMode, repcap.TestMode)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:TMODe{testMode_cmd_val}:SLOT{slot_cmd_val}:LDIRection{channel_cmd_val}:SDATa?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceB)

	def clone(self) -> 'Sdata':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sdata(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
