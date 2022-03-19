from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconfiguration:
	"""Pconfiguration commands group definition. 121 total commands, 45 Subgroups, 52 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pconfiguration", core, parent)

	@property
	def aaddress(self):
		"""aaddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aaddress'):
			from .Aaddress import Aaddress
			self._aaddress = Aaddress(self._core, self._cmd_group)
		return self._aaddress

	@property
	def acad(self):
		"""acad commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_acad'):
			from .Acad import Acad
			self._acad = Acad(self._core, self._cmd_group)
		return self._acad

	@property
	def acAssigned(self):
		"""acAssigned commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acAssigned'):
			from .AcAssigned import AcAssigned
			self._acAssigned = AcAssigned(self._core, self._cmd_group)
		return self._acAssigned

	@property
	def acid(self):
		"""acid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acid'):
			from .Acid import Acid
			self._acid = Acid(self._core, self._cmd_group)
		return self._acid

	@property
	def adid(self):
		"""adid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adid'):
			from .Adid import Adid
			self._adid = Adid(self._core, self._cmd_group)
		return self._adid

	@property
	def alap(self):
		"""alap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alap'):
			from .Alap import Alap
			self._alap = Alap(self._core, self._cmd_group)
		return self._alap

	@property
	def anuap(self):
		"""anuap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anuap'):
			from .Anuap import Anuap
			self._anuap = Anuap(self._core, self._cmd_group)
		return self._anuap

	@property
	def asid(self):
		"""asid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asid'):
			from .Asid import Asid
			self._asid = Asid(self._core, self._cmd_group)
		return self._asid

	@property
	def cid(self):
		"""cid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cid'):
			from .Cid import Cid
			self._cid = Cid(self._core, self._cmd_group)
		return self._cid

	@property
	def ciValue(self):
		"""ciValue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ciValue'):
			from .CiValue import CiValue
			self._ciValue = CiValue(self._core, self._cmd_group)
		return self._ciValue

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dcmTable(self):
		"""dcmTable commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcmTable'):
			from .DcmTable import DcmTable
			self._dcmTable = DcmTable(self._core, self._cmd_group)
		return self._dcmTable

	@property
	def ecode(self):
		"""ecode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ecode'):
			from .Ecode import Ecode
			self._ecode = Ecode(self._core, self._cmd_group)
		return self._ecode

	@property
	def ediversifier(self):
		"""ediversifier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ediversifier'):
			from .Ediversifier import Ediversifier
			self._ediversifier = Ediversifier(self._core, self._cmd_group)
		return self._ediversifier

	@property
	def eheader(self):
		"""eheader commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eheader'):
			from .Eheader import Eheader
			self._eheader = Eheader(self._core, self._cmd_group)
		return self._eheader

	@property
	def ehFlags(self):
		"""ehFlags commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_ehFlags'):
			from .EhFlags import EhFlags
			self._ehFlags = EhFlags(self._core, self._cmd_group)
		return self._ehFlags

	@property
	def fsbit(self):
		"""fsbit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsbit'):
			from .Fsbit import Fsbit
			self._fsbit = Fsbit(self._core, self._cmd_group)
		return self._fsbit

	@property
	def icAssigned(self):
		"""icAssigned commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icAssigned'):
			from .IcAssigned import IcAssigned
			self._icAssigned = IcAssigned(self._core, self._cmd_group)
		return self._icAssigned

	@property
	def icid(self):
		"""icid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icid'):
			from .Icid import Icid
			self._icid = Icid(self._core, self._cmd_group)
		return self._icid

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def ilap(self):
		"""ilap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ilap'):
			from .Ilap import Ilap
			self._ilap = Ilap(self._core, self._cmd_group)
		return self._ilap

	@property
	def inuap(self):
		"""inuap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inuap'):
			from .Inuap import Inuap
			self._inuap = Inuap(self._core, self._cmd_group)
		return self._inuap

	@property
	def miVector(self):
		"""miVector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_miVector'):
			from .MiVector import MiVector
			self._miVector = MiVector(self._core, self._cmd_group)
		return self._miVector

	@property
	def mskd(self):
		"""mskd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mskd'):
			from .Mskd import Mskd
			self._mskd = Mskd(self._core, self._cmd_group)
		return self._mskd

	@property
	def mtsphy(self):
		"""mtsphy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtsphy'):
			from .Mtsphy import Mtsphy
			self._mtsphy = Mtsphy(self._core, self._cmd_group)
		return self._mtsphy

	@property
	def offset(self):
		"""offset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def phy(self):
		"""phy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_phy'):
			from .Phy import Phy
			self._phy = Phy(self._core, self._cmd_group)
		return self._phy

	@property
	def phys(self):
		"""phys commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_phys'):
			from .Phys import Phys
			self._phys = Phys(self._core, self._cmd_group)
		return self._phys

	@property
	def ropCode(self):
		"""ropCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ropCode'):
			from .RopCode import RopCode
			self._ropCode = RopCode(self._core, self._cmd_group)
		return self._ropCode

	@property
	def rphys(self):
		"""rphys commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rphys'):
			from .Rphys import Rphys
			self._rphys = Rphys(self._core, self._cmd_group)
		return self._rphys

	@property
	def rvector(self):
		"""rvector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvector'):
			from .Rvector import Rvector
			self._rvector = Rvector(self._core, self._cmd_group)
		return self._rvector

	@property
	def scAssigned(self):
		"""scAssigned commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scAssigned'):
			from .ScAssigned import ScAssigned
			self._scAssigned = ScAssigned(self._core, self._cmd_group)
		return self._scAssigned

	@property
	def scid(self):
		"""scid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scid'):
			from .Scid import Scid
			self._scid = Scid(self._core, self._cmd_group)
		return self._scid

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import Sid
			self._sid = Sid(self._core, self._cmd_group)
		return self._sid

	@property
	def siVector(self):
		"""siVector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siVector'):
			from .SiVector import SiVector
			self._siVector = SiVector(self._core, self._cmd_group)
		return self._siVector

	@property
	def slap(self):
		"""slap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slap'):
			from .Slap import Slap
			self._slap = Slap(self._core, self._cmd_group)
		return self._slap

	@property
	def snuap(self):
		"""snuap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snuap'):
			from .Snuap import Snuap
			self._snuap = Snuap(self._core, self._cmd_group)
		return self._snuap

	@property
	def sskd(self):
		"""sskd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sskd'):
			from .Sskd import Sskd
			self._sskd = Sskd(self._core, self._cmd_group)
		return self._sskd

	@property
	def stmPhy(self):
		"""stmPhy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_stmPhy'):
			from .StmPhy import StmPhy
			self._stmPhy = StmPhy(self._core, self._cmd_group)
		return self._stmPhy

	@property
	def svNumber(self):
		"""svNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_svNumber'):
			from .SvNumber import SvNumber
			self._svNumber = SvNumber(self._core, self._cmd_group)
		return self._svNumber

	@property
	def tlap(self):
		"""tlap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tlap'):
			from .Tlap import Tlap
			self._tlap = Tlap(self._core, self._cmd_group)
		return self._tlap

	@property
	def tnuap(self):
		"""tnuap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tnuap'):
			from .Tnuap import Tnuap
			self._tnuap = Tnuap(self._core, self._cmd_group)
		return self._tnuap

	@property
	def tphys(self):
		"""tphys commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tphys'):
			from .Tphys import Tphys
			self._tphys = Tphys(self._core, self._cmd_group)
		return self._tphys

	@property
	def utype(self):
		"""utype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utype'):
			from .Utype import Utype
			self._utype = Utype(self._core, self._cmd_group)
		return self._utype

	@property
	def vnumber(self):
		"""vnumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vnumber'):
			from .Vnumber import Vnumber
			self._vnumber = Vnumber(self._core, self._cmd_group)
		return self._vnumber

	def get_alength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ALENgth \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_alength() \n
		Specifies the length of ACAD data pattern. \n
			:return: length: integer Range: 0 to 62
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ALENgth?')
		return Conversions.str_to_int(response)

	def set_alength(self, length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ALENgth \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_alength(length = 1) \n
		Specifies the length of ACAD data pattern. \n
			:param length: integer Range: 0 to 62
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ALENgth {param}')

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.BtoAdvMode:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AMODe \n
		Snippet: value: enums.BtoAdvMode = driver.source.bb.btooth.econfiguration.pconfiguration.get_amode() \n
		Indicates the mode of the advertisement. \n
			:return: amode: NCNS| CNS| NCS NCNS: Non-connectable, non-scannable CNS: Connectable, non-scannable NCS: Non-connectable, non-scannable
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.BtoAdvMode)

	def set_amode(self, amode: enums.BtoAdvMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AMODe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_amode(amode = enums.BtoAdvMode.CNS) \n
		Indicates the mode of the advertisement. \n
			:param amode: NCNS| CNS| NCS NCNS: Non-connectable, non-scannable CNS: Connectable, non-scannable NCS: Non-connectable, non-scannable
		"""
		param = Conversions.enum_scalar_to_str(amode, enums.BtoAdvMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AMODe {param}')

	def get_aoffset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOFFset \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_aoffset() \n
		Specifies the time from the start of the packet containing the AuxPtr field to the approximate start of the auxiliary
		packet. The offset is determined by multiplying the value by the unit,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOUNits \n
			:return: aoffset: float Range: 0 to 245.7 or 246 to 2457 depending on offset unit
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AOFFset?')
		return Conversions.str_to_float(response)

	def set_aoffset(self, aoffset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOFFset \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_aoffset(aoffset = 1.0) \n
		Specifies the time from the start of the packet containing the AuxPtr field to the approximate start of the auxiliary
		packet. The offset is determined by multiplying the value by the unit,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOUNits \n
			:param aoffset: float Range: 0 to 245.7 or 246 to 2457 depending on offset unit
		"""
		param = Conversions.decimal_value_to_str(aoffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AOFFset {param}')

	# noinspection PyTypeChecker
	def get_ao_units(self) -> enums.BtoOffsUnit:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOUNits \n
		Snippet: value: enums.BtoOffsUnit = driver.source.bb.btooth.econfiguration.pconfiguration.get_ao_units() \n
		Indicates the units used by the 'Aux Offset' parameter, see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOFFset \n
			:return: unit: U30| U300 U30: 30 µs U300: 300 µs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AOUNits?')
		return Conversions.str_to_scalar_enum(response, enums.BtoOffsUnit)

	def set_ao_units(self, unit: enums.BtoOffsUnit) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOUNits \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ao_units(unit = enums.BtoOffsUnit.U30) \n
		Indicates the units used by the 'Aux Offset' parameter, see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:AOFFset \n
			:param unit: U30| U300 U30: 30 µs U300: 300 µs
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.BtoOffsUnit)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:AOUNits {param}')

	# noinspection PyTypeChecker
	def get_aphy(self) -> enums.PackFormat:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:APHY \n
		Snippet: value: enums.PackFormat = driver.source.bb.btooth.econfiguration.pconfiguration.get_aphy() \n
		Specifies the physical layer used to transmit the auxiliary packet. \n
			:return: aphy: L1M| L2M| LCOD LE 1M, LE 2M, LE coded PHY
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:APHY?')
		return Conversions.str_to_scalar_enum(response, enums.PackFormat)

	def set_aphy(self, aphy: enums.PackFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:APHY \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_aphy(aphy = enums.PackFormat.L1M) \n
		Specifies the physical layer used to transmit the auxiliary packet. \n
			:param aphy: L1M| L2M| LCOD LE 1M, LE 2M, LE coded PHY
		"""
		param = Conversions.enum_scalar_to_str(aphy, enums.PackFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:APHY {param}')

	# noinspection PyTypeChecker
	def get_atype(self) -> enums.BtoUlpAddrType:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ATYPe \n
		Snippet: value: enums.BtoUlpAddrType = driver.source.bb.btooth.econfiguration.pconfiguration.get_atype() \n
		Sets the address type in the payload of Bluetooth LE LL_PERIODIC_SYNC_IND packets. \n
			:return: atype: PUBLic| RANDom
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ATYPe?')
		return Conversions.str_to_scalar_enum(response, enums.BtoUlpAddrType)

	def set_atype(self, atype: enums.BtoUlpAddrType) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ATYPe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_atype(atype = enums.BtoUlpAddrType.PUBLic) \n
		Sets the address type in the payload of Bluetooth LE LL_PERIODIC_SYNC_IND packets. \n
			:param atype: PUBLic| RANDom
		"""
		param = Conversions.enum_scalar_to_str(atype, enums.BtoUlpAddrType)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ATYPe {param}')

	# noinspection PyTypeChecker
	def get_caccuracy(self) -> enums.BtoClkAcc:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CACCuracy \n
		Snippet: value: enums.BtoClkAcc = driver.source.bb.btooth.econfiguration.pconfiguration.get_caccuracy() \n
		Specifies the clock accuracy of the advertiser used between the packet containing this data and the auxiliary packet. \n
			:return: caccuracy: T500| T50 T500: 51 ppm to 500 ppm T50: 0 ppm to 50 ppm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CACCuracy?')
		return Conversions.str_to_scalar_enum(response, enums.BtoClkAcc)

	def set_caccuracy(self, caccuracy: enums.BtoClkAcc) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CACCuracy \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_caccuracy(caccuracy = enums.BtoClkAcc.T50) \n
		Specifies the clock accuracy of the advertiser used between the packet containing this data and the auxiliary packet. \n
			:param caccuracy: T500| T50 T500: 51 ppm to 500 ppm T50: 0 ppm to 50 ppm
		"""
		param = Conversions.enum_scalar_to_str(caccuracy, enums.BtoClkAcc)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CACCuracy {param}')

	def get_ce_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CECount \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_ce_count() \n
		Specifies the connection event count in the CtrData field of the LL_PERIODIC_SYNC_IND control data PDU. \n
			:return: ce_count: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CECount?')
		return Conversions.str_to_int(response)

	def set_ce_count(self, ce_count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CECount \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ce_count(ce_count = 1) \n
		Specifies the connection event count in the CtrData field of the LL_PERIODIC_SYNC_IND control data PDU. \n
			:param ce_count: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ce_count)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CECount {param}')

	def get_cinstant(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CINStant \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_cinstant() \n
		Sets a connection instant for indicating the connection event at which the new connection parameters are taken in use. \n
			:return: cinstant: integer Range: 1 to depends on sequence length
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CINStant?')
		return Conversions.str_to_int(response)

	def set_cinstant(self, cinstant: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CINStant \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_cinstant(cinstant = 1) \n
		Sets a connection instant for indicating the connection event at which the new connection parameters are taken in use. \n
			:param cinstant: integer Range: 1 to depends on sequence length
		"""
		param = Conversions.decimal_value_to_str(cinstant)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CINStant {param}')

	def get_cinterval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CINTerval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_cinterval() \n
		Sets the time interval between the start points of two consecutive connection events for the packet type DATA and all
		CONTROL_DATA packet types. Command sets the values in ms. Query returns values in s. \n
			:return: cinterval: float Range: 7.5E-3 s to depends on oversampling , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CINTerval?')
		return Conversions.str_to_float(response)

	def set_cinterval(self, cinterval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CINTerval \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_cinterval(cinterval = 1.0) \n
		Sets the time interval between the start points of two consecutive connection events for the packet type DATA and all
		CONTROL_DATA packet types. Command sets the values in ms. Query returns values in s. \n
			:param cinterval: float Range: 7.5E-3 s to depends on oversampling , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(cinterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CINTerval {param}')

	def get_cpresent(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CPResent \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.get_cpresent() \n
		Activates the CTEInfo field in the header of Bluetooth LE data packets in the LE uncoded PHY. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CPResent?')
		return Conversions.str_to_bool(response)

	def set_cpresent(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CPResent \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_cpresent(state = False) \n
		Activates the CTEInfo field in the header of Bluetooth LE data packets in the LE uncoded PHY. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CPResent {param}')

	# noinspection PyTypeChecker
	def get_cselection(self) -> enums.BtoChSel:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CSELection \n
		Snippet: value: enums.BtoChSel = driver.source.bb.btooth.econfiguration.pconfiguration.get_cselection() \n
		Specifies the algorithm of channel selection. \n
			:return: cselection: CS1| CS2 Algorithm #1 or algorithm #2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CSELection?')
		return Conversions.str_to_scalar_enum(response, enums.BtoChSel)

	def set_cselection(self, cselection: enums.BtoChSel) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CSELection \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_cselection(cselection = enums.BtoChSel.CS1) \n
		Specifies the algorithm of channel selection. \n
			:param cselection: CS1| CS2 Algorithm #1 or algorithm #2
		"""
		param = Conversions.enum_scalar_to_str(cselection, enums.BtoChSel)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CSELection {param}')

	def get_ctime(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CTIMe \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_ctime() \n
		Sets the CTETime comprising the length of constant tone extension field of the Bluetooth LE PDU. \n
			:return: ctime: float Range: 16E-6 to 160E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CTIMe?')
		return Conversions.str_to_float(response)

	def set_ctime(self, ctime: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CTIMe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ctime(ctime = 1.0) \n
		Sets the CTETime comprising the length of constant tone extension field of the Bluetooth LE PDU. \n
			:param ctime: float Range: 16E-6 to 160E-6
		"""
		param = Conversions.decimal_value_to_str(ctime)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CTIMe {param}')

	# noinspection PyTypeChecker
	def get_ct_req(self) -> enums.BtoCteType:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CTReq \n
		Snippet: value: enums.BtoCteType = driver.source.bb.btooth.econfiguration.pconfiguration.get_ct_req() \n
		Sets the CTE type in the CTETypeReq field of the CtrData field of the LL_CTE_REQ PDU. \n
			:return: ct_req: AOD1| AOA| AOD2 AOA AoA Constant Tone Extension AOD1 AoD Constant Tone Extension with 1 µs time slots AOD2 AoD Constant Tone Extension with 2 µs time slots
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CTReq?')
		return Conversions.str_to_scalar_enum(response, enums.BtoCteType)

	def set_ct_req(self, ct_req: enums.BtoCteType) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CTReq \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ct_req(ct_req = enums.BtoCteType.AOA) \n
		Sets the CTE type in the CTETypeReq field of the CtrData field of the LL_CTE_REQ PDU. \n
			:param ct_req: AOD1| AOA| AOD2 AOA AoA Constant Tone Extension AOD1 AoD Constant Tone Extension with 1 µs time slots AOD2 AoD Constant Tone Extension with 2 µs time slots
		"""
		param = Conversions.enum_scalar_to_str(ct_req, enums.BtoCteType)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CTReq {param}')

	# noinspection PyTypeChecker
	def get_ctype(self) -> enums.BtoCteType:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CTYPe \n
		Snippet: value: enums.BtoCteType = driver.source.bb.btooth.econfiguration.pconfiguration.get_ctype() \n
		Sets the type of constant tone extension. The type specifies the CTE AoA/AoD method and for AoD the length of the
		switching and I/Q sampling slots. \n
			:return: ctype: AOD1| AOA| AOD2 AOA AoA Constant Tone Extension AOD1 AoD Constant Tone Extension with 1 µs time slots AOD2 AoD Constant Tone Extension with 2 µs time slots
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.BtoCteType)

	def set_ctype(self, ctype: enums.BtoCteType) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:CTYPe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ctype(ctype = enums.BtoCteType.AOA) \n
		Sets the type of constant tone extension. The type specifies the CTE AoA/AoD method and for AoD the length of the
		switching and I/Q sampling slots. \n
			:param ctype: AOD1| AOA| AOD2 AOA AoA Constant Tone Extension AOD1 AoD Constant Tone Extension with 1 µs time slots AOD2 AoD Constant Tone Extension with 2 µs time slots
		"""
		param = Conversions.enum_scalar_to_str(ctype, enums.BtoCteType)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:CTYPe {param}')

	def get_dlength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DLENgth \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_dlength() \n
		Sets the payload data length in bytes. \n
			:return: dlength: integer Range: 0 to 255 (advertiser) or 251 (data)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DLENgth?')
		return Conversions.str_to_int(response)

	def set_dlength(self, dlength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DLENgth \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_dlength(dlength = 1) \n
		Sets the payload data length in bytes. \n
			:param dlength: integer Range: 0 to 255 (advertiser) or 251 (data)
		"""
		param = Conversions.decimal_value_to_str(dlength)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DLENgth {param}')

	def get_dwhitening(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DWHitening \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.get_dwhitening() \n
		Activates or deactivates the Data Whitening. Evenly distributed white noise is ideal for the transmission and real data
		can be forced to look similar to white noise with different methods called Data Whitening. Applied to the PDU and CRC
		fields of all packet types, whitening is used to avoid long equal seqeunces in the data bit stream. \n
			:return: dwhitening: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DWHitening?')
		return Conversions.str_to_bool(response)

	def set_dwhitening(self, dwhitening: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:DWHitening \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_dwhitening(dwhitening = False) \n
		Activates or deactivates the Data Whitening. Evenly distributed white noise is ideal for the transmission and real data
		can be forced to look similar to white noise with different methods called Data Whitening. Applied to the PDU and CRC
		fields of all packet types, whitening is used to avoid long equal seqeunces in the data bit stream. \n
			:param dwhitening: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dwhitening)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:DWHitening {param}')

	def get_ecounter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ECOunter \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_ecounter() \n
		Counts the AUX_SYNC_IND packets that the SyncInfo field describes. \n
			:return: ecounter: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ECOunter?')
		return Conversions.str_to_int(response)

	def set_ecounter(self, ecounter: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ECOunter \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ecounter(ecounter = 1) \n
		Counts the AUX_SYNC_IND packets that the SyncInfo field describes. \n
			:param ecounter: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ecounter)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ECOunter {param}')

	def get_fs_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:FSLength \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_fs_length() \n
		Enables that the feature set length is indicated. \n
			:return: fs_length: integer Range: 1 to 26
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:FSLength?')
		return Conversions.str_to_int(response)

	def set_fs_length(self, fs_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:FSLength \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_fs_length(fs_length = 1) \n
		Enables that the feature set length is indicated. \n
			:param fs_length: integer Range: 1 to 26
		"""
		param = Conversions.decimal_value_to_str(fs_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:FSLength {param}')

	def get_hlength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:HLENgth \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_hlength() \n
		Requires data event and advertising frame configuration with the packet type CONNECT_IND. Sets the difference from the
		current channel to the next channel. The Central and Peripherals determine the data channel in use for every connection
		event from the channel map. Hop_length is set for the LL connection and communicated in the CONNECT_IND and
		LL_CHANNEL_MAP_IND packets. \n
			:return: hlength: integer Range: 5 to 16
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:HLENgth?')
		return Conversions.str_to_int(response)

	def set_hlength(self, hlength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:HLENgth \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_hlength(hlength = 1) \n
		Requires data event and advertising frame configuration with the packet type CONNECT_IND. Sets the difference from the
		current channel to the next channel. The Central and Peripherals determine the data channel in use for every connection
		event from the channel map. Hop_length is set for the LL connection and communicated in the CONNECT_IND and
		LL_CHANNEL_MAP_IND packets. \n
			:param hlength: integer Range: 5 to 16
		"""
		param = Conversions.decimal_value_to_str(hlength)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:HLENgth {param}')

	def get_lc_timeout(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:LCTimeout \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_lc_timeout() \n
		Defines the maximum time between two correctly received Bluetooth LE packets in the LL connection before the connection
		is considered lost for the packet type CONNECT_IND. Command sets the values in ms. Query returns values in s. \n
			:return: lc_timeout: float Range: 100E-3 s to 32000E-3 s , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:LCTimeout?')
		return Conversions.str_to_float(response)

	def set_lc_timeout(self, lc_timeout: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:LCTimeout \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_lc_timeout(lc_timeout = 1.0) \n
		Defines the maximum time between two correctly received Bluetooth LE packets in the LL connection before the connection
		is considered lost for the packet type CONNECT_IND. Command sets the values in ms. Query returns values in s. \n
			:param lc_timeout: float Range: 100E-3 s to 32000E-3 s , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(lc_timeout)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:LCTimeout {param}')

	def get_lpe_counter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:LPECounter \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_lpe_counter() \n
		Specifies the lastPaEventCounter field in the CtrData field of the LL_PERIODIC_SYNC_IND PDU. \n
			:return: lpe_counter: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:LPECounter?')
		return Conversions.str_to_int(response)

	def set_lpe_counter(self, lpe_counter: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:LPECounter \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_lpe_counter(lpe_counter = 1) \n
		Specifies the lastPaEventCounter field in the CtrData field of the LL_PERIODIC_SYNC_IND PDU. \n
			:param lpe_counter: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(lpe_counter)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:LPECounter {param}')

	def get_mcl_req(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MCLReq \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_mcl_req() \n
		Specifies the minimum CTE length in the CtrData field of the LL_CTE_Req PDU. \n
			:return: mcl_req: float Range: 16E-6 to 160E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MCLReq?')
		return Conversions.str_to_float(response)

	def set_mcl_req(self, mcl_req: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MCLReq \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mcl_req(mcl_req = 1.0) \n
		Specifies the minimum CTE length in the CtrData field of the LL_CTE_Req PDU. \n
			:param mcl_req: float Range: 16E-6 to 160E-6
		"""
		param = Conversions.decimal_value_to_str(mcl_req)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MCLReq {param}')

	def get_mn_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MNINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_mn_interval() \n
		Specifies the minimum allowed connection interval. Command sets the values in ms. Query returns values in s. \n
			:return: mn_interval: float Range: 7.5E-3 s to depending on Max. Interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MNINterval?')
		return Conversions.str_to_float(response)

	def set_mn_interval(self, mn_interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MNINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mn_interval(mn_interval = 1.0) \n
		Specifies the minimum allowed connection interval. Command sets the values in ms. Query returns values in s. \n
			:param mn_interval: float Range: 7.5E-3 s to depending on Max. Interval
		"""
		param = Conversions.decimal_value_to_str(mn_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MNINterval {param}')

	def get_mr_octets(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MROCtets \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_mr_octets() \n
		Specifies the maximum allowed payload length of a packet to be received (..:MROCtets) or transmitted (..:MTOCtets) .
		Information is signaled via LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:return: mr_octets: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MROCtets?')
		return Conversions.str_to_int(response)

	def set_mr_octets(self, mr_octets: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MROCtets \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mr_octets(mr_octets = 1) \n
		Specifies the maximum allowed payload length of a packet to be received (..:MROCtets) or transmitted (..:MTOCtets) .
		Information is signaled via LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:param mr_octets: integer Range: 27 to 251
		"""
		param = Conversions.decimal_value_to_str(mr_octets)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MROCtets {param}')

	def get_mr_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MRTime \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_mr_time() \n
		Specifies the maximum allowed time to receive (..:MRTime) or transmit (..:MTTime) a packet. Information is signaled via
		LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:return: mr_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MRTime?')
		return Conversions.str_to_float(response)

	def set_mr_time(self, mr_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MRTime \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mr_time(mr_time = 1.0) \n
		Specifies the maximum allowed time to receive (..:MRTime) or transmit (..:MTTime) a packet. Information is signaled via
		LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:param mr_time: float Range: 0.328E-3 to 17.04E-3
		"""
		param = Conversions.decimal_value_to_str(mr_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MRTime {param}')

	def get_mt_octets(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MTOCtets \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_mt_octets() \n
		Specifies the maximum allowed payload length of a packet to be received (..:MROCtets) or transmitted (..:MTOCtets) .
		Information is signaled via LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:return: mt_octets: integer Range: 27 to 251
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MTOCtets?')
		return Conversions.str_to_int(response)

	def set_mt_octets(self, mt_octets: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MTOCtets \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mt_octets(mt_octets = 1) \n
		Specifies the maximum allowed payload length of a packet to be received (..:MROCtets) or transmitted (..:MTOCtets) .
		Information is signaled via LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:param mt_octets: integer Range: 27 to 251
		"""
		param = Conversions.decimal_value_to_str(mt_octets)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MTOCtets {param}')

	def get_mt_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MTTime \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_mt_time() \n
		Specifies the maximum allowed time to receive (..:MRTime) or transmit (..:MTTime) a packet. Information is signaled via
		LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:return: mt_time: float Range: 0.328E-3 to 17.04E-3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MTTime?')
		return Conversions.str_to_float(response)

	def set_mt_time(self, mt_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MTTime \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mt_time(mt_time = 1.0) \n
		Specifies the maximum allowed time to receive (..:MRTime) or transmit (..:MTTime) a packet. Information is signaled via
		LL_LENGTH_REQ and LL_LENGTH_RSP. \n
			:param mt_time: float Range: 0.328E-3 to 17.04E-3
		"""
		param = Conversions.decimal_value_to_str(mt_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MTTime {param}')

	def get_mu_channels(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MUCHannels \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_mu_channels() \n
		Specifies the minimum number of channels to be used on the specified PHYs,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:PHYS:L1M:STATe etc. \n
			:return: mu_channels: integer Range: 2 to 37
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MUCHannels?')
		return Conversions.str_to_int(response)

	def set_mu_channels(self, mu_channels: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MUCHannels \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mu_channels(mu_channels = 1) \n
		Specifies the minimum number of channels to be used on the specified PHYs,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:PHYS:L1M:STATe etc. \n
			:param mu_channels: integer Range: 2 to 37
		"""
		param = Conversions.decimal_value_to_str(mu_channels)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MUCHannels {param}')

	def get_mx_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MXINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_mx_interval() \n
		Specifies the maximum allowed connection interval. Command sets the values in ms. Query returns values in s. \n
			:return: minterval: float Range: 7.5E-3 s to 4000E-3 s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MXINterval?')
		return Conversions.str_to_float(response)

	def set_mx_interval(self, minterval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:MXINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_mx_interval(minterval = 1.0) \n
		Specifies the maximum allowed connection interval. Command sets the values in ms. Query returns values in s. \n
			:param minterval: float Range: 7.5E-3 s to 4000E-3 s
		"""
		param = Conversions.decimal_value_to_str(minterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:MXINterval {param}')

	def get_nc_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NCINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_nc_interval() \n
		Sets the time interval new connection events for the packet types CONNECT_IND and LL_CONNECTION_UPDATE_IND. Command sets
		the values in ms. Query returns values in s. \n
			:return: nc_interval: float Range: 7.5E-3 s to depends on oversampling , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NCINterval?')
		return Conversions.str_to_float(response)

	def set_nc_interval(self, nc_interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NCINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_nc_interval(nc_interval = 1.0) \n
		Sets the time interval new connection events for the packet types CONNECT_IND and LL_CONNECTION_UPDATE_IND. Command sets
		the values in ms. Query returns values in s. \n
			:param nc_interval: float Range: 7.5E-3 s to depends on oversampling , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(nc_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NCINterval {param}')

	def get_nlc_timeout(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NLCTimeout \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_nlc_timeout() \n
		Defines the maximum time between two correctly received Bluetooth LE packets in the LL connection before the connection
		is considered lost only for the packet type LL_CONNECTION_UPDATE_IND. Command sets the values in ms. Query returns values
		in s. \n
			:return: nlc_timeout: float Range: 100E-3 s to 32000E-3 s , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NLCTimeout?')
		return Conversions.str_to_float(response)

	def set_nlc_timeout(self, nlc_timeout: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NLCTimeout \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_nlc_timeout(nlc_timeout = 1.0) \n
		Defines the maximum time between two correctly received Bluetooth LE packets in the LL connection before the connection
		is considered lost only for the packet type LL_CONNECTION_UPDATE_IND. Command sets the values in ms. Query returns values
		in s. \n
			:param nlc_timeout: float Range: 100E-3 s to 32000E-3 s , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(nlc_timeout)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NLCTimeout {param}')

	def get_ns_latency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NSLatency \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_ns_latency() \n
		Requires a data event and advertising frame configuration with the packet type LL_CONNECTION_UPDATE_IND. Sets the number
		of consecutive connection events the Peripheral can ignore for asymmetric link layer connections. \n
			:return: ns_latency: integer Range: 0 to depends on LL connection timeout and connection event interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NSLatency?')
		return Conversions.str_to_int(response)

	def set_ns_latency(self, ns_latency: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NSLatency \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ns_latency(ns_latency = 1) \n
		Requires a data event and advertising frame configuration with the packet type LL_CONNECTION_UPDATE_IND. Sets the number
		of consecutive connection events the Peripheral can ignore for asymmetric link layer connections. \n
			:param ns_latency: integer Range: 0 to depends on LL connection timeout and connection event interval
		"""
		param = Conversions.decimal_value_to_str(ns_latency)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NSLatency {param}')

	def get_ns_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NSValue \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_ns_value() \n
		Sets the start value of the next expected packet from the same device in the LL connection ('N'ext'E'xpected
		'S'equence'N'umber) . This parameter can be set in the first event. From the second event this field is not indicated. \n
			:return: ns_value: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NSValue?')
		return Conversions.str_to_int(response)

	def set_ns_value(self, ns_value: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NSValue \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ns_value(ns_value = 1) \n
		Sets the start value of the next expected packet from the same device in the LL connection ('N'ext'E'xpected
		'S'equence'N'umber) . This parameter can be set in the first event. From the second event this field is not indicated. \n
			:param ns_value: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(ns_value)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NSValue {param}')

	def get_nw_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NWOFfset \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_nw_offset() \n
		Sets the start point of the transmit window for data event and advertising frame configuration with the packet type
		LL_CONNECTION_UPDATE_IND. Command sets the values in ms. Query returns values in s. \n
			:return: nw_offset: float Range: 0 s to depends on connection event interval , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NWOFfset?')
		return Conversions.str_to_float(response)

	def set_nw_offset(self, nw_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NWOFfset \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_nw_offset(nw_offset = 1.0) \n
		Sets the start point of the transmit window for data event and advertising frame configuration with the packet type
		LL_CONNECTION_UPDATE_IND. Command sets the values in ms. Query returns values in s. \n
			:param nw_offset: float Range: 0 s to depends on connection event interval , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(nw_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NWOFfset {param}')

	def get_nw_size(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NWSize \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_nw_size() \n
		Sets the size of the transmit window, regarding to the start point for data event and advertising frame configuration
		with the packet type LL_CONNECTION_UPDATE_IND. \n
			:return: nw_size: float Range: 1.25E-3 to depends on connection event interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NWSize?')
		return Conversions.str_to_float(response)

	def set_nw_size(self, nw_size: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:NWSize \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_nw_size(nw_size = 1.0) \n
		Sets the size of the transmit window, regarding to the start point for data event and advertising frame configuration
		with the packet type LL_CONNECTION_UPDATE_IND. \n
			:param nw_size: float Range: 1.25E-3 to depends on connection event interval
		"""
		param = Conversions.decimal_value_to_str(nw_size)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:NWSize {param}')

	def get_oadjust(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:OADJust \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.get_oadjust() \n
		Adjusts the 'Sync Packet Offset' automatically to the next value, which is a multiple of the ''Offset Units'. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:OADJust?')
		return Conversions.str_to_bool(response)

	def set_oadjust(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:OADJust \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_oadjust(state = False) \n
		Adjusts the 'Sync Packet Offset' automatically to the next value, which is a multiple of the ''Offset Units'. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:OADJust {param}')

	def get_pa_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PAINterval \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_pa_interval() \n
		Sets the time interval between the start of two AUX_SYNC_IND PDUs from the same advertising set. Command sets the values
		in ms. Query returns values in s. \n
			:return: interval: float Range: 7.5E-3 s to depending on oversampling , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PAINterval?')
		return Conversions.str_to_float(response)

	def set_pa_interval(self, interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PAINterval \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_pa_interval(interval = 1.0) \n
		Sets the time interval between the start of two AUX_SYNC_IND PDUs from the same advertising set. Command sets the values
		in ms. Query returns values in s. \n
			:param interval: float Range: 7.5E-3 s to depending on oversampling , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PAINterval {param}')

	def get_pperiodicity(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PPERiodicity \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_pperiodicity() \n
		Specifies a value the connection interval is preferred to be a multiple of. \n
			:return: pperiodicity: float Range: 0 to depends on Max. Interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PPERiodicity?')
		return Conversions.str_to_float(response)

	def set_pperiodicity(self, pperiodicity: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PPERiodicity \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_pperiodicity(pperiodicity = 1.0) \n
		Specifies a value the connection interval is preferred to be a multiple of. \n
			:param pperiodicity: float Range: 0 to depends on Max. Interval
		"""
		param = Conversions.decimal_value_to_str(pperiodicity)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PPERiodicity {param}')

	# noinspection PyTypeChecker
	def get_ra_type(self) -> enums.BtoUlpAddrType:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:RATYpe \n
		Snippet: value: enums.BtoUlpAddrType = driver.source.bb.btooth.econfiguration.pconfiguration.get_ra_type() \n
		Selects the address type of the controller device. Depending on the Bluetooth controller role either Tx or Rx or both
		address types are assigned. Subdivided into private and random, a Bluetooth LE device address consits of 48 bits.
		The format of the device address differs depending on the selected address type. \n
			:return: ra_type: PUBLic| RANDom PUBlic Allocates a unique 48 bit address to each Bluetooth LE device. The public address is given from the registration authority IEEE. RANDom Allocates a 48-bit address to each Bluetooth LE device. A random address is optional.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:RATYpe?')
		return Conversions.str_to_scalar_enum(response, enums.BtoUlpAddrType)

	def set_ra_type(self, ra_type: enums.BtoUlpAddrType) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:RATYpe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ra_type(ra_type = enums.BtoUlpAddrType.PUBLic) \n
		Selects the address type of the controller device. Depending on the Bluetooth controller role either Tx or Rx or both
		address types are assigned. Subdivided into private and random, a Bluetooth LE device address consits of 48 bits.
		The format of the device address differs depending on the selected address type. \n
			:param ra_type: PUBLic| RANDom PUBlic Allocates a unique 48 bit address to each Bluetooth LE device. The public address is given from the registration authority IEEE. RANDom Allocates a 48-bit address to each Bluetooth LE device. A random address is optional.
		"""
		param = Conversions.enum_scalar_to_str(ra_type, enums.BtoUlpAddrType)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:RATYpe {param}')

	def get_rce_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:RCECount \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_rce_count() \n
		Specifies the ReferenceConnEventCount field of LL_CONNECTION_PARAM_REQ. \n
			:return: rce_count: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:RCECount?')
		return Conversions.str_to_int(response)

	def set_rce_count(self, rce_count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:RCECount \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_rce_count(rce_count = 1) \n
		Specifies the ReferenceConnEventCount field of LL_CONNECTION_PARAM_REQ. \n
			:param rce_count: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(rce_count)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:RCECount {param}')

	# noinspection PyTypeChecker
	def get_sc_accuracy(self) -> enums.BtoSlpClckAccrcy:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SCACcuracy \n
		Snippet: value: enums.BtoSlpClckAccrcy = driver.source.bb.btooth.econfiguration.pconfiguration.get_sc_accuracy() \n
		Defines the clock accuracy of the Central with specified encoding. This parameter is used by the Peripheral to determine
		required listening windows in the LL connection. It is a controller design parameter known by the bluetooth controller. \n
			:return: sc_accuracy: SCA0| SCA1| SCA2| SCA3| SCA4| SCA5| SCA6| SCA7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SCACcuracy?')
		return Conversions.str_to_scalar_enum(response, enums.BtoSlpClckAccrcy)

	def set_sc_accuracy(self, sc_accuracy: enums.BtoSlpClckAccrcy) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SCACcuracy \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_sc_accuracy(sc_accuracy = enums.BtoSlpClckAccrcy.SCA0) \n
		Defines the clock accuracy of the Central with specified encoding. This parameter is used by the Peripheral to determine
		required listening windows in the LL connection. It is a controller design parameter known by the bluetooth controller. \n
			:param sc_accuracy: SCA0| SCA1| SCA2| SCA3| SCA4| SCA5| SCA6| SCA7
		"""
		param = Conversions.enum_scalar_to_str(sc_accuracy, enums.BtoSlpClckAccrcy)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SCACcuracy {param}')

	def get_sce_counter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SCECounter \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_sce_counter() \n
		No command help available \n
			:return: sce_counter: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SCECounter?')
		return Conversions.str_to_int(response)

	def set_sce_counter(self, sce_counter: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SCECounter \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_sce_counter(sce_counter = 1) \n
		No command help available \n
			:param sce_counter: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(sce_counter)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SCECounter {param}')

	def get_slatency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SLATency \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_slatency() \n
		Requires data event and advertising frame configuration with the packet type CONNECT_IND. Sets the number of consecutive
		connection events the Peripheral can ignore for asymmetric link layer connections. \n
			:return: slatency: integer Range: 0 to depends on LL connection timeout and connection event interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SLATency?')
		return Conversions.str_to_int(response)

	def set_slatency(self, slatency: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SLATency \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_slatency(slatency = 1) \n
		Requires data event and advertising frame configuration with the packet type CONNECT_IND. Sets the number of consecutive
		connection events the Peripheral can ignore for asymmetric link layer connections. \n
			:param slatency: integer Range: 0 to depends on LL connection timeout and connection event interval
		"""
		param = Conversions.decimal_value_to_str(slatency)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SLATency {param}')

	# noinspection PyTypeChecker
	def get_sounits(self) -> enums.BtoOffsUnit:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SOUNits \n
		Snippet: value: enums.BtoOffsUnit = driver.source.bb.btooth.econfiguration.pconfiguration.get_sounits() \n
		Indicates the units used by the 'Sync Packet Offset' parameter,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:SPOFfset \n
			:return: unit: U30| U300 U30 30 µs U300 300 µs
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SOUNits?')
		return Conversions.str_to_scalar_enum(response, enums.BtoOffsUnit)

	def set_sounits(self, unit: enums.BtoOffsUnit) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SOUNits \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_sounits(unit = enums.BtoOffsUnit.U30) \n
		Indicates the units used by the 'Sync Packet Offset' parameter,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:SPOFfset \n
			:param unit: U30| U300 U30 30 µs U300 300 µs
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.BtoOffsUnit)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SOUNits {param}')

	# noinspection PyTypeChecker
	def get_spbit(self) -> enums.BtoSymPerBit:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SPBit \n
		Snippet: value: enums.BtoSymPerBit = driver.source.bb.btooth.econfiguration.pconfiguration.get_spbit() \n
		Specifies a coding for LE coded packets. The specification for Bluetooth wireless technology defines two values S for
		forward error correction: S = 2 symbol/bit and S = 8 symbol/bit. \n
			:return: spb: TWO| EIGHt
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SPBit?')
		return Conversions.str_to_scalar_enum(response, enums.BtoSymPerBit)

	def set_spbit(self, spb: enums.BtoSymPerBit) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SPBit \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_spbit(spb = enums.BtoSymPerBit.EIGHt) \n
		Specifies a coding for LE coded packets. The specification for Bluetooth wireless technology defines two values S for
		forward error correction: S = 2 symbol/bit and S = 8 symbol/bit. \n
			:param spb: TWO| EIGHt
		"""
		param = Conversions.enum_scalar_to_str(spb, enums.BtoSymPerBit)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SPBit {param}')

	def get_sp_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SPOFfset \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_sp_offset() \n
		Specifies the time from the start of the AUX_ADV_IND packet containing the SyncInfo field to the start of the
		AUX_SYNC_IND packet. The offset is determined by multiplying the value by the unit,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:SOUNits \n
			:return: sp_offset: float Range: 0 to 245.7 or 246 to 2457 depending on offset unit
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SPOFfset?')
		return Conversions.str_to_float(response)

	def set_sp_offset(self, sp_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SPOFfset \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_sp_offset(sp_offset = 1.0) \n
		Specifies the time from the start of the AUX_ADV_IND packet containing the SyncInfo field to the start of the
		AUX_SYNC_IND packet. The offset is determined by multiplying the value by the unit,
		see [:SOURce<hw>]:BB:BTOoth:ECONfiguration:PCONfiguration:SOUNits \n
			:param sp_offset: float Range: 0 to 245.7 or 246 to 2457 depending on offset unit
		"""
		param = Conversions.decimal_value_to_str(sp_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SPOFfset {param}')

	def get_ss_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SSValue \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_ss_value() \n
		Sets the sequence number of the packet. This parameter can be set in the first event. From the second event, this field
		is not indicated. \n
			:return: ss_value: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SSValue?')
		return Conversions.str_to_int(response)

	def set_ss_value(self, ss_value: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SSValue \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ss_value(ss_value = 1) \n
		Sets the sequence number of the packet. This parameter can be set in the first event. From the second event, this field
		is not indicated. \n
			:param ss_value: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(ss_value)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SSValue {param}')

	# noinspection PyTypeChecker
	def get_ta_type(self) -> enums.BtoUlpAddrType:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TATYpe \n
		Snippet: value: enums.BtoUlpAddrType = driver.source.bb.btooth.econfiguration.pconfiguration.get_ta_type() \n
		Selects the address type of the controller device. Depending on the Bluetooth controller role either Tx or Rx or both
		address types are assigned. Subdivided into private and random, a Bluetooth LE device address consits of 48 bits.
		The format of the device address differs depending on the selected address type. \n
			:return: ta_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TATYpe?')
		return Conversions.str_to_scalar_enum(response, enums.BtoUlpAddrType)

	def set_ta_type(self, ta_type: enums.BtoUlpAddrType) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TATYpe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_ta_type(ta_type = enums.BtoUlpAddrType.PUBLic) \n
		Selects the address type of the controller device. Depending on the Bluetooth controller role either Tx or Rx or both
		address types are assigned. Subdivided into private and random, a Bluetooth LE device address consits of 48 bits.
		The format of the device address differs depending on the selected address type. \n
			:param ta_type: PUBLic| RANDom PUBlic Allocates a unique 48 bit address to each Bluetooth LE device. The public address is given from the registration authority IEEE. RANDom Allocates a 48-bit address to each Bluetooth LE device. A random address is optional.
		"""
		param = Conversions.enum_scalar_to_str(ta_type, enums.BtoUlpAddrType)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TATYpe {param}')

	def get_tpower(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TPOWer \n
		Snippet: value: int = driver.source.bb.btooth.econfiguration.pconfiguration.get_tpower() \n
		Sets the required transmit power to be signaled within an extended header. \n
			:return: tpower: integer Range: -127 to 126
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TPOWer?')
		return Conversions.str_to_int(response)

	def set_tpower(self, tpower: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TPOWer \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_tpower(tpower = 1) \n
		Sets the required transmit power to be signaled within an extended header. \n
			:param tpower: integer Range: -127 to 126
		"""
		param = Conversions.decimal_value_to_str(tpower)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TPOWer {param}')

	def get_woffset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:WOFFset \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_woffset() \n
		Sets the start point of the window transmit for data event and advertising frame configuration with the packet type
		CONNECT_IND. Command sets the values in ms. Query returns values in s. \n
			:return: woffset: float Range: 0 s to depending on connection event interval , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:WOFFset?')
		return Conversions.str_to_float(response)

	def set_woffset(self, woffset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:WOFFset \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_woffset(woffset = 1.0) \n
		Sets the start point of the window transmit for data event and advertising frame configuration with the packet type
		CONNECT_IND. Command sets the values in ms. Query returns values in s. \n
			:param woffset: float Range: 0 s to depending on connection event interval , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(woffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:WOFFset {param}')

	def get_wsize(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:WSIZe \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.get_wsize() \n
		Sets the size of the transmit window, regarding to the start point for data event and advertising frame configuration
		with the packet type CONNECT_IND. \n
			:return: wsize: float Range: 1.25E-3 to depends on connection event interval
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:WSIZe?')
		return Conversions.str_to_float(response)

	def set_wsize(self, wsize: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:WSIZe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.set_wsize(wsize = 1.0) \n
		Sets the size of the transmit window, regarding to the start point for data event and advertising frame configuration
		with the packet type CONNECT_IND. \n
			:param wsize: float Range: 1.25E-3 to depends on connection event interval
		"""
		param = Conversions.decimal_value_to_str(wsize)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:WSIZe {param}')

	def clone(self) -> 'Pconfiguration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pconfiguration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
