from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Powc:
	"""Powc commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powc", core, parent)

	# noinspection PyTypeChecker
	def get_lev_reference(self) -> enums.PowcLevRef:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:POWC:LEVReference \n
		Snippet: value: enums.PowcLevRef = driver.source.bb.oneweb.powc.get_lev_reference() \n
		No command help available \n
			:return: level_reference: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:POWC:LEVReference?')
		return Conversions.str_to_scalar_enum(response, enums.PowcLevRef)

	def set_lev_reference(self, level_reference: enums.PowcLevRef) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:POWC:LEVReference \n
		Snippet: driver.source.bb.oneweb.powc.set_lev_reference(level_reference = enums.PowcLevRef.DRMS) \n
		No command help available \n
			:param level_reference: No help available
		"""
		param = Conversions.enum_scalar_to_str(level_reference, enums.PowcLevRef)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:POWC:LEVReference {param}')

	# noinspection PyTypeChecker
	def get_ref_channel(self) -> enums.PowcRefChan:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:POWC:REFChannel \n
		Snippet: value: enums.PowcRefChan = driver.source.bb.oneweb.powc.get_ref_channel() \n
		No command help available \n
			:return: ref_channel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:POWC:REFChannel?')
		return Conversions.str_to_scalar_enum(response, enums.PowcRefChan)

	def set_ref_channel(self, ref_channel: enums.PowcRefChan) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:POWC:REFChannel \n
		Snippet: driver.source.bb.oneweb.powc.set_ref_channel(ref_channel = enums.PowcRefChan.NF) \n
		No command help available \n
			:param ref_channel: No help available
		"""
		param = Conversions.enum_scalar_to_str(ref_channel, enums.PowcRefChan)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:POWC:REFChannel {param}')

	def get_ref_subframe(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:POWC:REFSubframe \n
		Snippet: value: int = driver.source.bb.oneweb.powc.get_ref_subframe() \n
		No command help available \n
			:return: ref_subframe: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:POWC:REFSubframe?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_rue(self) -> enums.MobStatType:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:POWC:RUE \n
		Snippet: value: enums.MobStatType = driver.source.bb.oneweb.powc.get_rue() \n
		No command help available \n
			:return: reference_ue: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:POWC:RUE?')
		return Conversions.str_to_scalar_enum(response, enums.MobStatType)
