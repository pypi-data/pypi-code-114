from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.GsmBursType, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:TYPE \n
		Snippet: driver.source.bb.gsm.frame.slot.typePy.set(type_py = enums.GsmBursType.A16Qam, frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default) \n
		Selects the burst (slot) type. \n
			:param type_py: NORMal| HALF| EDGE| SYNC| FCORrection| DUMMy| ACCess| ADATa| AEDGe| N16Qam| N32Qam| A16Qam| A32Qam| HQPSk| H16Qam| H32Qam| HAQPsk| HA16Qam| HA32Qam| NAFF| NAFH| NAHH| AAQPsk N16Qam | N32Qam Normal 16QAM | Normal 32QAM HQPSk | H16Qam | H32Qam HSR QPSK | HSR 16QAM | HSR 32QAM NAFF | NAFH | NAHH Normal AQPSK Full rate - Full rate | Normal AQPSK Full rate - Half rate | Normal AQPSK Half rate - Half rate Axxxxx (All Data) The types All Data xxx are not defined in the standard.
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.GsmBursType)
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default) -> enums.GsmBursType:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:TYPE \n
		Snippet: value: enums.GsmBursType = driver.source.bb.gsm.frame.slot.typePy.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default) \n
		Selects the burst (slot) type. \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: type_py: NORMal| HALF| EDGE| SYNC| FCORrection| DUMMy| ACCess| ADATa| AEDGe| N16Qam| N32Qam| A16Qam| A32Qam| HQPSk| H16Qam| H32Qam| HAQPsk| HA16Qam| HA32Qam| NAFF| NAFH| NAHH| AAQPsk N16Qam | N32Qam Normal 16QAM | Normal 32QAM HQPSk | H16Qam | H32Qam HSR QPSK | HSR 16QAM | HSR 32QAM NAFF | NAFH | NAHH Normal AQPSK Full rate - Full rate | Normal AQPSK Full rate - Half rate | Normal AQPSK Half rate - Half rate Axxxxx (All Data) The types All Data xxx are not defined in the standard."""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.GsmBursType)
