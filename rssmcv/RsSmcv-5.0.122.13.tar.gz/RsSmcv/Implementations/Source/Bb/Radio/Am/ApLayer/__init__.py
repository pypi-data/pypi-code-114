from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApLayer:
	"""ApLayer commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

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

	def get_att(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:APLayer:ATT \n
		Snippet: value: float = driver.source.bb.radio.am.apLayer.get_att() \n
		Sets the attenuation. \n
			:return: attenuation: float Range: 0 to 30
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:APLayer:ATT?')
		return Conversions.str_to_float(response)

	def set_att(self, attenuation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:APLayer:ATT \n
		Snippet: driver.source.bb.radio.am.apLayer.set_att(attenuation = 1.0) \n
		Sets the attenuation. \n
			:param attenuation: float Range: 0 to 30
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:APLayer:ATT {param}')

	def clone(self) -> 'ApLayer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApLayer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
