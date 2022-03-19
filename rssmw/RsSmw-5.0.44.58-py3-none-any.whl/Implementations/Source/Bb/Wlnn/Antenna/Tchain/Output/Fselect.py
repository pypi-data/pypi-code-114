from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fselect:
	"""Fselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fselect", core, parent)

	def set(self, fselect: str, transmissionChain=repcap.TransmissionChain.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:OUTPut:FSELect \n
		Snippet: driver.source.bb.wlnn.antenna.tchain.output.fselect.set(fselect = '1', transmissionChain = repcap.TransmissionChain.Default) \n
		The command saves the IQ chain in a file. \n
			:param fselect: string
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
		"""
		param = Conversions.value_to_quoted_str(fselect)
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:OUTPut:FSELect {param}')

	def get(self, transmissionChain=repcap.TransmissionChain.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:OUTPut:FSELect \n
		Snippet: value: str = driver.source.bb.wlnn.antenna.tchain.output.fselect.get(transmissionChain = repcap.TransmissionChain.Default) \n
		The command saves the IQ chain in a file. \n
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
			:return: fselect: string"""
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:OUTPut:FSELect?')
		return trim_str_response(response)
