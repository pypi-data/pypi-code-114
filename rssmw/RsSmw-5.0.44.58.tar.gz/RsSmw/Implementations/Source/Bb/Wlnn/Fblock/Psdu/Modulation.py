from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.ModulationF:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PSDU:MODulation \n
		Snippet: value: enums.ModulationF = driver.source.bb.wlnn.fblock.psdu.modulation.get(frameBlock = repcap.FrameBlock.Default) \n
		(available only for CCK and PBCC Tx modes) Queries the modulation type. The modulation mode depends on the selected PSDU
		bit rate which depends on the selected physical layer mode (SOUR:BB:WLNN:MODE) . \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: modulation: BPSK| QPSK| DBPSK| DQPSK| CCK| PBCC"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PSDU:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationF)
