from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bb:
	"""Bb commands group definition. 10147 total commands, 40 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bb", core, parent)

	@property
	def arbitrary(self):
		"""arbitrary commands group. 12 Sub-classes, 3 commands."""
		if not hasattr(self, '_arbitrary'):
			from .Arbitrary import Arbitrary
			self._arbitrary = Arbitrary(self._core, self._cmd_group)
		return self._arbitrary

	@property
	def btooth(self):
		"""btooth commands group. 16 Sub-classes, 17 commands."""
		if not hasattr(self, '_btooth'):
			from .Btooth import Btooth
			self._btooth = Btooth(self._core, self._cmd_group)
		return self._btooth

	@property
	def c2K(self):
		"""c2K commands group. 13 Sub-classes, 5 commands."""
		if not hasattr(self, '_c2K'):
			from .C2K import C2K
			self._c2K = C2K(self._core, self._cmd_group)
		return self._c2K

	@property
	def coder(self):
		"""coder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coder'):
			from .Coder import Coder
			self._coder = Coder(self._core, self._cmd_group)
		return self._coder

	@property
	def dab(self):
		"""dab commands group. 11 Sub-classes, 7 commands."""
		if not hasattr(self, '_dab'):
			from .Dab import Dab
			self._dab = Dab(self._core, self._cmd_group)
		return self._dab

	@property
	def dm(self):
		"""dm commands group. 19 Sub-classes, 7 commands."""
		if not hasattr(self, '_dm'):
			from .Dm import Dm
			self._dm = Dm(self._core, self._cmd_group)
		return self._dm

	@property
	def dvb(self):
		"""dvb commands group. 13 Sub-classes, 3 commands."""
		if not hasattr(self, '_dvb'):
			from .Dvb import Dvb
			self._dvb = Dvb(self._core, self._cmd_group)
		return self._dvb

	@property
	def esequencer(self):
		"""esequencer commands group. 12 Sub-classes, 6 commands."""
		if not hasattr(self, '_esequencer'):
			from .Esequencer import Esequencer
			self._esequencer = Esequencer(self._core, self._cmd_group)
		return self._esequencer

	@property
	def eutra(self):
		"""eutra commands group. 20 Sub-classes, 7 commands."""
		if not hasattr(self, '_eutra'):
			from .Eutra import Eutra
			self._eutra = Eutra(self._core, self._cmd_group)
		return self._eutra

	@property
	def evdo(self):
		"""evdo commands group. 13 Sub-classes, 8 commands."""
		if not hasattr(self, '_evdo'):
			from .Evdo import Evdo
			self._evdo = Evdo(self._core, self._cmd_group)
		return self._evdo

	@property
	def gbas(self):
		"""gbas commands group. 8 Sub-classes, 9 commands."""
		if not hasattr(self, '_gbas'):
			from .Gbas import Gbas
			self._gbas = Gbas(self._core, self._cmd_group)
		return self._gbas

	@property
	def gnpr(self):
		"""gnpr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gnpr'):
			from .Gnpr import Gnpr
			self._gnpr = Gnpr(self._core, self._cmd_group)
		return self._gnpr

	@property
	def gnss(self):
		"""gnss commands group. 27 Sub-classes, 7 commands."""
		if not hasattr(self, '_gnss'):
			from .Gnss import Gnss
			self._gnss = Gnss(self._core, self._cmd_group)
		return self._gnss

	@property
	def graphics(self):
		"""graphics commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_graphics'):
			from .Graphics import Graphics
			self._graphics = Graphics(self._core, self._cmd_group)
		return self._graphics

	@property
	def gsm(self):
		"""gsm commands group. 19 Sub-classes, 8 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import Gsm
			self._gsm = Gsm(self._core, self._cmd_group)
		return self._gsm

	@property
	def huwb(self):
		"""huwb commands group. 12 Sub-classes, 12 commands."""
		if not hasattr(self, '_huwb'):
			from .Huwb import Huwb
			self._huwb = Huwb(self._core, self._cmd_group)
		return self._huwb

	@property
	def impairment(self):
		"""impairment commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_impairment'):
			from .Impairment import Impairment
			self._impairment = Impairment(self._core, self._cmd_group)
		return self._impairment

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def lora(self):
		"""lora commands group. 7 Sub-classes, 6 commands."""
		if not hasattr(self, '_lora'):
			from .Lora import Lora
			self._lora = Lora(self._core, self._cmd_group)
		return self._lora

	@property
	def mccw(self):
		"""mccw commands group. 5 Sub-classes, 2 commands."""
		if not hasattr(self, '_mccw'):
			from .Mccw import Mccw
			self._mccw = Mccw(self._core, self._cmd_group)
		return self._mccw

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	@property
	def nfc(self):
		"""nfc commands group. 10 Sub-classes, 12 commands."""
		if not hasattr(self, '_nfc'):
			from .Nfc import Nfc
			self._nfc = Nfc(self._core, self._cmd_group)
		return self._nfc

	@property
	def nr5G(self):
		"""nr5G commands group. 27 Sub-classes, 6 commands."""
		if not hasattr(self, '_nr5G'):
			from .Nr5G import Nr5G
			self._nr5G = Nr5G(self._core, self._cmd_group)
		return self._nr5G

	@property
	def ofdm(self):
		"""ofdm commands group. 15 Sub-classes, 17 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import Ofdm
			self._ofdm = Ofdm(self._core, self._cmd_group)
		return self._ofdm

	@property
	def oneweb(self):
		"""oneweb commands group. 16 Sub-classes, 7 commands."""
		if not hasattr(self, '_oneweb'):
			from .Oneweb import Oneweb
			self._oneweb = Oneweb(self._core, self._cmd_group)
		return self._oneweb

	@property
	def packet(self):
		"""packet commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_packet'):
			from .Packet import Packet
			self._packet = Packet(self._core, self._cmd_group)
		return self._packet

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pramp(self):
		"""pramp commands group. 5 Sub-classes, 2 commands."""
		if not hasattr(self, '_pramp'):
			from .Pramp import Pramp
			self._pramp = Pramp(self._core, self._cmd_group)
		return self._pramp

	@property
	def progress(self):
		"""progress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_progress'):
			from .Progress import Progress
			self._progress = Progress(self._core, self._cmd_group)
		return self._progress

	@property
	def sirius(self):
		"""sirius commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_sirius'):
			from .Sirius import Sirius
			self._sirius = Sirius(self._core, self._cmd_group)
		return self._sirius

	@property
	def stereo(self):
		"""stereo commands group. 7 Sub-classes, 5 commands."""
		if not hasattr(self, '_stereo'):
			from .Stereo import Stereo
			self._stereo = Stereo(self._core, self._cmd_group)
		return self._stereo

	@property
	def tdscdma(self):
		"""tdscdma commands group. 12 Sub-classes, 6 commands."""
		if not hasattr(self, '_tdscdma'):
			from .Tdscdma import Tdscdma
			self._tdscdma = Tdscdma(self._core, self._cmd_group)
		return self._tdscdma

	@property
	def tetra(self):
		"""tetra commands group. 11 Sub-classes, 9 commands."""
		if not hasattr(self, '_tetra'):
			from .Tetra import Tetra
			self._tetra = Tetra(self._core, self._cmd_group)
		return self._tetra

	@property
	def trigger(self):
		"""trigger commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def v5G(self):
		"""v5G commands group. 15 Sub-classes, 6 commands."""
		if not hasattr(self, '_v5G'):
			from .V5G import V5G
			self._v5G = V5G(self._core, self._cmd_group)
		return self._v5G

	@property
	def w3Gpp(self):
		"""w3Gpp commands group. 14 Sub-classes, 5 commands."""
		if not hasattr(self, '_w3Gpp'):
			from .W3Gpp import W3Gpp
			self._w3Gpp = W3Gpp(self._core, self._cmd_group)
		return self._w3Gpp

	@property
	def wlad(self):
		"""wlad commands group. 8 Sub-classes, 6 commands."""
		if not hasattr(self, '_wlad'):
			from .Wlad import Wlad
			self._wlad = Wlad(self._core, self._cmd_group)
		return self._wlad

	@property
	def wlnn(self):
		"""wlnn commands group. 9 Sub-classes, 8 commands."""
		if not hasattr(self, '_wlnn'):
			from .Wlnn import Wlnn
			self._wlnn = Wlnn(self._core, self._cmd_group)
		return self._wlnn

	@property
	def xmRadio(self):
		"""xmRadio commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_xmRadio'):
			from .XmRadio import XmRadio
			self._xmRadio = XmRadio(self._core, self._cmd_group)
		return self._xmRadio

	def get_cfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:CFACtor \n
		Snippet: value: float = driver.source.bb.get_cfactor() \n
		Queries the crest factor of the baseband signal. \n
			:return: cfactor: float Range: 0 to 100, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:CFACtor?')
		return Conversions.str_to_float(response)

	def get_foffset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:FOFFset \n
		Snippet: value: float = driver.source.bb.get_foffset() \n
		Sets a frequency offset for the internal/external baseband signal. The offset affects the generated baseband signal. \n
			:return: foffset: float Range: depends on the installed options , Unit: Hz E.g. -60 MHz to +60 MHz (R&S SMW-B10)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, foffset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:FOFFset \n
		Snippet: driver.source.bb.set_foffset(foffset = 1.0) \n
		Sets a frequency offset for the internal/external baseband signal. The offset affects the generated baseband signal. \n
			:param foffset: float Range: depends on the installed options , Unit: Hz E.g. -60 MHz to +60 MHz (R&S SMW-B10)
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:FOFFset {param}')

	# noinspection PyTypeChecker
	def get_iq_gain(self) -> enums.IqGainAll:
		"""SCPI: [SOURce<HW>]:BB:IQGain \n
		Snippet: value: enums.IqGainAll = driver.source.bb.get_iq_gain() \n
		Optimizes the modulation of the I/Q modulator for a subset of measurement requirement. \n
			:return: ipartq_gain: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:IQGain?')
		return Conversions.str_to_scalar_enum(response, enums.IqGainAll)

	def set_iq_gain(self, ipartq_gain: enums.IqGainAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:IQGain \n
		Snippet: driver.source.bb.set_iq_gain(ipartq_gain = enums.IqGainAll.AUTO) \n
		Optimizes the modulation of the I/Q modulator for a subset of measurement requirement. \n
			:param ipartq_gain: DBM4| DBM2| DB0| DB2| DB4| DB8| DB6| DBM3| DB3| AUTO Dynamic range of 16 dB divided into 2 dB steps. DB0|DB2|DB4|DB6|DB8 Activates the specified gain of 0 dB, +2 dB, +4 dB, +6 dB, +8 dB DBM2|DBM4 Activates the specified gain of -2 dB, -4 dB DBM3|DB3 (setting only) Provided only for backward compatibility with other Rohde & Schwarz signal generators. The R&S SMW accepts these values and maps them automatically as follows: DBM3 = DBM2, DB3 = DB2 AUTO The gain value is retrieved form the connected R&S SZU. The I/Q modulator is configured automatically.
		"""
		param = Conversions.enum_scalar_to_str(ipartq_gain, enums.IqGainAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:IQGain {param}')

	def get_mfp_correction(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MFPCorrection \n
		Snippet: value: float = driver.source.bb.get_mfp_correction() \n
		No command help available \n
			:return: mfp_correction: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MFPCorrection?')
		return Conversions.str_to_float(response)

	def get_pgain(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PGAin \n
		Snippet: value: float = driver.source.bb.get_pgain() \n
		Sets the relative gain for the internal or external baseband signal compared with the signals of the other baseband
		sources. \n
			:return: pgain: float Range: -50 to 50, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PGAin?')
		return Conversions.str_to_float(response)

	def set_pgain(self, pgain: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PGAin \n
		Snippet: driver.source.bb.set_pgain(pgain = 1.0) \n
		Sets the relative gain for the internal or external baseband signal compared with the signals of the other baseband
		sources. \n
			:param pgain: float Range: -50 to 50, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(pgain)
		self._core.io.write(f'SOURce<HwInstance>:BB:PGAin {param}')

	def get_poffset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:POFFset \n
		Snippet: value: float = driver.source.bb.get_poffset() \n
		Sets the relative phase offset for the selected baseband signal. The latter applies for the other paths or the external
		baseband. \n
			:return: poffset: float Range: 0 to 359.9, Unit: DEG
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, poffset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:POFFset \n
		Snippet: driver.source.bb.set_poffset(poffset = 1.0) \n
		Sets the relative phase offset for the selected baseband signal. The latter applies for the other paths or the external
		baseband. \n
			:param poffset: float Range: 0 to 359.9, Unit: DEG
		"""
		param = Conversions.decimal_value_to_str(poffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:POFFset {param}')

	# noinspection PyTypeChecker
	def get_route(self) -> enums.PathUniCodBbin:
		"""SCPI: [SOURce<HW>]:BB:ROUTe \n
		Snippet: value: enums.PathUniCodBbin = driver.source.bb.get_route() \n
		Selects the signal route for the internal/external baseband signal. The internal and external signals are summed, if
		necessary. \n
			:return: route: A | B| AB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ROUTe?')
		return Conversions.str_to_scalar_enum(response, enums.PathUniCodBbin)

	def set_route(self, route: enums.PathUniCodBbin) -> None:
		"""SCPI: [SOURce<HW>]:BB:ROUTe \n
		Snippet: driver.source.bb.set_route(route = enums.PathUniCodBbin.A) \n
		Selects the signal route for the internal/external baseband signal. The internal and external signals are summed, if
		necessary. \n
			:param route: A | B| AB
		"""
		param = Conversions.enum_scalar_to_str(route, enums.PathUniCodBbin)
		self._core.io.write(f'SOURce<HwInstance>:BB:ROUTe {param}')

	def clone(self) -> 'Bb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
