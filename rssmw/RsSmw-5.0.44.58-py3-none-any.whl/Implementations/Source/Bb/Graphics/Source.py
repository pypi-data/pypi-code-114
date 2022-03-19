from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	# noinspection PyTypeChecker
	def get_mux(self) -> enums.TranRecSourMux:
		"""SCPI: [SOURce]:BB:GRAPhics:SOURce:MUX \n
		Snippet: value: enums.TranRecSourMux = driver.source.bb.graphics.source.get_mux() \n
		In SCONfiguration:OUTPut:MODE DIGMux mode, select which of the multiplexed streams is displayed. \n
			:return: mode: STRA| STRB| STRC| STRD| STRE| STRF| STRG| STRH
		"""
		response = self._core.io.query_str('SOURce:BB:GRAPhics:SOURce:MUX?')
		return Conversions.str_to_scalar_enum(response, enums.TranRecSourMux)

	def set_mux(self, mode: enums.TranRecSourMux) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:SOURce:MUX \n
		Snippet: driver.source.bb.graphics.source.set_mux(mode = enums.TranRecSourMux.STRA) \n
		In SCONfiguration:OUTPut:MODE DIGMux mode, select which of the multiplexed streams is displayed. \n
			:param mode: STRA| STRB| STRC| STRD| STRE| STRF| STRG| STRH
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TranRecSourMux)
		self._core.io.write(f'SOURce:BB:GRAPhics:SOURce:MUX {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.TranRecSour:
		"""SCPI: [SOURce]:BB:GRAPhics:SOURce \n
		Snippet: value: enums.TranRecSour = driver.source.bb.graphics.source.get_value() \n
		Defines the signal acquisition point, that is the location in the signal flow where the displayed signal is tapped from.
		The available acquisition points depend on the selected system configuration. \n
			:return: source: STRA| STRB| STRC| STRD| STRE| STRF| STRG| STRH| BBA| BBB| BBC| BBD| BBE| BBF| BBG| BBH| RFA| RFB| RFC| RFD| IQO1| IQO2| DO1| DO2| BBIA| BBIB STRA|STRB|STRC|STRD|STRE|STRF|STRG|STRH Streams (A to H) ; input stream of the 'IQ Stream Mapper' BBA|BBB|BBC|BBD|BBE|BBF|BBG|BBH Baseband signals (A to H) BBIA|BBIB Digital baseband input signals RFA|RFB|RFC|RFD RF signals (A to D) IQO1|IQO2 Analog I/Q output signals DO1|DO2 Digital I/Q output signals; outputs of the 'IQ Stream Mapper'
		"""
		response = self._core.io.query_str('SOURce:BB:GRAPhics:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TranRecSour)

	def set_value(self, source: enums.TranRecSour) -> None:
		"""SCPI: [SOURce]:BB:GRAPhics:SOURce \n
		Snippet: driver.source.bb.graphics.source.set_value(source = enums.TranRecSour.BBA) \n
		Defines the signal acquisition point, that is the location in the signal flow where the displayed signal is tapped from.
		The available acquisition points depend on the selected system configuration. \n
			:param source: STRA| STRB| STRC| STRD| STRE| STRF| STRG| STRH| BBA| BBB| BBC| BBD| BBE| BBF| BBG| BBH| RFA| RFB| RFC| RFD| IQO1| IQO2| DO1| DO2| BBIA| BBIB STRA|STRB|STRC|STRD|STRE|STRF|STRG|STRH Streams (A to H) ; input stream of the 'IQ Stream Mapper' BBA|BBB|BBC|BBD|BBE|BBF|BBG|BBH Baseband signals (A to H) BBIA|BBIB Digital baseband input signals RFA|RFB|RFC|RFD RF signals (A to D) IQO1|IQO2 Analog I/Q output signals DO1|DO2 Digital I/Q output signals; outputs of the 'IQ Stream Mapper'
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TranRecSour)
		self._core.io.write(f'SOURce:BB:GRAPhics:SOURce {param}')
