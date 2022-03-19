from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApLayer:
	"""ApLayer commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apLayer", core, parent)

	@property
	def library(self):
		"""library commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_library'):
			from .Library import Library
			self._library = Library(self._core, self._cmd_group)
		return self._library

	def get_att_1(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:APLayer:ATT1 \n
		Snippet: value: float = driver.source.bb.radio.fm.apLayer.get_att_1() \n
		Sets the attenuation. \n
			:return: attl: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:APLayer:ATT1?')
		return Conversions.str_to_float(response)

	def set_att_1(self, attl: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:APLayer:ATT1 \n
		Snippet: driver.source.bb.radio.fm.apLayer.set_att_1(attl = 1.0) \n
		Sets the attenuation. \n
			:param attl: float Range: 0 to 30, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(attl)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:APLayer:ATT1 {param}')

	def get_att_2(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:APLayer:ATT2 \n
		Snippet: value: float = driver.source.bb.radio.fm.apLayer.get_att_2() \n
		Sets the attenuation. \n
			:return: attr: float Range: 0 to 30, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:APLayer:ATT2?')
		return Conversions.str_to_float(response)

	def set_att_2(self, attr: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:APLayer:ATT2 \n
		Snippet: driver.source.bb.radio.fm.apLayer.set_att_2(attr = 1.0) \n
		Sets the attenuation. \n
			:param attr: float Range: 0 to 30, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(attr)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:APLayer:ATT2 {param}')

	def clone(self) -> 'ApLayer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApLayer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
