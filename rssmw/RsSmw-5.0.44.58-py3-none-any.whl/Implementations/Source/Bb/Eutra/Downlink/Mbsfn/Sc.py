from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sc:
	"""Sc commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sc", core, parent)

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.EutraMbsfnSfAllMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:AMODe \n
		Snippet: value: enums.EutraMbsfnSfAllMode = driver.source.bb.eutra.downlink.mbsfn.sc.get_amode() \n
		Defines whether MBSFN periodic scheduling is 1 or 4 frames. \n
			:return: allocation_mode: F1| F4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMbsfnSfAllMode)

	def set_amode(self, allocation_mode: enums.EutraMbsfnSfAllMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:AMODe \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.sc.set_amode(allocation_mode = enums.EutraMbsfnSfAllMode.F1) \n
		Defines whether MBSFN periodic scheduling is 1 or 4 frames. \n
			:param allocation_mode: F1| F4
		"""
		param = Conversions.enum_scalar_to_str(allocation_mode, enums.EutraMbsfnSfAllMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:AMODe {param}')

	def get_aoffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:AOFFset \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.sc.get_aoffset() \n
		Sets the Radio Frame Allocation Offset \n
			:return: offset: integer Range: 0 to 31
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:AOFFset?')
		return Conversions.str_to_int(response)

	def set_aoffset(self, offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:AOFFset \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.sc.set_aoffset(offset = 1) \n
		Sets the Radio Frame Allocation Offset \n
			:param offset: integer Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:AOFFset {param}')

	# noinspection PyTypeChecker
	def get_aper(self) -> enums.EutraMbsfnRfAllPer:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:APER \n
		Snippet: value: enums.EutraMbsfnRfAllPer = driver.source.bb.eutra.downlink.mbsfn.sc.get_aper() \n
		Sets the Radio Frame Allocation Period. \n
			:return: alloc_period: AP1| AP2| AP4| AP8| AP16| AP32
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:APER?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMbsfnRfAllPer)

	def set_aper(self, alloc_period: enums.EutraMbsfnRfAllPer) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:APER \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.sc.set_aper(alloc_period = enums.EutraMbsfnRfAllPer.AP1) \n
		Sets the Radio Frame Allocation Period. \n
			:param alloc_period: AP1| AP2| AP4| AP8| AP16| AP32
		"""
		param = Conversions.enum_scalar_to_str(alloc_period, enums.EutraMbsfnRfAllPer)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:APER {param}')

	def get_aval(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:AVAL \n
		Snippet: value: int = driver.source.bb.eutra.downlink.mbsfn.sc.get_aval() \n
		Defines which MBSFN subframes are allocated. \n
			:return: allocation_value: integer Range: 0 to #HFFFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:AVAL?')
		return Conversions.str_to_int(response)

	def set_aval(self, allocation_value: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:SC:AVAL \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.sc.set_aval(allocation_value = 1) \n
		Defines which MBSFN subframes are allocated. \n
			:param allocation_value: integer Range: 0 to #HFFFFFF
		"""
		param = Conversions.decimal_value_to_str(allocation_value)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:SC:AVAL {param}')
