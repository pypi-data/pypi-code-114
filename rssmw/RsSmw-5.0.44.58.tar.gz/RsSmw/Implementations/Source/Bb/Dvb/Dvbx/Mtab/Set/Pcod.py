from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcod:
	"""Pcod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcod", core, parent)

	def get(self, modCodSet=repcap.ModCodSet.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MTAB:SET<ST>:PCOD \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.mtab.set.pcod.get(modCodSet = repcap.ModCodSet.Default) \n
		Queries the PLS code. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: pls_code: integer Range: 0 to 1000"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBX:MTAB:SET{modCodSet_cmd_val}:PCOD?')
		return Conversions.str_to_int(response)
