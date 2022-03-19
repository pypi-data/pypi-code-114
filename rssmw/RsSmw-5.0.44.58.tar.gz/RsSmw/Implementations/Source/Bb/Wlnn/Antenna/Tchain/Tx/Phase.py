from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase: float, transmissionChain=repcap.TransmissionChain.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:TX<DIR>:PHASe \n
		Snippet: driver.source.bb.wlnn.antenna.tchain.tx.phase.set(phase = 1.0, transmissionChain = repcap.TransmissionChain.Default, index = repcap.Index.Default) \n
		Sets the phase when cylindrical mapping coordinates are selected. \n
			:param phase: float Range: 0 to 359.99
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tx')
		"""
		param = Conversions.decimal_value_to_str(phase)
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:TX{index_cmd_val}:PHASe {param}')

	def get(self, transmissionChain=repcap.TransmissionChain.Default, index=repcap.Index.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:TX<DIR>:PHASe \n
		Snippet: value: float = driver.source.bb.wlnn.antenna.tchain.tx.phase.get(transmissionChain = repcap.TransmissionChain.Default, index = repcap.Index.Default) \n
		Sets the phase when cylindrical mapping coordinates are selected. \n
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tx')
			:return: phase: float Range: 0 to 359.99"""
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:TX{index_cmd_val}:PHASe?')
		return Conversions.str_to_float(response)
