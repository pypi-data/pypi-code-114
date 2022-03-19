from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def get(self, noisePoint=repcap.NoisePoint.Default) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:LEVel<CH>:[ABSolute] \n
		Snippet: value: float = driver.source.noise.level.absolute.get(noisePoint = repcap.NoisePoint.Default) \n
		Queries the level of the noise signal in the system bandwidth within the enabled bandwidth limitation. \n
			:param noisePoint: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
			:return: absolute: float"""
		noisePoint_cmd_val = self._cmd_group.get_repcap_cmd_value(noisePoint, repcap.NoisePoint)
		response = self._core.io.query_str(f'SOURce<HwInstance>:NOISe:LEVel{noisePoint_cmd_val}:ABSolute?')
		return Conversions.str_to_float(response)
