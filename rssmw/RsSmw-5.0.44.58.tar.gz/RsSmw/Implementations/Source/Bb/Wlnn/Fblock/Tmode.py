from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmode:
	"""Tmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmode", core, parent)

	def set(self, tmode: enums.WlannFbTxMode, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:TMODe \n
		Snippet: driver.source.bb.wlnn.fblock.tmode.set(tmode = enums.WlannFbTxMode.CCK, frameBlock = repcap.FrameBlock.Default) \n
		Sets the Tx mode. The available Tx modes are dependent on the physical mode. \n
			:param tmode: L20| LDUP| LUP| LLOW| HT20| HT40| HTDup| HTUP| HTLow| CCK| PBCC| V20| V40| V80| V160| V8080| L10| S1| S2| S4| S16| HE20| HE40| HE80| HE8080| HE160| EHT320| EHT20| EHT40| EHT80| EHT160| EHT320
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(tmode, enums.WlannFbTxMode)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:TMODe {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbTxMode:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:TMODe \n
		Snippet: value: enums.WlannFbTxMode = driver.source.bb.wlnn.fblock.tmode.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the Tx mode. The available Tx modes are dependent on the physical mode. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: tmode: L20| LDUP| LUP| LLOW| HT20| HT40| HTDup| HTUP| HTLow| CCK| PBCC| V20| V40| V80| V160| V8080| L10| S1| S2| S4| S16| HE20| HE40| HE80| HE8080| HE160| EHT320| EHT20| EHT40| EHT80| EHT160| EHT320"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbTxMode)
