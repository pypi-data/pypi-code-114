from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, generatorIx=repcap.GeneratorIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:PM<CH>:STATe \n
		Snippet: driver.source.pm.state.set(state = False, generatorIx = repcap.GeneratorIx.Default) \n
		Activates phase modulation. Activation of phase modulation deactivates frequency modulation. \n
			:param state: 1| ON| 0| OFF
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pm')
		"""
		param = Conversions.bool_to_str(state)
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		self._core.io.write(f'SOURce<HwInstance>:PM{generatorIx_cmd_val}:STATe {param}')

	def get(self, generatorIx=repcap.GeneratorIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:PM<CH>:STATe \n
		Snippet: value: bool = driver.source.pm.state.get(generatorIx = repcap.GeneratorIx.Default) \n
		Activates phase modulation. Activation of phase modulation deactivates frequency modulation. \n
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pm')
			:return: state: 1| ON| 0| OFF"""
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:PM{generatorIx_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
