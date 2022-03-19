from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pinterval:
	"""Pinterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pinterval", core, parent)

	def set(self, pinterval: float, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:PINTerval \n
		Snippet: driver.source.bb.c2K.bstation.pdChannel.pinterval.set(pinterval = 1.0, baseStation = repcap.BaseStation.Default) \n
		The command sets the interval between two data packets for F-PDCH. The range depends on the ARB settings sequence length
		(BB:C2K:SLENgth) . The values 80 ms, 40 ms, 20 ms, 10 ms and 5 ms can always be set, and the maximum value is 2000 ms.
		All intermediate values must satisfy the condition: Sequence Length * 80ms/2^n, where n is a whole number. \n
			:param pinterval: float Range: 5 ms to 2000 ms
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.decimal_value_to_str(pinterval)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:PINTerval {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:PINTerval \n
		Snippet: value: float = driver.source.bb.c2K.bstation.pdChannel.pinterval.get(baseStation = repcap.BaseStation.Default) \n
		The command sets the interval between two data packets for F-PDCH. The range depends on the ARB settings sequence length
		(BB:C2K:SLENgth) . The values 80 ms, 40 ms, 20 ms, 10 ms and 5 ms can always be set, and the maximum value is 2000 ms.
		All intermediate values must satisfy the condition: Sequence Length * 80ms/2^n, where n is a whole number. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: pinterval: float Range: 5 ms to 2000 ms"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:PINTerval?')
		return Conversions.str_to_float(response)
