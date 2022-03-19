from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconfig:
	"""Pconfig commands group definition. 55 total commands, 11 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pconfig", core, parent)

	@property
	def btRequest(self):
		"""btRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_btRequest'):
			from .BtRequest import BtRequest
			self._btRequest = BtRequest(self._core, self._cmd_group)
		return self._btRequest

	@property
	def coding(self):
		"""coding commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_coding'):
			from .Coding import Coding
			self._coding = Coding(self._core, self._cmd_group)
		return self._coding

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dindicator(self):
		"""dindicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dindicator'):
			from .Dindicator import Dindicator
			self._dindicator = Dindicator(self._core, self._cmd_group)
		return self._dindicator

	@property
	def gpi(self):
		"""gpi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gpi'):
			from .Gpi import Gpi
			self._gpi = Gpi(self._core, self._cmd_group)
		return self._gpi

	@property
	def mac(self):
		"""mac commands group. 5 Sub-classes, 2 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import Mac
			self._mac = Mac(self._core, self._cmd_group)
		return self._mac

	@property
	def mpdu(self):
		"""mpdu commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpdu'):
			from .Mpdu import Mpdu
			self._mpdu = Mpdu(self._core, self._cmd_group)
		return self._mpdu

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def scrambler(self):
		"""scrambler commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_scrambler'):
			from .Scrambler import Scrambler
			self._scrambler = Scrambler(self._core, self._cmd_group)
		return self._scrambler

	@property
	def taRound(self):
		"""taRound commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taRound'):
			from .TaRound import TaRound
			self._taRound = TaRound(self._core, self._cmd_group)
		return self._taRound

	@property
	def tdWindowing(self):
		"""tdWindowing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdWindowing'):
			from .TdWindowing import TdWindowing
			self._tdWindowing = TdWindowing(self._core, self._cmd_group)
		return self._tdWindowing

	def get_em_indication(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:EMINdication \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.get_em_indication() \n
		The value of this field indicates the length of the PSDU. \n
			:return: ext_sc_mcs_ind: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:EMINdication?')
		return Conversions.str_to_bool(response)

	def set_em_indication(self, ext_sc_mcs_ind: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:EMINdication \n
		Snippet: driver.source.bb.wlad.pconfig.set_em_indication(ext_sc_mcs_ind = False) \n
		The value of this field indicates the length of the PSDU. \n
			:param ext_sc_mcs_ind: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(ext_sc_mcs_ind)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:EMINdication {param}')

	# noinspection PyTypeChecker
	def get_lrssi(self) -> enums.WlanadLastRssi:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:LRSSi \n
		Snippet: value: enums.WlanadLastRssi = driver.source.bb.wlad.pconfig.get_lrssi() \n
		Sets the last RSSI. \n
			:return: lrssi: NA| M68| M67| M65| M63| M61| M59| M57| M55| M53| M51| M49| M47| M45| M43| M42
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:LRSSi?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadLastRssi)

	def set_lrssi(self, lrssi: enums.WlanadLastRssi) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:LRSSi \n
		Snippet: driver.source.bb.wlad.pconfig.set_lrssi(lrssi = enums.WlanadLastRssi.M42) \n
		Sets the last RSSI. \n
			:param lrssi: NA| M68| M67| M65| M63| M61| M59| M57| M55| M53| M51| M49| M47| M45| M43| M42
		"""
		param = Conversions.enum_scalar_to_str(lrssi, enums.WlanadLastRssi)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:LRSSi {param}')

	# noinspection PyTypeChecker
	def get_mcs(self) -> enums.WlannMcs:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MCS \n
		Snippet: value: enums.WlannMcs = driver.source.bb.wlad.pconfig.get_mcs() \n
		Selects the modulation and coding scheme for all spatial streams. \n
			:return: mcs: MCS0| MCS1| MCS2| MCS3| MCS4| MCS5| MCS6| MCS7| MCS8| MCS9| MCS10| MCS11| MCS12| MCS91| MCS121| MCS122| MCS123| MCS124| MCS125| MCS126
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MCS?')
		return Conversions.str_to_scalar_enum(response, enums.WlannMcs)

	def set_mcs(self, mcs: enums.WlannMcs) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MCS \n
		Snippet: driver.source.bb.wlad.pconfig.set_mcs(mcs = enums.WlannMcs.MCS0) \n
		Selects the modulation and coding scheme for all spatial streams. \n
			:param mcs: MCS0| MCS1| MCS2| MCS3| MCS4| MCS5| MCS6| MCS7| MCS8| MCS9| MCS10| MCS11| MCS12| MCS91| MCS121| MCS122| MCS123| MCS124| MCS125| MCS126
		"""
		param = Conversions.enum_scalar_to_str(mcs, enums.WlannMcs)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MCS {param}')

	# noinspection PyTypeChecker
	def get_mtype(self) -> enums.WlanadModType:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MTYPe \n
		Snippet: value: enums.WlanadModType = driver.source.bb.wlad.pconfig.get_mtype() \n
		Sets the modulation type. \n
			:return: mtype: DBPSK| SQPSK| QPSK| QAM16| QAM64| P2BPSK| P2QPSK| P2QAM16| P2QAM64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadModType)

	def set_mtype(self, mtype: enums.WlanadModType) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MTYPe \n
		Snippet: driver.source.bb.wlad.pconfig.set_mtype(mtype = enums.WlanadModType.DBPSK) \n
		Sets the modulation type. \n
			:param mtype: DBPSK| SQPSK| QPSK| QAM16| QAM64| P2BPSK| P2QPSK| P2QAM16| P2QAM64
		"""
		param = Conversions.enum_scalar_to_str(mtype, enums.WlanadModType)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MTYPe {param}')

	# noinspection PyTypeChecker
	def get_ptype(self) -> enums.WlanadPackType:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:PTYPe \n
		Snippet: value: enums.WlanadPackType = driver.source.bb.wlad.pconfig.get_ptype() \n
		Sets the packet type. \n
			:return: ptype: TRNR| TRNT
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:PTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadPackType)

	def set_ptype(self, ptype: enums.WlanadPackType) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:PTYPe \n
		Snippet: driver.source.bb.wlad.pconfig.set_ptype(ptype = enums.WlanadPackType.TRNR) \n
		Sets the packet type. \n
			:param ptype: TRNR| TRNT
		"""
		param = Conversions.enum_scalar_to_str(ptype, enums.WlanadPackType)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:PTYPe {param}')

	def get_repetition(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:REPetition \n
		Snippet: value: int = driver.source.bb.wlad.pconfig.get_repetition() \n
		Sets the repetition number. \n
			:return: rep: integer Range: 1 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:REPetition?')
		return Conversions.str_to_int(response)

	def set_repetition(self, rep: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:REPetition \n
		Snippet: driver.source.bb.wlad.pconfig.set_repetition(rep = 1) \n
		Sets the repetition number. \n
			:param rep: integer Range: 1 to 2
		"""
		param = Conversions.decimal_value_to_str(rep)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:REPetition {param}')

	def get_tlength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TLENgth \n
		Snippet: value: int = driver.source.bb.wlad.pconfig.get_tlength() \n
		Sets the training length. \n
			:return: tlen: integer Range: 0 to 16
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:TLENgth?')
		return Conversions.str_to_int(response)

	def set_tlength(self, tlen: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TLENgth \n
		Snippet: driver.source.bb.wlad.pconfig.set_tlength(tlen = 1) \n
		Sets the training length. \n
			:param tlen: integer Range: 0 to 16
		"""
		param = Conversions.decimal_value_to_str(tlen)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:TLENgth {param}')

	# noinspection PyTypeChecker
	def get_tp_type(self) -> enums.WlanadTonePairType:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TPTYpe \n
		Snippet: value: enums.WlanadTonePairType = driver.source.bb.wlad.pconfig.get_tp_type() \n
		No command help available \n
			:return: tp_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:TPTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadTonePairType)

	def set_tp_type(self, tp_type: enums.WlanadTonePairType) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TPTYpe \n
		Snippet: driver.source.bb.wlad.pconfig.set_tp_type(tp_type = enums.WlanadTonePairType.DYNamic) \n
		No command help available \n
			:param tp_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(tp_type, enums.WlanadTonePairType)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:TPTYpe {param}')

	def get_ttime(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TTIMe \n
		Snippet: value: float = driver.source.bb.wlad.pconfig.get_ttime() \n
		No command help available \n
			:return: ttime: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:TTIMe?')
		return Conversions.str_to_float(response)

	def set_ttime(self, ttime: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:TTIMe \n
		Snippet: driver.source.bb.wlad.pconfig.set_ttime(ttime = 1.0) \n
		No command help available \n
			:param ttime: No help available
		"""
		param = Conversions.decimal_value_to_str(ttime)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:TTIMe {param}')

	def clone(self) -> 'Pconfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pconfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
