from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymDuration:
	"""SymDuration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symDuration", core, parent)

	def set(self, he_ltf_sym_dur: enums.WlannFbPpduHeLtfSymbDuraion, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SYMDuration \n
		Snippet: driver.source.bb.wlnn.fblock.symDuration.set(he_ltf_sym_dur = enums.WlannFbPpduHeLtfSymbDuraion.SD128, frameBlock = repcap.FrameBlock.Default) \n
		Selects the duration of the HE long training field (LTF) .The symbol duration value does not include the guard interval. \n
			:param he_ltf_sym_dur: SD32| SD64| SD128
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(he_ltf_sym_dur, enums.WlannFbPpduHeLtfSymbDuraion)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SYMDuration {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbPpduHeLtfSymbDuraion:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SYMDuration \n
		Snippet: value: enums.WlannFbPpduHeLtfSymbDuraion = driver.source.bb.wlnn.fblock.symDuration.get(frameBlock = repcap.FrameBlock.Default) \n
		Selects the duration of the HE long training field (LTF) .The symbol duration value does not include the guard interval. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: he_ltf_sym_dur: SD32| SD64| SD128"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SYMDuration?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduHeLtfSymbDuraion)
