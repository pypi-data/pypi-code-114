from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pformat:
	"""Pformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pformat", core, parent)

	def set(self, ppdu_format: enums.WlannFbPpduFormat, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PFORmat \n
		Snippet: driver.source.bb.wlnn.fblock.pformat.set(ppdu_format = enums.WlannFbPpduFormat.MU, frameBlock = repcap.FrameBlock.Default) \n
		Sets the PPDU format. \n
			:param ppdu_format: SU| MU| SUEXt| TRIG SU HE SU (single-user) carries a single PSDU. The HE Signal A (HE-SIG-A) field is not repeated. MU HE MU (multi-user) carries multiple PSDUs to one or more users. SUEXt Carries a single PSDU. The HE-SIG-A field is repeated. TRIG Carries a single PSDU. It is send as a response to a PPDU that contains a trigger frame.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(ppdu_format, enums.WlannFbPpduFormat)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PFORmat {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbPpduFormat:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PFORmat \n
		Snippet: value: enums.WlannFbPpduFormat = driver.source.bb.wlnn.fblock.pformat.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the PPDU format. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: ppdu_format: SU| MU| SUEXt| TRIG SU HE SU (single-user) carries a single PSDU. The HE Signal A (HE-SIG-A) field is not repeated. MU HE MU (multi-user) carries multiple PSDUs to one or more users. SUEXt Carries a single PSDU. The HE-SIG-A field is repeated. TRIG Carries a single PSDU. It is send as a response to a PPDU that contains a trigger frame."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduFormat)
