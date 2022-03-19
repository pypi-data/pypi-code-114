from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, modCodSet=repcap.ModCodSet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:ADFL:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.mtab.set.adfl.state.set(state = False, modCodSet = repcap.ModCodSet.Default) \n
		Defines if the DFL is set automatically or manually. \n
			:param state: 1| ON| 0| OFF
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.bool_to_str(state)
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:ADFL:STATe {param}')

	def get(self, modCodSet=repcap.ModCodSet.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:ADFL:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.mtab.set.adfl.state.get(modCodSet = repcap.ModCodSet.Default) \n
		Defines if the DFL is set automatically or manually. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: state: 1| ON| 0| OFF"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:ADFL:STATe?')
		return Conversions.str_to_bool(response)
