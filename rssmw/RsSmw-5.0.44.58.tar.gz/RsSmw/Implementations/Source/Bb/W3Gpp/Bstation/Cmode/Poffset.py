from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, poffset: float, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:POFFset \n
		Snippet: driver.source.bb.w3Gpp.bstation.cmode.poffset.set(poffset = 1.0, baseStation = repcap.BaseStation.Default) \n
		The command sets the power offset for mode USER. \n
			:param poffset: float Range: 0 dB to 10 dB
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.decimal_value_to_str(poffset)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:POFFset {param}')

	def get(self, baseStation=repcap.BaseStation.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:POFFset \n
		Snippet: value: float = driver.source.bb.w3Gpp.bstation.cmode.poffset.get(baseStation = repcap.BaseStation.Default) \n
		The command sets the power offset for mode USER. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: poffset: float Range: 0 dB to 10 dB"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:POFFset?')
		return Conversions.str_to_float(response)
