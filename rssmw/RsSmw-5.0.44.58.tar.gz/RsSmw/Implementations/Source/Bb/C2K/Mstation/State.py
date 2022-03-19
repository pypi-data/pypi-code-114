from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:STATe \n
		Snippet: driver.source.bb.c2K.mstation.state.set(state = False, mobileStation = repcap.MobileStation.Default) \n
		The command activates and deactivates the specified mobile station. \n
			:param state: 1| ON| 0| OFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(state)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:STATe {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:STATe \n
		Snippet: value: bool = driver.source.bb.c2K.mstation.state.get(mobileStation = repcap.MobileStation.Default) \n
		The command activates and deactivates the specified mobile station. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: state: 1| ON| 0| OFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
