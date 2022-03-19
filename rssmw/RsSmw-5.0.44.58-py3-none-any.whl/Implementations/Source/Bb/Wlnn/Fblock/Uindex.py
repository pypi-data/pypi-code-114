from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uindex:
	"""Uindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uindex", core, parent)

	def set(self, uind: enums.WlannFbUserIdx, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:UINDex \n
		Snippet: driver.source.bb.wlnn.fblock.uindex.set(uind = enums.WlannFbUserIdx.UIDX0, frameBlock = repcap.FrameBlock.Default) \n
		Defines the currently generated user. In activated Multi User MIMO only, one user can be generated at a time.
		This parameter selects the generated one out of four available users. \n
			:param uind: UIDX0| UIDX1| UIDX2| UIDX3
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(uind, enums.WlannFbUserIdx)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:UINDex {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbUserIdx:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:UINDex \n
		Snippet: value: enums.WlannFbUserIdx = driver.source.bb.wlnn.fblock.uindex.get(frameBlock = repcap.FrameBlock.Default) \n
		Defines the currently generated user. In activated Multi User MIMO only, one user can be generated at a time.
		This parameter selects the generated one out of four available users. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: uind: UIDX0| UIDX1| UIDX2| UIDX3"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:UINDex?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbUserIdx)
