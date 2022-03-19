from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class View:
	"""View commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("view", core, parent)

	def get_bis(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:BIS \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.view.get_bis() \n
		No command help available \n
			:return: block_info: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:VIEW:BIS?')
		return Conversions.str_to_bool(response)

	def set_bis(self, block_info: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:BIS \n
		Snippet: driver.source.bb.eutra.downlink.view.set_bis(block_info = False) \n
		No command help available \n
			:param block_info: No help available
		"""
		param = Conversions.bool_to_str(block_info)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:VIEW:BIS {param}')

	# noinspection PyTypeChecker
	def get_cindex(self) -> enums.CcIndex:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:CINDex \n
		Snippet: value: enums.CcIndex = driver.source.bb.eutra.downlink.view.get_cindex() \n
		No command help available \n
			:return: dl_tp_cell_idx: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:VIEW:CINDex?')
		return Conversions.str_to_scalar_enum(response, enums.CcIndex)

	def set_cindex(self, dl_tp_cell_idx: enums.CcIndex) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:CINDex \n
		Snippet: driver.source.bb.eutra.downlink.view.set_cindex(dl_tp_cell_idx = enums.CcIndex.PC) \n
		No command help available \n
			:param dl_tp_cell_idx: No help available
		"""
		param = Conversions.enum_scalar_to_str(dl_tp_cell_idx, enums.CcIndex)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:VIEW:CINDex {param}')

	def get_fsts(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:FSTS \n
		Snippet: value: int = driver.source.bb.eutra.downlink.view.get_fsts() \n
		No command help available \n
			:return: fsts: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:VIEW:FSTS?')
		return Conversions.str_to_int(response)

	def set_fsts(self, fsts: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:FSTS \n
		Snippet: driver.source.bb.eutra.downlink.view.set_fsts(fsts = 1) \n
		No command help available \n
			:param fsts: No help available
		"""
		param = Conversions.decimal_value_to_str(fsts)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:VIEW:FSTS {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ViewMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:MODE \n
		Snippet: value: enums.ViewMode = driver.source.bb.eutra.downlink.view.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:VIEW:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ViewMode)

	def set_mode(self, mode: enums.ViewMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:MODE \n
		Snippet: driver.source.bb.eutra.downlink.view.set_mode(mode = enums.ViewMode.PRB) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ViewMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:VIEW:MODE {param}')

	def get_viss(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:VISS \n
		Snippet: value: int = driver.source.bb.eutra.downlink.view.get_viss() \n
		No command help available \n
			:return: viss: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:VIEW:VISS?')
		return Conversions.str_to_int(response)

	def set_viss(self, viss: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:VIEW:VISS \n
		Snippet: driver.source.bb.eutra.downlink.view.set_viss(viss = 1) \n
		No command help available \n
			:param viss: No help available
		"""
		param = Conversions.decimal_value_to_str(viss)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:VIEW:VISS {param}')
