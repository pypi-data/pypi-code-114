from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbol:
	"""Symbol commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbol", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DvbIleavMode:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:IINTerleaver:SYMBol:MODE \n
		Snippet: value: enums.DvbIleavMode = driver.source.bb.dvb.dvbt.iinterleaver.symbol.get_mode() \n
		Selects the inner interleaver mode. \n
			:return: mode: NATive| NATIve| IDEPth NATive The interleaver interleaves the bits over one OFDMA symbol. IDEPth The interleaver interleaves the bits over two (4K transmission mode) or four (2K transmission mode) OFDMA symbols.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:IINTerleaver:SYMBol:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbIleavMode)

	def set_mode(self, mode: enums.DvbIleavMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:IINTerleaver:SYMBol:MODE \n
		Snippet: driver.source.bb.dvb.dvbt.iinterleaver.symbol.set_mode(mode = enums.DvbIleavMode.IDEPth) \n
		Selects the inner interleaver mode. \n
			:param mode: NATive| NATIve| IDEPth NATive The interleaver interleaves the bits over one OFDMA symbol. IDEPth The interleaver interleaves the bits over two (4K transmission mode) or four (2K transmission mode) OFDMA symbols.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DvbIleavMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBT:IINTerleaver:SYMBol:MODE {param}')

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.DvbTranMode:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:IINTerleaver:SYMBol:TMODe \n
		Snippet: value: enums.DvbTranMode = driver.source.bb.dvb.dvbt.iinterleaver.symbol.get_tmode() \n
		Selects the transmission mode. \n
			:return: tmode: T2K| T4K| T8K
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:IINTerleaver:SYMBol:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DvbTranMode)

	def set_tmode(self, tmode: enums.DvbTranMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:IINTerleaver:SYMBol:TMODe \n
		Snippet: driver.source.bb.dvb.dvbt.iinterleaver.symbol.set_tmode(tmode = enums.DvbTranMode.T2K) \n
		Selects the transmission mode. \n
			:param tmode: T2K| T4K| T8K
		"""
		param = Conversions.enum_scalar_to_str(tmode, enums.DvbTranMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBT:IINTerleaver:SYMBol:TMODe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:IINTerleaver:SYMBol:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbt.iinterleaver.symbol.get_state() \n
		Activates/deactivates the inner symbol interleaver. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:IINTerleaver:SYMBol:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:IINTerleaver:SYMBol:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbt.iinterleaver.symbol.set_state(state = False) \n
		Activates/deactivates the inner symbol interleaver. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBT:IINTerleaver:SYMBol:STATe {param}')
