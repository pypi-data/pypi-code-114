from enum import Enum


# noinspection SpellCheckingInspection
class AcDc(Enum):
	"""2 Members, AC ... DC"""
	AC = 0
	DC = 1


# noinspection SpellCheckingInspection
class All(Enum):
	"""2 Members, NONE ... TTSP"""
	NONE = 0
	TTSP = 1


# noinspection SpellCheckingInspection
class AmSourceInt(Enum):
	"""6 Members, LF1 ... NOISe"""
	LF1 = 0
	LF12 = 1
	LF1Noise = 2
	LF2 = 3
	LF2Noise = 4
	NOISe = 5


# noinspection SpellCheckingInspection
class AnalogDigital(Enum):
	"""2 Members, ANALog ... DIGital"""
	ANALog = 0
	DIGital = 1


# noinspection SpellCheckingInspection
class ArbLevMode(Enum):
	"""2 Members, HIGHest ... UNCHanged"""
	HIGHest = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class ArbMultCarrCresMode(Enum):
	"""3 Members, MAX ... OFF"""
	MAX = 0
	MIN = 1
	OFF = 2


# noinspection SpellCheckingInspection
class ArbMultCarrLevRef(Enum):
	"""2 Members, PEAK ... RMS"""
	PEAK = 0
	RMS = 1


# noinspection SpellCheckingInspection
class ArbMultCarrSigDurMod(Enum):
	"""4 Members, LCM ... USER"""
	LCM = 0
	LONG = 1
	SHORt = 2
	USER = 3


# noinspection SpellCheckingInspection
class ArbMultCarrSpacMode(Enum):
	"""2 Members, ARBitrary ... EQUidistant"""
	ARBitrary = 0
	EQUidistant = 1


# noinspection SpellCheckingInspection
class ArbSegmNextSource(Enum):
	"""2 Members, INTernal ... NSEGM1"""
	INTernal = 0
	NSEGM1 = 1


# noinspection SpellCheckingInspection
class ArbSignType(Enum):
	"""4 Members, AWGN ... SINE"""
	AWGN = 0
	CIQ = 1
	RECT = 2
	SINE = 3


# noinspection SpellCheckingInspection
class ArbTrigSegmModeNoEhop(Enum):
	"""4 Members, NEXT ... SEQuencer"""
	NEXT = 0
	NSEam = 1
	SAME = 2
	SEQuencer = 3


# noinspection SpellCheckingInspection
class ArbWaveSegmClocMode(Enum):
	"""3 Members, HIGHest ... USER"""
	HIGHest = 0
	UNCHanged = 1
	USER = 2


# noinspection SpellCheckingInspection
class ArbWaveSegmMarkMode(Enum):
	"""2 Members, IGNore ... TAKE"""
	IGNore = 0
	TAKE = 1


# noinspection SpellCheckingInspection
class ArbWaveSegmPowMode(Enum):
	"""2 Members, ERMS ... UNCHanged"""
	ERMS = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class ArbWaveSegmRest(Enum):
	"""5 Members, MRK1 ... OFF"""
	MRK1 = 0
	MRK2 = 1
	MRK3 = 2
	MRK4 = 3
	OFF = 4


# noinspection SpellCheckingInspection
class Atsc30Coderate(Enum):
	"""12 Members, R10_15 ... R9_15"""
	R10_15 = 0
	R11_15 = 1
	R12_15 = 2
	R13_15 = 3
	R2_15 = 4
	R3_15 = 5
	R4_15 = 6
	R5_15 = 7
	R6_15 = 8
	R7_15 = 9
	R8_15 = 10
	R9_15 = 11


# noinspection SpellCheckingInspection
class Atsc30Constellation(Enum):
	"""6 Members, T1024 ... T64"""
	T1024 = 0
	T16 = 1
	T256 = 2
	T4 = 3
	T4096 = 4
	T64 = 5


# noinspection SpellCheckingInspection
class Atsc30Depth(Enum):
	"""6 Members, D1024 ... D887"""
	D1024 = 0
	D1254 = 1
	D1448 = 2
	D512 = 3
	D724 = 4
	D887 = 5


# noinspection SpellCheckingInspection
class Atsc30EmergencyAlertSignaling(Enum):
	"""4 Members, NOEMergency ... SET3"""
	NOEMergency = 0
	SET1 = 1
	SET2 = 2
	SET3 = 3


# noinspection SpellCheckingInspection
class Atsc30FecType(Enum):
	"""6 Members, B16K ... O64K"""
	B16K = 0
	B64K = 1
	C16K = 2
	C64K = 3
	O16K = 4
	O64K = 5


# noinspection SpellCheckingInspection
class Atsc30FftSize(Enum):
	"""3 Members, M16K ... M8K"""
	M16K = 0
	M32K = 1
	M8K = 2


# noinspection SpellCheckingInspection
class Atsc30FrameInfoBandwidth(Enum):
	"""4 Members, BW_6 ... BW8G"""
	BW_6 = 0
	BW_7 = 1
	BW_8 = 2
	BW8G = 3


# noinspection SpellCheckingInspection
class Atsc30FrameLengthMode(Enum):
	"""2 Members, SYMBol ... TIME"""
	SYMBol = 0
	TIME = 1


# noinspection SpellCheckingInspection
class Atsc30GuardInterval(Enum):
	"""12 Members, G1024 ... G768"""
	G1024 = 0
	G1536 = 1
	G192 = 2
	G2048 = 3
	G2432 = 4
	G3072 = 5
	G3648 = 6
	G384 = 7
	G4096 = 8
	G4864 = 9
	G512 = 10
	G768 = 11


# noinspection SpellCheckingInspection
class Atsc30InputSignalTestSignal(Enum):
	"""2 Members, TIPP ... TTSP"""
	TIPP = 0
	TTSP = 1


# noinspection SpellCheckingInspection
class Atsc30InputType(Enum):
	"""2 Members, IP ... TS"""
	IP = 0
	TS = 1


# noinspection SpellCheckingInspection
class Atsc30L1DetailAdditionalParityMode(Enum):
	"""3 Members, K1 ... OFF"""
	K1 = 0
	K2 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Atsc30Layer(Enum):
	"""2 Members, CORE ... ENHanced"""
	CORE = 0
	ENHanced = 1


# noinspection SpellCheckingInspection
class Atsc30LdmInjectionLayer(Enum):
	"""31 Members, L00 ... L90"""
	L00 = 0
	L05 = 1
	L10 = 2
	L100 = 3
	L110 = 4
	L120 = 5
	L130 = 6
	L140 = 7
	L15 = 8
	L150 = 9
	L160 = 10
	L170 = 11
	L180 = 12
	L190 = 13
	L20 = 14
	L200 = 15
	L210 = 16
	L220 = 17
	L230 = 18
	L240 = 19
	L25 = 20
	L250 = 21
	L30 = 22
	L35 = 23
	L40 = 24
	L45 = 25
	L50 = 26
	L60 = 27
	L70 = 28
	L80 = 29
	L90 = 30


# noinspection SpellCheckingInspection
class Atsc30LowLevelSignaling(Enum):
	"""2 Members, ABSent ... PRESent"""
	ABSent = 0
	PRESent = 1


# noinspection SpellCheckingInspection
class Atsc30MinTimeToNext(Enum):
	"""33 Members, N100 ... NOTapplicable"""
	N100 = 0
	N1000 = 1
	N1100 = 2
	N1200 = 3
	N1400 = 4
	N150 = 5
	N1500 = 6
	N1600 = 7
	N1700 = 8
	N1900 = 9
	N200 = 10
	N2100 = 11
	N2300 = 12
	N250 = 13
	N2500 = 14
	N2700 = 15
	N2900 = 16
	N300 = 17
	N3300 = 18
	N350 = 19
	N3700 = 20
	N400 = 21
	N4100 = 22
	N4500 = 23
	N4900 = 24
	N50 = 25
	N500 = 26
	N5300 = 27
	N600 = 28
	N700 = 29
	N800 = 30
	N900 = 31
	NOTapplicable = 32


# noinspection SpellCheckingInspection
class Atsc30Miso(Enum):
	"""3 Members, C256 ... OFF"""
	C256 = 0
	C64 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Atsc30PilotPattern(Enum):
	"""8 Members, D12 ... D8"""
	D12 = 0
	D16 = 1
	D24 = 2
	D3 = 3
	D32 = 4
	D4 = 5
	D6 = 6
	D8 = 7


# noinspection SpellCheckingInspection
class Atsc30PilotPatternSiso(Enum):
	"""16 Members, SP12_2 ... SP8_4"""
	SP12_2 = 0
	SP12_4 = 1
	SP16_2 = 2
	SP16_4 = 3
	SP24_2 = 4
	SP24_4 = 5
	SP3_2 = 6
	SP3_4 = 7
	SP32_2 = 8
	SP32_4 = 9
	SP4_2 = 10
	SP4_4 = 11
	SP6_2 = 12
	SP6_4 = 13
	SP8_2 = 14
	SP8_4 = 15


# noinspection SpellCheckingInspection
class Atsc30Protocol(Enum):
	"""3 Members, AUTO ... UDP"""
	AUTO = 0
	RTP = 1
	UDP = 2


# noinspection SpellCheckingInspection
class Atsc30TestIppAcket(Enum):
	"""1 Members, HUDP ... HUDP"""
	HUDP = 0


# noinspection SpellCheckingInspection
class Atsc30TimeInfo(Enum):
	"""4 Members, MSEC ... USEC"""
	MSEC = 0
	NSEC = 1
	OFF = 2
	USEC = 3


# noinspection SpellCheckingInspection
class Atsc30TimeInfoL1BasicFecType(Enum):
	"""7 Members, MOD1 ... MOD7"""
	MOD1 = 0
	MOD2 = 1
	MOD3 = 2
	MOD4 = 3
	MOD5 = 4
	MOD6 = 5
	MOD7 = 6


# noinspection SpellCheckingInspection
class Atsc30TimeInterleaverMode(Enum):
	"""3 Members, CTI ... OFF"""
	CTI = 0
	HTI = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Atsc30TxIdInjectionLevel(Enum):
	"""14 Members, L120 ... OFF"""
	L120 = 0
	L150 = 1
	L180 = 2
	L210 = 3
	L240 = 4
	L270 = 5
	L300 = 6
	L330 = 7
	L360 = 8
	L390 = 9
	L420 = 10
	L450 = 11
	L90 = 12
	OFF = 13


# noinspection SpellCheckingInspection
class Atsc30TxIdMode(Enum):
	"""3 Members, AUTo ... OFF"""
	AUTo = 0
	MANual = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Atsc30Type(Enum):
	"""2 Members, DISPersed ... NONDispersed"""
	DISPersed = 0
	NONDispersed = 1


# noinspection SpellCheckingInspection
class AtscmhBuryRatio(Enum):
	"""7 Members, DB21 ... DB39"""
	DB21 = 0
	DB24 = 1
	DB27 = 2
	DB30 = 3
	DB33 = 4
	DB36 = 5
	DB39 = 6


# noinspection SpellCheckingInspection
class AtscmhCodingConstel(Enum):
	"""1 Members, VSB8 ... VSB8"""
	VSB8 = 0


# noinspection SpellCheckingInspection
class AtscmhCodingInputSignalPacketLength(Enum):
	"""3 Members, INValid ... P208"""
	INValid = 0
	P188 = 1
	P208 = 2


# noinspection SpellCheckingInspection
class AtscmhCodingRolloff(Enum):
	"""1 Members, R115 ... R115"""
	R115 = 0


# noinspection SpellCheckingInspection
class AtscmhGeneralVsbFrequency(Enum):
	"""2 Members, CENTer ... PILot"""
	CENTer = 0
	PILot = 1


# noinspection SpellCheckingInspection
class AtscmhInputSignalTestSignal(Enum):
	"""4 Members, PBEM ... TTSP"""
	PBEM = 0
	PBET = 1
	PBIN = 2
	TTSP = 3


# noinspection SpellCheckingInspection
class AudioBcFmDarcInformation(Enum):
	"""3 Members, DATa ... PRBS"""
	DATa = 0
	OFF = 1
	PRBS = 2


# noinspection SpellCheckingInspection
class AudioBcFmInputSignalAfMode(Enum):
	"""5 Members, LEFT ... RNELeft"""
	LEFT = 0
	RELeft = 1
	REMLeft = 2
	RIGHt = 3
	RNELeft = 4


# noinspection SpellCheckingInspection
class AudioBcFmModulationMode(Enum):
	"""2 Members, MONO ... STEReo"""
	MONO = 0
	STEReo = 1


# noinspection SpellCheckingInspection
class AudioBcFmModulationPreemphasis(Enum):
	"""3 Members, D50us ... OFF"""
	D50us = 0
	D75us = 1
	OFF = 2


# noinspection SpellCheckingInspection
class AudioBcInputSignal(Enum):
	"""4 Members, AGENerator ... OFF"""
	AGENerator = 0
	APLayer = 1
	EXTernal = 2
	OFF = 3


# noinspection SpellCheckingInspection
class AutoManStep(Enum):
	"""3 Members, AUTO ... STEP"""
	AUTO = 0
	MANual = 1
	STEP = 2


# noinspection SpellCheckingInspection
class AutoManualMode(Enum):
	"""2 Members, AUTO ... MANual"""
	AUTO = 0
	MANual = 1


# noinspection SpellCheckingInspection
class AutoStep(Enum):
	"""2 Members, AUTO ... STEP"""
	AUTO = 0
	STEP = 1


# noinspection SpellCheckingInspection
class AutoUser(Enum):
	"""2 Members, AUTO ... USER"""
	AUTO = 0
	USER = 1


# noinspection SpellCheckingInspection
class BasebandModShape(Enum):
	"""1 Members, SINE ... SINE"""
	SINE = 0


# noinspection SpellCheckingInspection
class BasebandPulseMode(Enum):
	"""2 Members, DOUBle ... SINGle"""
	DOUBle = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class BasebandPulseTransType(Enum):
	"""2 Members, FAST ... SMOothed"""
	FAST = 0
	SMOothed = 1


# noinspection SpellCheckingInspection
class BbCodMode(Enum):
	"""2 Members, BBIN ... CODer"""
	BBIN = 0
	CODer = 1


# noinspection SpellCheckingInspection
class BbConfig(Enum):
	"""2 Members, NORMal ... PACKet"""
	NORMal = 0
	PACKet = 1


# noinspection SpellCheckingInspection
class BbDigInpBb(Enum):
	"""9 Members, A ... NONE"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	G = 6
	H = 7
	NONE = 8


# noinspection SpellCheckingInspection
class BbDmModType(Enum):
	"""35 Members, APSK16 ... USER"""
	APSK16 = 0
	APSK32 = 1
	AQPSk = 2
	ASK = 3
	BPSK = 4
	FSK16 = 5
	FSK2 = 6
	FSK32 = 7
	FSK4 = 8
	FSK64 = 9
	FSK8 = 10
	FSKVar = 11
	MSK = 12
	OQPSk = 13
	P2DBpsk = 14
	P4DQpsk = 15
	P4QPsk = 16
	P8D8psk = 17
	P8EDge = 18
	PSK8 = 19
	QAM1024 = 20
	QAM128 = 21
	QAM16 = 22
	QAM16EDge = 23
	QAM2048 = 24
	QAM256 = 25
	QAM32 = 26
	QAM32EDge = 27
	QAM4096 = 28
	QAM512 = 29
	QAM64 = 30
	QEDGe = 31
	QPSK = 32
	QPSK45 = 33
	USER = 34


# noinspection SpellCheckingInspection
class BbImpOptMode(Enum):
	"""4 Members, FAST ... UCORrection"""
	FAST = 0
	QHIGh = 1
	QHTable = 2
	UCORrection = 3


# noinspection SpellCheckingInspection
class BbinInterfaceMode(Enum):
	"""2 Members, DIGital ... HSDin"""
	DIGital = 0
	HSDin = 1


# noinspection SpellCheckingInspection
class BbinSampRateModeb(Enum):
	"""2 Members, HSDin ... USER"""
	HSDin = 0
	USER = 1


# noinspection SpellCheckingInspection
class BboutClocSour(Enum):
	"""3 Members, DIN ... USER"""
	DIN = 0
	DOUT = 1
	USER = 2


# noinspection SpellCheckingInspection
class BcInputSignalSource(Enum):
	"""1 Members, SPDif ... SPDif"""
	SPDif = 0


# noinspection SpellCheckingInspection
class BicmFecFrame(Enum):
	"""2 Members, NORMal ... SHORt"""
	NORMal = 0
	SHORt = 1


# noinspection SpellCheckingInspection
class BitOrder(Enum):
	"""2 Members, LSBit ... MSBit"""
	LSBit = 0
	MSBit = 1


# noinspection SpellCheckingInspection
class ByteOrder(Enum):
	"""2 Members, NORMal ... SWAPped"""
	NORMal = 0
	SWAPped = 1


# noinspection SpellCheckingInspection
class CalDataMode(Enum):
	"""2 Members, CUSTomer ... FACTory"""
	CUSTomer = 0
	FACTory = 1


# noinspection SpellCheckingInspection
class CalPowAttMode(Enum):
	"""2 Members, NEW ... OLD"""
	NEW = 0
	OLD = 1


# noinspection SpellCheckingInspection
class CfrAlgo(Enum):
	"""1 Members, CLFiltering ... CLFiltering"""
	CLFiltering = 0


# noinspection SpellCheckingInspection
class CfrFiltMode(Enum):
	"""2 Members, ENHanced ... SIMPle"""
	ENHanced = 0
	SIMPle = 1


# noinspection SpellCheckingInspection
class ClockModeUnits(Enum):
	"""2 Members, MSAMple ... SAMPle"""
	MSAMple = 0
	SAMPle = 1


# noinspection SpellCheckingInspection
class ClockSourceB(Enum):
	"""3 Members, AINTernal ... INTernal"""
	AINTernal = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class ClocOutpMode(Enum):
	"""2 Members, BIT ... SYMBol"""
	BIT = 0
	SYMBol = 1


# noinspection SpellCheckingInspection
class ClocSourBb(Enum):
	"""4 Members, AINTernal ... INTernal"""
	AINTernal = 0
	COUPled = 1
	EXTernal = 2
	INTernal = 3


# noinspection SpellCheckingInspection
class CodingChannelBandwidth(Enum):
	"""3 Members, BW_6 ... BW_8"""
	BW_6 = 0
	BW_7 = 1
	BW_8 = 2


# noinspection SpellCheckingInspection
class CodingCoderate(Enum):
	"""5 Members, R1_2 ... R7_8"""
	R1_2 = 0
	R2_3 = 1
	R3_4 = 2
	R5_6 = 3
	R7_8 = 4


# noinspection SpellCheckingInspection
class CodingGuardInterval(Enum):
	"""4 Members, G1_16 ... G1_8"""
	G1_16 = 0
	G1_32 = 1
	G1_4 = 2
	G1_8 = 3


# noinspection SpellCheckingInspection
class CodingInputFormat(Enum):
	"""2 Members, ASI ... SMPTE"""
	ASI = 0
	SMPTE = 1


# noinspection SpellCheckingInspection
class CodingInputSignalInputA(Enum):
	"""8 Members, ASI1 ... TS2"""
	ASI1 = 0
	ASI2 = 1
	IP = 2
	SMP1 = 3
	SMP2 = 4
	TS = 5
	TS1 = 6
	TS2 = 7


# noinspection SpellCheckingInspection
class CodingInputSignalInputAsi(Enum):
	"""4 Members, ASI1 ... ASIRear"""
	ASI1 = 0
	ASI2 = 1
	ASIFront = 2
	ASIRear = 3


# noinspection SpellCheckingInspection
class CodingInputSignalInputB(Enum):
	"""6 Members, ASIFront ... TS"""
	ASIFront = 0
	ASIRear = 1
	IP = 2
	SPIFront = 3
	SPIRear = 4
	TS = 5


# noinspection SpellCheckingInspection
class CodingInputSignalInputSfe(Enum):
	"""8 Members, ASI1 ... SMPRear"""
	ASI1 = 0
	ASI2 = 1
	ASIFront = 2
	ASIRear = 3
	SMP1 = 4
	SMP2 = 5
	SMPFront = 6
	SMPRear = 7


# noinspection SpellCheckingInspection
class CodingInputSignalPacketLength(Enum):
	"""2 Members, INValid ... P188"""
	INValid = 0
	P188 = 1


# noinspection SpellCheckingInspection
class CodingInputSignalSource(Enum):
	"""3 Members, EXTernal ... TSPLayer"""
	EXTernal = 0
	TESTsignal = 1
	TSPLayer = 2


# noinspection SpellCheckingInspection
class CodingInputSignalTestSignal(Enum):
	"""1 Members, TTSP ... TTSP"""
	TTSP = 0


# noinspection SpellCheckingInspection
class CodingIpType(Enum):
	"""2 Members, MULTicast ... UNIcast"""
	MULTicast = 0
	UNIcast = 1


# noinspection SpellCheckingInspection
class CodingIsdbtCodingConstel(Enum):
	"""4 Members, C_16QAM ... C_QPSK"""
	C_16QAM = 0
	C_64QAM = 1
	C_DQPSK = 2
	C_QPSK = 3


# noinspection SpellCheckingInspection
class CodingIsdbtMode(Enum):
	"""3 Members, M1_2K ... M3_8K"""
	M1_2K = 0
	M2_4K = 1
	M3_8K = 2


# noinspection SpellCheckingInspection
class CodingPacketLength(Enum):
	"""4 Members, INV ... P208"""
	INV = 0
	P188 = 1
	P204 = 2
	P208 = 3


# noinspection SpellCheckingInspection
class CodingPortions(Enum):
	"""7 Members, CCC ... PDD"""
	CCC = 0
	DCC = 1
	DDC = 2
	DDD = 3
	PCC = 4
	PDC = 5
	PDD = 6


# noinspection SpellCheckingInspection
class CodingTimeInterleaving(Enum):
	"""7 Members, _0 ... _8"""
	_0 = 0
	_1 = 1
	_16 = 2
	_2 = 3
	_32 = 4
	_4 = 5
	_8 = 6


# noinspection SpellCheckingInspection
class Colour(Enum):
	"""4 Members, GREen ... YELLow"""
	GREen = 0
	NONE = 1
	RED = 2
	YELLow = 3


# noinspection SpellCheckingInspection
class ConnDirection(Enum):
	"""3 Members, INPut ... UNUSed"""
	INPut = 0
	OUTPut = 1
	UNUSed = 2


# noinspection SpellCheckingInspection
class Count(Enum):
	"""2 Members, _1 ... _2"""
	_1 = 0
	_2 = 1


# noinspection SpellCheckingInspection
class DabDataSour(Enum):
	"""5 Members, ALL0 ... PN23"""
	ALL0 = 0
	ALL1 = 1
	ETI = 2
	PN15 = 3
	PN23 = 4


# noinspection SpellCheckingInspection
class DabTxMode(Enum):
	"""4 Members, I ... IV"""
	I = 0
	II = 1
	III = 2
	IV = 3


# noinspection SpellCheckingInspection
class DetAtt(Enum):
	"""5 Members, HIGH ... OVR"""
	HIGH = 0
	LOW = 1
	MED = 2
	OFF = 3
	OVR = 4


# noinspection SpellCheckingInspection
class DevExpFormat(Enum):
	"""4 Members, CGPRedefined ... XML"""
	CGPRedefined = 0
	CGUSer = 1
	SCPI = 2
	XML = 3


# noinspection SpellCheckingInspection
class DexchExtension(Enum):
	"""2 Members, CSV ... TXT"""
	CSV = 0
	TXT = 1


# noinspection SpellCheckingInspection
class DexchMode(Enum):
	"""2 Members, EXPort ... IMPort"""
	EXPort = 0
	IMPort = 1


# noinspection SpellCheckingInspection
class DexchSepCol(Enum):
	"""4 Members, COMMa ... TABulator"""
	COMMa = 0
	SEMicolon = 1
	SPACe = 2
	TABulator = 3


# noinspection SpellCheckingInspection
class DexchSepDec(Enum):
	"""2 Members, COMMa ... DOT"""
	COMMa = 0
	DOT = 1


# noinspection SpellCheckingInspection
class DispKeybLockMode(Enum):
	"""5 Members, DISabled ... VNConly"""
	DISabled = 0
	DONLy = 1
	ENABled = 2
	TOFF = 3
	VNConly = 4


# noinspection SpellCheckingInspection
class DmApskGamma(Enum):
	"""6 Members, G2D3 ... G9D10"""
	G2D3 = 0
	G3D4 = 1
	G4D5 = 2
	G5D6 = 3
	G8D9 = 4
	G9D10 = 5


# noinspection SpellCheckingInspection
class DmApskGamma1(Enum):
	"""5 Members, G3D4 ... G9D10"""
	G3D4 = 0
	G4D5 = 1
	G5D6 = 2
	G8D9 = 3
	G9D10 = 4


# noinspection SpellCheckingInspection
class DmClocMode(Enum):
	"""3 Members, BIT ... SYMBol"""
	BIT = 0
	MSYMbol = 1
	SYMBol = 2


# noinspection SpellCheckingInspection
class DmCod(Enum):
	"""21 Members, APCO25 ... WCDMA"""
	APCO25 = 0
	APCO258PSK = 1
	APCO25FSK = 2
	CDMA2000 = 3
	DGRay = 4
	DIFF = 5
	DPHS = 6
	EDGE = 7
	GRAY = 8
	GSM = 9
	ICO = 10
	INMarsat = 11
	NADC = 12
	OFF = 13
	PDC = 14
	PHS = 15
	PWT = 16
	TETRa = 17
	TFTS = 18
	VDL = 19
	WCDMA = 20


# noinspection SpellCheckingInspection
class DmDataPrbs(Enum):
	"""14 Members, _11 ... PN9"""
	_11 = 0
	_15 = 1
	_16 = 2
	_20 = 3
	_21 = 4
	_23 = 5
	_9 = 6
	PN11 = 7
	PN15 = 8
	PN16 = 9
	PN20 = 10
	PN21 = 11
	PN23 = 12
	PN9 = 13


# noinspection SpellCheckingInspection
class DmDataSourV(Enum):
	"""5 Members, DLISt ... ZERO"""
	DLISt = 0
	ONE = 1
	PATTern = 2
	PRBS = 3
	ZERO = 4


# noinspection SpellCheckingInspection
class DmExtRcvStateType(Enum):
	"""5 Members, INValid ... UFLow"""
	INValid = 0
	OFF = 1
	OFLow = 2
	OPERational = 3
	UFLow = 4


# noinspection SpellCheckingInspection
class DmFilter(Enum):
	"""23 Members, APCO25 ... USER"""
	APCO25 = 0
	APCO25Hcpm = 1
	APCO25Lsm = 2
	C2K3x = 3
	COEQualizer = 4
	COF705 = 5
	COFequalizer = 6
	CONE = 7
	COSine = 8
	DIRac = 9
	ENPShape = 10
	EWPShape = 11
	GAUSs = 12
	HRP = 13
	LGAuss = 14
	LPASs = 15
	LPASSEVM = 16
	LTEFilter = 17
	PGAuss = 18
	RCOSine = 19
	RECTangle = 20
	SPHase = 21
	USER = 22


# noinspection SpellCheckingInspection
class DmFilterA(Enum):
	"""18 Members, APCO25 ... SPHase"""
	APCO25 = 0
	C2K3x = 1
	COEQualizer = 2
	COF705 = 3
	COFequalizer = 4
	CONE = 5
	COSine = 6
	DIRac = 7
	ENPShape = 8
	EWPShape = 9
	GAUSs = 10
	LGAuss = 11
	LPASs = 12
	LPASSEVM = 13
	PGAuss = 14
	RCOSine = 15
	RECTangle = 16
	SPHase = 17


# noinspection SpellCheckingInspection
class DmFskModType(Enum):
	"""3 Members, FSK16 ... FSK8"""
	FSK16 = 0
	FSK4 = 1
	FSK8 = 2


# noinspection SpellCheckingInspection
class DmMarkMode(Enum):
	"""5 Members, CLISt ... TRIGger"""
	CLISt = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	TRIGger = 4


# noinspection SpellCheckingInspection
class DmStan(Enum):
	"""25 Members, APCOPH1C4fm ... WORLdspace"""
	APCOPH1C4fm = 0
	APCOPH1CQpsk = 1
	APCOPH1Lsm = 2
	APCOPH1Wcqpsk = 3
	APCOPH2HCpm = 4
	APCOPH2HD8PSKN = 5
	APCOPH2HD8PSKW = 6
	APCOPH2HDQpsk = 7
	BLUetooth = 8
	CFORward = 9
	CREVerse = 10
	CWBPsk = 11
	DECT = 12
	ETC = 13
	GSM = 14
	GSMEdge = 15
	NADC = 16
	PDC = 17
	PHS = 18
	TDSCdma = 19
	TETRa = 20
	TFTS = 21
	USER = 22
	W3GPp = 23
	WORLdspace = 24


# noinspection SpellCheckingInspection
class DmTrigMode(Enum):
	"""5 Members, AAUTo ... SINGle"""
	AAUTo = 0
	ARETrigger = 1
	AUTO = 2
	RETRigger = 3
	SINGle = 4


# noinspection SpellCheckingInspection
class DrmCodingChannelBw(Enum):
	"""8 Members, INV ... K20"""
	INV = 0
	K045 = 1
	K05 = 2
	K09 = 3
	K10 = 4
	K100 = 5
	K18 = 6
	K20 = 7


# noinspection SpellCheckingInspection
class DrmCodingCoderate(Enum):
	"""17 Members, INV ... R078"""
	INV = 0
	R025 = 1
	R033 = 2
	R040 = 3
	R041 = 4
	R045 = 5
	R048 = 6
	R050 = 7
	R055 = 8
	R057 = 9
	R058 = 10
	R060 = 11
	R062 = 12
	R066 = 13
	R071 = 14
	R072 = 15
	R078 = 16


# noinspection SpellCheckingInspection
class DrmCodingConstelMsc(Enum):
	"""6 Members, INV ... Q64Q"""
	INV = 0
	Q16 = 1
	Q4 = 2
	Q64I = 3
	Q64N = 4
	Q64Q = 5


# noinspection SpellCheckingInspection
class DrmCodingConstelSdc(Enum):
	"""3 Members, INV ... Q4"""
	INV = 0
	Q16 = 1
	Q4 = 2


# noinspection SpellCheckingInspection
class DrmCodingInterleaver(Enum):
	"""4 Members, INV ... S2"""
	INV = 0
	MS4 = 1
	MS6 = 2
	S2 = 3


# noinspection SpellCheckingInspection
class DrmCodingProtectionLevelMsc(Enum):
	"""5 Members, _0 ... INV"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	INV = 4


# noinspection SpellCheckingInspection
class DrmCodingProtectionLevelSdc(Enum):
	"""3 Members, _0 ... INV"""
	_0 = 0
	_1 = 1
	INV = 2


# noinspection SpellCheckingInspection
class DrmCodingProtectionProfileMsc(Enum):
	"""4 Members, HPP ... VSPP"""
	HPP = 0
	INV = 1
	LPP = 2
	VSPP = 3


# noinspection SpellCheckingInspection
class DrmCodingProtectionProfileSdc(Enum):
	"""2 Members, EEP ... INV"""
	EEP = 0
	INV = 1


# noinspection SpellCheckingInspection
class DrmCodingRobustness(Enum):
	"""6 Members, A ... INV"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	INV = 5


# noinspection SpellCheckingInspection
class DrmInputSignalLayerType(Enum):
	"""3 Members, BASE ... INV"""
	BASE = 0
	ENHancement = 1
	INV = 2


# noinspection SpellCheckingInspection
class DrmInputSignalServices(Enum):
	"""6 Members, _0 ... INV"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	_4 = 4
	INV = 5


# noinspection SpellCheckingInspection
class DrmInputSignalSource(Enum):
	"""2 Members, EXTernal ... FILE"""
	EXTernal = 0
	FILE = 1


# noinspection SpellCheckingInspection
class DtmbCodingCoderate(Enum):
	"""3 Members, R04 ... R08"""
	R04 = 0
	R06 = 1
	R08 = 2


# noinspection SpellCheckingInspection
class DtmbCodingConstel(Enum):
	"""5 Members, D16 ... D64"""
	D16 = 0
	D32 = 1
	D4 = 2
	D4NR = 3
	D64 = 4


# noinspection SpellCheckingInspection
class DtmbCodingGipN(Enum):
	"""2 Members, CONSt ... VAR"""
	CONSt = 0
	VAR = 1


# noinspection SpellCheckingInspection
class DtmbCodingGuardInterval(Enum):
	"""3 Members, G420 ... G945"""
	G420 = 0
	G595 = 1
	G945 = 2


# noinspection SpellCheckingInspection
class DtmbCodingInputSignalPacketLength(Enum):
	"""2 Members, INV ... P188"""
	INV = 0
	P188 = 1


# noinspection SpellCheckingInspection
class DtmbCodingTimeInterleaver(Enum):
	"""3 Members, I240 ... OFF"""
	I240 = 0
	I720 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class DvbcCodingDvbcCodingConstel(Enum):
	"""5 Members, C128 ... C64"""
	C128 = 0
	C16 = 1
	C256 = 2
	C32 = 3
	C64 = 4


# noinspection SpellCheckingInspection
class DvbcCodingDvbcCodingRolloff(Enum):
	"""2 Members, _0_dot_13 ... _0_dot_15"""
	_0_dot_13 = 0
	_0_dot_15 = 1


# noinspection SpellCheckingInspection
class DvbcCodingDvbcInputSignalTestSignal(Enum):
	"""3 Members, PBDE ... TTSP"""
	PBDE = 0
	PBEM = 1
	TTSP = 2


# noinspection SpellCheckingInspection
class Dvbs2CodingCoderateSfe(Enum):
	"""12 Members, R1_2 ... UNDef"""
	R1_2 = 0
	R1_3 = 1
	R1_4 = 2
	R2_3 = 3
	R2_5 = 4
	R3_4 = 5
	R3_5 = 6
	R4_5 = 7
	R5_6 = 8
	R8_9 = 9
	R9_10 = 10
	UNDef = 11


# noinspection SpellCheckingInspection
class Dvbs2CodingConstelSfe(Enum):
	"""5 Members, A16 ... UNDef"""
	A16 = 0
	A32 = 1
	S4 = 2
	S8 = 3
	UNDef = 4


# noinspection SpellCheckingInspection
class Dvbs2CodingFecFrame(Enum):
	"""3 Members, MEDium ... SHORt"""
	MEDium = 0
	NORMal = 1
	SHORt = 2


# noinspection SpellCheckingInspection
class Dvbs2CodingModCod(Enum):
	"""107 Members, _0 ... _99"""
	_0 = 0
	_1 = 1
	_10 = 2
	_100 = 3
	_101 = 4
	_102 = 5
	_103 = 6
	_104 = 7
	_105 = 8
	_106 = 9
	_11 = 10
	_12 = 11
	_13 = 12
	_14 = 13
	_15 = 14
	_16 = 15
	_17 = 16
	_18 = 17
	_19 = 18
	_2 = 19
	_20 = 20
	_21 = 21
	_22 = 22
	_23 = 23
	_24 = 24
	_25 = 25
	_26 = 26
	_27 = 27
	_28 = 28
	_29 = 29
	_3 = 30
	_30 = 31
	_31 = 32
	_32 = 33
	_33 = 34
	_34 = 35
	_35 = 36
	_36 = 37
	_37 = 38
	_38 = 39
	_39 = 40
	_4 = 41
	_40 = 42
	_41 = 43
	_42 = 44
	_43 = 45
	_44 = 46
	_45 = 47
	_46 = 48
	_47 = 49
	_48 = 50
	_49 = 51
	_5 = 52
	_50 = 53
	_51 = 54
	_52 = 55
	_53 = 56
	_54 = 57
	_55 = 58
	_56 = 59
	_57 = 60
	_58 = 61
	_59 = 62
	_6 = 63
	_60 = 64
	_61 = 65
	_62 = 66
	_63 = 67
	_64 = 68
	_65 = 69
	_66 = 70
	_67 = 71
	_68 = 72
	_69 = 73
	_7 = 74
	_70 = 75
	_71 = 76
	_72 = 77
	_73 = 78
	_74 = 79
	_75 = 80
	_76 = 81
	_77 = 82
	_78 = 83
	_79 = 84
	_8 = 85
	_80 = 86
	_81 = 87
	_82 = 88
	_83 = 89
	_84 = 90
	_85 = 91
	_86 = 92
	_87 = 93
	_88 = 94
	_89 = 95
	_9 = 96
	_90 = 97
	_91 = 98
	_92 = 99
	_93 = 100
	_94 = 101
	_95 = 102
	_96 = 103
	_97 = 104
	_98 = 105
	_99 = 106


# noinspection SpellCheckingInspection
class Dvbs2CodingRolloff(Enum):
	"""6 Members, _0_dot_05 ... _0_dot_35"""
	_0_dot_05 = 0
	_0_dot_10 = 1
	_0_dot_15 = 2
	_0_dot_20 = 3
	_0_dot_25 = 4
	_0_dot_35 = 5


# noinspection SpellCheckingInspection
class Dvbs2InputSignalCmMode(Enum):
	"""3 Members, ACM ... VCM"""
	ACM = 0
	CCM = 1
	VCM = 2


# noinspection SpellCheckingInspection
class DvbsCodingDvbsCodingCoderate(Enum):
	"""6 Members, R1_2 ... R8_9"""
	R1_2 = 0
	R2_3 = 1
	R3_4 = 2
	R5_6 = 3
	R7_8 = 4
	R8_9 = 5


# noinspection SpellCheckingInspection
class DvbsCodingDvbsCodingConstel(Enum):
	"""3 Members, S16 ... S8"""
	S16 = 0
	S4 = 1
	S8 = 2


# noinspection SpellCheckingInspection
class DvbsCodingDvbsCodingRolloff(Enum):
	"""3 Members, _0_dot_20 ... _0_dot_35"""
	_0_dot_20 = 0
	_0_dot_25 = 1
	_0_dot_35 = 2


# noinspection SpellCheckingInspection
class DvbsCodingDvbsInputSignalTestSignal(Enum):
	"""2 Members, PBEC ... TTSP"""
	PBEC = 0
	TTSP = 1


# noinspection SpellCheckingInspection
class Dvbt2BicmCoderate(Enum):
	"""8 Members, R1_2 ... R5_6"""
	R1_2 = 0
	R1_3 = 1
	R2_3 = 2
	R2_5 = 3
	R3_4 = 4
	R3_5 = 5
	R4_5 = 6
	R5_6 = 7


# noinspection SpellCheckingInspection
class Dvbt2BicmConstel(Enum):
	"""4 Members, T16 ... T64"""
	T16 = 0
	T256 = 1
	T4 = 2
	T64 = 3


# noinspection SpellCheckingInspection
class Dvbt2FramingChannelBandwidth(Enum):
	"""5 Members, BW_2 ... BW_8"""
	BW_2 = 0
	BW_5 = 1
	BW_6 = 2
	BW_7 = 3
	BW_8 = 4


# noinspection SpellCheckingInspection
class Dvbt2FramingFftSize(Enum):
	"""9 Members, M16E ... M8K"""
	M16E = 0
	M16K = 1
	M1K = 2
	M2K = 3
	M32E = 4
	M32K = 5
	M4K = 6
	M8E = 7
	M8K = 8


# noinspection SpellCheckingInspection
class Dvbt2FramingGuardInterval(Enum):
	"""7 Members, G1_16 ... G19256"""
	G1_16 = 0
	G1_32 = 1
	G1_4 = 2
	G1_8 = 3
	G1128 = 4
	G19128 = 5
	G19256 = 6


# noinspection SpellCheckingInspection
class Dvbt2FramingPilotPattern(Enum):
	"""8 Members, PP1 ... PP8"""
	PP1 = 0
	PP2 = 1
	PP3 = 2
	PP4 = 3
	PP5 = 4
	PP6 = 5
	PP7 = 6
	PP8 = 7


# noinspection SpellCheckingInspection
class Dvbt2InputIssy(Enum):
	"""3 Members, LONG ... SHORt"""
	LONG = 0
	OFF = 1
	SHORt = 2


# noinspection SpellCheckingInspection
class Dvbt2InputSignalCm(Enum):
	"""2 Members, ACM ... CCM"""
	ACM = 0
	CCM = 1


# noinspection SpellCheckingInspection
class Dvbt2InputSignalMeasurementMode(Enum):
	"""2 Members, ABSOLUTE ... DELTA"""
	ABSOLUTE = 0
	DELTA = 1


# noinspection SpellCheckingInspection
class Dvbt2ModeStreamAdapterPlpType(Enum):
	"""3 Members, COMMon ... DT2"""
	COMMon = 0
	DT1 = 1
	DT2 = 2


# noinspection SpellCheckingInspection
class Dvbt2PlpInputFormat(Enum):
	"""4 Members, GCS ... TS"""
	GCS = 0
	GFPS = 1
	GSE = 2
	TS = 3


# noinspection SpellCheckingInspection
class Dvbt2T2SystemFefPayload(Enum):
	"""2 Members, NOISe ... NULL"""
	NOISe = 0
	NULL = 1


# noinspection SpellCheckingInspection
class Dvbt2T2SystemL1PostModulation(Enum):
	"""4 Members, T16 ... T64"""
	T16 = 0
	T2 = 1
	T4 = 2
	T64 = 3


# noinspection SpellCheckingInspection
class Dvbt2T2SystemL1T2Version(Enum):
	"""3 Members, V111 ... V131"""
	V111 = 0
	V121 = 1
	V131 = 2


# noinspection SpellCheckingInspection
class Dvbt2T2SystemMisoGroupScpi(Enum):
	"""2 Members, G1 ... G2"""
	G1 = 0
	G2 = 1


# noinspection SpellCheckingInspection
class Dvbt2T2SystemProfileMode(Enum):
	"""2 Members, MULTI ... SINGLE"""
	MULTI = 0
	SINGLE = 1


# noinspection SpellCheckingInspection
class Dvbt2Transmission(Enum):
	"""5 Members, MISO ... T2LS"""
	MISO = 0
	NONT2 = 1
	SISO = 2
	T2LM = 3
	T2LS = 4


# noinspection SpellCheckingInspection
class DvbtCodingChannelBandwidth(Enum):
	"""5 Members, BW_5 ... BW_Var"""
	BW_5 = 0
	BW_6 = 1
	BW_7 = 2
	BW_8 = 3
	BW_Var = 4


# noinspection SpellCheckingInspection
class DvbtCodingConstel(Enum):
	"""3 Members, T16 ... T64"""
	T16 = 0
	T4 = 1
	T64 = 2


# noinspection SpellCheckingInspection
class DvbtCodingDvbhSymbolInterleaver(Enum):
	"""2 Members, INDepth ... NATive"""
	INDepth = 0
	NATive = 1


# noinspection SpellCheckingInspection
class DvbtCodingFftMode(Enum):
	"""3 Members, M2K ... M8K"""
	M2K = 0
	M4K = 1
	M8K = 2


# noinspection SpellCheckingInspection
class DvbtCodingGuardInterval(Enum):
	"""5 Members, G1 ... G1_8"""
	G1 = 0
	G1_16 = 1
	G1_32 = 2
	G1_4 = 3
	G1_8 = 4


# noinspection SpellCheckingInspection
class DvbtCodingHierarchy(Enum):
	"""4 Members, A1 ... NONHier"""
	A1 = 0
	A2 = 1
	A4 = 2
	NONHier = 3


# noinspection SpellCheckingInspection
class DvbxCodingInputSignalPacketLength(Enum):
	"""3 Members, INValid ... P204"""
	INValid = 0
	P188 = 1
	P204 = 2


# noinspection SpellCheckingInspection
class EnetworkMode(Enum):
	"""2 Members, MFN ... SFN"""
	MFN = 0
	SFN = 1


# noinspection SpellCheckingInspection
class ErFpowSensMapping(Enum):
	"""9 Members, SENS1 ... UNMapped"""
	SENS1 = 0
	SENS2 = 1
	SENS3 = 2
	SENS4 = 3
	SENSor1 = 4
	SENSor2 = 5
	SENSor3 = 6
	SENSor4 = 7
	UNMapped = 8


# noinspection SpellCheckingInspection
class FilterWidth(Enum):
	"""2 Members, NARRow ... WIDE"""
	NARRow = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class FormData(Enum):
	"""2 Members, ASCii ... PACKed"""
	ASCii = 0
	PACKed = 1


# noinspection SpellCheckingInspection
class FormStatReg(Enum):
	"""4 Members, ASCii ... OCTal"""
	ASCii = 0
	BINary = 1
	HEXadecimal = 2
	OCTal = 3


# noinspection SpellCheckingInspection
class FreqMode(Enum):
	"""5 Members, COMBined ... SWEep"""
	COMBined = 0
	CW = 1
	FIXed = 2
	LIST = 3
	SWEep = 4


# noinspection SpellCheckingInspection
class FreqStepMode(Enum):
	"""2 Members, DECimal ... USER"""
	DECimal = 0
	USER = 1


# noinspection SpellCheckingInspection
class GsmRampFunc(Enum):
	"""2 Members, COSine ... LINear"""
	COSine = 0
	LINear = 1


# noinspection SpellCheckingInspection
class HardCopyImageFormat(Enum):
	"""4 Members, BMP ... XPM"""
	BMP = 0
	JPG = 1
	PNG = 2
	XPM = 3


# noinspection SpellCheckingInspection
class HardCopyRegion(Enum):
	"""2 Members, ALL ... DIALog"""
	ALL = 0
	DIALog = 1


# noinspection SpellCheckingInspection
class IecTermMode(Enum):
	"""2 Members, EOI ... STANdard"""
	EOI = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class ImpG50G1KcoerceG10K(Enum):
	"""2 Members, G1K ... G50"""
	G1K = 0
	G50 = 1


# noinspection SpellCheckingInspection
class InclExcl(Enum):
	"""2 Members, EXCLude ... INCLude"""
	EXCLude = 0
	INCLude = 1


# noinspection SpellCheckingInspection
class InpOutpConnGlbMapSignb(Enum):
	"""10 Members, CLOCK1 ... TS"""
	CLOCK1 = 0
	ETI = 1
	INSTtrigger = 2
	MARKA1 = 3
	NONE = 4
	NSEGM1 = 5
	PPS = 6
	SDIF = 7
	TRIG1 = 8
	TS = 9


# noinspection SpellCheckingInspection
class InputImpRf(Enum):
	"""3 Members, G10K ... G50"""
	G10K = 0
	G1K = 1
	G50 = 2


# noinspection SpellCheckingInspection
class InputSignalPacketLength(Enum):
	"""4 Members, INValid ... P208"""
	INValid = 0
	P188 = 1
	P204 = 2
	P208 = 3


# noinspection SpellCheckingInspection
class InputSignalTestSignal(Enum):
	"""3 Members, PAFC ... TTSP"""
	PAFC = 0
	PBEC = 1
	TTSP = 2


# noinspection SpellCheckingInspection
class IqGain(Enum):
	"""7 Members, DB0 ... DBM4"""
	DB0 = 0
	DB2 = 1
	DB4 = 2
	DB6 = 3
	DB8 = 4
	DBM2 = 5
	DBM4 = 6


# noinspection SpellCheckingInspection
class IqMode(Enum):
	"""2 Members, ANALog ... BASeband"""
	ANALog = 0
	BASeband = 1


# noinspection SpellCheckingInspection
class IqOutDispViaType(Enum):
	"""2 Members, LEVel ... PEP"""
	LEVel = 0
	PEP = 1


# noinspection SpellCheckingInspection
class IqOutMode(Enum):
	"""3 Members, FIXed ... VATTenuated"""
	FIXed = 0
	VARiable = 1
	VATTenuated = 2


# noinspection SpellCheckingInspection
class IsdbtCodingSystem(Enum):
	"""3 Members, T ... TSB3"""
	T = 0
	TSB1 = 1
	TSB3 = 2


# noinspection SpellCheckingInspection
class IsdbtEewInfoType(Enum):
	"""2 Members, CANCeled ... ISSued"""
	CANCeled = 0
	ISSued = 1


# noinspection SpellCheckingInspection
class IsdbtEewSignalType(Enum):
	"""4 Members, TWA ... WWOA"""
	TWA = 0
	TWOA = 1
	WWA = 2
	WWOA = 3


# noinspection SpellCheckingInspection
class IsdbtSpecialTmcc(Enum):
	"""2 Members, CURRent ... UNUSed"""
	CURRent = 0
	UNUSed = 1


# noinspection SpellCheckingInspection
class IsdbtSpecialTxParam(Enum):
	"""15 Members, N1 ... NORMal"""
	N1 = 0
	N10 = 1
	N11 = 2
	N12 = 3
	N13 = 4
	N14 = 5
	N15 = 6
	N2 = 7
	N4 = 8
	N5 = 9
	N6 = 10
	N7 = 11
	N8 = 12
	N9 = 13
	NORMal = 14


# noinspection SpellCheckingInspection
class J83BcodingJ83BcodingConstel(Enum):
	"""3 Members, J1024 ... J64"""
	J1024 = 0
	J256 = 1
	J64 = 2


# noinspection SpellCheckingInspection
class J83BcodingJ83BcodingRolloff(Enum):
	"""2 Members, _0_dot_12 ... _0_dot_18"""
	_0_dot_12 = 0
	_0_dot_18 = 1


# noinspection SpellCheckingInspection
class J83BcodingJ83BinputSignalTestSignal(Enum):
	"""3 Members, PBEM ... TTSP"""
	PBEM = 0
	PBTR = 1
	TTSP = 2


# noinspection SpellCheckingInspection
class KbLayout(Enum):
	"""20 Members, CHINese ... SWEDish"""
	CHINese = 0
	DANish = 1
	DUTBe = 2
	DUTCh = 3
	ENGLish = 4
	ENGUK = 5
	ENGUS = 6
	FINNish = 7
	FREBe = 8
	FRECa = 9
	FRENch = 10
	GERMan = 11
	ITALian = 12
	JAPanese = 13
	KORean = 14
	NORWegian = 15
	PORTuguese = 16
	RUSSian = 17
	SPANish = 18
	SWEDish = 19


# noinspection SpellCheckingInspection
class LfFreqMode(Enum):
	"""3 Members, CW ... SWEep"""
	CW = 0
	FIXed = 1
	SWEep = 2


# noinspection SpellCheckingInspection
class LmodRunMode(Enum):
	"""2 Members, LEARned ... LIVE"""
	LEARned = 0
	LIVE = 1


# noinspection SpellCheckingInspection
class LoRaBw(Enum):
	"""10 Members, BW10 ... BW7"""
	BW10 = 0
	BW125 = 1
	BW15 = 2
	BW20 = 3
	BW250 = 4
	BW31 = 5
	BW41 = 6
	BW500 = 7
	BW62 = 8
	BW7 = 9


# noinspection SpellCheckingInspection
class LoRaCodRate(Enum):
	"""5 Members, CR0 ... CR4"""
	CR0 = 0
	CR1 = 1
	CR2 = 2
	CR3 = 3
	CR4 = 4


# noinspection SpellCheckingInspection
class LoRaFreqDfTp(Enum):
	"""2 Members, LINear ... SINE"""
	LINear = 0
	SINE = 1


# noinspection SpellCheckingInspection
class LoRaSf(Enum):
	"""7 Members, SF10 ... SF9"""
	SF10 = 0
	SF11 = 1
	SF12 = 2
	SF6 = 3
	SF7 = 4
	SF8 = 5
	SF9 = 6


# noinspection SpellCheckingInspection
class LoRaSyncMode(Enum):
	"""2 Members, PRIVate ... PUBLic"""
	PRIVate = 0
	PUBLic = 1


# noinspection SpellCheckingInspection
class MappingType(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MarkModeA(Enum):
	"""6 Members, FRAMe ... TRIGger"""
	FRAMe = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	RESTart = 4
	TRIGger = 5


# noinspection SpellCheckingInspection
class MccwCrestFactMode(Enum):
	"""3 Members, CHIRp ... SLOW"""
	CHIRp = 0
	OFF = 1
	SLOW = 2


# noinspection SpellCheckingInspection
class MultInstMsMode(Enum):
	"""2 Members, PRIMary ... SECondary"""
	PRIMary = 0
	SECondary = 1


# noinspection SpellCheckingInspection
class MultInstSyncState(Enum):
	"""2 Members, NOSYnc ... SYNC"""
	NOSYnc = 0
	SYNC = 1


# noinspection SpellCheckingInspection
class NetMode(Enum):
	"""2 Members, AUTO ... STATic"""
	AUTO = 0
	STATic = 1


# noinspection SpellCheckingInspection
class NetProtocol(Enum):
	"""2 Members, TCP ... UDP"""
	TCP = 0
	UDP = 1


# noinspection SpellCheckingInspection
class NetworkMode(Enum):
	"""1 Members, MFN ... MFN"""
	MFN = 0


# noinspection SpellCheckingInspection
class NoisAwgnDispMode(Enum):
	"""2 Members, IQOUT1 ... RFA"""
	IQOUT1 = 0
	RFA = 1


# noinspection SpellCheckingInspection
class NoisAwgnFseState(Enum):
	"""3 Members, ADD ... ONLY"""
	ADD = 0
	OFF = 1
	ONLY = 2


# noinspection SpellCheckingInspection
class NoisAwgnMode(Enum):
	"""3 Members, ADD ... ONLY"""
	ADD = 0
	CW = 1
	ONLY = 2


# noinspection SpellCheckingInspection
class NoisAwgnPowMode(Enum):
	"""3 Members, CN ... SN"""
	CN = 0
	EN = 1
	SN = 2


# noinspection SpellCheckingInspection
class NoisAwgnPowRefMode(Enum):
	"""2 Members, CARRier ... NOISe"""
	CARRier = 0
	NOISe = 1


# noinspection SpellCheckingInspection
class NormalInverted(Enum):
	"""2 Members, INVerted ... NORMal"""
	INVerted = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class NumberA(Enum):
	"""4 Members, _1 ... _4"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3


# noinspection SpellCheckingInspection
class OutpConnGlbSignalb(Enum):
	"""2 Members, MARKA1 ... NONE"""
	MARKA1 = 0
	NONE = 1


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class PathUniCodBbin(Enum):
	"""3 Members, A ... B"""
	A = 0
	AB = 1
	B = 2


# noinspection SpellCheckingInspection
class PathUniCodBbinA(Enum):
	"""1 Members, A ... A"""
	A = 0


# noinspection SpellCheckingInspection
class PayloadTestStuff(Enum):
	"""3 Members, H00 ... PRBS"""
	H00 = 0
	HFF = 1
	PRBS = 2


# noinspection SpellCheckingInspection
class PidTestPacket(Enum):
	"""2 Members, NULL ... VARiable"""
	NULL = 0
	VARiable = 1


# noinspection SpellCheckingInspection
class PowAttRfOffMode(Enum):
	"""2 Members, FATTenuation ... UNCHanged"""
	FATTenuation = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class PowerAttMode(Enum):
	"""5 Members, AUTO ... NORMal"""
	AUTO = 0
	FIXed = 1
	HPOWer = 2
	MANual = 3
	NORMal = 4


# noinspection SpellCheckingInspection
class PowLevBehaviour(Enum):
	"""2 Members, AUTO ... UNINterrupted"""
	AUTO = 0
	UNINterrupted = 1


# noinspection SpellCheckingInspection
class PowSensDisplayPriority(Enum):
	"""2 Members, AVERage ... PEAK"""
	AVERage = 0
	PEAK = 1


# noinspection SpellCheckingInspection
class PowSensFiltType(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	NSRatio = 1
	USER = 2


# noinspection SpellCheckingInspection
class PowSensSource(Enum):
	"""4 Members, A ... USER"""
	A = 0
	B = 1
	RF = 2
	USER = 3


# noinspection SpellCheckingInspection
class PulseSoure(Enum):
	"""4 Members, CODer ... RANDom"""
	CODer = 0
	EXTernal = 1
	INTernal = 2
	RANDom = 3


# noinspection SpellCheckingInspection
class RecScpiCmdMode(Enum):
	"""4 Members, AUTO ... OFF"""
	AUTO = 0
	DAUTo = 1
	MANual = 2
	OFF = 3


# noinspection SpellCheckingInspection
class RoscFreqExt(Enum):
	"""3 Members, _10MHZ ... _5MHZ"""
	_10MHZ = 0
	_13MHZ = 1
	_5MHZ = 2


# noinspection SpellCheckingInspection
class RoscOutpFreqMode(Enum):
	"""3 Members, DER10M ... OFF"""
	DER10M = 0
	LOOPthrough = 1
	OFF = 2


# noinspection SpellCheckingInspection
class RoscSourSetup(Enum):
	"""3 Members, ELOop ... INTernal"""
	ELOop = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class SampRateFifoStatus(Enum):
	"""3 Members, OFLow ... URUN"""
	OFLow = 0
	OK = 1
	URUN = 2


# noinspection SpellCheckingInspection
class SelftLev(Enum):
	"""3 Members, CUSTomer ... SERVice"""
	CUSTomer = 0
	PRODuction = 1
	SERVice = 2


# noinspection SpellCheckingInspection
class SelftLevWrite(Enum):
	"""4 Members, CUSTomer ... SERVice"""
	CUSTomer = 0
	NONE = 1
	PRODuction = 2
	SERVice = 3


# noinspection SpellCheckingInspection
class SettingsPrbs(Enum):
	"""2 Members, P15_1 ... P23_1"""
	P15_1 = 0
	P23_1 = 1


# noinspection SpellCheckingInspection
class SettingsTestTsPacket(Enum):
	"""2 Members, H184 ... S187"""
	H184 = 0
	S187 = 1


# noinspection SpellCheckingInspection
class SfeBbType(Enum):
	"""21 Members, AM ... TDMB"""
	AM = 0
	ARB = 1
	AT3SC = 2
	ATSM = 3
	ATV = 4
	AUDio = 5
	DIGital = 6
	DRMDRM = 7
	DTMB = 8
	DTV = 9
	DVBC = 10
	DVBS = 11
	DVBS2 = 12
	DVBT = 13
	FM = 14
	ISDBt = 15
	J83B = 16
	NONE = 17
	SERVice = 18
	T2DVb = 19
	TDMB = 20


# noinspection SpellCheckingInspection
class SfnMode(Enum):
	"""2 Members, ABSolute ... RELative"""
	ABSolute = 0
	RELative = 1


# noinspection SpellCheckingInspection
class SingExtAuto(Enum):
	"""8 Members, AUTO ... SINGle"""
	AUTO = 0
	BUS = 1
	DHOP = 2
	EAUTo = 3
	EXTernal = 4
	HOP = 5
	IMMediate = 6
	SINGle = 7


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class Spacing(Enum):
	"""3 Members, LINear ... RAMP"""
	LINear = 0
	LOGarithmic = 1
	RAMP = 2


# noinspection SpellCheckingInspection
class SpecialAcData(Enum):
	"""2 Members, ALL1 ... PRBS"""
	ALL1 = 0
	PRBS = 1


# noinspection SpellCheckingInspection
class StateExtended(Enum):
	"""6 Members, _0 ... ON"""
	_0 = 0
	_1 = 1
	_2 = 2
	DEFault = 3
	OFF = 4
	ON = 5


# noinspection SpellCheckingInspection
class StateOn(Enum):
	"""2 Members, _1 ... ON"""
	_1 = 0
	ON = 1


# noinspection SpellCheckingInspection
class SweCyclMode(Enum):
	"""2 Members, SAWTooth ... TRIangle"""
	SAWTooth = 0
	TRIangle = 1


# noinspection SpellCheckingInspection
class SystConfBbConf(Enum):
	"""3 Members, COUPled ... SEParate"""
	COUPled = 0
	CPENtity = 1
	SEParate = 2


# noinspection SpellCheckingInspection
class SystConfHsChannels(Enum):
	"""9 Members, CH0 ... CH8"""
	CH0 = 0
	CH1 = 1
	CH2 = 2
	CH3 = 3
	CH4 = 4
	CH5 = 5
	CH6 = 6
	CH7 = 7
	CH8 = 8


# noinspection SpellCheckingInspection
class SystConfOutpMode(Enum):
	"""6 Members, ALL ... HSDigital"""
	ALL = 0
	ANALog = 1
	DIGital = 2
	DIGMux = 3
	HSALl = 4
	HSDigital = 5


# noinspection SpellCheckingInspection
class SystemPostExtension(Enum):
	"""1 Members, OFF ... OFF"""
	OFF = 0


# noinspection SpellCheckingInspection
class T2SystemPapr(Enum):
	"""2 Members, OFF ... TR"""
	OFF = 0
	TR = 1


# noinspection SpellCheckingInspection
class TdmaDataSource(Enum):
	"""11 Members, DLISt ... ZERO"""
	DLISt = 0
	ONE = 1
	PATTern = 2
	PN11 = 3
	PN15 = 4
	PN16 = 5
	PN20 = 6
	PN21 = 7
	PN23 = 8
	PN9 = 9
	ZERO = 10


# noinspection SpellCheckingInspection
class TdmbInputSignalEtiSignal(Enum):
	"""4 Members, E537 ... INValid"""
	E537 = 0
	E559 = 1
	ENI = 2
	INValid = 3


# noinspection SpellCheckingInspection
class TdmbInputSignalInputFormat(Enum):
	"""1 Members, ETI ... ETI"""
	ETI = 0


# noinspection SpellCheckingInspection
class TdmbInputSignalProtectionLevel(Enum):
	"""14 Members, EP1A ... UP5"""
	EP1A = 0
	EP1B = 1
	EP2A = 2
	EP2B = 3
	EP3A = 4
	EP3B = 5
	EP4A = 6
	EP4B = 7
	UNDefined = 8
	UP1 = 9
	UP2 = 10
	UP3 = 11
	UP4 = 12
	UP5 = 13


# noinspection SpellCheckingInspection
class TdmbInputSignalProtectionProfile(Enum):
	"""2 Members, EEP ... UEP"""
	EEP = 0
	UEP = 1


# noinspection SpellCheckingInspection
class TdmbSettingsPrbs(Enum):
	"""4 Members, P15_1 ... ZERO"""
	P15_1 = 0
	P20_1 = 1
	P23_1 = 2
	ZERO = 3


# noinspection SpellCheckingInspection
class TdmbSpecialTransmissionMode(Enum):
	"""2 Members, MANual ... MID"""
	MANual = 0
	MID = 1


# noinspection SpellCheckingInspection
class Test(Enum):
	"""4 Members, _0 ... STOPped"""
	_0 = 0
	_1 = 1
	RUNning = 2
	STOPped = 3


# noinspection SpellCheckingInspection
class TestBbGenIqSour(Enum):
	"""4 Members, ARB ... TTONe"""
	ARB = 0
	CONStant = 1
	SINE = 2
	TTONe = 3


# noinspection SpellCheckingInspection
class TranRecFftLen(Enum):
	"""5 Members, LEN1024 ... LEN512"""
	LEN1024 = 0
	LEN2048 = 1
	LEN256 = 2
	LEN4096 = 3
	LEN512 = 4


# noinspection SpellCheckingInspection
class TranRecMode(Enum):
	"""7 Members, CCDF ... VECTor"""
	CCDF = 0
	CONStellation = 1
	EYEI = 2
	EYEQ = 3
	IQ = 4
	PSPectrum = 5
	VECTor = 6


# noinspection SpellCheckingInspection
class TranRecSampFactMode(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	FULL = 1
	USER = 2


# noinspection SpellCheckingInspection
class TranRecSize(Enum):
	"""2 Members, MAXimized ... MINimized"""
	MAXimized = 0
	MINimized = 1


# noinspection SpellCheckingInspection
class TranRecSour(Enum):
	"""6 Members, BBA ... STRA"""
	BBA = 0
	BBIA = 1
	DO1 = 2
	IQO1 = 3
	RFA = 4
	STRA = 5


# noinspection SpellCheckingInspection
class TranRecTrigSour(Enum):
	"""2 Members, MARKer ... SOFTware"""
	MARKer = 0
	SOFTware = 1


# noinspection SpellCheckingInspection
class TrigDelUnit(Enum):
	"""2 Members, SAMPle ... TIME"""
	SAMPle = 0
	TIME = 1


# noinspection SpellCheckingInspection
class TriggerMarkModeA(Enum):
	"""6 Members, PATTern ... UNCHanged"""
	PATTern = 0
	PULSe = 1
	RATio = 2
	RESTart = 3
	TRIGger = 4
	UNCHanged = 5


# noinspection SpellCheckingInspection
class TriggerMarkModeB(Enum):
	"""5 Members, PATTern ... TRIGger"""
	PATTern = 0
	PULSe = 1
	RATio = 2
	RESTart = 3
	TRIGger = 4


# noinspection SpellCheckingInspection
class TriggerSourceB(Enum):
	"""4 Members, BEXTernal ... OBASeband"""
	BEXTernal = 0
	EXTernal = 1
	INTernal = 2
	OBASeband = 3


# noinspection SpellCheckingInspection
class TrigRunMode(Enum):
	"""2 Members, RUN ... STOP"""
	RUN = 0
	STOP = 1


# noinspection SpellCheckingInspection
class TrigSour(Enum):
	"""4 Members, BBSY ... INTernal"""
	BBSY = 0
	EGT1 = 1
	EXTernal = 2
	INTernal = 3


# noinspection SpellCheckingInspection
class TrigSweepSourNoHopExtAuto(Enum):
	"""5 Members, AUTO ... SINGle"""
	AUTO = 0
	BUS = 1
	EXTernal = 2
	IMMediate = 3
	SINGle = 4


# noinspection SpellCheckingInspection
class TspLayerSettingsTestTsPacket(Enum):
	"""6 Members, H184 ... S207"""
	H184 = 0
	H200 = 1
	H204 = 2
	S187 = 3
	S203 = 4
	S207 = 5


# noinspection SpellCheckingInspection
class TspLayerStatus(Enum):
	"""4 Members, PAUSe ... STOP"""
	PAUSe = 0
	PLAY = 1
	RESet = 2
	STOP = 3


# noinspection SpellCheckingInspection
class TxAudioBcFmRdsAfBorder(Enum):
	"""2 Members, ASC ... DESC"""
	ASC = 0
	DESC = 1


# noinspection SpellCheckingInspection
class TxAudioBcFmRdsEonAfMethod(Enum):
	"""2 Members, A ... MAPF"""
	A = 0
	MAPF = 1


# noinspection SpellCheckingInspection
class TxAudioBcFmRdsMs(Enum):
	"""2 Members, MUSic ... SPEech"""
	MUSic = 0
	SPEech = 1


# noinspection SpellCheckingInspection
class UnchOff(Enum):
	"""2 Members, OFF ... UNCHanged"""
	OFF = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class UnitAngle(Enum):
	"""3 Members, DEGree ... RADian"""
	DEGree = 0
	DEGRee = 1
	RADian = 2


# noinspection SpellCheckingInspection
class UnitPower(Enum):
	"""3 Members, DBM ... V"""
	DBM = 0
	DBUV = 1
	V = 2


# noinspection SpellCheckingInspection
class UnitPowSens(Enum):
	"""3 Members, DBM ... WATT"""
	DBM = 0
	DBUV = 1
	WATT = 2


# noinspection SpellCheckingInspection
class UnitSlB(Enum):
	"""2 Members, SAMPle ... SEQuence"""
	SAMPle = 0
	SEQuence = 1


# noinspection SpellCheckingInspection
class UnitSpeed(Enum):
	"""4 Members, KMH ... NMPH"""
	KMH = 0
	MPH = 1
	MPS = 2
	NMPH = 3


# noinspection SpellCheckingInspection
class UpdPolicyMode(Enum):
	"""3 Members, CONFirm ... STRict"""
	CONFirm = 0
	IGNore = 1
	STRict = 2
