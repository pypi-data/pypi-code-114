from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnOffset:
	"""PnOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnOffset", core, parent)

	def set(self, pn_offset: int, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PNOFfset \n
		Snippet: driver.source.bb.c2K.bstation.pnOffset.set(pn_offset = 1, baseStation = repcap.BaseStation.Default) \n
		The command sets the PN offset (short code) of the base station. The PN offset permits signals of different base stations
		to be distinguished. \n
			:param pn_offset: integer Range: 0 to 511
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.decimal_value_to_str(pn_offset)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PNOFfset {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PNOFfset \n
		Snippet: value: int = driver.source.bb.c2K.bstation.pnOffset.get(baseStation = repcap.BaseStation.Default) \n
		The command sets the PN offset (short code) of the base station. The PN offset permits signals of different base stations
		to be distinguished. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: pn_offset: integer Range: 0 to 511"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PNOFfset?')
		return Conversions.str_to_int(response)
