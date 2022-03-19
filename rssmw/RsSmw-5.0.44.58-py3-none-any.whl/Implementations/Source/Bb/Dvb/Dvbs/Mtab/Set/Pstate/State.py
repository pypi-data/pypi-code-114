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

	def set(self, pstate: bool, modCodSet=repcap.ModCodSet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:PSTate:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.mtab.set.pstate.state.set(pstate = False, modCodSet = repcap.ModCodSet.Default) \n
		Activates the pilot. \n
			:param pstate: 1| ON| 0| OFF
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.bool_to_str(pstate)
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:PSTate:STATe {param}')

	def get(self, modCodSet=repcap.ModCodSet.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:PSTate:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.mtab.set.pstate.state.get(modCodSet = repcap.ModCodSet.Default) \n
		Activates the pilot. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: pstate: 1| ON| 0| OFF"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:PSTate:STATe?')
		return Conversions.str_to_bool(response)
