from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emtc:
	"""Emtc commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emtc", core, parent)

	@property
	def valid(self):
		"""valid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_valid'):
			from .Valid import Valid
			self._valid = Valid(self._core, self._cmd_group)
		return self._valid

	def get_nn_bands(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:EMTC:NNBands \n
		Snippet: value: int = driver.source.bb.eutra.uplink.emtc.get_nn_bands() \n
		Queries the number of eMTC narrowbands NRBUL available within the selected channel bandwidth. \n
			:return: num_narrowbands: integer Range: 0 to 18
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:EMTC:NNBands?')
		return Conversions.str_to_int(response)

	def get_nw_bands(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:EMTC:NWBands \n
		Snippet: value: int = driver.source.bb.eutra.uplink.emtc.get_nw_bands() \n
		Queries the number of widebands. \n
			:return: num_widebands: integer Range: 0 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:EMTC:NWBands?')
		return Conversions.str_to_int(response)

	def get_rsymbol(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:EMTC:RSYMbol \n
		Snippet: value: int = driver.source.bb.eutra.uplink.emtc.get_rsymbol() \n
		Sets the number of retuning symbols. \n
			:return: retuning_symbol: integer Range: 0 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:EMTC:RSYMbol?')
		return Conversions.str_to_int(response)

	def set_rsymbol(self, retuning_symbol: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:EMTC:RSYMbol \n
		Snippet: driver.source.bb.eutra.uplink.emtc.set_rsymbol(retuning_symbol = 1) \n
		Sets the number of retuning symbols. \n
			:param retuning_symbol: integer Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(retuning_symbol)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:EMTC:RSYMbol {param}')

	def get_wbcfg(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:EMTC:WBCFg \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.emtc.get_wbcfg() \n
		If enabled, the available channel bandwidth is split into eMTC widebands. \n
			:return: wb_config: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:EMTC:WBCFg?')
		return Conversions.str_to_bool(response)

	def set_wbcfg(self, wb_config: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:EMTC:WBCFg \n
		Snippet: driver.source.bb.eutra.uplink.emtc.set_wbcfg(wb_config = False) \n
		If enabled, the available channel bandwidth is split into eMTC widebands. \n
			:param wb_config: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(wb_config)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:EMTC:WBCFg {param}')

	def clone(self) -> 'Emtc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emtc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
