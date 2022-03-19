from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EcpState:
	"""EcpState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ecpState", core, parent)

	def set(self, scs_ecp_state: bool, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:ECPState \n
		Snippet: driver.source.bb.nr5G.trigger.output.ecpState.set(scs_ecp_state = False, output = repcap.Output.Default) \n
		Enables/disables the extended cyclic prefix (ECP) for a UL/DL pattern containing a marker. \n
			:param scs_ecp_state: 1| ON| 0| OFF 0|OFF Disables the ECP. 1|ON Enables the ECP.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(scs_ecp_state)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:ECPState {param}')

	def get(self, output=repcap.Output.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:ECPState \n
		Snippet: value: bool = driver.source.bb.nr5G.trigger.output.ecpState.get(output = repcap.Output.Default) \n
		Enables/disables the extended cyclic prefix (ECP) for a UL/DL pattern containing a marker. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: scs_ecp_state: 1| ON| 0| OFF 0|OFF Disables the ECP. 1|ON Enables the ECP."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:ECPState?')
		return Conversions.str_to_bool(response)
