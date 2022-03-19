from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Real:
	"""Real commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("real", core, parent)

	def set(self, real: float, transmissionChain=repcap.TransmissionChain.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:TX<DIR>:REAL \n
		Snippet: driver.source.bb.wlnn.antenna.tchain.tx.real.set(real = 1.0, transmissionChain = repcap.TransmissionChain.Default, index = repcap.Index.Default) \n
		Sets the value for the Real coordinate. \n
			:param real: float Range: -1000 to 1000
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tx')
		"""
		param = Conversions.decimal_value_to_str(real)
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:TX{index_cmd_val}:REAL {param}')

	def get(self, transmissionChain=repcap.TransmissionChain.Default, index=repcap.Index.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:TX<DIR>:REAL \n
		Snippet: value: float = driver.source.bb.wlnn.antenna.tchain.tx.real.get(transmissionChain = repcap.TransmissionChain.Default, index = repcap.Index.Default) \n
		Sets the value for the Real coordinate. \n
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tx')
			:return: real: float Range: -1000 to 1000"""
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:TX{index_cmd_val}:REAL?')
		return Conversions.str_to_float(response)
