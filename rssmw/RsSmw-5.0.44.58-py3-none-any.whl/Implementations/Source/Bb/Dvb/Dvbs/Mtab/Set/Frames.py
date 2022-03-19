from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frames:
	"""Frames commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frames", core, parent)

	def set(self, frames: int, modCodSet=repcap.ModCodSet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:FRAMes \n
		Snippet: driver.source.bb.dvb.dvbs.mtab.set.frames.set(frames = 1, modCodSet = repcap.ModCodSet.Default) \n
		Sets the number of the transmitted frames. \n
			:param frames: integer Range: 1 to max
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.decimal_value_to_str(frames)
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:FRAMes {param}')

	def get(self, modCodSet=repcap.ModCodSet.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:FRAMes \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.mtab.set.frames.get(modCodSet = repcap.ModCodSet.Default) \n
		Sets the number of the transmitted frames. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: frames: integer Range: 1 to max"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:FRAMes?')
		return Conversions.str_to_int(response)
