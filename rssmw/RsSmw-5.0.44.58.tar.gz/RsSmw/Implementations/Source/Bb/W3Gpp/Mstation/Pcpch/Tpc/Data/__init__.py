from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def dselect(self):
		"""dselect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dselect'):
			from .Dselect import Dselect
			self._dselect = Dselect(self._core, self._cmd_group)
		return self._dselect

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def set(self, data: enums.TpcDataSour, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:TPC:DATA \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.tpc.data.set(data = enums.TpcDataSour.DLISt, mobileStation = repcap.MobileStation.Default) \n
		The command determines the data source for the TPC field of the PCPCH. \n
			:param data: ZERO| ONE| PATTern| DLISt DLISt A data list is used. The data list is selected with the command [:SOURcehw]:BB:W3GPp:MSTationst:PCPCh:TPC:DATA:DSELect. ZERO | ONE Internal 0 and 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined by the command [:SOURcehw]:BB:W3GPp:MSTationst:PCPCh:TPC:DATA:PATTern. The maximum length is 64 bits.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.TpcDataSour)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:TPC:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.TpcDataSour:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:TPC:DATA \n
		Snippet: value: enums.TpcDataSour = driver.source.bb.w3Gpp.mstation.pcpch.tpc.data.get(mobileStation = repcap.MobileStation.Default) \n
		The command determines the data source for the TPC field of the PCPCH. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: data: ZERO| ONE| PATTern| DLISt DLISt A data list is used. The data list is selected with the command [:SOURcehw]:BB:W3GPp:MSTationst:PCPCh:TPC:DATA:DSELect. ZERO | ONE Internal 0 and 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined by the command [:SOURcehw]:BB:W3GPp:MSTationst:PCPCh:TPC:DATA:PATTern. The maximum length is 64 bits."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:TPC:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.TpcDataSour)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
