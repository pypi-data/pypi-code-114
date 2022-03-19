from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.WlannFbScrMode, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:SCRambler:MODE \n
		Snippet: driver.source.bb.wlnn.fblock.user.scrambler.mode.set(mode = enums.WlannFbScrMode.OFF, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		The command selects the different options for the scrambler. \n
			:param mode: OFF| RANDom| USER| ON| PREamble OFF The scrambler is deactivated. RANDom (not for CCK/PBCC) The scrambler is activated. The initialization value of the scrambler is selected at random. Each frame has a different random initialization value. This value is also different in case of successive recalculations with the same setting parameters so that different signals are generated for each calculation. USER (not for CCK/PBCC) The scrambler is activated. The initialization value of the scrambler is set to a fixed value that is set using the command BB:WLNN:FBL5:SCR:PATT. This value is then identical in each generated frame. ON (CCK/PBCC only) The scrambler is activated. PREamble (CCK/PBCC only) The scrambler is activated. Only the preamble is scrambled.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.WlannFbScrMode)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:SCRambler:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> enums.WlannFbScrMode:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:SCRambler:MODE \n
		Snippet: value: enums.WlannFbScrMode = driver.source.bb.wlnn.fblock.user.scrambler.mode.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		The command selects the different options for the scrambler. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: mode: OFF| RANDom| USER| ON| PREamble OFF The scrambler is deactivated. RANDom (not for CCK/PBCC) The scrambler is activated. The initialization value of the scrambler is selected at random. Each frame has a different random initialization value. This value is also different in case of successive recalculations with the same setting parameters so that different signals are generated for each calculation. USER (not for CCK/PBCC) The scrambler is activated. The initialization value of the scrambler is set to a fixed value that is set using the command BB:WLNN:FBL5:SCR:PATT. This value is then identical in each generated frame. ON (CCK/PBCC only) The scrambler is activated. PREamble (CCK/PBCC only) The scrambler is activated. Only the preamble is scrambled."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:SCRambler:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbScrMode)
