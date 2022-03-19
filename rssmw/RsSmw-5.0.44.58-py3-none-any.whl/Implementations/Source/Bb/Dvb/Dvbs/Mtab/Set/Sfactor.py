from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfactor:
	"""Sfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfactor", core, parent)

	def get(self, modCodSet=repcap.ModCodSet.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:SFACtor \n
		Snippet: value: float = driver.source.bb.dvb.dvbs.mtab.set.sfactor.get(modCodSet = repcap.ModCodSet.Default) \n
		Queries the spreading factor. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: sfactor: float Range: 1 to 2"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:SFACtor?')
		return Conversions.str_to_float(response)
