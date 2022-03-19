from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmode:
	"""Pmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmode", core, parent)

	def set(self, pmode: enums.WlannFbPhyMode, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PMODe \n
		Snippet: driver.source.bb.wlnn.fblock.pmode.set(pmode = enums.WlannFbPhyMode.GFIeld, frameBlock = repcap.FrameBlock.Default) \n
		Selects the preamble design. For physical type SOUNDING, only GREEN FIELD is available. \n
			:param pmode: LEGacy| MIXed| GFIeld LEGacy Compatible with 802.11 a/g OFDM devices. MIXed For High Throughput (HT) and 802.11a/g OFDM devices. GFIeld For HT only networks.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(pmode, enums.WlannFbPhyMode)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PMODe {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbPhyMode:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PMODe \n
		Snippet: value: enums.WlannFbPhyMode = driver.source.bb.wlnn.fblock.pmode.get(frameBlock = repcap.FrameBlock.Default) \n
		Selects the preamble design. For physical type SOUNDING, only GREEN FIELD is available. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: pmode: LEGacy| MIXed| GFIeld LEGacy Compatible with 802.11 a/g OFDM devices. MIXed For High Throughput (HT) and 802.11a/g OFDM devices. GFIeld For HT only networks."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPhyMode)
