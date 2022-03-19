from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CpnSequence:
	"""CpnSequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cpnSequence", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:CPNSequence:STATe \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.cpnSequence.get_state() \n
		Activates transmission of the complete sequence of pseudo-random noise bits within the baseband frame. \n
			:return: complete_pn_seq: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:CPNSequence:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, complete_pn_seq: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:CPNSequence:STATe \n
		Snippet: driver.source.bb.dvb.dvbx.cpnSequence.set_state(complete_pn_seq = False) \n
		Activates transmission of the complete sequence of pseudo-random noise bits within the baseband frame. \n
			:param complete_pn_seq: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(complete_pn_seq)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:CPNSequence:STATe {param}')
