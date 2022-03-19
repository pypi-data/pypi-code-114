from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.CckFormat, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PLCP:FORMat \n
		Snippet: driver.source.bb.wlnn.fblock.plcp.formatPy.set(format_py = enums.CckFormat.LONG, frameBlock = repcap.FrameBlock.Default) \n
		(available only for CCK and PBCC transport modes) Selects the packet type (PPDU format) with long or short PLCP (physical
		layer convergence protocol) . Depending on the format selected, the structure, modulation and data rate of the PLCP
		preamble and header are modified. \n
			:param format_py: LONG| SHORt
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.CckFormat)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PLCP:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.CckFormat:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PLCP:FORMat \n
		Snippet: value: enums.CckFormat = driver.source.bb.wlnn.fblock.plcp.formatPy.get(frameBlock = repcap.FrameBlock.Default) \n
		(available only for CCK and PBCC transport modes) Selects the packet type (PPDU format) with long or short PLCP (physical
		layer convergence protocol) . Depending on the format selected, the structure, modulation and data rate of the PLCP
		preamble and header are modified. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: format_py: LONG| SHORt"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PLCP:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CckFormat)
