from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def set(self, standard: enums.WlannFbStd, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:STANdard \n
		Snippet: driver.source.bb.wlnn.fblock.standard.set(standard = enums.WlannFbStd.USER, frameBlock = repcap.FrameBlock.Default) \n
		Sets the IEEE 802.11 WLAN standard. \n
			:param standard: USER| WAG| WBG| WPJ| WN| WAC| WAX| WBE USER Sets a user defined standard. WAG Sets the IEEE 802.11a/g standard. WBG Sets the IEEE 802.11b/g standard. WPJ Sets the IEEE 802.11p/j standard. WN Sets the IEEE 802.11n standard. WAC Sets the IEEE 802.11a/c standard. WAX Sets the IEEE 802.11ax standard. WBE Sets the IEEE 802.11be standard.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.WlannFbStd)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:STANdard {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbStd:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:STANdard \n
		Snippet: value: enums.WlannFbStd = driver.source.bb.wlnn.fblock.standard.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the IEEE 802.11 WLAN standard. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: standard: USER| WAG| WBG| WPJ| WN| WAC| WAX| WBE USER Sets a user defined standard. WAG Sets the IEEE 802.11a/g standard. WBG Sets the IEEE 802.11b/g standard. WPJ Sets the IEEE 802.11p/j standard. WN Sets the IEEE 802.11n standard. WAC Sets the IEEE 802.11a/c standard. WAX Sets the IEEE 802.11ax standard. WBE Sets the IEEE 802.11be standard."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbStd)
