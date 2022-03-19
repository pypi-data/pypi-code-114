from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dfl:
	"""Dfl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfl", core, parent)

	def set(self, df_length: float, modCodSet=repcap.ModCodSet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:DFL \n
		Snippet: driver.source.bb.dvb.dvbs.mtab.set.dfl.set(df_length = 1.0, modCodSet = repcap.ModCodSet.Default) \n
		Sets the data field length (DFL) . \n
			:param df_length: integer Range: 1 to 7264
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.decimal_value_to_str(df_length)
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:DFL {param}')

	def get(self, modCodSet=repcap.ModCodSet.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:MTAB:SET<ST>:DFL \n
		Snippet: value: float = driver.source.bb.dvb.dvbs.mtab.set.dfl.get(modCodSet = repcap.ModCodSet.Default) \n
		Sets the data field length (DFL) . \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: df_length: integer Range: 1 to 7264"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBS:MTAB:SET{modCodSet_cmd_val}:DFL?')
		return Conversions.str_to_float(response)
