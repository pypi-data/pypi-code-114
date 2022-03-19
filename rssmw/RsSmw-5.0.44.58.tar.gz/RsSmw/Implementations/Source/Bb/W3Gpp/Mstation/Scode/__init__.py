from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scode:
	"""Scode commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scode", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, scode: List[str], mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:SCODe \n
		Snippet: driver.source.bb.w3Gpp.mstation.scode.set(scode = ['raw1', 'raw2', 'raw3'], mobileStation = repcap.MobileStation.Default) \n
		The command sets the scrambling code. Long or short scrambling codes can be generated (command
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:SCODe:MODE) . \n
			:param scode: integer Range: #H0 to #HFFFFFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.list_to_csv_str(scode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:SCODe {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:SCODe \n
		Snippet: value: List[str] = driver.source.bb.w3Gpp.mstation.scode.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the scrambling code. Long or short scrambling codes can be generated (command
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:SCODe:MODE) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: scode: integer Range: #H0 to #HFFFFFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:SCODe?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Scode':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scode(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
