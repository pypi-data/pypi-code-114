from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Siso:
	"""Siso commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("siso", core, parent)

	def set(self, sisp_pilot_pat: enums.Atsc30PilotPatternSiso, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:PILot:SISO \n
		Snippet: driver.source.bb.a3Tsc.subframe.pilot.siso.set(sisp_pilot_pat = enums.Atsc30PilotPatternSiso.SP12_2, subframe = repcap.Subframe.Default) \n
		Sets the scattered pilot pattern for single input and single output (SISO) . \n
			:param sisp_pilot_pat: SP32_4| SP32_2| SP24_4| SP16_4| SP3_2| SP3_4| SP4_2| SP4_4| SP6_2| SP6_4| SP8_2| SP8_4| SP12_2| SP12_4| SP16_2| SP24_2 | SP3_2| SP3_4| SP4_2| SP4_4| SP6_2| SP6_4| SP8_2| SP8_4| SP12_2| SP12_4| SP16_2| SP16_4| SP24_2| SP24_4| SP32_2| SP32_4
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(sisp_pilot_pat, enums.Atsc30PilotPatternSiso)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:PILot:SISO {param}')

	# noinspection PyTypeChecker
	def get(self, subframe=repcap.Subframe.Default) -> enums.Atsc30PilotPatternSiso:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:PILot:SISO \n
		Snippet: value: enums.Atsc30PilotPatternSiso = driver.source.bb.a3Tsc.subframe.pilot.siso.get(subframe = repcap.Subframe.Default) \n
		Sets the scattered pilot pattern for single input and single output (SISO) . \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: sisp_pilot_pat: SP32_4| SP32_2| SP24_4| SP16_4| SP3_2| SP3_4| SP4_2| SP4_4| SP6_2| SP6_4| SP8_2| SP8_4| SP12_2| SP12_4| SP16_2| SP24_2 | SP3_2| SP3_4| SP4_2| SP4_4| SP6_2| SP6_4| SP8_2| SP8_4| SP12_2| SP12_4| SP16_2| SP16_4| SP24_2| SP24_4| SP32_2| SP32_4"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:PILot:SISO?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30PilotPatternSiso)
