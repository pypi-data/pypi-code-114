from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def get_pre(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:GAIN:PRE \n
		Snippet: value: float = driver.source.iq.dpd.gain.get_pre() \n
		Sets a pre-gain (i.e. an attenuation) to define the range the static DPD is applied in. \n
			:return: pre_gain: float Range: -50 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:GAIN:PRE?')
		return Conversions.str_to_float(response)

	def set_pre(self, pre_gain: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:GAIN:PRE \n
		Snippet: driver.source.iq.dpd.gain.set_pre(pre_gain = 1.0) \n
		Sets a pre-gain (i.e. an attenuation) to define the range the static DPD is applied in. \n
			:param pre_gain: float Range: -50 to 20
		"""
		param = Conversions.decimal_value_to_str(pre_gain)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:GAIN:PRE {param}')
