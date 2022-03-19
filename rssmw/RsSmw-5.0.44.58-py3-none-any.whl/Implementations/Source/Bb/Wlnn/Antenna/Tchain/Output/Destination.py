from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Destination:
	"""Destination commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("destination", core, parent)

	def set(self, destination: enums.WlannTxOutpDest, transmissionChain=repcap.TransmissionChain.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:OUTPut:DESTination \n
		Snippet: driver.source.bb.wlnn.antenna.tchain.output.destination.set(destination = enums.WlannTxOutpDest.BB, transmissionChain = repcap.TransmissionChain.Default) \n
		Selects the destination of the calculated IQ chains. \n
			:param destination: OFF| BB| BB_B| FILE OFF No mapping takes place. BB The IQ chain is output to the baseband A. Exactly one output stream can be mapped as 'Baseband A'. BB_B The IQ chain is output to the baseband B. Exactly one output stream can be mapped as 'Baseband B'. FILE The IQ chain is saved in a file.
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.WlannTxOutpDest)
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:OUTPut:DESTination {param}')

	# noinspection PyTypeChecker
	def get(self, transmissionChain=repcap.TransmissionChain.Default) -> enums.WlannTxOutpDest:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:TCHain<CH>:OUTPut:DESTination \n
		Snippet: value: enums.WlannTxOutpDest = driver.source.bb.wlnn.antenna.tchain.output.destination.get(transmissionChain = repcap.TransmissionChain.Default) \n
		Selects the destination of the calculated IQ chains. \n
			:param transmissionChain: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tchain')
			:return: destination: OFF| BB| BB_B| FILE OFF No mapping takes place. BB The IQ chain is output to the baseband A. Exactly one output stream can be mapped as 'Baseband A'. BB_B The IQ chain is output to the baseband B. Exactly one output stream can be mapped as 'Baseband B'. FILE The IQ chain is saved in a file."""
		transmissionChain_cmd_val = self._cmd_group.get_repcap_cmd_value(transmissionChain, repcap.TransmissionChain)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:ANTenna:TCHain{transmissionChain_cmd_val}:OUTPut:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.WlannTxOutpDest)
