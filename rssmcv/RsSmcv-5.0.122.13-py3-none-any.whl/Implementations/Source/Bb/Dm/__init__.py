from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dm:
	"""Dm commands group definition. 106 total commands, 19 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dm", core, parent)

	@property
	def apsk16(self):
		"""apsk16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apsk16'):
			from .Apsk16 import Apsk16
			self._apsk16 = Apsk16(self._core, self._cmd_group)
		return self._apsk16

	@property
	def apsk32(self):
		"""apsk32 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apsk32'):
			from .Apsk32 import Apsk32
			self._apsk32 = Apsk32(self._core, self._cmd_group)
		return self._apsk32

	@property
	def aqPsk(self):
		"""aqPsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aqPsk'):
			from .AqPsk import AqPsk
			self._aqPsk = AqPsk(self._core, self._cmd_group)
		return self._aqPsk

	@property
	def ask(self):
		"""ask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ask'):
			from .Ask import Ask
			self._ask = Ask(self._core, self._cmd_group)
		return self._ask

	@property
	def clist(self):
		"""clist commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_clist'):
			from .Clist import Clist
			self._clist = Clist(self._core, self._cmd_group)
		return self._clist

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def dlist(self):
		"""dlist commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_dlist'):
			from .Dlist import Dlist
			self._dlist = Dlist(self._core, self._cmd_group)
		return self._dlist

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def flist(self):
		"""flist commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_flist'):
			from .Flist import Flist
			self._flist = Flist(self._core, self._cmd_group)
		return self._flist

	@property
	def fsk(self):
		"""fsk commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	@property
	def mlist(self):
		"""mlist commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_mlist'):
			from .Mlist import Mlist
			self._mlist = Mlist(self._core, self._cmd_group)
		return self._mlist

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def pramp(self):
		"""pramp commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_pramp'):
			from .Pramp import Pramp
			self._pramp = Pramp(self._core, self._cmd_group)
		return self._pramp

	@property
	def prbs(self):
		"""prbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbs'):
			from .Prbs import Prbs
			self._prbs = Prbs(self._core, self._cmd_group)
		return self._prbs

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def smodulation(self):
		"""smodulation commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_smodulation'):
			from .Smodulation import Smodulation
			self._smodulation = Smodulation(self._core, self._cmd_group)
		return self._smodulation

	@property
	def standard(self):
		"""standard commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import Standard
			self._standard = Standard(self._core, self._cmd_group)
		return self._standard

	@property
	def switching(self):
		"""switching commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_switching'):
			from .Switching import Switching
			self._switching = Switching(self._core, self._cmd_group)
		return self._switching

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 4 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	# noinspection PyTypeChecker
	def get_coding(self) -> enums.DmCod:
		"""SCPI: [SOURce<HW>]:BB:DM:CODing \n
		Snippet: value: enums.DmCod = driver.source.bb.dm.get_coding() \n
		Selects the modulation coding. \n
			:return: coding: OFF| DIFF| DPHS| DGRay| GRAY| GSM| NADC| PDC| PHS| TETRa| APCO25| PWT| TFTS| INMarsat| VDL| EDGE| APCO25FSK| ICO| CDMA2000| WCDMA| APCO258PSK OFF The coding is automatically disabled if the selected modulation type is not possible with the coding that has been set DPHS Phase Difference DGRay Difference + Gray
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:CODing?')
		return Conversions.str_to_scalar_enum(response, enums.DmCod)

	def set_coding(self, coding: enums.DmCod) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:CODing \n
		Snippet: driver.source.bb.dm.set_coding(coding = enums.DmCod.APCO25) \n
		Selects the modulation coding. \n
			:param coding: OFF| DIFF| DPHS| DGRay| GRAY| GSM| NADC| PDC| PHS| TETRa| APCO25| PWT| TFTS| INMarsat| VDL| EDGE| APCO25FSK| ICO| CDMA2000| WCDMA| APCO258PSK OFF The coding is automatically disabled if the selected modulation type is not possible with the coding that has been set DPHS Phase Difference DGRay Difference + Gray
		"""
		param = Conversions.enum_scalar_to_str(coding, enums.DmCod)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:CODing {param}')

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.BbDmModType:
		"""SCPI: [SOURce<HW>]:BB:DM:FORMat \n
		Snippet: value: enums.BbDmModType = driver.source.bb.dm.get_format_py() \n
		Sets the modulation type. When a standard is selected ([:SOURce<hw>]:BB:DM:STANdard) , the modulation type is set to the
		default value. \n
			:return: format_py: ASK| BPSK| P2DBpsk| QPSK| QPSK45| OQPSk| P4QPsk| P4DQpsk| PSK8| P8D8psk| P8EDge| QAM16| QAM32| QAM64| QAM256| QAM1024| MSK| FSK2| FSK4| USER| FSKVar| QAM128| QEDGe| QAM16EDge| QAM32EDge| AQPSk| QAM4096| APSK16| APSK32| FSK32| FSK64| FSK8| FSK16| QAM512| QAM2048
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.BbDmModType)

	def set_format_py(self, format_py: enums.BbDmModType) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FORMat \n
		Snippet: driver.source.bb.dm.set_format_py(format_py = enums.BbDmModType.APSK16) \n
		Sets the modulation type. When a standard is selected ([:SOURce<hw>]:BB:DM:STANdard) , the modulation type is set to the
		default value. \n
			:param format_py: ASK| BPSK| P2DBpsk| QPSK| QPSK45| OQPSk| P4QPsk| P4DQpsk| PSK8| P8D8psk| P8EDge| QAM16| QAM32| QAM64| QAM256| QAM1024| MSK| FSK2| FSK4| USER| FSKVar| QAM128| QEDGe| QAM16EDge| QAM32EDge| AQPSk| QAM4096| APSK16| APSK32| FSK32| FSK64| FSK8| FSK16| QAM512| QAM2048
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.BbDmModType)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FORMat {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRESet \n
		Snippet: driver.source.bb.dm.preset() \n
		Sets the default settings for digital modulation (*RST values specified for the commands) . Not affected is the state set
		with the command SOURce<hw>:BB:DM:STATe \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:PRESet \n
		Snippet: driver.source.bb.dm.preset_with_opc() \n
		Sets the default settings for digital modulation (*RST values specified for the commands) . Not affected is the state set
		with the command SOURce<hw>:BB:DM:STATe \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DM:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.DmDataSourV:
		"""SCPI: [SOURce<HW>]:BB:DM:SOURce \n
		Snippet: value: enums.DmDataSourV = driver.source.bb.dm.get_source() \n
		Selects the data source. \n
			:return: source: ZERO| ONE| PRBS| PATTern| DLISt
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.DmDataSourV)

	def set_source(self, source: enums.DmDataSourV) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SOURce \n
		Snippet: driver.source.bb.dm.set_source(source = enums.DmDataSourV.DLISt) \n
		Selects the data source. \n
			:param source: ZERO| ONE| PRBS| PATTern| DLISt
		"""
		param = Conversions.enum_scalar_to_str(source, enums.DmDataSourV)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SOURce {param}')

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:SRATe \n
		Snippet: value: float = driver.source.bb.dm.get_symbol_rate() \n
		Sets the symbol rate in Hz/kHz/MHz or sym/s, ksym/s and Msym/s. \n
			:return: srate: float Range: 400 to depends on the installed options, Unit: Hz or sym/s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, srate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SRATe \n
		Snippet: driver.source.bb.dm.set_symbol_rate(srate = 1.0) \n
		Sets the symbol rate in Hz/kHz/MHz or sym/s, ksym/s and Msym/s. \n
			:param srate: float Range: 400 to depends on the installed options, Unit: Hz or sym/s
		"""
		param = Conversions.decimal_value_to_str(srate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SRATe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DM:STATe \n
		Snippet: value: bool = driver.source.bb.dm.get_state() \n
		Enables/disables digital modulation. Switching on digital modulation turns off all the other digital standards in the
		same signal path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:STATe \n
		Snippet: driver.source.bb.dm.set_state(state = False) \n
		Enables/disables digital modulation. Switching on digital modulation turns off all the other digital standards in the
		same signal path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:STATe {param}')

	def clone(self) -> 'Dm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
