from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bmp:
	"""Bmp commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bmp", core, parent)

	@property
	def valSubFrames(self):
		"""valSubFrames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_valSubFrames'):
			from .ValSubFrames import ValSubFrames
			self._valSubFrames = ValSubFrames(self._core, self._cmd_group)
		return self._valSubFrames

	# noinspection PyTypeChecker
	def get_conf(self) -> enums.EutraBitmap:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NPRS:BMP:CONF \n
		Snippet: value: enums.EutraBitmap = driver.source.bb.eutra.downlink.niot.nprs.bmp.get_conf() \n
		Sets if the NPRS subframe Part A configuration lasts 10 ms or 40 ms. \n
			:return: nprs_bmp: 10| 40
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NPRS:BMP:CONF?')
		return Conversions.str_to_scalar_enum(response, enums.EutraBitmap)

	def set_conf(self, nprs_bmp: enums.EutraBitmap) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NPRS:BMP:CONF \n
		Snippet: driver.source.bb.eutra.downlink.niot.nprs.bmp.set_conf(nprs_bmp = enums.EutraBitmap._10) \n
		Sets if the NPRS subframe Part A configuration lasts 10 ms or 40 ms. \n
			:param nprs_bmp: 10| 40
		"""
		param = Conversions.enum_scalar_to_str(nprs_bmp, enums.EutraBitmap)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NPRS:BMP:CONF {param}')

	def clone(self) -> 'Bmp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bmp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
