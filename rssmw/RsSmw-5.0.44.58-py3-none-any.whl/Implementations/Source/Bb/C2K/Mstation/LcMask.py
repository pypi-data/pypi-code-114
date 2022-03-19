from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LcMask:
	"""LcMask commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcMask", core, parent)

	def set(self, lc_mask: List[str], mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:LCMask \n
		Snippet: driver.source.bb.c2K.mstation.lcMask.set(lc_mask = ['raw1', 'raw2', 'raw3'], mobileStation = repcap.MobileStation.Default) \n
		Sets the mask of the Long Code Generator of the mobile station. \n
			:param lc_mask: 42 bits
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.list_to_csv_str(lc_mask)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:LCMask {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:LCMask \n
		Snippet: value: List[str] = driver.source.bb.c2K.mstation.lcMask.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the mask of the Long Code Generator of the mobile station. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: lc_mask: 42 bits"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:LCMask?')
		return Conversions.str_to_str_list(response)
