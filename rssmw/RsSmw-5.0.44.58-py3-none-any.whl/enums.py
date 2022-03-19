from enum import Enum


# noinspection SpellCheckingInspection
class AcDc(Enum):
	"""2 Members, AC ... DC"""
	AC = 0
	DC = 1


# noinspection SpellCheckingInspection
class AckNackAll(Enum):
	"""3 Members, JOIN ... SEP"""
	JOIN = 0
	NCON = 1
	SEP = 2


# noinspection SpellCheckingInspection
class AckNackMode(Enum):
	"""2 Members, BUNDling ... MUX"""
	BUNDling = 0
	MUX = 1


# noinspection SpellCheckingInspection
class AcqDataFormatGlonass(Enum):
	"""2 Members, G3GPP ... GRS"""
	G3GPP = 0
	GRS = 1


# noinspection SpellCheckingInspection
class AichTranTim(Enum):
	"""3 Members, ATT0 ... VOID"""
	ATT0 = 0
	ATT1 = 1
	VOID = 2


# noinspection SpellCheckingInspection
class AlcOffMode(Enum):
	"""2 Members, SHOLd ... TABLe"""
	SHOLd = 0
	TABLe = 1


# noinspection SpellCheckingInspection
class AlcOnOffAuto(Enum):
	"""9 Members, _0 ... PRESet"""
	_0 = 0
	_1 = 1
	AUTO = 2
	OFF = 3
	OFFTable = 4
	ON = 5
	ONSample = 6
	ONTable = 7
	PRESet = 8


# noinspection SpellCheckingInspection
class All(Enum):
	"""3 Members, AUTO ... RXTX"""
	AUTO = 0
	LOCK = 1
	RXTX = 2


# noinspection SpellCheckingInspection
class AllCancellInd(Enum):
	"""10 Members, _1 ... _8"""
	_1 = 0
	_112 = 1
	_14 = 2
	_16 = 3
	_2 = 4
	_32 = 5
	_4 = 6
	_56 = 7
	_7 = 8
	_8 = 9


# noinspection SpellCheckingInspection
class AllCdmType(Enum):
	"""4 Members, CDM2 ... NOCDm"""
	CDM2 = 0
	CDM4 = 1
	CDM8 = 2
	NOCDm = 3


# noinspection SpellCheckingInspection
class AllChannelRaster(Enum):
	"""3 Members, R100 ... R60"""
	R100 = 0
	R15 = 1
	R60 = 2


# noinspection SpellCheckingInspection
class AllDensity(Enum):
	"""4 Members, DEN1 ... ODD5"""
	DEN1 = 0
	DEN3 = 1
	EVE5 = 2
	ODD5 = 3


# noinspection SpellCheckingInspection
class AllHarqAckCbr16(Enum):
	"""2 Members, EDYN ... NCON"""
	EDYN = 0
	NCON = 1


# noinspection SpellCheckingInspection
class AllHarqAckCodebook(Enum):
	"""2 Members, DYNamic ... SEMistatic"""
	DYNamic = 0
	SEMistatic = 1


# noinspection SpellCheckingInspection
class AllocDciaGgLvl(Enum):
	"""5 Members, AL1 ... AL8"""
	AL1 = 0
	AL16 = 1
	AL2 = 2
	AL4 = 3
	AL8 = 4


# noinspection SpellCheckingInspection
class AllocDciFmt(Enum):
	"""16 Members, CUSTom ... F31"""
	CUSTom = 0
	F00 = 1
	F01 = 2
	F02 = 3
	F10 = 4
	F11 = 5
	F12 = 6
	F20 = 7
	F21 = 8
	F22 = 9
	F23 = 10
	F24 = 11
	F25 = 12
	F26 = 13
	F30 = 14
	F31 = 15


# noinspection SpellCheckingInspection
class AllocDciSearchSpace(Enum):
	"""6 Members, CSS0 ... USS"""
	CSS0 = 0
	CSS0A = 1
	CSS1 = 2
	CSS2 = 3
	CSS3 = 4
	USS = 5


# noinspection SpellCheckingInspection
class AllocDciUsage(Enum):
	"""21 Members, AI ... V"""
	AI = 0
	C = 1
	CI = 2
	CS = 3
	CUSTom = 4
	INT = 5
	MCSC = 6
	MSGB = 7
	P = 8
	PS = 9
	RA = 10
	SFI = 11
	SI = 12
	SL = 13
	SLCS = 14
	SPCS = 15
	TC = 16
	TPUC = 17
	TPUS = 18
	TSRS = 19
	V = 20


# noinspection SpellCheckingInspection
class AllocPxschDciFmt(Enum):
	"""6 Members, F00 ... F12"""
	F00 = 0
	F01 = 1
	F02 = 2
	F10 = 3
	F11 = 4
	F12 = 5


# noinspection SpellCheckingInspection
class AllPeriodicity(Enum):
	"""13 Members, _10 ... _80"""
	_10 = 0
	_16 = 1
	_160 = 2
	_20 = 3
	_32 = 4
	_320 = 5
	_4 = 6
	_40 = 7
	_5 = 8
	_64 = 9
	_640 = 10
	_8 = 11
	_80 = 12


# noinspection SpellCheckingInspection
class AllPorts(Enum):
	"""8 Members, _1 ... _8"""
	_1 = 0
	_12 = 1
	_16 = 2
	_2 = 3
	_24 = 4
	_32 = 5
	_4 = 6
	_8 = 7


# noinspection SpellCheckingInspection
class AllPsschScSize(Enum):
	"""5 Members, RB10 ... RB25"""
	RB10 = 0
	RB12 = 1
	RB15 = 2
	RB20 = 3
	RB25 = 4


# noinspection SpellCheckingInspection
class AllPxschSequenceGeneration(Enum):
	"""2 Members, CELLid ... DMRSid"""
	CELLid = 0
	DMRSid = 1


# noinspection SpellCheckingInspection
class AllSlPorts(Enum):
	"""3 Members, P1000 ... PBOTH"""
	P1000 = 0
	P1001 = 1
	PBOTH = 2


# noinspection SpellCheckingInspection
class AllTciSize(Enum):
	"""4 Members, TCI1 ... UNCF"""
	TCI1 = 0
	TCI2 = 1
	TCI3 = 2
	UNCF = 3


# noinspection SpellCheckingInspection
class AnalogDigital(Enum):
	"""2 Members, ANALog ... DIGital"""
	ANALog = 0
	DIGital = 1


# noinspection SpellCheckingInspection
class AntennaNr(Enum):
	"""4 Members, A1 ... A4"""
	A1 = 0
	A2 = 1
	A3 = 2
	A4 = 3


# noinspection SpellCheckingInspection
class AntMod3DaNtPattern(Enum):
	"""6 Members, DIPole ... USER"""
	DIPole = 0
	DPISotripic = 1
	ISOtropic = 2
	SEC3 = 3
	SEC6 = 4
	USER = 5


# noinspection SpellCheckingInspection
class AntModCalcGeoMode(Enum):
	"""3 Members, BFORming ... SPACing"""
	BFORming = 0
	RELativphase = 1
	SPACing = 2


# noinspection SpellCheckingInspection
class AntModCalcMode(Enum):
	"""2 Members, RELativphase ... SPACing"""
	RELativphase = 0
	SPACing = 1


# noinspection SpellCheckingInspection
class AntModPatMode(Enum):
	"""2 Members, SEParate ... SINGle"""
	SEParate = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class AntModPolAngle(Enum):
	"""4 Members, POLCO0 ... POLCROSS90"""
	POLCO0 = 0
	POLCO90 = 1
	POLCROSS45 = 2
	POLCROSS90 = 3


# noinspection SpellCheckingInspection
class AntModStructure(Enum):
	"""2 Members, CROSS ... LIN"""
	CROSS = 0
	LIN = 1


# noinspection SpellCheckingInspection
class AntViewType(Enum):
	"""4 Members, AATTenuation ... POSition"""
	AATTenuation = 0
	APHase = 1
	BODY = 2
	POSition = 3


# noinspection SpellCheckingInspection
class ApConfAll(Enum):
	"""4 Members, A00 ... A11"""
	A00 = 0
	A01 = 1
	A10 = 2
	A11 = 3


# noinspection SpellCheckingInspection
class ArbEthMode(Enum):
	"""2 Members, M10G ... M40G"""
	M10G = 0
	M40G = 1


# noinspection SpellCheckingInspection
class ArbLevMode(Enum):
	"""2 Members, HIGHest ... UNCHanged"""
	HIGHest = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class ArbMode(Enum):
	"""3 Members, ESTReaming ... STANdard"""
	ESTReaming = 0
	EUPLoad = 1
	STANdard = 2


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
	"""3 Members, INTernal ... NSEGM2"""
	INTernal = 0
	NSEGM1 = 1
	NSEGM2 = 2


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
class AsEqMcsMode(Enum):
	"""3 Members, FIXed ... TCR"""
	FIXed = 0
	MANual = 1
	TCR = 2


# noinspection SpellCheckingInspection
class AttitMode(Enum):
	"""5 Members, CONStant ... SPINning"""
	CONStant = 0
	FILE = 1
	MOTion = 2
	REMote = 3
	SPINning = 4


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
class AutoMode(Enum):
	"""3 Members, AUTO ... ON"""
	AUTO = 0
	OFF = 1
	ON = 2


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
class AxisType(Enum):
	"""2 Members, CIRCles ... GRID"""
	CIRCles = 0
	GRID = 1


# noinspection SpellCheckingInspection
class Band(Enum):
	"""32 Members, N1 ... N86"""
	N1 = 0
	N12 = 1
	N2 = 2
	N20 = 3
	N25 = 4
	N28 = 5
	N3 = 6
	N34 = 7
	N38 = 8
	N39 = 9
	N40 = 10
	N41 = 11
	N5 = 12
	N50 = 13
	N51 = 14
	N66 = 15
	N7 = 16
	N70 = 17
	N71 = 18
	N74 = 19
	N75 = 20
	N76 = 21
	N77 = 22
	N78 = 23
	N79 = 24
	N8 = 25
	N80 = 26
	N81 = 27
	N82 = 28
	N83 = 29
	N84 = 30
	N86 = 31


# noinspection SpellCheckingInspection
class BbClock(Enum):
	"""9 Members, CR025 ... CR500"""
	CR025 = 0
	CR050 = 1
	CR062 = 2
	CR100 = 3
	CR125 = 4
	CR1G = 5
	CR200 = 6
	CR250 = 7
	CR500 = 8


# noinspection SpellCheckingInspection
class BbCodMode(Enum):
	"""2 Members, BBIN ... CODer"""
	BBIN = 0
	CODer = 1


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
class BbImpOptModeRangeFresponse(Enum):
	"""3 Members, FAST ... QHTable"""
	FAST = 0
	QHIGh = 1
	QHTable = 2


# noinspection SpellCheckingInspection
class BbinDigInpSour(Enum):
	"""4 Members, CODER1 ... FADER2"""
	CODER1 = 0
	CODER2 = 1
	FADER1 = 2
	FADER2 = 3


# noinspection SpellCheckingInspection
class BbinInterfaceMode(Enum):
	"""2 Members, DIGital ... HSDin"""
	DIGital = 0
	HSDin = 1


# noinspection SpellCheckingInspection
class BbinModeDigital(Enum):
	"""1 Members, DIGital ... DIGital"""
	DIGital = 0


# noinspection SpellCheckingInspection
class BbinSampRateMode(Enum):
	"""3 Members, DIN ... USER"""
	DIN = 0
	HSDin = 1
	USER = 2


# noinspection SpellCheckingInspection
class BbMeasPowAcq(Enum):
	"""4 Members, CONTinuous ... NOMinal"""
	CONTinuous = 0
	GATed = 1
	MGATed = 2
	NOMinal = 3


# noinspection SpellCheckingInspection
class BbMeasPowGateSour(Enum):
	"""5 Members, MARK1 ... NONE"""
	MARK1 = 0
	MARK2 = 1
	MARK3 = 2
	MGATed = 3
	NONE = 4


# noinspection SpellCheckingInspection
class BbMeasPowOutp(Enum):
	"""6 Members, BBMM1 ... RFB"""
	BBMM1 = 0
	BBMM2 = 1
	IQOUT1 = 2
	IQOUT2 = 3
	RFA = 4
	RFB = 5


# noinspection SpellCheckingInspection
class BbMeasPowSour(Enum):
	"""48 Members, AWGNA ... STREAMH"""
	AWGNA = 0
	AWGNB = 1
	AWGNC = 2
	AWGND = 3
	AWGNE = 4
	AWGNF = 5
	AWGNG = 6
	AWGNH = 7
	BBA = 8
	BBB = 9
	BBC = 10
	BBD = 11
	BBE = 12
	BBF = 13
	BBG = 14
	BBH = 15
	BBINA = 16
	BBINB = 17
	BBINC = 18
	BBIND = 19
	BBINE = 20
	BBINF = 21
	BBING = 22
	BBINH = 23
	FADINPA = 24
	FADINPB = 25
	FADINPC = 26
	FADINPD = 27
	FADINPE = 28
	FADINPF = 29
	FADINPG = 30
	FADINPH = 31
	FADOUTA = 32
	FADOUTB = 33
	FADOUTC = 34
	FADOUTD = 35
	FADOUTE = 36
	FADOUTF = 37
	FADOUTG = 38
	FADOUTH = 39
	STREAMA = 40
	STREAMB = 41
	STREAMC = 42
	STREAMD = 43
	STREAME = 44
	STREAMF = 45
	STREAMG = 46
	STREAMH = 47


# noinspection SpellCheckingInspection
class BboutClocSour(Enum):
	"""2 Members, DOUT ... USER"""
	DOUT = 0
	USER = 1


# noinspection SpellCheckingInspection
class BehUnsSubFrames(Enum):
	"""2 Members, DTX ... DUData"""
	DTX = 0
	DUData = 1


# noinspection SpellCheckingInspection
class BertCrcOrder(Enum):
	"""2 Members, LSB ... MSB"""
	LSB = 0
	MSB = 1


# noinspection SpellCheckingInspection
class BertDataConn(Enum):
	"""2 Members, MRK1 ... TRIGger"""
	MRK1 = 0
	TRIGger = 1


# noinspection SpellCheckingInspection
class BertMask(Enum):
	"""3 Members, HIGH ... OFF"""
	HIGH = 0
	LOW = 1
	OFF = 2


# noinspection SpellCheckingInspection
class BertPattIgn(Enum):
	"""3 Members, OFF ... ZERO"""
	OFF = 0
	ONE = 1
	ZERO = 2


# noinspection SpellCheckingInspection
class BertPrbs(Enum):
	"""14 Members, PN11 ... PRBS9"""
	PN11 = 0
	PN15 = 1
	PN16 = 2
	PN20 = 3
	PN21 = 4
	PN23 = 5
	PN9 = 6
	PRBS11 = 7
	PRBS15 = 8
	PRBS16 = 9
	PRBS20 = 10
	PRBS21 = 11
	PRBS23 = 12
	PRBS9 = 13


# noinspection SpellCheckingInspection
class BertTestMode(Enum):
	"""2 Members, BER ... BLER"""
	BER = 0
	BLER = 1


# noinspection SpellCheckingInspection
class BertTgEnTrigMode(Enum):
	"""2 Members, DENable ... RESTart"""
	DENable = 0
	RESTart = 1


# noinspection SpellCheckingInspection
class BertType(Enum):
	"""1 Members, CRC16 ... CRC16"""
	CRC16 = 0


# noinspection SpellCheckingInspection
class BertUnit(Enum):
	"""3 Members, ENGineering ... PPM"""
	ENGineering = 0
	PCT = 1
	PPM = 2


# noinspection SpellCheckingInspection
class BfapMapMode(Enum):
	"""3 Members, CB ... RCB"""
	CB = 0
	FW = 1
	RCB = 2


# noinspection SpellCheckingInspection
class BfTransScheme(Enum):
	"""4 Members, TM10 ... TM9"""
	TM10 = 0
	TM7 = 1
	TM8 = 2
	TM9 = 3


# noinspection SpellCheckingInspection
class BitOrder(Enum):
	"""2 Members, LSBit ... MSBit"""
	LSBit = 0
	MSBit = 1


# noinspection SpellCheckingInspection
class BlerTrigMode(Enum):
	"""2 Members, AUTO ... SINGle"""
	AUTO = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class BrsTransPeriod(Enum):
	"""4 Members, P00 ... P11"""
	P00 = 0
	P01 = 1
	P10 = 2
	P11 = 3


# noinspection SpellCheckingInspection
class BsClass(Enum):
	"""3 Members, LOC ... WIDE"""
	LOC = 0
	MED = 1
	WIDE = 2


# noinspection SpellCheckingInspection
class BsType(Enum):
	"""3 Members, BT1H ... BT2O"""
	BT1H = 0
	BT1O = 1
	BT2O = 2


# noinspection SpellCheckingInspection
class BtoAckNldgmt(Enum):
	"""2 Members, ACK ... NAK"""
	ACK = 0
	NAK = 1


# noinspection SpellCheckingInspection
class BtoAdvMode(Enum):
	"""3 Members, CNS ... NCS"""
	CNS = 0
	NCNS = 1
	NCS = 2


# noinspection SpellCheckingInspection
class BtoChnnelType(Enum):
	"""2 Members, ADVertising ... DATA"""
	ADVertising = 0
	DATA = 1


# noinspection SpellCheckingInspection
class BtoChSel(Enum):
	"""2 Members, CS1 ... CS2"""
	CS1 = 0
	CS2 = 1


# noinspection SpellCheckingInspection
class BtoClkAcc(Enum):
	"""2 Members, T50 ... T500"""
	T50 = 0
	T500 = 1


# noinspection SpellCheckingInspection
class BtoCteType(Enum):
	"""3 Members, AOA ... AOD2"""
	AOA = 0
	AOD1 = 1
	AOD2 = 2


# noinspection SpellCheckingInspection
class BtoCtrlRol(Enum):
	"""5 Members, ADVertiser ... SCANner"""
	ADVertiser = 0
	CENTral = 1
	INITiator = 2
	PERipheral = 3
	SCANner = 4


# noinspection SpellCheckingInspection
class BtoDataSourForPck(Enum):
	"""2 Members, ADATa ... PEDit"""
	ADATa = 0
	PEDit = 1


# noinspection SpellCheckingInspection
class BtoFlowCtrl(Enum):
	"""2 Members, GO ... STOP"""
	GO = 0
	STOP = 1


# noinspection SpellCheckingInspection
class BtoLlCnctMod(Enum):
	"""2 Members, ENC ... UENC"""
	ENC = 0
	UENC = 1


# noinspection SpellCheckingInspection
class BtoMarkMode(Enum):
	"""8 Members, ACTive ... TRIGger"""
	ACTive = 0
	IACTive = 1
	PATTern = 2
	PULSe = 3
	RATio = 4
	RESTart = 5
	STARt = 6
	TRIGger = 7


# noinspection SpellCheckingInspection
class BtoMode(Enum):
	"""3 Members, BASic ... QHS"""
	BASic = 0
	BLENergy = 1
	QHS = 2


# noinspection SpellCheckingInspection
class BtoModIdxMode(Enum):
	"""2 Members, STABle ... STANdard"""
	STABle = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class BtoNumOfPackPerSet(Enum):
	"""3 Members, NP1 ... NP50"""
	NP1 = 0
	NP2 = 1
	NP50 = 2


# noinspection SpellCheckingInspection
class BtoOffsUnit(Enum):
	"""2 Members, U30 ... U300"""
	U30 = 0
	U300 = 1


# noinspection SpellCheckingInspection
class BtoPckType(Enum):
	"""28 Members, ADH1 ... POLL"""
	ADH1 = 0
	ADH3 = 1
	ADH5 = 2
	AEDH1 = 3
	AEDH3 = 4
	AEDH5 = 5
	AUX1 = 6
	DH1 = 7
	DH3 = 8
	DH5 = 9
	DM1 = 10
	DM3 = 11
	DM5 = 12
	DV = 13
	EEEV3 = 14
	EEEV5 = 15
	EEV3 = 16
	EEV5 = 17
	EV3 = 18
	EV4 = 19
	EV5 = 20
	FHS = 21
	HV1 = 22
	HV2 = 23
	HV3 = 24
	ID = 25
	NULL = 26
	POLL = 27


# noinspection SpellCheckingInspection
class BtoPyLdSour(Enum):
	"""8 Members, PAT1 ... PN15"""
	PAT1 = 0
	PAT2 = 1
	PAT3 = 2
	PAT4 = 3
	PAT5 = 4
	PAT6 = 5
	PN09 = 6
	PN15 = 7


# noinspection SpellCheckingInspection
class BtoScanReMode(Enum):
	"""3 Members, R0 ... R2"""
	R0 = 0
	R1 = 1
	R2 = 2


# noinspection SpellCheckingInspection
class BtoSlotTiming(Enum):
	"""2 Members, LOOPback ... TX"""
	LOOPback = 0
	TX = 1


# noinspection SpellCheckingInspection
class BtoSlpClckAccrcy(Enum):
	"""8 Members, SCA0 ... SCA7"""
	SCA0 = 0
	SCA1 = 1
	SCA2 = 2
	SCA3 = 3
	SCA4 = 4
	SCA5 = 5
	SCA6 = 6
	SCA7 = 7


# noinspection SpellCheckingInspection
class BtoSymPerBit(Enum):
	"""2 Members, EIGHt ... TWO"""
	EIGHt = 0
	TWO = 1


# noinspection SpellCheckingInspection
class BtoTranMode(Enum):
	"""3 Members, ACL ... SCO"""
	ACL = 0
	ESCO = 1
	SCO = 2


# noinspection SpellCheckingInspection
class BtoUlpAddrType(Enum):
	"""2 Members, PUBLic ... RANDom"""
	PUBLic = 0
	RANDom = 1


# noinspection SpellCheckingInspection
class BtoUlpPckType(Enum):
	"""49 Members, AAINd ... VIND"""
	AAINd = 0
	ACINd = 1
	ACReq = 2
	ACRSp = 3
	ADCind = 4
	ADINd = 5
	AEINd = 6
	AIND = 7
	ANINd = 8
	ASINd = 9
	ASPSp = 10
	ASReq = 11
	CAReq = 12
	CARSp = 13
	CMReq = 14
	CONT = 15
	CPR = 16
	CPRS = 17
	CREQ = 18
	CTEP = 19
	CTEQ = 20
	CUReq = 21
	DATA = 22
	EREQ = 23
	ERSP = 24
	FREQ = 25
	FRSP = 26
	LREQ = 27
	LRSP = 28
	MUCH = 29
	PEReq = 30
	PERSp = 31
	PIR = 32
	PIRS = 33
	PREQ = 34
	PRSP = 35
	PSINd = 36
	PUIN = 37
	REIN = 38
	RIND = 39
	SEReq = 40
	SERSp = 41
	SFR = 42
	SREQ = 43
	SRSP = 44
	TIND = 45
	TPACket = 46
	URSP = 47
	VIND = 48


# noinspection SpellCheckingInspection
class ByteOrder(Enum):
	"""2 Members, NORMal ... SWAPped"""
	NORMal = 0
	SWAPped = 1


# noinspection SpellCheckingInspection
class C5GbaseMod(Enum):
	"""7 Members, BPSK ... SCMA"""
	BPSK = 0
	CIQ = 1
	QAM16 = 2
	QAM256 = 3
	QAM64 = 4
	QPSK = 5
	SCMA = 6


# noinspection SpellCheckingInspection
class C5GcontentType(Enum):
	"""4 Members, DATA ... REServed"""
	DATA = 0
	PILot = 1
	PREamble = 2
	REServed = 3


# noinspection SpellCheckingInspection
class C5Gds(Enum):
	"""17 Members, DLISt ... ZERO"""
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
	USER0 = 10
	USER1 = 11
	USER2 = 12
	USER3 = 13
	USER4 = 14
	USER5 = 15
	ZERO = 16


# noinspection SpellCheckingInspection
class C5GfilterWind(Enum):
	"""3 Members, HAMMing ... NONE"""
	HAMMing = 0
	HANNing = 1
	NONE = 2


# noinspection SpellCheckingInspection
class C5GfiltT(Enum):
	"""9 Members, DCH ... USER"""
	DCH = 0
	DIRichlet = 1
	NONE = 2
	PHYDyas = 3
	RC = 4
	RECT = 5
	RRC = 6
	STRunc = 7
	USER = 8


# noinspection SpellCheckingInspection
class C5Gmod(Enum):
	"""5 Members, FBMC ... UFMC"""
	FBMC = 0
	FOFDm = 1
	GFDM = 2
	OFDM = 3
	UFMC = 4


# noinspection SpellCheckingInspection
class C5GscmaUser(Enum):
	"""6 Members, USER0 ... USER5"""
	USER0 = 0
	USER1 = 1
	USER2 = 2
	USER3 = 3
	USER4 = 4
	USER5 = 5


# noinspection SpellCheckingInspection
class CalDataMode(Enum):
	"""2 Members, CUSTomer ... FACTory"""
	CUSTomer = 0
	FACTory = 1


# noinspection SpellCheckingInspection
class CalDataUpdate(Enum):
	"""6 Members, BBFRC ... RFFRC"""
	BBFRC = 0
	FREQuency = 1
	IALL = 2
	LEVel = 3
	LEVForced = 4
	RFFRC = 5


# noinspection SpellCheckingInspection
class CalPowAttMode(Enum):
	"""2 Members, NEW ... OLD"""
	NEW = 0
	OLD = 1


# noinspection SpellCheckingInspection
class CalPowBandwidth(Enum):
	"""2 Members, AUTO ... HIGH"""
	AUTO = 0
	HIGH = 1


# noinspection SpellCheckingInspection
class CalPowOpuMode(Enum):
	"""6 Members, AUTO ... RFOpu"""
	AUTO = 0
	MW44opu = 1
	MW4opu = 2
	MW70opu = 3
	MWOpu = 4
	RFOpu = 5


# noinspection SpellCheckingInspection
class CbMode(Enum):
	"""2 Members, N1 ... N2"""
	N1 = 0
	N2 = 1


# noinspection SpellCheckingInspection
class CcIndex(Enum):
	"""5 Members, PC ... SC4"""
	PC = 0
	SC1 = 1
	SC2 = 2
	SC3 = 3
	SC4 = 4


# noinspection SpellCheckingInspection
class CckFormat(Enum):
	"""2 Members, LONG ... SHORt"""
	LONG = 0
	SHORt = 1


# noinspection SpellCheckingInspection
class Cdma2KchanCodBlkIlea(Enum):
	"""20 Members, _1152 ... NONE"""
	_1152 = 0
	_12288 = 1
	_128 = 2
	_144 = 3
	_1536 = 4
	_18432 = 5
	_192 = 6
	_2304 = 7
	_288 = 8
	_3072 = 9
	_36864 = 10
	_384 = 11
	_4608 = 12
	_48 = 13
	_576 = 14
	_6144 = 15
	_768 = 16
	_9216 = 17
	_96 = 18
	NONE = 19


# noinspection SpellCheckingInspection
class Cdma2KchanCoderType(Enum):
	"""10 Members, CON2 ... TUR5"""
	CON2 = 0
	CON3 = 1
	CON4 = 2
	CON6 = 3
	DEFault = 4
	OFF = 5
	TUR2 = 6
	TUR3 = 7
	TUR4 = 8
	TUR5 = 9


# noinspection SpellCheckingInspection
class Cdma2KchanCodSymbPunc(Enum):
	"""9 Members, _1OF5 ... T4OF12"""
	_1OF5 = 0
	_1OF9 = 1
	_2OF18 = 2
	_2OF6 = 3
	_4OF12 = 4
	_8OF24 = 5
	NONE = 6
	T2OF18 = 7
	T4OF12 = 8


# noinspection SpellCheckingInspection
class Cdma2KchanTypeDn(Enum):
	"""16 Members, F_dash_APICH ... F_dash_TDPICH"""
	F_dash_APICH = 0
	F_dash_ATDPICH = 1
	F_dash_BCH = 2
	F_dash_CACH = 3
	F_dash_CCCH = 4
	F_dash_CPCCH = 5
	F_dash_DCCH = 6
	F_dash_FCH = 7
	F_dash_PCH = 8
	F_dash_PDCCH = 9
	F_dash_PDCH = 10
	F_dash_PICH = 11
	F_dash_QPCH = 12
	F_dash_SCH = 13
	F_dash_SYNC = 14
	F_dash_TDPICH = 15


# noinspection SpellCheckingInspection
class Cdma2KchanTypeUp(Enum):
	"""9 Members, R_dash_ACH ... R_dash_SCH2"""
	R_dash_ACH = 0
	R_dash_CCCH = 1
	R_dash_DCCH = 2
	R_dash_EACH = 3
	R_dash_FCH = 4
	R_dash_PICH = 5
	R_dash_SCCH = 6
	R_dash_SCH1 = 7
	R_dash_SCH2 = 8


# noinspection SpellCheckingInspection
class Cdma2KchipRate(Enum):
	"""1 Members, R1M2 ... R1M2"""
	R1M2 = 0


# noinspection SpellCheckingInspection
class Cdma2KcodMode(Enum):
	"""4 Members, COMPlete ... OINTerleaving"""
	COMPlete = 0
	NOINterleaving = 1
	OFF = 2
	OINTerleaving = 3


# noinspection SpellCheckingInspection
class Cdma2KdataRate(Enum):
	"""26 Members, DR1036K8 ... NUSed"""
	DR1036K8 = 0
	DR115K2 = 1
	DR14K4 = 2
	DR153K6 = 3
	DR19K2 = 4
	DR1K2 = 5
	DR1K3 = 6
	DR1K5 = 7
	DR1K8 = 8
	DR230K4 = 9
	DR259K2 = 10
	DR28K8 = 11
	DR2K4 = 12
	DR2K7 = 13
	DR307K2 = 14
	DR38K4 = 15
	DR3K6 = 16
	DR460K8 = 17
	DR4K8 = 18
	DR518K4 = 19
	DR57K6 = 20
	DR614K4 = 21
	DR76K8 = 22
	DR7K2 = 23
	DR9K6 = 24
	NUSed = 25


# noinspection SpellCheckingInspection
class Cdma2KdomConfModeDn(Enum):
	"""2 Members, BREV ... HAD"""
	BREV = 0
	HAD = 1


# noinspection SpellCheckingInspection
class Cdma2KframLen(Enum):
	"""8 Members, _10 ... NUSed"""
	_10 = 0
	_160 = 1
	_20 = 2
	_26_dot_6 = 3
	_40 = 4
	_5 = 5
	_80 = 6
	NUSed = 7


# noinspection SpellCheckingInspection
class Cdma2KframLenUp(Enum):
	"""6 Members, _10 ... _80"""
	_10 = 0
	_20 = 1
	_26_dot_6 = 2
	_40 = 3
	_5 = 4
	_80 = 5


# noinspection SpellCheckingInspection
class Cdma2KmarkMode(Enum):
	"""9 Members, CSPeriod ... USER"""
	CSPeriod = 0
	ESECond = 1
	PCGRoup = 2
	RATio = 3
	RFRame = 4
	SCFRame = 5
	SFRame = 6
	TRIGger = 7
	USER = 8


# noinspection SpellCheckingInspection
class Cdma2KmpPdchFiveColDn(Enum):
	"""127 Members, _1 ... _99"""
	_1 = 0
	_10 = 1
	_100 = 2
	_101 = 3
	_102 = 4
	_103 = 5
	_104 = 6
	_105 = 7
	_106 = 8
	_107 = 9
	_108 = 10
	_109 = 11
	_11 = 12
	_110 = 13
	_111 = 14
	_112 = 15
	_113 = 16
	_114 = 17
	_115 = 18
	_116 = 19
	_117 = 20
	_118 = 21
	_119 = 22
	_12 = 23
	_120 = 24
	_121 = 25
	_122 = 26
	_123 = 27
	_124 = 28
	_125 = 29
	_126 = 30
	_127 = 31
	_13 = 32
	_14 = 33
	_15 = 34
	_16 = 35
	_17 = 36
	_18 = 37
	_19 = 38
	_2 = 39
	_20 = 40
	_21 = 41
	_22 = 42
	_23 = 43
	_24 = 44
	_25 = 45
	_26 = 46
	_27 = 47
	_28 = 48
	_29 = 49
	_3 = 50
	_30 = 51
	_31 = 52
	_32 = 53
	_33 = 54
	_34 = 55
	_35 = 56
	_36 = 57
	_37 = 58
	_38 = 59
	_39 = 60
	_4 = 61
	_40 = 62
	_41 = 63
	_42 = 64
	_43 = 65
	_44 = 66
	_45 = 67
	_46 = 68
	_47 = 69
	_48 = 70
	_49 = 71
	_5 = 72
	_50 = 73
	_51 = 74
	_52 = 75
	_53 = 76
	_54 = 77
	_55 = 78
	_56 = 79
	_57 = 80
	_58 = 81
	_59 = 82
	_6 = 83
	_60 = 84
	_61 = 85
	_62 = 86
	_63 = 87
	_64 = 88
	_65 = 89
	_66 = 90
	_67 = 91
	_68 = 92
	_69 = 93
	_7 = 94
	_70 = 95
	_71 = 96
	_72 = 97
	_73 = 98
	_74 = 99
	_75 = 100
	_76 = 101
	_77 = 102
	_78 = 103
	_79 = 104
	_8 = 105
	_80 = 106
	_81 = 107
	_82 = 108
	_83 = 109
	_84 = 110
	_85 = 111
	_86 = 112
	_87 = 113
	_88 = 114
	_89 = 115
	_9 = 116
	_90 = 117
	_91 = 118
	_92 = 119
	_93 = 120
	_94 = 121
	_95 = 122
	_96 = 123
	_97 = 124
	_98 = 125
	_99 = 126


# noinspection SpellCheckingInspection
class Cdma2KmsMode(Enum):
	"""4 Members, ACCess ... TRAFfic"""
	ACCess = 0
	CCONtrol = 1
	EACCess = 2
	TRAFfic = 3


# noinspection SpellCheckingInspection
class Cdma2KpredFramLen(Enum):
	"""3 Members, _20 ... _80"""
	_20 = 0
	_40 = 1
	_80 = 2


# noinspection SpellCheckingInspection
class Cdma2KradioConf(Enum):
	"""5 Members, _1 ... _5"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3
	_5 = 4


# noinspection SpellCheckingInspection
class Cdma2KtxDiv(Enum):
	"""3 Members, ANT1 ... OFF"""
	ANT1 = 0
	ANT2 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Cdma2KtxDivMode(Enum):
	"""2 Members, OTD ... STS"""
	OTD = 0
	STS = 1


# noinspection SpellCheckingInspection
class CellAll(Enum):
	"""16 Members, _0 ... _9"""
	_0 = 0
	_1 = 1
	_10 = 2
	_11 = 3
	_12 = 4
	_13 = 5
	_14 = 6
	_15 = 7
	_2 = 8
	_3 = 9
	_4 = 10
	_5 = 11
	_6 = 12
	_7 = 13
	_8 = 14
	_9 = 15


# noinspection SpellCheckingInspection
class CellBarring(Enum):
	"""2 Members, BARR ... NBAR"""
	BARR = 0
	NBAR = 1


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
class ChanCodMode(Enum):
	"""3 Members, COMBined ... ULSChonly"""
	COMBined = 0
	UCIonly = 1
	ULSChonly = 2


# noinspection SpellCheckingInspection
class ChanCodType(Enum):
	"""8 Members, AMR ... M64K"""
	AMR = 0
	BTFD1 = 1
	BTFD2 = 2
	BTFD3 = 3
	M12K2 = 4
	M144k = 5
	M384k = 6
	M64K = 7


# noinspection SpellCheckingInspection
class ChanCodTypeEnhPcpc(Enum):
	"""2 Members, TB168 ... TB360"""
	TB168 = 0
	TB360 = 1


# noinspection SpellCheckingInspection
class ChanCodTypeEnhPrac(Enum):
	"""4 Members, TB168 ... TU360"""
	TB168 = 0
	TB360 = 1
	TU168 = 2
	TU360 = 3


# noinspection SpellCheckingInspection
class ChannelBandwidth(Enum):
	"""10 Members, BW0_20 ... USER"""
	BW0_20 = 0
	BW1_25 = 1
	BW1_40 = 2
	BW10_00 = 3
	BW15_00 = 4
	BW2_50 = 5
	BW20_00 = 6
	BW3_00 = 7
	BW5_00 = 8
	USER = 9


# noinspection SpellCheckingInspection
class ChanTypeDn(Enum):
	"""22 Members, AICH ... SSCH"""
	AICH = 0
	APAich = 1
	DPCCh = 2
	DPCH = 3
	EAGCh = 4
	EHICh = 5
	ERGCh = 6
	FDPCh = 7
	HS16Qam = 8
	HS64Qam = 9
	HSMimo = 10
	HSQam = 11
	HSQPsk = 12
	HSSCch = 13
	PCCPch = 14
	PCPich = 15
	PDSCh = 16
	PICH = 17
	PSCH = 18
	SCCPch = 19
	SCPich = 20
	SSCH = 21


# noinspection SpellCheckingInspection
class ChipRate(Enum):
	"""1 Members, R3M8 ... R3M8"""
	R3M8 = 0


# noinspection SpellCheckingInspection
class CifAll(Enum):
	"""8 Members, _0 ... _7"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	_4 = 4
	_5 = 5
	_6 = 6
	_7 = 7


# noinspection SpellCheckingInspection
class ClipMode(Enum):
	"""2 Members, SCALar ... VECTor"""
	SCALar = 0
	VECTor = 1


# noinspection SpellCheckingInspection
class ClockMode(Enum):
	"""1 Members, SAMPle ... SAMPle"""
	SAMPle = 0


# noinspection SpellCheckingInspection
class ClockModeA(Enum):
	"""2 Members, CHIP ... MCHip"""
	CHIP = 0
	MCHip = 1


# noinspection SpellCheckingInspection
class ClockSourceA(Enum):
	"""1 Members, INTernal ... INTernal"""
	INTernal = 0


# noinspection SpellCheckingInspection
class ClockSourceB(Enum):
	"""3 Members, AINTernal ... INTernal"""
	AINTernal = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class ClockSourceC(Enum):
	"""3 Members, ELCLock ... INTernal"""
	ELCLock = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class ClocModeB(Enum):
	"""2 Members, MSAMple ... SAMPle"""
	MSAMple = 0
	SAMPle = 1


# noinspection SpellCheckingInspection
class ClocSyncMode(Enum):
	"""3 Members, NONE ... SECondary"""
	NONE = 0
	PRIMary = 1
	SECondary = 2


# noinspection SpellCheckingInspection
class CmMethDn(Enum):
	"""3 Members, HLSCheduling ... SF2"""
	HLSCheduling = 0
	PUNCturing = 1
	SF2 = 2


# noinspection SpellCheckingInspection
class CmMethUp(Enum):
	"""2 Members, HLSCheduling ... SF2"""
	HLSCheduling = 0
	SF2 = 1


# noinspection SpellCheckingInspection
class CodebookSubsetAll(Enum):
	"""3 Members, FPNC ... PNC"""
	FPNC = 0
	NC = 1
	PNC = 2


# noinspection SpellCheckingInspection
class CodebookType(Enum):
	"""1 Members, T1SP ... T1SP"""
	T1SP = 0


# noinspection SpellCheckingInspection
class CodeOnL2(Enum):
	"""3 Members, CACode ... REServed"""
	CACode = 0
	PCODe = 1
	REServed = 2


# noinspection SpellCheckingInspection
class CodeType(Enum):
	"""1 Members, BCHSfn ... BCHSfn"""
	BCHSfn = 0


# noinspection SpellCheckingInspection
class CodeWordIdx(Enum):
	"""2 Members, CW1 ... CW2"""
	CW1 = 0
	CW2 = 1


# noinspection SpellCheckingInspection
class Colour(Enum):
	"""4 Members, GREen ... YELLow"""
	GREen = 0
	NONE = 1
	RED = 2
	YELLow = 3


# noinspection SpellCheckingInspection
class Config(Enum):
	"""9 Members, E1RL ... OUTF"""
	E1RL = 0
	E1RR = 1
	EFL = 2
	EFR = 3
	I1RL = 4
	I1RR = 5
	INNF = 6
	MAN = 7
	OUTF = 8


# noinspection SpellCheckingInspection
class ConnDirection(Enum):
	"""3 Members, INPut ... UNUSed"""
	INPut = 0
	OUTPut = 1
	UNUSed = 2


# noinspection SpellCheckingInspection
class CoordMapMode(Enum):
	"""2 Members, CARTesian ... CYLindrical"""
	CARTesian = 0
	CYLindrical = 1


# noinspection SpellCheckingInspection
class CopySelection(Enum):
	"""2 Members, CARRier ... LOADfile"""
	CARRier = 0
	LOADfile = 1


# noinspection SpellCheckingInspection
class CoresetUnusedRes(Enum):
	"""3 Members, _0 ... ALLowpdsch"""
	_0 = 0
	_1 = 1
	ALLowpdsch = 2


# noinspection SpellCheckingInspection
class Count(Enum):
	"""2 Members, _1 ... _2"""
	_1 = 0
	_2 = 1


# noinspection SpellCheckingInspection
class CresFactMode(Enum):
	"""3 Members, AVERage ... WORSt"""
	AVERage = 0
	MINimum = 1
	WORSt = 2


# noinspection SpellCheckingInspection
class CrestFactoralgorithm(Enum):
	"""1 Members, CLF ... CLF"""
	CLF = 0


# noinspection SpellCheckingInspection
class CsiPart(Enum):
	"""2 Members, CSIP_1 ... CSIP_2"""
	CSIP_1 = 0
	CSIP_2 = 1


# noinspection SpellCheckingInspection
class CsiRsNumAp(Enum):
	"""4 Members, AP1 ... AP8"""
	AP1 = 0
	AP2 = 1
	AP4 = 2
	AP8 = 3


# noinspection SpellCheckingInspection
class CyclicPrefixGs(Enum):
	"""3 Members, EXTended ... USER"""
	EXTended = 0
	NORMal = 1
	USER = 2


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
class DataSourceA(Enum):
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
class DataSourceB(Enum):
	"""11 Members, ALL0 ... PN23"""
	ALL0 = 0
	ALL1 = 1
	DLISt = 2
	PATTern = 3
	PN09 = 4
	PN11 = 5
	PN15 = 6
	PN16 = 7
	PN20 = 8
	PN21 = 9
	PN23 = 10


# noinspection SpellCheckingInspection
class DataSourGnss(Enum):
	"""13 Members, DLISt ... ZNData"""
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
	RNData = 10
	ZERO = 11
	ZNData = 12


# noinspection SpellCheckingInspection
class DeclaredDir(Enum):
	"""3 Members, MREFD ... OTHD"""
	MREFD = 0
	OREFD = 1
	OTHD = 2


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
class DlContentType(Enum):
	"""5 Members, EPD1 ... PDSCh"""
	EPD1 = 0
	EPD2 = 1
	PBCH = 2
	PDCCh = 3
	PDSCh = 4


# noinspection SpellCheckingInspection
class DlecpRecScheme(Enum):
	"""2 Members, NONE ... TXD"""
	NONE = 0
	TXD = 1


# noinspection SpellCheckingInspection
class DlpRbBundlingGranularity(Enum):
	"""3 Members, N2 ... WIDeband"""
	N2 = 0
	N4 = 1
	WIDeband = 2


# noinspection SpellCheckingInspection
class DlpRecCycDelDiv(Enum):
	"""3 Members, LADelay ... SMDelay"""
	LADelay = 0
	NOCDd = 1
	SMDelay = 2


# noinspection SpellCheckingInspection
class DlpRecMultAntScheme(Enum):
	"""4 Members, BF ... TXD"""
	BF = 0
	NONE = 1
	SPM = 2
	TXD = 3


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
	"""3 Members, FSYMbol ... SYMBol"""
	FSYMbol = 0
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
class DmDataSourW(Enum):
	"""6 Members, DLISt ... ZERO"""
	DLISt = 0
	ONE = 1
	PATTern = 2
	PRBS = 3
	SERial = 4
	ZERO = 5


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
	"""17 Members, APCO25 ... SPHase"""
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
	PGAuss = 13
	RCOSine = 14
	RECTangle = 15
	SPHase = 16


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
class DmFilterB(Enum):
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
class DmFilterEutra(Enum):
	"""20 Members, APCO25 ... USER"""
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
	LTEFilter = 14
	PGAuss = 15
	RCOSine = 16
	RECTangle = 17
	SPHase = 18
	USER = 19


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
class DohertyShapeMode(Enum):
	"""4 Members, DOHerty ... TABLe"""
	DOHerty = 0
	NORMalized = 1
	POLYnomial = 2
	TABLe = 3


# noinspection SpellCheckingInspection
class Doppler(Enum):
	"""2 Members, CONStant ... HIGH"""
	CONStant = 0
	HIGH = 1


# noinspection SpellCheckingInspection
class DopplerConfig(Enum):
	"""3 Members, USER ... VEL2"""
	USER = 0
	VEL1 = 1
	VEL2 = 2


# noinspection SpellCheckingInspection
class DpdPowRef(Enum):
	"""3 Members, ADPD ... SDPD"""
	ADPD = 0
	BDPD = 1
	SDPD = 2


# noinspection SpellCheckingInspection
class DpdShapeMode(Enum):
	"""3 Members, NORMalized ... TABLe"""
	NORMalized = 0
	POLYnomial = 1
	TABLe = 2


# noinspection SpellCheckingInspection
class DrsDuration(Enum):
	"""5 Members, DUR1 ... DUR5"""
	DUR1 = 0
	DUR2 = 1
	DUR3 = 2
	DUR4 = 3
	DUR5 = 4


# noinspection SpellCheckingInspection
class DsPeriod(Enum):
	"""3 Members, P160 ... P80"""
	P160 = 0
	P40 = 1
	P80 = 2


# noinspection SpellCheckingInspection
class DuplexModeExtRange(Enum):
	"""3 Members, FDD ... TDD"""
	FDD = 0
	LAA = 1
	TDD = 2


# noinspection SpellCheckingInspection
class DvbClocMode(Enum):
	"""2 Members, MSAMp ... SAMP"""
	MSAMp = 0
	SAMP = 1


# noinspection SpellCheckingInspection
class DvbCoderate(Enum):
	"""5 Members, CR1D2 ... CR7D8"""
	CR1D2 = 0
	CR2D3 = 1
	CR3D4 = 2
	CR5D6 = 3
	CR7D8 = 4


# noinspection SpellCheckingInspection
class DvbDataSour(Enum):
	"""5 Members, DLISt ... PN23"""
	DLISt = 0
	PAC0 = 1
	PAC1 = 2
	PN15 = 3
	PN23 = 4


# noinspection SpellCheckingInspection
class DvbDataSource(Enum):
	"""13 Members, DLISt ... ZERO"""
	DLISt = 0
	GFILe = 1
	ONE = 2
	PATTern = 3
	PN11 = 4
	PN15 = 5
	PN16 = 6
	PN20 = 7
	PN21 = 8
	PN23 = 9
	PN9 = 10
	TFILe = 11
	ZERO = 12


# noinspection SpellCheckingInspection
class DvbGuardInt(Enum):
	"""4 Members, GI1D16 ... GI1D8"""
	GI1D16 = 0
	GI1D32 = 1
	GI1D4 = 2
	GI1D8 = 3


# noinspection SpellCheckingInspection
class DvbHierarchyMode(Enum):
	"""4 Members, HIErarchical ... NHIErarchical"""
	HIErarchical = 0
	HIERarchical = 1
	NHIerarchical = 2
	NHIErarchical = 3


# noinspection SpellCheckingInspection
class DvbIleavMode(Enum):
	"""3 Members, IDEPth ... NATIve"""
	IDEPth = 0
	NATive = 1
	NATIve = 2


# noinspection SpellCheckingInspection
class DvbMarkMode(Enum):
	"""9 Members, FRAMe ... TRIGger"""
	FRAMe = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	RESTart = 4
	SFRame = 5
	SFRAMe = 6
	SOSF = 7
	TRIGger = 8


# noinspection SpellCheckingInspection
class DvbRcs2Mode(Enum):
	"""2 Members, PRED ... USERD"""
	PRED = 0
	USERD = 1


# noinspection SpellCheckingInspection
class DvbRcs2ModType(Enum):
	"""4 Members, BPSK ... QPSK"""
	BPSK = 0
	PSK8 = 1
	QAM16 = 2
	QPSK = 3


# noinspection SpellCheckingInspection
class DvbRcs2PayloadType(Enum):
	"""4 Members, CTRL ... TRAFFIC_CTRL"""
	CTRL = 0
	LOGON = 1
	TRAFFIC = 2
	TRAFFIC_CTRL = 3


# noinspection SpellCheckingInspection
class DvbRcs2SpreadFactor(Enum):
	"""4 Members, SF_16 ... SF_8"""
	SF_16 = 0
	SF_2 = 1
	SF_4 = 2
	SF_8 = 3


# noinspection SpellCheckingInspection
class DvbRcs2TxFormatClassRange(Enum):
	"""2 Members, LM ... SSLM"""
	LM = 0
	SSLM = 1


# noinspection SpellCheckingInspection
class DvbRcs2WaveformId(Enum):
	"""59 Members, LM1 ... SSLM9"""
	LM1 = 0
	LM10 = 1
	LM11 = 2
	LM12 = 3
	LM13 = 4
	LM14 = 5
	LM15 = 6
	LM16 = 7
	LM17 = 8
	LM18 = 9
	LM19 = 10
	LM2 = 11
	LM20 = 12
	LM21 = 13
	LM22 = 14
	LM3 = 15
	LM32 = 16
	LM33 = 17
	LM34 = 18
	LM35 = 19
	LM36 = 20
	LM37 = 21
	LM38 = 22
	LM39 = 23
	LM4 = 24
	LM40 = 25
	LM41 = 26
	LM42 = 27
	LM43 = 28
	LM44 = 29
	LM45 = 30
	LM46 = 31
	LM47 = 32
	LM48 = 33
	LM49 = 34
	LM5 = 35
	LM6 = 36
	LM7 = 37
	LM8 = 38
	LM9 = 39
	SSLM1 = 40
	SSLM10 = 41
	SSLM11 = 42
	SSLM12 = 43
	SSLM13 = 44
	SSLM14 = 45
	SSLM15 = 46
	SSLM16 = 47
	SSLM17 = 48
	SSLM18 = 49
	SSLM19 = 50
	SSLM2 = 51
	SSLM3 = 52
	SSLM4 = 53
	SSLM5 = 54
	SSLM6 = 55
	SSLM7 = 56
	SSLM8 = 57
	SSLM9 = 58


# noinspection SpellCheckingInspection
class DvbS2XccmAcm(Enum):
	"""2 Members, ACM ... CCM"""
	ACM = 0
	CCM = 1


# noinspection SpellCheckingInspection
class DvbS2XcodeType(Enum):
	"""3 Members, MEDium ... SHORt"""
	MEDium = 0
	NORMal = 1
	SHORt = 2


# noinspection SpellCheckingInspection
class DvbS2XcodRate(Enum):
	"""42 Members, CR100D180 ... CR9D20"""
	CR100D180 = 0
	CR104D180 = 1
	CR116D180 = 2
	CR11D20 = 3
	CR11D45 = 4
	CR124D180 = 5
	CR128D180 = 6
	CR132D180 = 7
	CR135D180 = 8
	CR13D18 = 9
	CR13D45 = 10
	CR140D180 = 11
	CR14D45 = 12
	CR154D180 = 13
	CR18D30 = 14
	CR1D2 = 15
	CR1D3 = 16
	CR1D4 = 17
	CR1D5 = 18
	CR20D30 = 19
	CR22D30 = 20
	CR23D36 = 21
	CR25D36 = 22
	CR26D45 = 23
	CR28D45 = 24
	CR2D3 = 25
	CR2D5 = 26
	CR2D9 = 27
	CR32D45 = 28
	CR3D4 = 29
	CR3D5 = 30
	CR4D15 = 31
	CR4D5 = 32
	CR5D6 = 33
	CR7D15 = 34
	CR7D9 = 35
	CR8D15 = 36
	CR8D9 = 37
	CR90D180 = 38
	CR96D180 = 39
	CR9D10 = 40
	CR9D20 = 41


# noinspection SpellCheckingInspection
class DvbS2XmodCod(Enum):
	"""93 Members, APSK128_X_N34 ... QPSK_X_VN29"""
	APSK128_X_N34 = 0
	APSK128_X_N79 = 1
	APSK16_S_23 = 2
	APSK16_S_34 = 3
	APSK16_S_45 = 4
	APSK16_S_56 = 5
	APSK16_S_89 = 6
	APSK16_S_910 = 7
	APSK16_X_N12L = 8
	APSK16_X_N1318 = 9
	APSK16_X_N2336 = 10
	APSK16_X_N23L = 11
	APSK16_X_N2536 = 12
	APSK16_X_N2645 = 13
	APSK16_X_N2845 = 14
	APSK16_X_N35 = 15
	APSK16_X_N35L = 16
	APSK16_X_N59L = 17
	APSK16_X_N7790 = 18
	APSK16_X_N79 = 19
	APSK16_X_N815L = 20
	APSK16_X_S2645 = 21
	APSK16_X_S3245 = 22
	APSK16_X_S35 = 23
	APSK16_X_S715 = 24
	APSK16_X_S815 = 25
	APSK256_X_N1115L = 26
	APSK256_X_N23L = 27
	APSK256_X_N2945L = 28
	APSK256_X_N3145L = 29
	APSK256_X_N3245 = 30
	APSK256_X_N34 = 31
	APSK32_S_34 = 32
	APSK32_S_45 = 33
	APSK32_S_56 = 34
	APSK32_S_89 = 35
	APSK32_S_910 = 36
	APSK32_X_N1115 = 37
	APSK32_X_N23L = 38
	APSK32_X_N3245 = 39
	APSK32_X_N79 = 40
	APSK32_X_S23 = 41
	APSK32_X_S3245 = 42
	APSK64_X_N1115 = 43
	APSK64_X_N3245L = 44
	APSK64_X_N45 = 45
	APSK64_X_N56 = 46
	APSK64_X_N79 = 47
	APSK8_X_N2645L = 48
	APSK8_X_N59L = 49
	BPSK_X_VM1145 = 50
	BPSK_X_VM13 = 51
	BPSK_X_VM15 = 52
	BPSK_X_VS1145 = 53
	BPSK_X_VS13 = 54
	BPSK_X_VS15 = 55
	BPSK_X_VS15S = 56
	BPSK_X_VS415 = 57
	PSK8_S_23 = 58
	PSK8_S_34 = 59
	PSK8_S_35 = 60
	PSK8_S_56 = 61
	PSK8_S_89 = 62
	PSK8_S_910 = 63
	PSK8_X_N1318 = 64
	PSK8_X_N2336 = 65
	PSK8_X_N2536 = 66
	PSK8_X_S2645 = 67
	PSK8_X_S3245 = 68
	PSK8_X_S715 = 69
	PSK8_X_S815 = 70
	QPSK_S_12 = 71
	QPSK_S_13 = 72
	QPSK_S_14 = 73
	QPSK_S_23 = 74
	QPSK_S_25 = 75
	QPSK_S_34 = 76
	QPSK_S_35 = 77
	QPSK_S_45 = 78
	QPSK_S_56 = 79
	QPSK_S_89 = 80
	QPSK_S_910 = 81
	QPSK_X_M15 = 82
	QPSK_X_N1120 = 83
	QPSK_X_N1345 = 84
	QPSK_X_N920 = 85
	QPSK_X_S1145 = 86
	QPSK_X_S1445 = 87
	QPSK_X_S3245 = 88
	QPSK_X_S415 = 89
	QPSK_X_S715 = 90
	QPSK_X_S815 = 91
	QPSK_X_VN29 = 92


# noinspection SpellCheckingInspection
class DvbS2XmodCodUnique(Enum):
	"""130 Members, MCU1 ... MCU99"""
	MCU1 = 0
	MCU10 = 1
	MCU100 = 2
	MCU101 = 3
	MCU102 = 4
	MCU103 = 5
	MCU104 = 6
	MCU105 = 7
	MCU106 = 8
	MCU107 = 9
	MCU108 = 10
	MCU109 = 11
	MCU11 = 12
	MCU110 = 13
	MCU111 = 14
	MCU112 = 15
	MCU113 = 16
	MCU114 = 17
	MCU115 = 18
	MCU116 = 19
	MCU117 = 20
	MCU118 = 21
	MCU119 = 22
	MCU12 = 23
	MCU120 = 24
	MCU121 = 25
	MCU122 = 26
	MCU123 = 27
	MCU124 = 28
	MCU125 = 29
	MCU126 = 30
	MCU127 = 31
	MCU128 = 32
	MCU129 = 33
	MCU13 = 34
	MCU130 = 35
	MCU14 = 36
	MCU15 = 37
	MCU16 = 38
	MCU17 = 39
	MCU18 = 40
	MCU19 = 41
	MCU2 = 42
	MCU20 = 43
	MCU21 = 44
	MCU22 = 45
	MCU23 = 46
	MCU24 = 47
	MCU25 = 48
	MCU26 = 49
	MCU27 = 50
	MCU28 = 51
	MCU29 = 52
	MCU3 = 53
	MCU30 = 54
	MCU31 = 55
	MCU32 = 56
	MCU33 = 57
	MCU34 = 58
	MCU35 = 59
	MCU36 = 60
	MCU37 = 61
	MCU38 = 62
	MCU39 = 63
	MCU4 = 64
	MCU40 = 65
	MCU41 = 66
	MCU42 = 67
	MCU43 = 68
	MCU44 = 69
	MCU45 = 70
	MCU46 = 71
	MCU47 = 72
	MCU48 = 73
	MCU49 = 74
	MCU5 = 75
	MCU50 = 76
	MCU51 = 77
	MCU52 = 78
	MCU53 = 79
	MCU54 = 80
	MCU55 = 81
	MCU56 = 82
	MCU57 = 83
	MCU58 = 84
	MCU59 = 85
	MCU6 = 86
	MCU60 = 87
	MCU61 = 88
	MCU62 = 89
	MCU63 = 90
	MCU64 = 91
	MCU65 = 92
	MCU66 = 93
	MCU67 = 94
	MCU68 = 95
	MCU69 = 96
	MCU7 = 97
	MCU70 = 98
	MCU71 = 99
	MCU72 = 100
	MCU73 = 101
	MCU74 = 102
	MCU75 = 103
	MCU76 = 104
	MCU77 = 105
	MCU78 = 106
	MCU79 = 107
	MCU8 = 108
	MCU80 = 109
	MCU81 = 110
	MCU82 = 111
	MCU83 = 112
	MCU84 = 113
	MCU85 = 114
	MCU86 = 115
	MCU87 = 116
	MCU88 = 117
	MCU89 = 118
	MCU9 = 119
	MCU90 = 120
	MCU91 = 121
	MCU92 = 122
	MCU93 = 123
	MCU94 = 124
	MCU95 = 125
	MCU96 = 126
	MCU97 = 127
	MCU98 = 128
	MCU99 = 129


# noinspection SpellCheckingInspection
class DvbS2Xmodulation(Enum):
	"""14 Members, APSK128 ... QPSK"""
	APSK128 = 0
	APSK16 = 1
	APSK16_8_8 = 2
	APSK256 = 3
	APSK32 = 4
	APSK32_4_12_16R = 5
	APSK32_4_8_4_16 = 6
	APSK64_16_16_16_16 = 7
	APSK64_4_12_20_28 = 8
	APSK64_8_16_20_20 = 9
	APSK8_2_4_2 = 10
	P2BPsk = 11
	PSK8 = 12
	QPSK = 13


# noinspection SpellCheckingInspection
class DvbS2XrollOff(Enum):
	"""6 Members, RO05 ... RO35"""
	RO05 = 0
	RO10 = 1
	RO15 = 2
	RO20 = 3
	RO25 = 4
	RO35 = 5


# noinspection SpellCheckingInspection
class DvbS2XsfFormat(Enum):
	"""8 Members, SFFI0 ... SFFI7"""
	SFFI0 = 0
	SFFI1 = 1
	SFFI2 = 2
	SFFI3 = 3
	SFFI4 = 4
	SFFI5 = 5
	SFFI6 = 6
	SFFI7 = 7


# noinspection SpellCheckingInspection
class DvbS2Xsfpli(Enum):
	"""4 Members, HEFF ... VROB"""
	HEFF = 0
	ROB = 1
	STD = 2
	VROB = 3


# noinspection SpellCheckingInspection
class DvbS2XstmType(Enum):
	"""4 Members, GC ... TRANsport"""
	GC = 0
	GHEM = 1
	GP = 2
	TRANsport = 3


# noinspection SpellCheckingInspection
class DvbStandard(Enum):
	"""5 Members, DVBH ... DVBX"""
	DVBH = 0
	DVBR = 1
	DVBS = 2
	DVBT = 3
	DVBX = 4


# noinspection SpellCheckingInspection
class DvbSysBand(Enum):
	"""4 Members, _5 ... _8"""
	_5 = 0
	_6 = 1
	_7 = 2
	_8 = 3


# noinspection SpellCheckingInspection
class DvbTranMode(Enum):
	"""3 Members, T2K ... T8K"""
	T2K = 0
	T4K = 1
	T8K = 2


# noinspection SpellCheckingInspection
class EidNr5GolpcParamSetTypeAll(Enum):
	"""3 Members, S1 ... SNC"""
	S1 = 0
	S2 = 1
	SNC = 2


# noinspection SpellCheckingInspection
class EidNr5GresAllocUserAlloc(Enum):
	"""3 Members, T0 ... T2"""
	T0 = 0
	T1 = 1
	T2 = 2


# noinspection SpellCheckingInspection
class EidNr5GscsGeneral(Enum):
	"""7 Members, SCS120 ... SCS960"""
	SCS120 = 0
	SCS15 = 1
	SCS240 = 2
	SCS30 = 3
	SCS480 = 4
	SCS60 = 5
	SCS960 = 6


# noinspection SpellCheckingInspection
class ElevMaskType(Enum):
	"""2 Members, ETANgent ... LHORizon"""
	ETANgent = 0
	LHORizon = 1


# noinspection SpellCheckingInspection
class EnhBitErr(Enum):
	"""2 Members, PHYSical ... TRANsport"""
	PHYSical = 0
	TRANsport = 1


# noinspection SpellCheckingInspection
class EnhHsHarqMode(Enum):
	"""2 Members, CACK ... CNACk"""
	CACK = 0
	CNACk = 1


# noinspection SpellCheckingInspection
class EnhTchErr(Enum):
	"""4 Members, CON2 ... TURBo3"""
	CON2 = 0
	CON3 = 1
	NONE = 2
	TURBo3 = 3


# noinspection SpellCheckingInspection
class EpdcchTransType(Enum):
	"""2 Members, DISTributed ... LOCalized"""
	DISTributed = 0
	LOCalized = 1


# noinspection SpellCheckingInspection
class EphAge(Enum):
	"""3 Members, A30M ... A60M"""
	A30M = 0
	A45M = 1
	A60M = 2


# noinspection SpellCheckingInspection
class EphSatType(Enum):
	"""3 Members, GLO ... GLOM"""
	GLO = 0
	GLOK = 1
	GLOM = 2


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
class EutraBbFreqSweepMode(Enum):
	"""3 Members, AFTer ... OFF"""
	AFTer = 0
	BEFore = 1
	OFF = 2


# noinspection SpellCheckingInspection
class EutraBfaNtSet(Enum):
	"""19 Members, AP107 ... AP8"""
	AP107 = 0
	AP107108 = 1
	AP107109 = 2
	AP108 = 3
	AP109 = 4
	AP11 = 5
	AP110 = 6
	AP1113 = 7
	AP13 = 8
	AP5 = 9
	AP7 = 10
	AP710 = 11
	AP711 = 12
	AP712 = 13
	AP713 = 14
	AP714 = 15
	AP78 = 16
	AP79 = 17
	AP8 = 18


# noinspection SpellCheckingInspection
class EutraBfaNtSetEmtc(Enum):
	"""16 Members, AP107 ... AP8"""
	AP107 = 0
	AP107108 = 1
	AP107109 = 2
	AP108 = 3
	AP109 = 4
	AP110 = 5
	AP5 = 6
	AP7 = 7
	AP710 = 8
	AP711 = 9
	AP712 = 10
	AP713 = 11
	AP714 = 12
	AP78 = 13
	AP79 = 14
	AP8 = 15


# noinspection SpellCheckingInspection
class EutraBitmap(Enum):
	"""2 Members, _10 ... _40"""
	_10 = 0
	_40 = 1


# noinspection SpellCheckingInspection
class EutraBlockOutput(Enum):
	"""8 Members, OUT0 ... OUT7"""
	OUT0 = 0
	OUT1 = 1
	OUT2 = 2
	OUT3 = 3
	OUT4 = 4
	OUT5 = 5
	OUT6 = 6
	OUT7 = 7


# noinspection SpellCheckingInspection
class EutraCaChannelBandwidth(Enum):
	"""6 Members, BW1_40 ... BW5_00"""
	BW1_40 = 0
	BW10_00 = 1
	BW15_00 = 2
	BW20_00 = 3
	BW3_00 = 4
	BW5_00 = 5


# noinspection SpellCheckingInspection
class EutraCcIndexS(Enum):
	"""5 Members, NONE ... SC4"""
	NONE = 0
	SC1 = 1
	SC2 = 2
	SC3 = 3
	SC4 = 4


# noinspection SpellCheckingInspection
class EutraCeLevel(Enum):
	"""2 Members, CE01 ... CE23"""
	CE01 = 0
	CE23 = 1


# noinspection SpellCheckingInspection
class EuTraClockMode(Enum):
	"""3 Members, CUSTom ... SAMPle"""
	CUSTom = 0
	MSAMp = 1
	SAMPle = 2


# noinspection SpellCheckingInspection
class EutraCsiRsCdmType(Enum):
	"""3 Members, _2 ... _8"""
	_2 = 0
	_4 = 1
	_8 = 2


# noinspection SpellCheckingInspection
class EutraCsiRsFreqDensity(Enum):
	"""3 Members, D1 ... D13"""
	D1 = 0
	D12 = 1
	D13 = 2


# noinspection SpellCheckingInspection
class EutraCsiRsNumCfg(Enum):
	"""6 Members, _1 ... _7"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3
	_5 = 4
	_7 = 5


# noinspection SpellCheckingInspection
class EutraCsiRsTransComb(Enum):
	"""3 Members, _0 ... _2"""
	_0 = 0
	_1 = 1
	_2 = 2


# noinspection SpellCheckingInspection
class EutraCw1CodeWord(Enum):
	"""2 Members, CW11 ... CW12"""
	CW11 = 0
	CW12 = 1


# noinspection SpellCheckingInspection
class EutraDataSourceDlNbiot(Enum):
	"""19 Members, DLISt ... ZERO"""
	DLISt = 0
	MIB = 1
	ONE = 2
	PATTern = 3
	PN11 = 4
	PN15 = 5
	PN16 = 6
	PN20 = 7
	PN21 = 8
	PN23 = 9
	PN9 = 10
	PRNTi = 11
	RARNti = 12
	SIB1nb = 13
	USER1 = 14
	USER2 = 15
	USER3 = 16
	USER4 = 17
	ZERO = 18


# noinspection SpellCheckingInspection
class EutraDciFormat(Enum):
	"""13 Members, F0 ... F3A"""
	F0 = 0
	F1 = 1
	F1A = 2
	F1B = 3
	F1C = 4
	F1D = 5
	F2 = 6
	F2A = 7
	F2B = 8
	F2C = 9
	F2D = 10
	F3 = 11
	F3A = 12


# noinspection SpellCheckingInspection
class EutraDciFormatEmtc(Enum):
	"""7 Members, F3 ... F62"""
	F3 = 0
	F3A = 1
	F60A = 2
	F60B = 3
	F61A = 4
	F61B = 5
	F62 = 6


# noinspection SpellCheckingInspection
class EutraDlDataSourceUser(Enum):
	"""18 Members, DLISt ... ZERO"""
	DLISt = 0
	MCCH = 1
	MIB = 2
	MTCH = 3
	ONE = 4
	PATTern = 5
	PN11 = 6
	PN15 = 7
	PN16 = 8
	PN20 = 9
	PN21 = 10
	PN23 = 11
	PN9 = 12
	USER1 = 13
	USER2 = 14
	USER3 = 15
	USER4 = 16
	ZERO = 17


# noinspection SpellCheckingInspection
class EutraDleMtcContentType(Enum):
	"""5 Members, MPD1 ... PSIB"""
	MPD1 = 0
	MPD2 = 1
	PBCH = 2
	PDSCh = 3
	PSIB = 4


# noinspection SpellCheckingInspection
class EutraDlNbiotContentType(Enum):
	"""4 Members, NPBCh ... NSIB"""
	NPBCh = 0
	NPDCch = 1
	NPDSch = 2
	NSIB = 3


# noinspection SpellCheckingInspection
class EutraDlNbiotRbIndex(Enum):
	"""37 Members, _12 ... USER"""
	_12 = 0
	_14 = 1
	_17 = 2
	_19 = 3
	_2 = 4
	_22 = 5
	_24 = 6
	_27 = 7
	_29 = 8
	_30 = 9
	_32 = 10
	_34 = 11
	_35 = 12
	_39 = 13
	_4 = 14
	_40 = 15
	_42 = 16
	_44 = 17
	_45 = 18
	_47 = 19
	_52 = 20
	_55 = 21
	_57 = 22
	_60 = 23
	_62 = 24
	_65 = 25
	_67 = 26
	_7 = 27
	_70 = 28
	_72 = 29
	_75 = 30
	_80 = 31
	_85 = 32
	_9 = 33
	_90 = 34
	_95 = 35
	USER = 36


# noinspection SpellCheckingInspection
class EutraDlNbiotStartSymbols(Enum):
	"""4 Members, SYM0 ... SYM3"""
	SYM0 = 0
	SYM1 = 1
	SYM2 = 2
	SYM3 = 3


# noinspection SpellCheckingInspection
class EutraDuplexMode(Enum):
	"""2 Members, FDD ... TDD"""
	FDD = 0
	TDD = 1


# noinspection SpellCheckingInspection
class EuTraDuration(Enum):
	"""2 Members, EXTended ... NORMal"""
	EXTended = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class EutraEmtcMpdcchNumRepetitions(Enum):
	"""9 Members, _1 ... _8"""
	_1 = 0
	_128 = 1
	_16 = 2
	_2 = 3
	_256 = 4
	_32 = 5
	_4 = 6
	_64 = 7
	_8 = 8


# noinspection SpellCheckingInspection
class EutraEmtcMpdcchStartSf(Enum):
	"""9 Members, S1 ... S8"""
	S1 = 0
	S1_5 = 1
	S10 = 2
	S2 = 3
	S2_5 = 4
	S20 = 5
	S4 = 6
	S5 = 7
	S8 = 8


# noinspection SpellCheckingInspection
class EutraEmtcPdcchCfg(Enum):
	"""6 Members, PRNTi ... USER4"""
	PRNTi = 0
	RARNti = 1
	USER1 = 2
	USER2 = 3
	USER3 = 4
	USER4 = 5


# noinspection SpellCheckingInspection
class EutraEmtcPdschNumRepetitions(Enum):
	"""12 Members, _1024 ... NON"""
	_1024 = 0
	_1536 = 1
	_16 = 2
	_192 = 3
	_2048 = 4
	_256 = 5
	_32 = 6
	_384 = 7
	_512 = 8
	_64 = 9
	_786 = 10
	NON = 11


# noinspection SpellCheckingInspection
class EutraEmtcPdschWideband(Enum):
	"""3 Members, BW20_00 ... OFF"""
	BW20_00 = 0
	BW5_00 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class EutraEmtcRbCnt(Enum):
	"""8 Members, CN12 ... CN9"""
	CN12 = 0
	CN15 = 1
	CN18 = 2
	CN21 = 3
	CN24 = 4
	CN3 = 5
	CN6 = 6
	CN9 = 7


# noinspection SpellCheckingInspection
class EutraEmtcVrbOffs(Enum):
	"""8 Members, OS0 ... OS9"""
	OS0 = 0
	OS12 = 1
	OS15 = 2
	OS18 = 3
	OS21 = 4
	OS3 = 5
	OS6 = 6
	OS9 = 7


# noinspection SpellCheckingInspection
class EutraIotHoppingIvl(Enum):
	"""9 Members, H1 ... H8"""
	H1 = 0
	H10 = 1
	H16 = 2
	H2 = 3
	H20 = 4
	H4 = 5
	H40 = 6
	H5 = 7
	H8 = 8


# noinspection SpellCheckingInspection
class EutraIotRepetitions(Enum):
	"""18 Members, R1 ... R8"""
	R1 = 0
	R1024 = 1
	R12 = 2
	R128 = 3
	R1536 = 4
	R16 = 5
	R192 = 6
	R2 = 7
	R2048 = 8
	R24 = 9
	R256 = 10
	R32 = 11
	R384 = 12
	R4 = 13
	R512 = 14
	R64 = 15
	R768 = 16
	R8 = 17


# noinspection SpellCheckingInspection
class EutraIotRepetitionsTcw(Enum):
	"""7 Members, R1 ... R8"""
	R1 = 0
	R16 = 1
	R2 = 2
	R32 = 3
	R4 = 4
	R64 = 5
	R8 = 6


# noinspection SpellCheckingInspection
class EutraIotRu(Enum):
	"""8 Members, RU1 ... RU8"""
	RU1 = 0
	RU10 = 1
	RU2 = 2
	RU3 = 3
	RU4 = 4
	RU5 = 5
	RU6 = 6
	RU8 = 7


# noinspection SpellCheckingInspection
class EutraLaadci1Cmode(Enum):
	"""4 Members, MANual ... N1N"""
	MANual = 0
	N = 1
	N1 = 2
	N1N = 3


# noinspection SpellCheckingInspection
class EutraLaalAstSf(Enum):
	"""7 Members, SY10 ... SY9"""
	SY10 = 0
	SY11 = 1
	SY12 = 2
	SY14 = 3
	SY3 = 4
	SY6 = 5
	SY9 = 6


# noinspection SpellCheckingInspection
class EutraLaaStartingSlots(Enum):
	"""2 Members, FIRSt ... SECond"""
	FIRSt = 0
	SECond = 1


# noinspection SpellCheckingInspection
class EutraMarkMode(Enum):
	"""8 Members, FAP ... TRIGger"""
	FAP = 0
	FRAM = 1
	PERiod = 2
	RATio = 3
	RESTart = 4
	SFNRestart = 5
	SUBFram = 6
	TRIGger = 7


# noinspection SpellCheckingInspection
class EutraMbsfnNotRepCoef(Enum):
	"""2 Members, NRC2 ... NRC4"""
	NRC2 = 0
	NRC4 = 1


# noinspection SpellCheckingInspection
class EutraMbsfnRfAllPer(Enum):
	"""6 Members, AP1 ... AP8"""
	AP1 = 0
	AP16 = 1
	AP2 = 2
	AP32 = 3
	AP4 = 4
	AP8 = 5


# noinspection SpellCheckingInspection
class EutraMbsfnSfAllMode(Enum):
	"""2 Members, F1 ... F4"""
	F1 = 0
	F4 = 1


# noinspection SpellCheckingInspection
class EutraMbsfnType(Enum):
	"""2 Members, MIXed ... OFF"""
	MIXed = 0
	OFF = 1


# noinspection SpellCheckingInspection
class EutraMcchMcs(Enum):
	"""4 Members, MCS13 ... MCS7"""
	MCS13 = 0
	MCS19 = 1
	MCS2 = 2
	MCS7 = 3


# noinspection SpellCheckingInspection
class EutraMcchModPer(Enum):
	"""2 Members, MP1024 ... MP512"""
	MP1024 = 0
	MP512 = 1


# noinspection SpellCheckingInspection
class EutraMcchRepPer(Enum):
	"""4 Members, RP128 ... RP64"""
	RP128 = 0
	RP256 = 1
	RP32 = 2
	RP64 = 3


# noinspection SpellCheckingInspection
class EutraMchSchedPer(Enum):
	"""9 Members, SPM ... SPRF8"""
	SPM = 0
	SPRF1024 = 1
	SPRF128 = 2
	SPRF16 = 3
	SPRF256 = 4
	SPRF32 = 5
	SPRF512 = 6
	SPRF64 = 7
	SPRF8 = 8


# noinspection SpellCheckingInspection
class EutraMcsTable(Enum):
	"""8 Members, _0 ... T4"""
	_0 = 0
	_1 = 1
	OFF = 2
	ON = 3
	T1 = 4
	T2 = 5
	T3 = 6
	T4 = 7


# noinspection SpellCheckingInspection
class EutraModulationDlNbiot(Enum):
	"""1 Members, QPSK ... QPSK"""
	QPSK = 0


# noinspection SpellCheckingInspection
class EutraMpdcchFormat(Enum):
	"""6 Members, _0 ... _5"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	_4 = 4
	_5 = 5


# noinspection SpellCheckingInspection
class EutraMtchSfAllPer(Enum):
	"""7 Members, AP128 ... AP8"""
	AP128 = 0
	AP16 = 1
	AP256 = 2
	AP32 = 3
	AP4 = 4
	AP64 = 5
	AP8 = 6


# noinspection SpellCheckingInspection
class EutraNbiotDciDistNpdcchNpdsch(Enum):
	"""3 Members, MIN ... ZERO"""
	MIN = 0
	STD = 1
	ZERO = 2


# noinspection SpellCheckingInspection
class EutraNbiotDciFormat(Enum):
	"""3 Members, N0 ... N2"""
	N0 = 0
	N1 = 1
	N2 = 2


# noinspection SpellCheckingInspection
class EutraNbiotEdtTranBlckSizeA(Enum):
	"""9 Members, _1000 ... _936"""
	_1000 = 0
	_328 = 1
	_408 = 2
	_504 = 3
	_584 = 4
	_680 = 5
	_808 = 6
	_88 = 7
	_936 = 8


# noinspection SpellCheckingInspection
class EutraNbiotEdtTranBlckSizeB(Enum):
	"""13 Members, _1000 ... _936"""
	_1000 = 0
	_328 = 1
	_408 = 2
	_456 = 3
	_504 = 4
	_536 = 5
	_584 = 6
	_680 = 7
	_712 = 8
	_776 = 9
	_808 = 10
	_88 = 11
	_936 = 12


# noinspection SpellCheckingInspection
class EutraNbiotGapDurationCoefficent(Enum):
	"""4 Members, _1_2 ... _3_8"""
	_1_2 = 0
	_1_4 = 1
	_1_8 = 2
	_3_8 = 3


# noinspection SpellCheckingInspection
class EutraNbiotGapPeriodicity(Enum):
	"""4 Members, _128 ... _64"""
	_128 = 0
	_256 = 1
	_512 = 2
	_64 = 3


# noinspection SpellCheckingInspection
class EutraNbiotGapThreshold(Enum):
	"""4 Members, _128 ... _64"""
	_128 = 0
	_256 = 1
	_32 = 2
	_64 = 3


# noinspection SpellCheckingInspection
class EutraNbiotInbandBitmapSfAll(Enum):
	"""2 Members, N10 ... N40"""
	N10 = 0
	N40 = 1


# noinspection SpellCheckingInspection
class EutraNbiotNprsConfigbPeriod(Enum):
	"""4 Members, PD_1280 ... PD_640"""
	PD_1280 = 0
	PD_160 = 1
	PD_320 = 2
	PD_640 = 3


# noinspection SpellCheckingInspection
class EutraNbiotNprsConfigbSfnumb(Enum):
	"""8 Members, SFNM_10 ... SFNM_80"""
	SFNM_10 = 0
	SFNM_1280 = 1
	SFNM_160 = 2
	SFNM_20 = 3
	SFNM_320 = 4
	SFNM_40 = 5
	SFNM_640 = 6
	SFNM_80 = 7


# noinspection SpellCheckingInspection
class EutraNbiotNprsConfigbStartsf(Enum):
	"""8 Members, STSF0_8 ... STSF7_8"""
	STSF0_8 = 0
	STSF1_8 = 1
	STSF2_8 = 2
	STSF3_8 = 3
	STSF4_8 = 4
	STSF5_8 = 5
	STSF6_8 = 6
	STSF7_8 = 7


# noinspection SpellCheckingInspection
class EutraNbiotNprsConfigType(Enum):
	"""3 Members, PA_A ... PA_B"""
	PA_A = 0
	PA_AB = 1
	PA_B = 2


# noinspection SpellCheckingInspection
class EutraNbiotNpuschFormat(Enum):
	"""2 Members, F1 ... F2"""
	F1 = 0
	F2 = 1


# noinspection SpellCheckingInspection
class EutraNbiotRmAx(Enum):
	"""12 Members, R1 ... R8"""
	R1 = 0
	R1024 = 1
	R128 = 2
	R16 = 3
	R2 = 4
	R2048 = 5
	R256 = 6
	R32 = 7
	R4 = 8
	R512 = 9
	R64 = 10
	R8 = 11


# noinspection SpellCheckingInspection
class EutraNbiotSearchSpaceOffset(Enum):
	"""4 Members, O0 ... O3_8"""
	O0 = 0
	O1_4 = 1
	O1_8 = 2
	O3_8 = 3


# noinspection SpellCheckingInspection
class EutraNbiotSearchSpaceStSubFrame(Enum):
	"""8 Members, S1_5 ... S8"""
	S1_5 = 0
	S16 = 1
	S2 = 2
	S32 = 3
	S4 = 4
	S48 = 5
	S64 = 6
	S8 = 7


# noinspection SpellCheckingInspection
class EutraNbiotSimAnt(Enum):
	"""4 Members, ALL ... NONE"""
	ALL = 0
	ANT1 = 1
	ANT2 = 2
	NONE = 3


# noinspection SpellCheckingInspection
class EutraNbiotWusDurationFormat(Enum):
	"""11 Members, DN_1 ... DN_8"""
	DN_1 = 0
	DN_1024 = 1
	DN_128 = 2
	DN_16 = 3
	DN_2 = 4
	DN_256 = 5
	DN_32 = 6
	DN_4 = 7
	DN_512 = 8
	DN_64 = 9
	DN_8 = 10


# noinspection SpellCheckingInspection
class EutraNbiotWusTimeOffsetFormat(Enum):
	"""4 Members, TO_40 ... TO240"""
	TO_40 = 0
	TO_80 = 1
	TO160 = 2
	TO240 = 3


# noinspection SpellCheckingInspection
class EutraNbMimoConf(Enum):
	"""2 Members, TX1 ... TX2"""
	TX1 = 0
	TX2 = 1


# noinspection SpellCheckingInspection
class EutraNumUpPts(Enum):
	"""3 Members, _0 ... _4"""
	_0 = 0
	_2 = 1
	_4 = 2


# noinspection SpellCheckingInspection
class EutraPdccFmtLaa(Enum):
	"""2 Members, F2 ... F3"""
	F2 = 0
	F3 = 1


# noinspection SpellCheckingInspection
class EutraPdcchCfg(Enum):
	"""17 Members, CCRNti ... USER4"""
	CCRNti = 0
	NONE = 1
	PRNTi = 2
	RARNti = 3
	SIRNti = 4
	U1Eimta = 5
	U1SPs = 6
	U2Eimta = 7
	U2SPs = 8
	U3Eimta = 9
	U3SPs = 10
	U4Eimta = 11
	U4SPs = 12
	USER1 = 13
	USER2 = 14
	USER3 = 15
	USER4 = 16


# noinspection SpellCheckingInspection
class EutraPdcchType(Enum):
	"""3 Members, EPD1 ... PDCCh"""
	EPD1 = 0
	EPD2 = 1
	PDCCh = 2


# noinspection SpellCheckingInspection
class EutraPdcchTypeEmtc(Enum):
	"""2 Members, MPD1 ... MPD2"""
	MPD1 = 0
	MPD2 = 1


# noinspection SpellCheckingInspection
class EutraPowcLevRef(Enum):
	"""5 Members, DRMS ... URMS"""
	DRMS = 0
	FRMS = 1
	NPBCH = 2
	UEBurst = 3
	URMS = 4


# noinspection SpellCheckingInspection
class EutraPowcRefChan(Enum):
	"""7 Members, NF ... SRS"""
	NF = 0
	PRACH = 1
	PUCCH = 2
	PUCPUS = 3
	PUSCH = 4
	SL = 5
	SRS = 6


# noinspection SpellCheckingInspection
class EutraPrachPreambleSet(Enum):
	"""5 Members, ARES ... URES"""
	ARES = 0
	BRES = 1
	OFF = 2
	ON = 3
	URES = 4


# noinspection SpellCheckingInspection
class EutraPracNbiotPeriodicity(Enum):
	"""10 Members, _10240 ... _80"""
	_10240 = 0
	_1280 = 1
	_160 = 2
	_240 = 3
	_2560 = 4
	_320 = 5
	_40 = 6
	_5120 = 7
	_640 = 8
	_80 = 9


# noinspection SpellCheckingInspection
class EutraPracNbiotPreambleFormat(Enum):
	"""7 Members, _0 ... F2"""
	_0 = 0
	_1 = 1
	F0 = 2
	F0A = 3
	F1 = 4
	F1A = 5
	F2 = 6


# noinspection SpellCheckingInspection
class EutraPracNbiotStartTimeMs(Enum):
	"""18 Members, _10 ... _80"""
	_10 = 0
	_1024 = 1
	_128 = 2
	_1280 = 3
	_16 = 4
	_160 = 5
	_20 = 6
	_256 = 7
	_2560 = 8
	_32 = 9
	_320 = 10
	_40 = 11
	_512 = 12
	_5120 = 13
	_64 = 14
	_640 = 15
	_8 = 16
	_80 = 17


# noinspection SpellCheckingInspection
class EutraPracNbiotSubcarrierOffset(Enum):
	"""18 Members, _0 ... _90"""
	_0 = 0
	_102 = 1
	_108 = 2
	_12 = 3
	_18 = 4
	_2 = 5
	_24 = 6
	_34 = 7
	_36 = 8
	_42 = 9
	_48 = 10
	_54 = 11
	_6 = 12
	_60 = 13
	_72 = 14
	_78 = 15
	_84 = 16
	_90 = 17


# noinspection SpellCheckingInspection
class EutraPracNbiotSubcarriers(Enum):
	"""4 Members, _12 ... _48"""
	_12 = 0
	_24 = 1
	_36 = 2
	_48 = 3


# noinspection SpellCheckingInspection
class EutraPuccN1Dmrs(Enum):
	"""8 Members, _0 ... _9"""
	_0 = 0
	_10 = 1
	_2 = 2
	_3 = 3
	_4 = 4
	_6 = 5
	_8 = 6
	_9 = 7


# noinspection SpellCheckingInspection
class EutraRepetitionsNbiot(Enum):
	"""8 Members, R1 ... R8"""
	R1 = 0
	R128 = 1
	R16 = 2
	R2 = 3
	R32 = 4
	R4 = 5
	R64 = 6
	R8 = 7


# noinspection SpellCheckingInspection
class EutraSciFormat(Enum):
	"""1 Members, _0 ... _0"""
	_0 = 0


# noinspection SpellCheckingInspection
class EutraSearchSpace(Enum):
	"""7 Members, _0 ... UE"""
	_0 = 0
	_1 = 1
	AUTO = 2
	COMMon = 3
	OFF = 4
	ON = 5
	UE = 6


# noinspection SpellCheckingInspection
class EutraSearchSpaceEmtc(Enum):
	"""4 Members, T0CM ... UE"""
	T0CM = 0
	T1CM = 1
	T2CM = 2
	UE = 3


# noinspection SpellCheckingInspection
class EutraSearchSpaceNbiot(Enum):
	"""3 Members, T1CM ... UE"""
	T1CM = 0
	T2CM = 1
	UE = 2


# noinspection SpellCheckingInspection
class EutraSerialRate(Enum):
	"""3 Members, SR1_6M ... SR115_2K"""
	SR1_6M = 0
	SR1_92M = 1
	SR115_2K = 2


# noinspection SpellCheckingInspection
class EutraSlCommControlPeriod(Enum):
	"""10 Members, _120 ... _80"""
	_120 = 0
	_140 = 1
	_160 = 2
	_240 = 3
	_280 = 4
	_320 = 5
	_40 = 6
	_60 = 7
	_70 = 8
	_80 = 9


# noinspection SpellCheckingInspection
class EutraSlDiscControlPeriod(Enum):
	"""6 Members, _1024 ... _64"""
	_1024 = 0
	_128 = 1
	_256 = 2
	_32 = 3
	_512 = 4
	_64 = 5


# noinspection SpellCheckingInspection
class EutraSlDiscType(Enum):
	"""2 Members, D1 ... D2B"""
	D1 = 0
	D2B = 1


# noinspection SpellCheckingInspection
class EutraSlMode(Enum):
	"""3 Members, COMM ... V2X"""
	COMM = 0
	DISC = 1
	V2X = 2


# noinspection SpellCheckingInspection
class EutraSlN3Pdsch(Enum):
	"""2 Members, _1 ... _5"""
	_1 = 0
	_5 = 1


# noinspection SpellCheckingInspection
class EutraSlV2xBmpLength(Enum):
	"""8 Members, _10 ... _60"""
	_10 = 0
	_100 = 1
	_16 = 2
	_20 = 3
	_30 = 4
	_40 = 5
	_50 = 6
	_60 = 7


# noinspection SpellCheckingInspection
class EutraSlV2xNumSubchannels(Enum):
	"""7 Members, _1 ... _8"""
	_1 = 0
	_10 = 1
	_15 = 2
	_20 = 3
	_3 = 4
	_5 = 5
	_8 = 6


# noinspection SpellCheckingInspection
class EutraSlV2xRmc(Enum):
	"""3 Members, R821 ... R823"""
	R821 = 0
	R822 = 1
	R823 = 2


# noinspection SpellCheckingInspection
class EutraSlV2xSubchannelSize(Enum):
	"""20 Members, _10 ... _96"""
	_10 = 0
	_100 = 1
	_12 = 2
	_15 = 3
	_16 = 4
	_18 = 5
	_20 = 6
	_25 = 7
	_30 = 8
	_32 = 9
	_4 = 10
	_48 = 11
	_5 = 12
	_50 = 13
	_6 = 14
	_72 = 15
	_75 = 16
	_8 = 17
	_9 = 18
	_96 = 19


# noinspection SpellCheckingInspection
class EutraStdMode(Enum):
	"""3 Members, IOT ... LTE"""
	IOT = 0
	LIOT = 1
	LTE = 2


# noinspection SpellCheckingInspection
class EutraSubCarrierSpacing(Enum):
	"""2 Members, S15 ... S375"""
	S15 = 0
	S375 = 1


# noinspection SpellCheckingInspection
class EutraTcwaNtSubset(Enum):
	"""5 Members, ALL ... AS78"""
	ALL = 0
	AS12 = 1
	AS34 = 2
	AS56 = 3
	AS78 = 4


# noinspection SpellCheckingInspection
class EutraTcwBurstFormat(Enum):
	"""5 Members, BF0 ... BF4"""
	BF0 = 0
	BF1 = 1
	BF2 = 2
	BF3 = 3
	BF4 = 4


# noinspection SpellCheckingInspection
class EutraTcwcHanBw(Enum):
	"""7 Members, BW00_20 ... BW5_00"""
	BW00_20 = 0
	BW1_40 = 1
	BW10_00 = 2
	BW15_00 = 3
	BW20_00 = 4
	BW3_00 = 5
	BW5_00 = 6


# noinspection SpellCheckingInspection
class EutraTcwConnector(Enum):
	"""3 Members, GLOBal ... NOFB"""
	GLOBal = 0
	LOCal = 1
	NOFB = 2


# noinspection SpellCheckingInspection
class EutraTcwfRactMaxThroughput(Enum):
	"""2 Members, FMT30 ... FMT70"""
	FMT30 = 0
	FMT70 = 1


# noinspection SpellCheckingInspection
class EutraTcwfReqAlloc(Enum):
	"""2 Members, HIGHer ... LOWer"""
	HIGHer = 0
	LOWer = 1


# noinspection SpellCheckingInspection
class EutraTcwfReqOffset(Enum):
	"""5 Members, FO_0 ... FO_625"""
	FO_0 = 0
	FO_1340 = 1
	FO_200 = 2
	FO_270 = 3
	FO_625 = 4


# noinspection SpellCheckingInspection
class EutraTcwfReqShift(Enum):
	"""13 Members, FS0 ... FS9"""
	FS0 = 0
	FS1 = 1
	FS10 = 2
	FS13 = 3
	FS14 = 4
	FS19 = 5
	FS2 = 6
	FS24 = 7
	FS3 = 8
	FS4 = 9
	FS5 = 10
	FS7 = 11
	FS9 = 12


# noinspection SpellCheckingInspection
class EutraTcwGeneratedSig(Enum):
	"""6 Members, ALL ... WSUE3UE4"""
	ALL = 0
	IF = 1
	IF23 = 2
	WSIF1AWGN = 3
	WSUE1UE2AWGN = 4
	WSUE3UE4 = 5


# noinspection SpellCheckingInspection
class EutraTcwGsModeDefaultRange(Enum):
	"""3 Members, ADRate ... FDRate"""
	ADRate = 0
	DRATe = 1
	FDRate = 2


# noinspection SpellCheckingInspection
class EutraTcwiNstSetup(Enum):
	"""2 Members, U1PATH ... U2PATH"""
	U1PATH = 0
	U2PATH = 1


# noinspection SpellCheckingInspection
class EutraTcwInterfType(Enum):
	"""4 Members, CW ... UTRA"""
	CW = 0
	EUTra = 1
	NEUTra = 2
	UTRA = 3


# noinspection SpellCheckingInspection
class EutraTcwMarkConf(Enum):
	"""2 Members, FRAMe ... UNCHanged"""
	FRAMe = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class EutraTcwNumOfRxAnt(Enum):
	"""3 Members, ANT1 ... ANT4"""
	ANT1 = 0
	ANT2 = 1
	ANT4 = 2


# noinspection SpellCheckingInspection
class EutraTcwoFfsChanEdge(Enum):
	"""3 Members, OCE12_5 ... OCE7_5"""
	OCE12_5 = 0
	OCE2_5 = 1
	OCE7_5 = 2


# noinspection SpellCheckingInspection
class EutraTcwPropagCond(Enum):
	"""14 Members, AWGNonly ... PDMov"""
	AWGNonly = 0
	EPA1 = 1
	EPA5 = 2
	ETU1 = 3
	ETU200 = 4
	ETU200Mov = 5
	ETU300 = 6
	ETU5 = 7
	ETU70 = 8
	EVA5 = 9
	EVA70 = 10
	HST1 = 11
	HST3 = 12
	PDMov = 13


# noinspection SpellCheckingInspection
class EutraTcwRelease(Enum):
	"""6 Members, REL10 ... REL9"""
	REL10 = 0
	REL11 = 1
	REL12 = 2
	REL13TO15 = 3
	REL8 = 4
	REL9 = 5


# noinspection SpellCheckingInspection
class EutraTcwrtfMode(Enum):
	"""3 Members, BIN ... SER3X8"""
	BIN = 0
	SER = 1
	SER3X8 = 2


# noinspection SpellCheckingInspection
class EutraTcwsIgAdvNtaOffs(Enum):
	"""2 Members, NTA0 ... NTA624"""
	NTA0 = 0
	NTA624 = 1


# noinspection SpellCheckingInspection
class EutraTcwSignalRout(Enum):
	"""2 Members, PORTA ... PORTB"""
	PORTA = 0
	PORTB = 1


# noinspection SpellCheckingInspection
class EutraTcwtRigConf(Enum):
	"""2 Members, AAUTo ... UNCHanged"""
	AAUTo = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class EutraTestCaseTs36141(Enum):
	"""37 Members, TS36141_TC626 ... TS36141_TC853"""
	TS36141_TC626 = 0
	TS36141_TC627 = 1
	TS36141_TC628 = 2
	TS36141_TC67 = 3
	TS36141_TC72 = 4
	TS36141_TC73 = 5
	TS36141_TC74 = 6
	TS36141_TC75A = 7
	TS36141_TC75B = 8
	TS36141_TC76 = 9
	TS36141_TC78 = 10
	TS36141_TC821 = 11
	TS36141_TC821A = 12
	TS36141_TC822 = 13
	TS36141_TC823 = 14
	TS36141_TC824 = 15
	TS36141_TC826 = 16
	TS36141_TC826A = 17
	TS36141_TC827 = 18
	TS36141_TC829 = 19
	TS36141_TC831 = 20
	TS36141_TC8310 = 21
	TS36141_TC8311 = 22
	TS36141_TC8312 = 23
	TS36141_TC8313 = 24
	TS36141_TC832 = 25
	TS36141_TC833 = 26
	TS36141_TC834 = 27
	TS36141_TC835 = 28
	TS36141_TC836 = 29
	TS36141_TC837 = 30
	TS36141_TC838 = 31
	TS36141_TC839 = 32
	TS36141_TC841 = 33
	TS36141_TC851 = 34
	TS36141_TC852 = 35
	TS36141_TC853 = 36


# noinspection SpellCheckingInspection
class EutraTxMode(Enum):
	"""11 Members, M1 ... USER"""
	M1 = 0
	M10 = 1
	M2 = 2
	M3 = 3
	M4 = 4
	M5 = 5
	M6 = 6
	M7 = 7
	M8 = 8
	M9 = 9
	USER = 10


# noinspection SpellCheckingInspection
class EutraUeCat(Enum):
	"""25 Members, C1 ... USER"""
	C1 = 0
	C10 = 1
	C11 = 2
	C12 = 3
	C13 = 4
	C14 = 5
	C15 = 6
	C16 = 7
	C17 = 8
	C18 = 9
	C19 = 10
	C2 = 11
	C20 = 12
	C3 = 13
	C4 = 14
	C5 = 15
	C6 = 16
	C7 = 17
	C8 = 18
	C9 = 19
	M1 = 20
	M2 = 21
	NB1 = 22
	NB2 = 23
	USER = 24


# noinspection SpellCheckingInspection
class EutraUeReleaseDl(Enum):
	"""5 Members, EM_A ... R89"""
	EM_A = 0
	EM_B = 1
	LADV = 2
	NIOT = 3
	R89 = 4


# noinspection SpellCheckingInspection
class EutraUlContentType(Enum):
	"""2 Members, PUCCh ... PUSCh"""
	PUCCh = 0
	PUSCh = 1


# noinspection SpellCheckingInspection
class EutraUlContentTypeWithIot(Enum):
	"""4 Members, EMTC ... PUSCh"""
	EMTC = 0
	NIOT = 1
	PUCCh = 2
	PUSCh = 3


# noinspection SpellCheckingInspection
class EutraUlFormat(Enum):
	"""9 Members, F1 ... F5"""
	F1 = 0
	F1A = 1
	F1B = 2
	F2 = 3
	F2A = 4
	F2B = 5
	F3 = 6
	F4 = 7
	F5 = 8


# noinspection SpellCheckingInspection
class EutraUlFormatEmtc(Enum):
	"""6 Members, F1 ... F2B"""
	F1 = 0
	F1A = 1
	F1B = 2
	F2 = 3
	F2A = 4
	F2B = 5


# noinspection SpellCheckingInspection
class EutraUlFrc(Enum):
	"""89 Members, A11 ... UE3"""
	A11 = 0
	A12 = 1
	A121 = 2
	A122 = 3
	A123 = 4
	A124 = 5
	A125 = 6
	A126 = 7
	A13 = 8
	A131 = 9
	A132 = 10
	A133 = 11
	A134 = 12
	A135 = 13
	A136 = 14
	A14 = 15
	A15 = 16
	A16 = 17
	A17 = 18
	A171 = 19
	A172 = 20
	A173 = 21
	A174 = 22
	A175 = 23
	A176 = 24
	A181 = 25
	A182 = 26
	A183 = 27
	A184 = 28
	A185 = 29
	A186 = 30
	A191 = 31
	A192 = 32
	A193 = 33
	A194 = 34
	A195 = 35
	A196 = 36
	A21 = 37
	A211 = 38
	A212 = 39
	A213 = 40
	A214 = 41
	A215 = 42
	A216 = 43
	A22 = 44
	A221 = 45
	A222 = 46
	A223 = 47
	A224 = 48
	A23 = 49
	A31 = 50
	A32 = 51
	A33 = 52
	A34 = 53
	A35 = 54
	A36 = 55
	A37 = 56
	A41 = 57
	A42 = 58
	A43 = 59
	A44 = 60
	A45 = 61
	A46 = 62
	A47 = 63
	A48 = 64
	A51 = 65
	A52 = 66
	A53 = 67
	A54 = 68
	A55 = 69
	A56 = 70
	A57 = 71
	A71 = 72
	A72 = 73
	A73 = 74
	A74 = 75
	A75 = 76
	A76 = 77
	A81 = 78
	A82 = 79
	A83 = 80
	A84 = 81
	A85 = 82
	A86 = 83
	UE11 = 84
	UE12 = 85
	UE21 = 86
	UE22 = 87
	UE3 = 88


# noinspection SpellCheckingInspection
class EutraUlFrcNbiotTcw(Enum):
	"""5 Members, A161 ... A165"""
	A161 = 0
	A162 = 1
	A163 = 2
	A164 = 3
	A165 = 4


# noinspection SpellCheckingInspection
class EutraUlNoNpuschRepNbiotAll(Enum):
	"""4 Members, _1 ... _64"""
	_1 = 0
	_16 = 1
	_2 = 2
	_64 = 3


# noinspection SpellCheckingInspection
class EutraUlSidelinkContentType(Enum):
	"""4 Members, PSBCh ... PSSCh"""
	PSBCh = 0
	PSCCh = 1
	PSDCh = 2
	PSSCh = 3


# noinspection SpellCheckingInspection
class EutraUlueNbiotModulation(Enum):
	"""3 Members, PI2Bpsk ... QPSK"""
	PI2Bpsk = 0
	PI4Qpsk = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class EvdoAckMode(Enum):
	"""2 Members, BPSK ... OOK"""
	BPSK = 0
	OOK = 1


# noinspection SpellCheckingInspection
class EvdoBandClass(Enum):
	"""22 Members, BC0 ... BC9"""
	BC0 = 0
	BC1 = 1
	BC10 = 2
	BC11 = 3
	BC12 = 4
	BC13 = 5
	BC14 = 6
	BC15 = 7
	BC16 = 8
	BC17 = 9
	BC18 = 10
	BC19 = 11
	BC2 = 12
	BC20 = 13
	BC21 = 14
	BC3 = 15
	BC4 = 16
	BC5 = 17
	BC6 = 18
	BC7 = 19
	BC8 = 20
	BC9 = 21


# noinspection SpellCheckingInspection
class EvdoDataRate(Enum):
	"""21 Members, DR1075K2 ... DR9K6"""
	DR1075K2 = 0
	DR1228K8 = 1
	DR1536K = 2
	DR153K6 = 3
	DR1843K2 = 4
	DR19K2 = 5
	DR2150K4 = 6
	DR2457K6 = 7
	DR3072K = 8
	DR307K2 = 9
	DR3686K4 = 10
	DR38K4 = 11
	DR4300K8 = 12
	DR460K8 = 13
	DR4915K2 = 14
	DR4K8 = 15
	DR614K4 = 16
	DR768K = 17
	DR76K8 = 18
	DR921K6 = 19
	DR9K6 = 20


# noinspection SpellCheckingInspection
class EvdoDrcLenDn(Enum):
	"""6 Members, DL1 ... DL8"""
	DL1 = 0
	DL16 = 1
	DL32 = 2
	DL4 = 3
	DL64 = 4
	DL8 = 5


# noinspection SpellCheckingInspection
class EvdoDrcLenUp(Enum):
	"""4 Members, DL1 ... DL8"""
	DL1 = 0
	DL2 = 1
	DL4 = 2
	DL8 = 3


# noinspection SpellCheckingInspection
class EvdoDrcPer(Enum):
	"""4 Members, DP0 ... DP8"""
	DP0 = 0
	DP16 = 1
	DP4 = 2
	DP8 = 3


# noinspection SpellCheckingInspection
class EvdoHarqMode(Enum):
	"""3 Members, ACK ... OFF"""
	ACK = 0
	NAK = 1
	OFF = 2


# noinspection SpellCheckingInspection
class EvdoLayerDn(Enum):
	"""3 Members, S1 ... S3"""
	S1 = 0
	S2 = 1
	S3 = 2


# noinspection SpellCheckingInspection
class EvdoMarkMode(Enum):
	"""7 Members, CSPeriod ... USER"""
	CSPeriod = 0
	ESM = 1
	PNSPeriod = 2
	RATio = 3
	SLOT = 4
	TRIGger = 5
	USER = 6


# noinspection SpellCheckingInspection
class EvdoModulation(Enum):
	"""5 Members, B4 ... Q4Q2"""
	B4 = 0
	E4E2 = 1
	Q2 = 2
	Q4 = 3
	Q4Q2 = 4


# noinspection SpellCheckingInspection
class EvdoPacketSize(Enum):
	"""14 Members, PS1024 ... PS8192"""
	PS1024 = 0
	PS12288 = 1
	PS128 = 2
	PS1536 = 3
	PS2048 = 4
	PS256 = 5
	PS3072 = 6
	PS4096 = 7
	PS512 = 8
	PS5120 = 9
	PS6144 = 10
	PS7168 = 11
	PS768 = 12
	PS8192 = 13


# noinspection SpellCheckingInspection
class EvdoPayload(Enum):
	"""12 Members, PS1024 ... PS8192"""
	PS1024 = 0
	PS12288 = 1
	PS128 = 2
	PS1536 = 3
	PS2048 = 4
	PS256 = 5
	PS3072 = 6
	PS4096 = 7
	PS512 = 8
	PS6144 = 9
	PS768 = 10
	PS8192 = 11


# noinspection SpellCheckingInspection
class EvdoPredSett(Enum):
	"""19 Members, ULS1DR153K6 ... USER"""
	ULS1DR153K6 = 0
	ULS1DR19K2 = 1
	ULS1DR38K4 = 2
	ULS1DR76K8 = 3
	ULS1DR9K6 = 4
	ULS2PS1024LL = 5
	ULS2PS12288LL = 6
	ULS2PS128LL = 7
	ULS2PS1536LL = 8
	ULS2PS2048LL = 9
	ULS2PS256HC = 10
	ULS2PS256LL = 11
	ULS2PS3072LL = 12
	ULS2PS4096LL = 13
	ULS2PS512LL = 14
	ULS2PS6144LL = 15
	ULS2PS768LL = 16
	ULS2PS8192LL = 17
	USER = 18


# noinspection SpellCheckingInspection
class EvdoRabLen(Enum):
	"""4 Members, RL16 ... RL8"""
	RL16 = 0
	RL32 = 1
	RL64 = 2
	RL8 = 3


# noinspection SpellCheckingInspection
class EvdoRpcMode(Enum):
	"""5 Members, DOWN ... UP"""
	DOWN = 0
	HOLD = 1
	PATTern = 2
	RANGe = 3
	UP = 4


# noinspection SpellCheckingInspection
class EvdoTermMode(Enum):
	"""2 Members, ACCess ... TRAFfic"""
	ACCess = 0
	TRAFfic = 1


# noinspection SpellCheckingInspection
class ExtSeqAdwMode(Enum):
	"""2 Members, DETerministic ... INSTant"""
	DETerministic = 0
	INSTant = 1


# noinspection SpellCheckingInspection
class ExtSeqAdwRate(Enum):
	"""4 Members, SR2G4 ... SR75M"""
	SR2G4 = 0
	SR300M = 1
	SR37M5 = 2
	SR75M = 3


# noinspection SpellCheckingInspection
class ExtSeqMarkMode(Enum):
	"""7 Members, ADW ... UNCHanged"""
	ADW = 0
	ENTRy = 1
	PDW = 2
	PULSe = 3
	READy = 4
	STARt = 5
	UNCHanged = 6


# noinspection SpellCheckingInspection
class ExtSeqMode(Enum):
	"""5 Members, ASEQuencing ... USER"""
	ASEQuencing = 0
	DFINding = 1
	PSEQuencer = 2
	RTCI = 3
	USER = 4


# noinspection SpellCheckingInspection
class ExtSeqPdwRate(Enum):
	"""4 Members, SR1M ... SR750K"""
	SR1M = 0
	SR250K = 1
	SR500K = 2
	SR750K = 3


# noinspection SpellCheckingInspection
class ExtSeqPdwVariant(Enum):
	"""2 Members, BASic ... EXPert"""
	BASic = 0
	EXPert = 1


# noinspection SpellCheckingInspection
class F1AcontentType(Enum):
	"""2 Members, PDSCh ... PRACh"""
	PDSCh = 0
	PRACh = 1


# noinspection SpellCheckingInspection
class Fad2CitfMode(Enum):
	"""2 Members, HOPPing ... SLIDing"""
	HOPPing = 0
	SLIDing = 1


# noinspection SpellCheckingInspection
class FadBdProf(Enum):
	"""1 Members, PDOPpler ... PDOPpler"""
	PDOPpler = 0


# noinspection SpellCheckingInspection
class FadConfPathOut(Enum):
	"""58 Members, FA1A2BFB1A2B ... FBMAXAB"""
	FA1A2BFB1A2B = 0
	FA1A2BFB1A2BM12 = 1
	FA1A2BFB1A2BM13 = 2
	FA1A2BFB1A2BM14 = 3
	FA1A2BFB1A2BM18 = 4
	FA1A2BFB1A2BM21 = 5
	FA1A2BFB1A2BM212 = 6
	FA1A2BFB1A2BM213 = 7
	FA1A2BFB1A2BM214 = 8
	FA1A2BFB1A2BM22 = 9
	FA1A2BFB1A2BM221 = 10
	FA1A2BFB1A2BM222 = 11
	FA1A2BFB1A2BM223 = 12
	FA1A2BFB1A2BM224 = 13
	FA1A2BFB1A2BM23 = 14
	FA1A2BFB1A2BM231 = 15
	FA1A2BFB1A2BM232 = 16
	FA1A2BFB1A2BM233 = 17
	FA1A2BFB1A2BM234 = 18
	FA1A2BFB1A2BM24 = 19
	FA1A2BFB1A2BM241 = 20
	FA1A2BFB1A2BM242 = 21
	FA1A2BFB1A2BM243 = 22
	FA1A2BFB1A2BM244 = 23
	FA1A2BFB1A2BM28 = 24
	FA1A2BFB1A2BM31 = 25
	FA1A2BFB1A2BM312 = 26
	FA1A2BFB1A2BM32 = 27
	FA1A2BFB1A2BM321 = 28
	FA1A2BFB1A2BM322 = 29
	FA1A2BFB1A2BM33 = 30
	FA1A2BFB1A2BM34 = 31
	FA1A2BFB1A2BM41 = 32
	FA1A2BFB1A2BM412 = 33
	FA1A2BFB1A2BM42 = 34
	FA1A2BFB1A2BM421 = 35
	FA1A2BFB1A2BM422 = 36
	FA1A2BFB1A2BM43 = 37
	FA1A2BFB1A2BM44 = 38
	FA1A2BFB1A2BM48 = 39
	FA1A2BFB1A2BM81 = 40
	FA1A2BFB1A2BM82 = 41
	FA1A2BFB1A2BM84 = 42
	FA1A2BFB1A2BM88 = 43
	FAA = 44
	FAABFBAB = 45
	FAAFBA = 46
	FAAFBB = 47
	FAAFBB311 = 48
	FAAFBB411 = 49
	FAAFBB511 = 50
	FAAFBB611 = 51
	FAAFBB711 = 52
	FAAFBB811 = 53
	FABFBB = 54
	FAMAXA = 55
	FAMAXAB = 56
	FBMAXAB = 57


# noinspection SpellCheckingInspection
class FadCopyHwdEst(Enum):
	"""9 Members, ALL ... FADH"""
	ALL = 0
	FADA = 1
	FADB = 2
	FADC = 3
	FADD = 4
	FADE = 5
	FADF = 6
	FADG = 7
	FADH = 8


# noinspection SpellCheckingInspection
class FadDssRealAppr(Enum):
	"""3 Members, DECimal ... ENU"""
	DECimal = 0
	DMS = 1
	ENU = 2


# noinspection SpellCheckingInspection
class FadDssS2SwatSurfType(Enum):
	"""3 Members, ROUGh ... STORmy"""
	ROUGh = 0
	SMOoth = 1
	STORmy = 2


# noinspection SpellCheckingInspection
class FadDssS2SwatType(Enum):
	"""2 Members, FRESh ... SALT"""
	FRESh = 0
	SALT = 1


# noinspection SpellCheckingInspection
class FadDssScen(Enum):
	"""3 Members, SHIPtoship ... USER"""
	SHIPtoship = 0
	TOWertoaircraft = 1
	USER = 2


# noinspection SpellCheckingInspection
class FadDssTerrType(Enum):
	"""5 Members, FORest ... WATer"""
	FORest = 0
	GRASsland = 1
	NONE = 2
	ROCK = 3
	WATer = 4


# noinspection SpellCheckingInspection
class FadDssUsrProfSour(Enum):
	"""3 Members, PROFile ... TXRXconfiguration"""
	PROFile = 0
	TPA = 1
	TXRXconfiguration = 2


# noinspection SpellCheckingInspection
class FadDssUsrTraj(Enum):
	"""3 Members, EPHemeris ... TDF"""
	EPHemeris = 0
	FIXedatpoint = 1
	TDF = 2


# noinspection SpellCheckingInspection
class FadDssUsrTrajBeh(Enum):
	"""4 Members, JUMP ... STOP"""
	JUMP = 0
	LOOP = 1
	RETurn = 2
	STOP = 3


# noinspection SpellCheckingInspection
class FadDssUsrVehCat(Enum):
	"""3 Members, AIR ... WATer"""
	AIR = 0
	LAND = 1
	WATer = 2


# noinspection SpellCheckingInspection
class FadDssUsrVehMode(Enum):
	"""3 Members, NONE ... USER"""
	NONE = 0
	PREDefined = 1
	USER = 2


# noinspection SpellCheckingInspection
class FadDssVehTypeAir(Enum):
	"""6 Members, AHELicopter ... AUAV"""
	AHELicopter = 0
	AJET = 1
	ALINer = 2
	ASPort = 3
	ATRansport = 4
	AUAV = 5


# noinspection SpellCheckingInspection
class FadDssVehTypeAll(Enum):
	"""13 Members, AHELicopter ... SPATrolboat"""
	AHELicopter = 0
	AJET = 1
	ALINer = 2
	ASPort = 3
	ATRansport = 4
	AUAV = 5
	LBICycle = 6
	LCAR = 7
	LPEDestrian = 8
	LTRain = 9
	SCARrier = 10
	SFRigate = 11
	SPATrolboat = 12


# noinspection SpellCheckingInspection
class FadDssVehTypeShip(Enum):
	"""3 Members, SCARrier ... SPATrolboat"""
	SCARrier = 0
	SFRigate = 1
	SPATrolboat = 2


# noinspection SpellCheckingInspection
class FadHoppMode(Enum):
	"""3 Members, IBANd ... OOBand"""
	IBANd = 0
	OFF = 1
	OOBand = 2


# noinspection SpellCheckingInspection
class FadingProfileA(Enum):
	"""18 Members, BELLindoor ... WRICe"""
	BELLindoor = 0
	BELVehicle = 1
	CPHase = 2
	CUSTom = 3
	DGAUs = 4
	GDOPpler = 5
	GFD1 = 6
	GFD8 = 7
	OGAUs = 8
	PDOPpler = 9
	RAYLeigh = 10
	RICE = 11
	SCM = 12
	SPATh = 13
	TGAUs = 14
	WATTerson = 15
	WDOPpler = 16
	WRICe = 17


# noinspection SpellCheckingInspection
class FadingProfileB(Enum):
	"""16 Members, BELLindoor ... WRICe"""
	BELLindoor = 0
	BELVehicle = 1
	CPHase = 2
	DGAUs = 3
	GDOPpler = 4
	GFD1 = 5
	GFD8 = 6
	OGAUs = 7
	PDOPpler = 8
	RAYLeigh = 9
	RICE = 10
	SPATh = 11
	TGAUs = 12
	WATTerson = 13
	WDOPpler = 14
	WRICe = 15


# noinspection SpellCheckingInspection
class FadInsLossMode(Enum):
	"""3 Members, LACP ... USER"""
	LACP = 0
	NORMal = 1
	USER = 2


# noinspection SpellCheckingInspection
class FadKeepConst(Enum):
	"""2 Members, DSHift ... SPEed"""
	DSHift = 0
	SPEed = 1


# noinspection SpellCheckingInspection
class FadMimoMatMode(Enum):
	"""4 Members, AOAaod ... SCWI"""
	AOAaod = 0
	INDividual = 1
	KRONecker = 2
	SCWI = 3


# noinspection SpellCheckingInspection
class FadMimoPowDispMode(Enum):
	"""2 Members, ABSolute ... RELative"""
	ABSolute = 0
	RELative = 1


# noinspection SpellCheckingInspection
class FadMimoScmDist(Enum):
	"""3 Members, EQUal ... LAPLace"""
	EQUal = 0
	GAUSs = 1
	LAPLace = 2


# noinspection SpellCheckingInspection
class FadMimoSubSet(Enum):
	"""3 Members, ALL ... SET2"""
	ALL = 0
	SET1 = 1
	SET2 = 2


# noinspection SpellCheckingInspection
class FadMimoTap(Enum):
	"""20 Members, TAP1 ... TAP9"""
	TAP1 = 0
	TAP10 = 1
	TAP11 = 2
	TAP12 = 3
	TAP13 = 4
	TAP14 = 5
	TAP15 = 6
	TAP16 = 7
	TAP17 = 8
	TAP18 = 9
	TAP19 = 10
	TAP2 = 11
	TAP20 = 12
	TAP3 = 13
	TAP4 = 14
	TAP5 = 15
	TAP6 = 16
	TAP7 = 17
	TAP8 = 18
	TAP9 = 19


# noinspection SpellCheckingInspection
class FadMpRopChanMode(Enum):
	"""2 Members, ALL ... ONE"""
	ALL = 0
	ONE = 1


# noinspection SpellCheckingInspection
class FadProfCustRange(Enum):
	"""2 Members, FLAT ... RAYLeigh"""
	FLAT = 0
	RAYLeigh = 1


# noinspection SpellCheckingInspection
class FadProfUdyn(Enum):
	"""3 Members, PDOPpler ... SPATh"""
	PDOPpler = 0
	RAYLeigh = 1
	SPATh = 2


# noinspection SpellCheckingInspection
class FadRestMode(Enum):
	"""3 Members, AAUT ... BBTRigger"""
	AAUT = 0
	AUTO = 1
	BBTRigger = 2


# noinspection SpellCheckingInspection
class FadSignDest(Enum):
	"""2 Members, BB ... RF"""
	BB = 0
	RF = 1


# noinspection SpellCheckingInspection
class FadStan(Enum):
	"""311 Members, BD1 ... WMSUI6A360P90"""
	BD1 = 0
	C1DMA30 = 1
	CDMA0 = 2
	CDMA100 = 3
	CDMA3 = 4
	CDMA30 = 5
	CDMA8 = 6
	DABRA04 = 7
	DABRA06 = 8
	DABSFN = 9
	DABTU06 = 10
	DABTU12 = 11
	EVDO1CH1 = 12
	EVDO1CH1BC5 = 13
	EVDO1CH2 = 14
	EVDO1CH2BC5 = 15
	EVDO1CH3 = 16
	EVDO1CH3BC5 = 17
	EVDO1CH4 = 18
	EVDO1CH4BC5 = 19
	EVDO1CH5 = 20
	EVDO1CH5BC5 = 21
	FR1CDLAUMA = 22
	FR1CDLAUMI = 23
	FR1CDLBUMA = 24
	FR1CDLBUMI = 25
	FR1CDLCUMA = 26
	FR1CDLCUMA4 = 27
	FR1CDLCUMI = 28
	FR1CDLCUMI2 = 29
	FR2CDLAINO = 30
	FR2CDLCUMI = 31
	G3C1 = 32
	G3C2 = 33
	G3C3 = 34
	G3C4 = 35
	G3HST1OS = 36
	G3HST1OSDU = 37
	G3HST2TLC = 38
	G3HST2TLCDU = 39
	G3HST3TMA = 40
	G3HST3TMADU = 41
	G3HT120 = 42
	G3MBSFN3 = 43
	G3RA120 = 44
	G3RA250 = 45
	G3SCMEUMA3 = 46
	G3SCMEUMA30 = 47
	G3SCMEUMI3 = 48
	G3SCMEUMI30 = 49
	G3TU120 = 50
	G3TU3 = 51
	G3TU50 = 52
	G3UEC1 = 53
	G3UEC2 = 54
	G3UEC3 = 55
	G3UEC4 = 56
	G3UEC5 = 57
	G3UEC6 = 58
	G3UEC7BE = 59
	G3UEC7SE = 60
	G3UEC8CQ = 61
	G3UEPA3 = 62
	G3UEPB3 = 63
	G3UEVA120 = 64
	G3UEVA3 = 65
	G3UEVA30 = 66
	G6HT100 = 67
	G6HT120 = 68
	G6HT200 = 69
	G6TU100 = 70
	G6TU1P5 = 71
	G6TU3 = 72
	G6TU3P6 = 73
	G6TU50 = 74
	G6TU6 = 75
	G6TU60 = 76
	GEOSCMEUMA3 = 77
	GEOSCMEUMA30 = 78
	GEOSCMEUMI3 = 79
	GEOSCMEUMI30 = 80
	GET100 = 81
	GET50 = 82
	GET60 = 83
	GHT100 = 84
	GHT120 = 85
	GHT200 = 86
	GRA130 = 87
	GRA250 = 88
	GRA300 = 89
	GRA500 = 90
	GTI5 = 91
	GTU100 = 92
	GTU1P5 = 93
	GTU3 = 94
	GTU3P6 = 95
	GTU50 = 96
	GTU6 = 97
	GTU60 = 98
	HL2A = 99
	HL2B = 100
	HL2C = 101
	HL2D = 102
	HL2E = 103
	HST1LTE500A = 104
	HST1LTE500B = 105
	HST1NR35015 = 106
	HST1NR35030 = 107
	HST1NR50015 = 108
	HST1NR50030 = 109
	HST3LTE500A = 110
	HST3LTE500B = 111
	HST3NR35015 = 112
	HST3NR35030 = 113
	HST3NR50015 = 114
	HST3NR50030 = 115
	LMEPA1H = 116
	LMEPA1L = 117
	LMEPA1M = 118
	LMEPA5H = 119
	LMEPA5L = 120
	LMEPA5M = 121
	LMETU1H = 122
	LMETU1L = 123
	LMETU1M = 124
	LMETU200H = 125
	LMETU200L = 126
	LMETU200M = 127
	LMETU300H = 128
	LMETU300L = 129
	LMETU300M = 130
	LMETU30H = 131
	LMETU30L = 132
	LMETU30M = 133
	LMETU5H = 134
	LMETU5L = 135
	LMETU5M = 136
	LMETU600H = 137
	LMETU600L = 138
	LMETU600M = 139
	LMETU70H = 140
	LMETU70L = 141
	LMETU70M = 142
	LMEVA5H = 143
	LMEVA5L = 144
	LMEVA5M = 145
	LMEVA70H = 146
	LMEVA70L = 147
	LMEVA70M = 148
	LTECQI5 = 149
	LTEEPA1 = 150
	LTEEPA5 = 151
	LTEETU1 = 152
	LTEETU200 = 153
	LTEETU30 = 154
	LTEETU300 = 155
	LTEETU5 = 156
	LTEETU600 = 157
	LTEETU70 = 158
	LTEEVA5 = 159
	LTEEVA70 = 160
	LTEMBSFN5 = 161
	MP1 = 162
	MPLTEETU200 = 163
	MPLTEPDOPP = 164
	MPX15 = 165
	MPX30 = 166
	MPY15 = 167
	MPY30 = 168
	MPZ15 = 169
	MPZ30 = 170
	NADC100 = 171
	NADC50 = 172
	NADC8 = 173
	P6HT100 = 174
	P6TU1 = 175
	P6TU50 = 176
	PET100 = 177
	PET50 = 178
	PHT100 = 179
	PRA130 = 180
	PTU1 = 181
	PTU50 = 182
	T4ET = 183
	T6HT = 184
	T6TU = 185
	TBU = 186
	TDLA30D10H = 187
	TDLA30D10L = 188
	TDLA30D10M = 189
	TDLA30D10MA = 190
	TDLA30D10S = 191
	TDLA30D300H = 192
	TDLA30D300L = 193
	TDLA30D300M = 194
	TDLA30D300MA = 195
	TDLA30D300S = 196
	TDLA30D35H = 197
	TDLA30D35L = 198
	TDLA30D35M = 199
	TDLA30D35MA = 200
	TDLA30D35S = 201
	TDLA30D5H = 202
	TDLA30D5L = 203
	TDLA30D5M = 204
	TDLA30D5MA = 205
	TDLA30D5S = 206
	TDLA30D75H = 207
	TDLA30D75L = 208
	TDLA30D75M = 209
	TDLA30D75MA = 210
	TDLA30D75S = 211
	TDLB100D400H = 212
	TDLB100D400L = 213
	TDLB100D400M = 214
	TDLB100D400MA = 215
	TDLB100D400S = 216
	TDLC300D100H = 217
	TDLC300D100L = 218
	TDLC300D100M = 219
	TDLC300D100MA = 220
	TDLC300D100S = 221
	TDLC300D1200H = 222
	TDLC300D1200L = 223
	TDLC300D1200M = 224
	TDLC300D1200S = 225
	TDLC300D400S = 226
	TDLC300D600H = 227
	TDLC300D600L = 228
	TDLC300D600M = 229
	TDLC300D600S = 230
	TDLC60D300H = 231
	TDLC60D300L = 232
	TDLC60D300M = 233
	TDLC60D300MA = 234
	TDLC60D300S = 235
	TDR = 236
	TDU = 237
	THT = 238
	TTU = 239
	USER = 240
	WATTI1 = 241
	WATTI2 = 242
	WATTI3 = 243
	WLANACMODA = 244
	WLANACMODB = 245
	WLANACMODC = 246
	WLANACMODD = 247
	WLANACMODE = 248
	WLANACMODF = 249
	WLANACSMODA = 250
	WLANACSMODB = 251
	WLANACSMODC = 252
	WLANACSMODD = 253
	WLANACSMODE = 254
	WLANACSMODF = 255
	WLANNMODA = 256
	WLANNMODB = 257
	WLANNMODC = 258
	WLANNMODD = 259
	WLANNMODE = 260
	WLANNMODF = 261
	WLANNSMODA = 262
	WLANNSMODB = 263
	WLANNSMODC = 264
	WLANNSMODD = 265
	WLANNSMODE = 266
	WLANNSMODF = 267
	WLANPHIGHWAYLOS = 268
	WLANPHIGHWAYNLOS = 269
	WLANPRURALLOS = 270
	WLANPURBANAPPLOS = 271
	WLANPURBANCRONLOS = 272
	WMITUOIPA = 273
	WMITUOIPB = 274
	WMITUPB3H = 275
	WMITUPB3L = 276
	WMITUPB3M = 277
	WMITUVA120 = 278
	WMITUVA60 = 279
	WMITUVA60H = 280
	WMITUVA60L = 281
	WMITUVA60M = 282
	WMSUI1A030P75 = 283
	WMSUI1A030P90 = 284
	WMSUI1A360P75 = 285
	WMSUI1A360P90 = 286
	WMSUI2A030P75 = 287
	WMSUI2A030P90 = 288
	WMSUI2A360P75 = 289
	WMSUI2A360P90 = 290
	WMSUI3A030P75 = 291
	WMSUI3A030P90 = 292
	WMSUI3A360P75 = 293
	WMSUI3A360P90 = 294
	WMSUI4A030P75 = 295
	WMSUI4A030P90 = 296
	WMSUI4A360P75 = 297
	WMSUI4A360P90 = 298
	WMSUI5A030P50 = 299
	WMSUI5A030P75 = 300
	WMSUI5A030P90 = 301
	WMSUI5A360P50 = 302
	WMSUI5A360P75 = 303
	WMSUI5A360P90 = 304
	WMSUI6A030P50 = 305
	WMSUI6A030P75 = 306
	WMSUI6A030P90 = 307
	WMSUI6A360P50 = 308
	WMSUI6A360P75 = 309
	WMSUI6A360P90 = 310


# noinspection SpellCheckingInspection
class FadType(Enum):
	"""9 Members, BIRThdeath ... TCInterferer"""
	BIRThdeath = 0
	CDYNamic = 1
	DEL30 = 2
	DEL50 = 3
	DSSimulation = 4
	HSTRain = 5
	MDELay = 6
	STANdard = 7
	TCInterferer = 8


# noinspection SpellCheckingInspection
class FbiMode(Enum):
	"""3 Members, D1B ... OFF"""
	D1B = 0
	D2B = 1
	OFF = 2


# noinspection SpellCheckingInspection
class FeedbackBlerMode(Enum):
	"""3 Members, APRocesses ... OFF"""
	APRocesses = 0
	FPRocess = 1
	OFF = 2


# noinspection SpellCheckingInspection
class FeedbackConnector(Enum):
	"""2 Members, GLOBal ... LOCal"""
	GLOBal = 0
	LOCal = 1


# noinspection SpellCheckingInspection
class FeedbackConnectorAll(Enum):
	"""1 Members, LOCal ... LOCal"""
	LOCal = 0


# noinspection SpellCheckingInspection
class FeedbackDistMode(Enum):
	"""2 Members, DIRect ... STD"""
	DIRect = 0
	STD = 1


# noinspection SpellCheckingInspection
class FeedbackMode(Enum):
	"""4 Members, BAN ... SERial"""
	BAN = 0
	OFF = 1
	S3X8 = 2
	SERial = 3


# noinspection SpellCheckingInspection
class FeedbackModeWithEthernet(Enum):
	"""4 Members, ETH ... SERial"""
	ETH = 0
	OFF = 1
	S3X8 = 2
	SERial = 3


# noinspection SpellCheckingInspection
class FeedbackRateAll(Enum):
	"""4 Members, CUST ... R1M9"""
	CUST = 0
	R115 = 1
	R1M6 = 2
	R1M9 = 3


# noinspection SpellCheckingInspection
class FenUmbRfCon(Enum):
	"""5 Members, NONE ... RFD"""
	NONE = 0
	RFA = 1
	RFB = 2
	RFC = 3
	RFD = 4


# noinspection SpellCheckingInspection
class FeRefFreq(Enum):
	"""4 Members, F10M ... FG64"""
	F10M = 0
	F1G = 1
	FG5 = 2
	FG64 = 3


# noinspection SpellCheckingInspection
class FilterBandwidth(Enum):
	"""18 Members, ALL ... F90"""
	ALL = 0
	F10 = 1
	F100 = 2
	F15 = 3
	F20 = 4
	F200 = 5
	F25 = 6
	F30 = 7
	F35 = 8
	F40 = 9
	F400 = 10
	F45 = 11
	F5 = 12
	F50 = 13
	F60 = 14
	F70 = 15
	F80 = 16
	F90 = 17


# noinspection SpellCheckingInspection
class FilterDuplexing(Enum):
	"""3 Members, ALL ... TDD"""
	ALL = 0
	FDD = 1
	TDD = 2


# noinspection SpellCheckingInspection
class FilterFreqRange(Enum):
	"""3 Members, ALL ... FR2"""
	ALL = 0
	FR1 = 1
	FR2 = 2


# noinspection SpellCheckingInspection
class FilterMode(Enum):
	"""8 Members, _0 ... USER"""
	_0 = 0
	_1 = 1
	_2 = 2
	BWP = 3
	CBW = 4
	FAST = 5
	OFF = 6
	USER = 7


# noinspection SpellCheckingInspection
class FilterSubcarrierSpacing(Enum):
	"""5 Members, ALL ... F60"""
	ALL = 0
	F120 = 1
	F15 = 2
	F30 = 3
	F60 = 4


# noinspection SpellCheckingInspection
class FilterTestModels(Enum):
	"""9 Members, ALL ... TM3_3"""
	ALL = 0
	TM1_1 = 1
	TM1_2 = 2
	TM2 = 3
	TM2a = 4
	TM3_1 = 5
	TM3_1A = 6
	TM3_2 = 7
	TM3_3 = 8


# noinspection SpellCheckingInspection
class FilterWidth(Enum):
	"""2 Members, NARRow ... WIDE"""
	NARRow = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class FiltOptMode(Enum):
	"""2 Members, OFFLine ... RTime"""
	OFFLine = 0
	RTime = 1


# noinspection SpellCheckingInspection
class FiltOptType(Enum):
	"""4 Members, ACP ... EVM"""
	ACP = 0
	ACPN = 1
	BENU = 2
	EVM = 3


# noinspection SpellCheckingInspection
class FirstRefSymPos(Enum):
	"""2 Members, SYM0 ... SYM1"""
	SYM0 = 0
	SYM1 = 1


# noinspection SpellCheckingInspection
class FmMode(Enum):
	"""2 Members, LNOise ... NORMal"""
	LNOise = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class FmSour(Enum):
	"""8 Members, EXT1 ... NOISe"""
	EXT1 = 0
	EXT2 = 1
	EXTernal = 2
	INTB = 3
	INTernal = 4
	LF1 = 5
	LF2 = 6
	NOISe = 7


# noinspection SpellCheckingInspection
class FmStereoAudExtClk(Enum):
	"""2 Members, _44100 ... _48000"""
	_44100 = 0
	_48000 = 1


# noinspection SpellCheckingInspection
class FmStereoAudSrc(Enum):
	"""4 Members, FILE ... SPEXt"""
	FILE = 0
	LFGen = 1
	OFF = 2
	SPEXt = 3


# noinspection SpellCheckingInspection
class FmStereoCfgMode(Enum):
	"""2 Members, RBDS ... RDS"""
	RBDS = 0
	RDS = 1


# noinspection SpellCheckingInspection
class FmStereoDateCfgSel(Enum):
	"""2 Members, SYSDate ... USRDate"""
	SYSDate = 0
	USRDate = 1


# noinspection SpellCheckingInspection
class FmStereoInpMeth(Enum):
	"""2 Members, PARameters ... UDMessage"""
	PARameters = 0
	UDMessage = 1


# noinspection SpellCheckingInspection
class FmStereoMode(Enum):
	"""5 Members, LEFT ... RNELeft"""
	LEFT = 0
	RELeft = 1
	REMLeft = 2
	RIGHt = 3
	RNELeft = 4


# noinspection SpellCheckingInspection
class FmStereoMscVce(Enum):
	"""2 Members, MUSic ... VOICe"""
	MUSic = 0
	VOICe = 1


# noinspection SpellCheckingInspection
class FmStereoPreEmph(Enum):
	"""3 Members, _50 ... OFF"""
	_50 = 0
	_75 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class FmStereoRdsRbdsCfgDataSource(Enum):
	"""2 Members, GRPList ... UDGRoups"""
	GRPList = 0
	UDGRoups = 1


# noinspection SpellCheckingInspection
class FmStereoRdsRbdsCfgUsrGrpBeh(Enum):
	"""2 Members, HEXFormat ... MSGFormat"""
	HEXFormat = 0
	MSGFormat = 1


# noinspection SpellCheckingInspection
class FmStereoTimeCfgSel(Enum):
	"""2 Members, SYSTime ... USRTime"""
	SYSTime = 0
	USRTime = 1


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
class FrcType(Enum):
	"""318 Members, FR1A11 ... TS38176_FR2A249"""
	FR1A11 = 0
	FR1A110 = 1
	FR1A111 = 2
	FR1A112 = 3
	FR1A113 = 4
	FR1A114 = 5
	FR1A115 = 6
	FR1A116 = 7
	FR1A117 = 8
	FR1A118 = 9
	FR1A119 = 10
	FR1A12 = 11
	FR1A13 = 12
	FR1A14 = 13
	FR1A15 = 14
	FR1A16 = 15
	FR1A17 = 16
	FR1A18 = 17
	FR1A19 = 18
	FR1A21 = 19
	FR1A210 = 20
	FR1A211 = 21
	FR1A212 = 22
	FR1A213 = 23
	FR1A214 = 24
	FR1A215 = 25
	FR1A216 = 26
	FR1A22 = 27
	FR1A23 = 28
	FR1A24 = 29
	FR1A25 = 30
	FR1A26 = 31
	FR1A27 = 32
	FR1A28 = 33
	FR1A29 = 34
	FR1A31 = 35
	FR1A310 = 36
	FR1A311 = 37
	FR1A312 = 38
	FR1A313 = 39
	FR1A314 = 40
	FR1A315 = 41
	FR1A316 = 42
	FR1A317 = 43
	FR1A318 = 44
	FR1A319 = 45
	FR1A32 = 46
	FR1A320 = 47
	FR1A321 = 48
	FR1A322 = 49
	FR1A323 = 50
	FR1A324 = 51
	FR1A325 = 52
	FR1A326 = 53
	FR1A327 = 54
	FR1A328 = 55
	FR1A329 = 56
	FR1A33 = 57
	FR1A330 = 58
	FR1A331 = 59
	FR1A332 = 60
	FR1A333 = 61
	FR1A333A = 62
	FR1A334 = 63
	FR1A334A = 64
	FR1A34 = 65
	FR1A35 = 66
	FR1A36 = 67
	FR1A37 = 68
	FR1A38 = 69
	FR1A39 = 70
	FR1A3A1 = 71
	FR1A3A2 = 72
	FR1A3A3 = 73
	FR1A3A4 = 74
	FR1A3B1 = 75
	FR1A3B2 = 76
	FR1A3B3 = 77
	FR1A3B4 = 78
	FR1A41 = 79
	FR1A410 = 80
	FR1A411 = 81
	FR1A412 = 82
	FR1A413 = 83
	FR1A414 = 84
	FR1A415 = 85
	FR1A416 = 86
	FR1A417 = 87
	FR1A418 = 88
	FR1A419 = 89
	FR1A42 = 90
	FR1A420 = 91
	FR1A421 = 92
	FR1A422 = 93
	FR1A423 = 94
	FR1A424 = 95
	FR1A425 = 96
	FR1A426 = 97
	FR1A427 = 98
	FR1A428 = 99
	FR1A429 = 100
	FR1A429A = 101
	FR1A43 = 102
	FR1A430 = 103
	FR1A430A = 104
	FR1A431 = 105
	FR1A431A = 106
	FR1A432 = 107
	FR1A432A = 108
	FR1A44 = 109
	FR1A45 = 110
	FR1A46 = 111
	FR1A47 = 112
	FR1A48 = 113
	FR1A49 = 114
	FR1A51 = 115
	FR1A510 = 116
	FR1A511 = 117
	FR1A512 = 118
	FR1A513 = 119
	FR1A514 = 120
	FR1A52 = 121
	FR1A53 = 122
	FR1A54 = 123
	FR1A55 = 124
	FR1A56 = 125
	FR1A57 = 126
	FR1A58 = 127
	FR1A59 = 128
	FR2A11 = 129
	FR2A12 = 130
	FR2A13 = 131
	FR2A14 = 132
	FR2A15 = 133
	FR2A31 = 134
	FR2A310 = 135
	FR2A311 = 136
	FR2A312 = 137
	FR2A313 = 138
	FR2A314 = 139
	FR2A315 = 140
	FR2A316 = 141
	FR2A317 = 142
	FR2A318 = 143
	FR2A319 = 144
	FR2A32 = 145
	FR2A320 = 146
	FR2A321 = 147
	FR2A322 = 148
	FR2A323 = 149
	FR2A324 = 150
	FR2A325 = 151
	FR2A326 = 152
	FR2A33 = 153
	FR2A34 = 154
	FR2A35 = 155
	FR2A36 = 156
	FR2A37 = 157
	FR2A38 = 158
	FR2A39 = 159
	FR2A3A1 = 160
	FR2A3A2 = 161
	FR2A3A3 = 162
	FR2A3A4 = 163
	FR2A3A5 = 164
	FR2A3A6 = 165
	FR2A3A7 = 166
	FR2A3A8 = 167
	FR2A41 = 168
	FR2A410 = 169
	FR2A411 = 170
	FR2A412 = 171
	FR2A413 = 172
	FR2A414 = 173
	FR2A415 = 174
	FR2A416 = 175
	FR2A417 = 176
	FR2A418 = 177
	FR2A419 = 178
	FR2A42 = 179
	FR2A420 = 180
	FR2A43 = 181
	FR2A44 = 182
	FR2A45 = 183
	FR2A46 = 184
	FR2A47 = 185
	FR2A48 = 186
	FR2A49 = 187
	FR2A51 = 188
	FR2A510 = 189
	FR2A52 = 190
	FR2A53 = 191
	FR2A54 = 192
	FR2A55 = 193
	FR2A56 = 194
	FR2A57 = 195
	FR2A58 = 196
	FR2A59 = 197
	FR2A71 = 198
	FR2A710 = 199
	FR2A72 = 200
	FR2A73 = 201
	FR2A74 = 202
	FR2A75 = 203
	FR2A76 = 204
	FR2A77 = 205
	FR2A78 = 206
	FR2A79 = 207
	NA = 208
	TS381411_FR1A71 = 209
	TS381411_FR1A72 = 210
	TS381411_FR1A73 = 211
	TS381411_FR1A74 = 212
	TS381412_FR1A81 = 213
	TS381412_FR1A82 = 214
	TS381412_FR1A83 = 215
	TS381412_FR1A84 = 216
	TS38176_FR1A211 = 217
	TS38176_FR1A2110 = 218
	TS38176_FR1A2111 = 219
	TS38176_FR1A2112 = 220
	TS38176_FR1A2113 = 221
	TS38176_FR1A2114 = 222
	TS38176_FR1A2115 = 223
	TS38176_FR1A2116 = 224
	TS38176_FR1A212 = 225
	TS38176_FR1A213 = 226
	TS38176_FR1A214 = 227
	TS38176_FR1A215 = 228
	TS38176_FR1A216 = 229
	TS38176_FR1A217 = 230
	TS38176_FR1A218 = 231
	TS38176_FR1A219 = 232
	TS38176_FR1A231 = 233
	TS38176_FR1A2310 = 234
	TS38176_FR1A2311 = 235
	TS38176_FR1A2312 = 236
	TS38176_FR1A2313 = 237
	TS38176_FR1A2314 = 238
	TS38176_FR1A232 = 239
	TS38176_FR1A233 = 240
	TS38176_FR1A234 = 241
	TS38176_FR1A235 = 242
	TS38176_FR1A236 = 243
	TS38176_FR1A237 = 244
	TS38176_FR1A238 = 245
	TS38176_FR1A239 = 246
	TS38176_FR1A241 = 247
	TS38176_FR1A242 = 248
	TS38176_FR1A243 = 249
	TS38176_FR1A244 = 250
	TS38176_FR1A245 = 251
	TS38176_FR1A246 = 252
	TS38176_FR1A247 = 253
	TS38176_FR2A211 = 254
	TS38176_FR2A2110 = 255
	TS38176_FR2A2111 = 256
	TS38176_FR2A2112 = 257
	TS38176_FR2A2113 = 258
	TS38176_FR2A2114 = 259
	TS38176_FR2A2115 = 260
	TS38176_FR2A2116 = 261
	TS38176_FR2A2117 = 262
	TS38176_FR2A2118 = 263
	TS38176_FR2A2119 = 264
	TS38176_FR2A212 = 265
	TS38176_FR2A2120 = 266
	TS38176_FR2A2121 = 267
	TS38176_FR2A2122 = 268
	TS38176_FR2A2123 = 269
	TS38176_FR2A2124 = 270
	TS38176_FR2A213 = 271
	TS38176_FR2A214 = 272
	TS38176_FR2A215 = 273
	TS38176_FR2A216 = 274
	TS38176_FR2A217 = 275
	TS38176_FR2A218 = 276
	TS38176_FR2A219 = 277
	TS38176_FR2A221 = 278
	TS38176_FR2A2210 = 279
	TS38176_FR2A222 = 280
	TS38176_FR2A223 = 281
	TS38176_FR2A224 = 282
	TS38176_FR2A225 = 283
	TS38176_FR2A226 = 284
	TS38176_FR2A227 = 285
	TS38176_FR2A228 = 286
	TS38176_FR2A229 = 287
	TS38176_FR2A231 = 288
	TS38176_FR2A2310 = 289
	TS38176_FR2A2311 = 290
	TS38176_FR2A2312 = 291
	TS38176_FR2A2313 = 292
	TS38176_FR2A2314 = 293
	TS38176_FR2A2315 = 294
	TS38176_FR2A2316 = 295
	TS38176_FR2A2317 = 296
	TS38176_FR2A2318 = 297
	TS38176_FR2A2319 = 298
	TS38176_FR2A232 = 299
	TS38176_FR2A2320 = 300
	TS38176_FR2A233 = 301
	TS38176_FR2A234 = 302
	TS38176_FR2A235 = 303
	TS38176_FR2A236 = 304
	TS38176_FR2A237 = 305
	TS38176_FR2A238 = 306
	TS38176_FR2A239 = 307
	TS38176_FR2A241 = 308
	TS38176_FR2A2410 = 309
	TS38176_FR2A242 = 310
	TS38176_FR2A243 = 311
	TS38176_FR2A244 = 312
	TS38176_FR2A245 = 313
	TS38176_FR2A246 = 314
	TS38176_FR2A247 = 315
	TS38176_FR2A248 = 316
	TS38176_FR2A249 = 317


# noinspection SpellCheckingInspection
class FrcTypeAll(Enum):
	"""18 Members, A141 ... A247"""
	A141 = 0
	A142 = 1
	A143 = 2
	A144 = 3
	A151 = 4
	A152 = 5
	A161 = 6
	A162 = 7
	A163 = 8
	A164 = 9
	A165 = 10
	A241 = 11
	A242 = 12
	A243 = 13
	A244 = 14
	A245 = 15
	A246 = 16
	A247 = 17


# noinspection SpellCheckingInspection
class FreqConvExt(Enum):
	"""2 Members, M01 ... M02"""
	M01 = 0
	M02 = 1


# noinspection SpellCheckingInspection
class FreqMode(Enum):
	"""5 Members, COMBined ... SWEep"""
	COMBined = 0
	CW = 1
	FIXed = 2
	LIST = 3
	SWEep = 4


# noinspection SpellCheckingInspection
class FreqOffset(Enum):
	"""8 Members, FO_0 ... FO_625"""
	FO_0 = 0
	FO_1340 = 1
	FO_1740 = 2
	FO_2334 = 3
	FO_3334 = 4
	FO_400 = 5
	FO_4000 = 6
	FO_625 = 7


# noinspection SpellCheckingInspection
class FreqPllModeA(Enum):
	"""3 Members, NARRow ... WIDE"""
	NARRow = 0
	NORMal = 1
	WIDE = 2


# noinspection SpellCheckingInspection
class FreqRange(Enum):
	"""2 Members, FR2GT37 ... FR2LT334"""
	FR2GT37 = 0
	FR2LT334 = 1


# noinspection SpellCheckingInspection
class FreqSel(Enum):
	"""2 Members, ALWD ... NALW"""
	ALWD = 0
	NALW = 1


# noinspection SpellCheckingInspection
class FreqShift(Enum):
	"""13 Members, FS0 ... FS99"""
	FS0 = 0
	FS1 = 1
	FS14 = 2
	FS19 = 3
	FS2 = 4
	FS24 = 5
	FS29 = 6
	FS3 = 7
	FS4 = 8
	FS54 = 9
	FS79 = 10
	FS9 = 11
	FS99 = 12


# noinspection SpellCheckingInspection
class FreqStepMode(Enum):
	"""2 Members, DECimal ... USER"""
	DECimal = 0
	USER = 1


# noinspection SpellCheckingInspection
class FullPwrTrans(Enum):
	"""4 Members, FP ... NCON"""
	FP = 0
	FPM1 = 1
	FPM2 = 2
	NCON = 3


# noinspection SpellCheckingInspection
class GbasAppPerDes(Enum):
	"""3 Members, GAB ... GCD"""
	GAB = 0
	GC = 1
	GCD = 2


# noinspection SpellCheckingInspection
class GbasAppTchUnitSel(Enum):
	"""2 Members, FEET ... MET"""
	FEET = 0
	MET = 1


# noinspection SpellCheckingInspection
class GbasDataSource(Enum):
	"""12 Members, DLISt ... ZERO"""
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
	RGData = 10
	ZERO = 11


# noinspection SpellCheckingInspection
class GbasGcid(Enum):
	"""2 Members, FC ... FD"""
	FC = 0
	FD = 1


# noinspection SpellCheckingInspection
class GbasGrdStAcDes(Enum):
	"""3 Members, GADA ... GADC"""
	GADA = 0
	GADB = 1
	GADC = 2


# noinspection SpellCheckingInspection
class GbasGrdStRefRec(Enum):
	"""3 Members, GW2R ... GW4R"""
	GW2R = 0
	GW3R = 1
	GW4R = 2


# noinspection SpellCheckingInspection
class GbasMarkMode(Enum):
	"""6 Members, PATTern ... TRIGger"""
	PATTern = 0
	PPS = 1
	PULSe = 2
	RATio = 3
	RESTart = 4
	TRIGger = 5


# noinspection SpellCheckingInspection
class GbasMode(Enum):
	"""2 Members, GBAS ... SCAT"""
	GBAS = 0
	SCAT = 1


# noinspection SpellCheckingInspection
class GbasRunLet(Enum):
	"""4 Members, LETC ... NLETter"""
	LETC = 0
	LETL = 1
	LETR = 2
	NLETter = 3


# noinspection SpellCheckingInspection
class GbasSsid(Enum):
	"""8 Members, A ... H"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	G = 6
	H = 7


# noinspection SpellCheckingInspection
class Gilter(Enum):
	"""1 Members, GAUSs ... GAUSs"""
	GAUSs = 0


# noinspection SpellCheckingInspection
class GilterEdge(Enum):
	"""1 Members, LGAuss ... LGAuss"""
	LGAuss = 0


# noinspection SpellCheckingInspection
class GilterHigh(Enum):
	"""2 Members, ENPShape ... EWPShape"""
	ENPShape = 0
	EWPShape = 1


# noinspection SpellCheckingInspection
class GlobMimoConf(Enum):
	"""4 Members, SIBF ... TX4"""
	SIBF = 0
	TX1 = 1
	TX2 = 2
	TX4 = 3


# noinspection SpellCheckingInspection
class Granularity(Enum):
	"""5 Members, N16 ... NCON"""
	N16 = 0
	N2 = 1
	N4 = 2
	N8 = 3
	NCON = 4


# noinspection SpellCheckingInspection
class GsmBursDataSour(Enum):
	"""11 Members, ALL0 ... PN9"""
	ALL0 = 0
	ALL1 = 1
	DLISt = 2
	PATTern = 3
	PN11 = 4
	PN15 = 5
	PN16 = 6
	PN20 = 7
	PN21 = 8
	PN23 = 9
	PN9 = 10


# noinspection SpellCheckingInspection
class GsmBursFix(Enum):
	"""3 Members, COMPact ... USER"""
	COMPact = 0
	STANdard = 1
	USER = 2


# noinspection SpellCheckingInspection
class GsmBursPowerRatio(Enum):
	"""8 Members, SCPIR0 ... SCPIR7"""
	SCPIR0 = 0
	SCPIR1 = 1
	SCPIR2 = 2
	SCPIR3 = 3
	SCPIR4 = 4
	SCPIR5 = 5
	SCPIR6 = 6
	SCPIR7 = 7


# noinspection SpellCheckingInspection
class GsmBursPowMode(Enum):
	"""3 Members, ATT ... OFF"""
	ATT = 0
	FULL = 1
	OFF = 2


# noinspection SpellCheckingInspection
class GsmBursSlotAtt(Enum):
	"""7 Members, A1 ... A7"""
	A1 = 0
	A2 = 1
	A3 = 2
	A4 = 3
	A5 = 4
	A6 = 5
	A7 = 6


# noinspection SpellCheckingInspection
class GsmBursSync(Enum):
	"""4 Members, T0 ... USER"""
	T0 = 0
	T1 = 1
	T2 = 2
	USER = 3


# noinspection SpellCheckingInspection
class GsmBursTsc(Enum):
	"""9 Members, T0 ... USER"""
	T0 = 0
	T1 = 1
	T2 = 2
	T3 = 3
	T4 = 4
	T5 = 5
	T6 = 6
	T7 = 7
	USER = 8


# noinspection SpellCheckingInspection
class GsmBursTscExt(Enum):
	"""4 Members, COMPact ... USER"""
	COMPact = 0
	CTS = 1
	STANdard = 2
	USER = 3


# noinspection SpellCheckingInspection
class GsmBursType(Enum):
	"""23 Members, A16Qam ... SYNC"""
	A16Qam = 0
	A32Qam = 1
	AAQPsk = 2
	ACCess = 3
	ADATa = 4
	AEDGe = 5
	DUMMy = 6
	EDGE = 7
	FCORrection = 8
	H16Qam = 9
	H32Qam = 10
	HA16Qam = 11
	HA32Qam = 12
	HALF = 13
	HAQPsk = 14
	HQPSk = 15
	N16Qam = 16
	N32Qam = 17
	NAFF = 18
	NAFH = 19
	NAHH = 20
	NORMal = 21
	SYNC = 22


# noinspection SpellCheckingInspection
class GsmMarkMode(Enum):
	"""7 Members, FRAMe ... TRIGger"""
	FRAMe = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	SDEF = 4
	SLOT = 5
	TRIGger = 6


# noinspection SpellCheckingInspection
class GsmMode(Enum):
	"""4 Members, DOUBle ... UNFRamed"""
	DOUBle = 0
	MULTiframe = 1
	SINGle = 2
	UNFRamed = 3


# noinspection SpellCheckingInspection
class GsmModType16Qam(Enum):
	"""1 Members, QAM16EDge ... QAM16EDge"""
	QAM16EDge = 0


# noinspection SpellCheckingInspection
class GsmModType32Qam(Enum):
	"""1 Members, QAM32EDge ... QAM32EDge"""
	QAM32EDge = 0


# noinspection SpellCheckingInspection
class GsmModTypeAqpsk(Enum):
	"""1 Members, AQPSk ... AQPSk"""
	AQPSk = 0


# noinspection SpellCheckingInspection
class GsmModTypeEdge(Enum):
	"""1 Members, P8EDge ... P8EDge"""
	P8EDge = 0


# noinspection SpellCheckingInspection
class GsmModTypeGsm(Enum):
	"""2 Members, FSK2 ... MSK"""
	FSK2 = 0
	MSK = 1


# noinspection SpellCheckingInspection
class GsmModTypeQpsk(Enum):
	"""1 Members, QEDGe ... QEDGe"""
	QEDGe = 0


# noinspection SpellCheckingInspection
class GsmSimMode(Enum):
	"""8 Members, AQPSk ... N32Qam"""
	AQPSk = 0
	EDGE = 1
	GSM = 2
	H16Qam = 3
	H32Qam = 4
	HQPSk = 5
	N16Qam = 6
	N32Qam = 7


# noinspection SpellCheckingInspection
class GsmSymbRateMode(Enum):
	"""2 Members, HSRate ... NSRate"""
	HSRate = 0
	NSRate = 1


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
class HilIfc(Enum):
	"""2 Members, SCPI ... UDP"""
	SCPI = 0
	UDP = 1


# noinspection SpellCheckingInspection
class HrpUwbActSegmentLength(Enum):
	"""8 Members, ASL_1024 ... ASL_64"""
	ASL_1024 = 0
	ASL_128 = 1
	ASL_16 = 2
	ASL_2048 = 3
	ASL_256 = 4
	ASL_32 = 5
	ASL_512 = 6
	ASL_64 = 7


# noinspection SpellCheckingInspection
class HrpUwbActSegmentNum(Enum):
	"""4 Members, ASN_1 ... ASN_4"""
	ASN_1 = 0
	ASN_2 = 1
	ASN_3 = 2
	ASN_4 = 3


# noinspection SpellCheckingInspection
class HrpUwbChipsPerBurst(Enum):
	"""9 Members, CPB_1 ... CPB_8"""
	CPB_1 = 0
	CPB_128 = 1
	CPB_16 = 2
	CPB_2 = 3
	CPB_32 = 4
	CPB_4 = 5
	CPB_512 = 6
	CPB_64 = 7
	CPB_8 = 8


# noinspection SpellCheckingInspection
class HrpUwbClocMode(Enum):
	"""3 Members, CSAMple ... SAMPle"""
	CSAMple = 0
	MSAMple = 1
	SAMPle = 2


# noinspection SpellCheckingInspection
class HrpUwbCodeIndex(Enum):
	"""32 Members, CI_1 ... CI_9"""
	CI_1 = 0
	CI_10 = 1
	CI_11 = 2
	CI_12 = 3
	CI_13 = 4
	CI_14 = 5
	CI_15 = 6
	CI_16 = 7
	CI_17 = 8
	CI_18 = 9
	CI_19 = 10
	CI_2 = 11
	CI_20 = 12
	CI_21 = 13
	CI_22 = 14
	CI_23 = 15
	CI_24 = 16
	CI_25 = 17
	CI_26 = 18
	CI_27 = 19
	CI_28 = 20
	CI_29 = 21
	CI_3 = 22
	CI_30 = 23
	CI_31 = 24
	CI_32 = 25
	CI_4 = 26
	CI_5 = 27
	CI_6 = 28
	CI_7 = 29
	CI_8 = 30
	CI_9 = 31


# noinspection SpellCheckingInspection
class HrpUwbConvConsLen(Enum):
	"""2 Members, CL3 ... CL7"""
	CL3 = 0
	CL7 = 1


# noinspection SpellCheckingInspection
class HrpUwbDataSource(Enum):
	"""11 Members, DLISt ... ZERO"""
	DLISt = 0
	ONE = 1
	PATT = 2
	PN11 = 3
	PN15 = 4
	PN16 = 5
	PN20 = 6
	PN21 = 7
	PN23 = 8
	PN9 = 9
	ZERO = 10


# noinspection SpellCheckingInspection
class HrpUwbDeltaLength(Enum):
	"""3 Members, DL_16 ... DL_64"""
	DL_16 = 0
	DL_4 = 1
	DL_64 = 2


# noinspection SpellCheckingInspection
class HrpUwbHopBurst(Enum):
	"""3 Members, HB_2 ... HB_8"""
	HB_2 = 0
	HB_32 = 1
	HB_8 = 2


# noinspection SpellCheckingInspection
class HrpUwbMacFcsLength(Enum):
	"""2 Members, MFL_2 ... MFL_4"""
	MFL_2 = 0
	MFL_4 = 1


# noinspection SpellCheckingInspection
class HrpUwbMacLenAddress(Enum):
	"""3 Members, L0 ... L8"""
	L0 = 0
	L2 = 1
	L8 = 2


# noinspection SpellCheckingInspection
class HrpUwbMacLenFrameControl(Enum):
	"""2 Members, L1 ... L2"""
	L1 = 0
	L2 = 1


# noinspection SpellCheckingInspection
class HrpUwbMacLenPanId(Enum):
	"""2 Members, L0 ... L2"""
	L0 = 0
	L2 = 1


# noinspection SpellCheckingInspection
class HrpUwbMacLenSeqNumber(Enum):
	"""2 Members, L0 ... L1"""
	L0 = 0
	L1 = 1


# noinspection SpellCheckingInspection
class HrpUwbMarkMode(Enum):
	"""2 Members, MAX ... RESTart"""
	MAX = 0
	RESTart = 1


# noinspection SpellCheckingInspection
class HrpUwbMaxDataLength(Enum):
	"""3 Members, MDL_1023 ... MDL_4095"""
	MDL_1023 = 0
	MDL_2047 = 1
	MDL_4095 = 2


# noinspection SpellCheckingInspection
class HrpUwbMode(Enum):
	"""3 Members, BPRF ... NONHRP"""
	BPRF = 0
	HPRF = 1
	NONHRP = 2


# noinspection SpellCheckingInspection
class HrpUwbOverSampling(Enum):
	"""8 Members, OS_1 ... OS_8"""
	OS_1 = 0
	OS_2 = 1
	OS_3 = 2
	OS_4 = 3
	OS_5 = 4
	OS_6 = 5
	OS_7 = 6
	OS_8 = 7


# noinspection SpellCheckingInspection
class HrpUwbPhrdAtaRateMode(Enum):
	"""4 Members, BMHP ... HMLR"""
	BMHP = 0
	BMLP = 1
	HMHR = 2
	HMLR = 3


# noinspection SpellCheckingInspection
class HrpUwbSfdIndex(Enum):
	"""9 Members, SFD_0 ... SFD_8"""
	SFD_0 = 0
	SFD_1 = 1
	SFD_2 = 2
	SFD_3 = 3
	SFD_4 = 4
	SFD_5 = 5
	SFD_6 = 6
	SFD_7 = 7
	SFD_8 = 8


# noinspection SpellCheckingInspection
class HrpUwbSfdlEngth(Enum):
	"""2 Members, SFDL_64 ... SFDL_8"""
	SFDL_64 = 0
	SFDL_8 = 1


# noinspection SpellCheckingInspection
class HrpUwbStsDeltaLen(Enum):
	"""2 Members, DL_4 ... DL_8"""
	DL_4 = 0
	DL_8 = 1


# noinspection SpellCheckingInspection
class HrpUwbStspAcketConfig(Enum):
	"""4 Members, SPC_0 ... SPC_3"""
	SPC_0 = 0
	SPC_1 = 1
	SPC_2 = 2
	SPC_3 = 3


# noinspection SpellCheckingInspection
class HrpUwbSyncLength(Enum):
	"""10 Members, SL_1024 ... SL_96"""
	SL_1024 = 0
	SL_128 = 1
	SL_16 = 2
	SL_24 = 3
	SL_256 = 4
	SL_32 = 5
	SL_4096 = 6
	SL_48 = 7
	SL_64 = 8
	SL_96 = 9


# noinspection SpellCheckingInspection
class HrpUwbUnit(Enum):
	"""2 Members, SAMP ... SEQ"""
	SAMP = 0
	SEQ = 1


# noinspection SpellCheckingInspection
class HrpUwbViterbiRate(Enum):
	"""2 Members, HALF ... ONE"""
	HALF = 0
	ONE = 1


# noinspection SpellCheckingInspection
class HsCompatMode(Enum):
	"""3 Members, REL7 ... REL8RT"""
	REL7 = 0
	REL8 = 1
	REL8RT = 2


# noinspection SpellCheckingInspection
class HsHsetPdscSlotForm(Enum):
	"""4 Members, _0 ... QPSK"""
	_0 = 0
	_1 = 1
	QAM16 = 2
	QPSK = 3


# noinspection SpellCheckingInspection
class HsHsetScchType(Enum):
	"""3 Members, LOPeration ... NORMal"""
	LOPeration = 0
	MIMO = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class HsHsetTable(Enum):
	"""2 Members, TAB0 ... TAB1"""
	TAB0 = 0
	TAB1 = 1


# noinspection SpellCheckingInspection
class HsHsetType(Enum):
	"""18 Members, P10QAM16 ... USER"""
	P10QAM16 = 0
	P10QPSK = 1
	P11QAM64QAM16 = 2
	P12QPSK = 3
	P1QAM16 = 4
	P1QPSK = 5
	P2QAM16 = 6
	P2QPSK = 7
	P3QAM16 = 8
	P3QPSK = 9
	P4QPSK = 10
	P5QPSK = 11
	P6QAM16 = 12
	P6QPSK = 13
	P7QPSK = 14
	P8QAM64 = 15
	P9QAM16QPSK = 16
	USER = 17


# noinspection SpellCheckingInspection
class HsMimoCqiType(Enum):
	"""3 Members, TADT ... TB"""
	TADT = 0
	TAST = 1
	TB = 2


# noinspection SpellCheckingInspection
class HsMimoHarqMode(Enum):
	"""7 Members, AACK ... SNACk"""
	AACK = 0
	ANACk = 1
	DTX = 2
	NACK = 3
	NNACk = 4
	SACK = 5
	SNACk = 6


# noinspection SpellCheckingInspection
class HsMode(Enum):
	"""7 Members, CONTinuous ... PSF4"""
	CONTinuous = 0
	HSET = 1
	PSF0 = 2
	PSF1 = 3
	PSF2 = 4
	PSF3 = 5
	PSF4 = 6


# noinspection SpellCheckingInspection
class HsRel8CqiType(Enum):
	"""6 Members, CCQI ... TB"""
	CCQI = 0
	CQI = 1
	DTX = 2
	TADT = 3
	TAST = 4
	TB = 5


# noinspection SpellCheckingInspection
class HsRel8HarqMode(Enum):
	"""94 Members, A ... S2_N_N_N"""
	A = 0
	D_DTX = 1
	DTX = 2
	M_A = 3
	M_AA = 4
	M_AN = 5
	M_N = 6
	M_NA = 7
	M_NN = 8
	MS_A_A = 9
	MS_A_AA = 10
	MS_A_AN = 11
	MS_A_D = 12
	MS_A_N = 13
	MS_A_NA = 14
	MS_A_NN = 15
	MS_AA_A = 16
	MS_AA_AA = 17
	MS_AA_AN = 18
	MS_AA_D = 19
	MS_AA_N = 20
	MS_AA_NA = 21
	MS_AA_NN = 22
	MS_AN_A = 23
	MS_AN_AA = 24
	MS_AN_AN = 25
	MS_AN_D = 26
	MS_AN_N = 27
	MS_AN_NA = 28
	MS_AN_NN = 29
	MS_D_A = 30
	MS_D_AA = 31
	MS_D_AN = 32
	MS_D_N = 33
	MS_D_NA = 34
	MS_D_NN = 35
	MS_N_A = 36
	MS_N_AA = 37
	MS_N_AN = 38
	MS_N_D = 39
	MS_N_N = 40
	MS_N_NA = 41
	MS_N_NN = 42
	MS_NA_A = 43
	MS_NA_AA = 44
	MS_NA_AN = 45
	MS_NA_D = 46
	MS_NA_N = 47
	MS_NA_NA = 48
	MS_NA_NN = 49
	MS_NN_A = 50
	MS_NN_AA = 51
	MS_NN_AN = 52
	MS_NN_D = 53
	MS_NN_N = 54
	MS_NN_NA = 55
	MS_NN_NN = 56
	N = 57
	POST = 58
	PRE = 59
	S_A_A = 60
	S_A_D = 61
	S_A_N = 62
	S_D_A = 63
	S_D_N = 64
	S_N_A = 65
	S_N_D = 66
	S_N_N = 67
	S2_A_A_A = 68
	S2_A_A_D = 69
	S2_A_A_N = 70
	S2_A_D_A = 71
	S2_A_D_D = 72
	S2_A_D_N = 73
	S2_A_N_A = 74
	S2_A_N_D = 75
	S2_A_N_N = 76
	S2_D_A_A = 77
	S2_D_A_D = 78
	S2_D_A_N = 79
	S2_D_D_A = 80
	S2_D_D_N = 81
	S2_D_N_A = 82
	S2_D_N_D = 83
	S2_D_N_N = 84
	S2_N_A_A = 85
	S2_N_A_D = 86
	S2_N_A_N = 87
	S2_N_D_A = 88
	S2_N_D_D = 89
	S2_N_D_N = 90
	S2_N_N_A = 91
	S2_N_N_D = 92
	S2_N_N_N = 93


# noinspection SpellCheckingInspection
class HsUpaAgchScope(Enum):
	"""2 Members, ALL ... PER"""
	ALL = 0
	PER = 1


# noinspection SpellCheckingInspection
class HsUpaCellType(Enum):
	"""2 Members, NOSERVing ... SERVing"""
	NOSERVing = 0
	SERVing = 1


# noinspection SpellCheckingInspection
class HsUpaDchTti(Enum):
	"""2 Members, _10ms ... _2ms"""
	_10ms = 0
	_2ms = 1


# noinspection SpellCheckingInspection
class HsUpaFrcMode(Enum):
	"""9 Members, _1 ... USER"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3
	_5 = 4
	_6 = 5
	_7 = 6
	_8 = 7
	USER = 8


# noinspection SpellCheckingInspection
class HsUpaFrcTable(Enum):
	"""6 Members, TAB0TTI10 ... TAB3TTI2"""
	TAB0TTI10 = 0
	TAB0TTI2 = 1
	TAB1TTI10 = 2
	TAB1TTI2 = 3
	TAB2TTI2 = 4
	TAB3TTI2 = 5


# noinspection SpellCheckingInspection
class HsUpaHsimMode(Enum):
	"""2 Members, HFEedback ... VHARq"""
	HFEedback = 0
	VHARq = 1


# noinspection SpellCheckingInspection
class HsUpaMod(Enum):
	"""2 Members, BPSK ... PAM4"""
	BPSK = 0
	PAM4 = 1


# noinspection SpellCheckingInspection
class Hybrid(Enum):
	"""7 Members, BEIDou ... SBAS"""
	BEIDou = 0
	GALileo = 1
	GLONass = 2
	GPS = 3
	NAVic = 4
	QZSS = 5
	SBAS = 6


# noinspection SpellCheckingInspection
class IdEutraDataSourceDlEmtc(Enum):
	"""19 Members, DLISt ... ZERO"""
	DLISt = 0
	MIB = 1
	ONE = 2
	PATTern = 3
	PN11 = 4
	PN15 = 5
	PN16 = 6
	PN20 = 7
	PN21 = 8
	PN23 = 9
	PN9 = 10
	PRNTi = 11
	RARNti = 12
	SIBBr = 13
	USER1 = 14
	USER2 = 15
	USER3 = 16
	USER4 = 17
	ZERO = 18


# noinspection SpellCheckingInspection
class IdEutraEmtcPrachStartingSfPeriod(Enum):
	"""9 Members, _128 ... NONE"""
	_128 = 0
	_16 = 1
	_2 = 2
	_256 = 3
	_32 = 4
	_4 = 5
	_64 = 6
	_8 = 7
	NONE = 8


# noinspection SpellCheckingInspection
class IdEutraNbiotMode(Enum):
	"""3 Members, ALON ... INBD"""
	ALON = 0
	GBD = 1
	INBD = 2


# noinspection SpellCheckingInspection
class IecTermMode(Enum):
	"""2 Members, EOI ... STANdard"""
	EOI = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class IlbUndleSize(Enum):
	"""3 Members, BS2 ... BS6"""
	BS2 = 0
	BS3 = 1
	BS6 = 2


# noinspection SpellCheckingInspection
class ImpG50G1K(Enum):
	"""2 Members, G1K ... G50"""
	G1K = 0
	G50 = 1


# noinspection SpellCheckingInspection
class ImpG50High(Enum):
	"""2 Members, G50 ... HIGH"""
	G50 = 0
	HIGH = 1


# noinspection SpellCheckingInspection
class InclExcl(Enum):
	"""2 Members, EXCLude ... INCLude"""
	EXCLude = 0
	INCLude = 1


# noinspection SpellCheckingInspection
class InpConnBbSignal(Enum):
	"""4 Members, CLOCk ... TRIGger"""
	CLOCk = 0
	DATA = 1
	FEEDback = 2
	TRIGger = 3


# noinspection SpellCheckingInspection
class InpOutpConnGlbMapSign(Enum):
	"""40 Members, BERCLKIN ... VIDEOB"""
	BERCLKIN = 0
	BERDATENIN = 1
	BERDATIN = 2
	BERRESTIN = 3
	CLOCK1 = 4
	CLOCK2 = 5
	DATA = 6
	ERRTA = 7
	ERRTB = 8
	FEEDback = 9
	IPULSA = 10
	IPULSB = 11
	MARKA1 = 12
	MARKA2 = 13
	MARKA3 = 14
	MARKB1 = 15
	MARKB2 = 16
	MARKB3 = 17
	MARKC1 = 18
	MARKC2 = 19
	MARKC3 = 20
	MARKD1 = 21
	MARKD2 = 22
	MARKD3 = 23
	NONE = 24
	NSEGM1 = 25
	NSEGM2 = 26
	OPULSA = 27
	OPULSB = 28
	RTRIGA = 29
	RTRIGB = 30
	SVALA = 31
	SVALB = 32
	SYNCA = 33
	SYNCB = 34
	SYNCIN = 35
	TRIG1 = 36
	TRIG2 = 37
	VIDEOA = 38
	VIDEOB = 39


# noinspection SpellCheckingInspection
class InputImpRf(Enum):
	"""3 Members, G10K ... G50"""
	G10K = 0
	G1K = 1
	G50 = 2


# noinspection SpellCheckingInspection
class InstSetup(Enum):
	"""2 Members, U1PORT ... U2PORT"""
	U1PORT = 0
	U2PORT = 1


# noinspection SpellCheckingInspection
class IntelSizeAll(Enum):
	"""3 Members, IS2 ... IS6"""
	IS2 = 0
	IS3 = 1
	IS6 = 2


# noinspection SpellCheckingInspection
class InterfererTypeCw(Enum):
	"""1 Members, CW ... CW"""
	CW = 0


# noinspection SpellCheckingInspection
class InterfererTypeNr(Enum):
	"""3 Members, CW ... NR"""
	CW = 0
	NNR = 1
	NR = 2


# noinspection SpellCheckingInspection
class Interpolation(Enum):
	"""3 Members, LINear ... POWer"""
	LINear = 0
	OFF = 1
	POWer = 2


# noinspection SpellCheckingInspection
class IonModel(Enum):
	"""4 Members, KLOBuchar ... NONE"""
	KLOBuchar = 0
	MOPS = 1
	NEQuick = 2
	NONE = 3


# noinspection SpellCheckingInspection
class IonoGridView(Enum):
	"""2 Members, GIVei ... VDELay"""
	GIVei = 0
	VDELay = 1


# noinspection SpellCheckingInspection
class IqGainAll(Enum):
	"""10 Members, AUTO ... DBM4"""
	AUTO = 0
	DB0 = 1
	DB2 = 2
	DB3 = 3
	DB4 = 4
	DB6 = 5
	DB8 = 6
	DBM2 = 7
	DBM3 = 8
	DBM4 = 9


# noinspection SpellCheckingInspection
class IqOutDispViaType(Enum):
	"""2 Members, LEVel ... PEP"""
	LEVel = 0
	PEP = 1


# noinspection SpellCheckingInspection
class IqOutEnvAdaption(Enum):
	"""3 Members, AUTO ... POWer"""
	AUTO = 0
	MANual = 1
	POWer = 2


# noinspection SpellCheckingInspection
class IqOutEnvDetrFunc(Enum):
	"""3 Members, F1 ... F3"""
	F1 = 0
	F2 = 1
	F3 = 2


# noinspection SpellCheckingInspection
class IqOutEnvEtRak(Enum):
	"""4 Members, ET1V2 ... USER"""
	ET1V2 = 0
	ET1V5 = 1
	ET2V0 = 2
	USER = 3


# noinspection SpellCheckingInspection
class IqOutEnvScale(Enum):
	"""2 Members, POWer ... VOLTage"""
	POWer = 0
	VOLTage = 1


# noinspection SpellCheckingInspection
class IqOutEnvShapeMode(Enum):
	"""6 Members, DETRoughing ... TABLe"""
	DETRoughing = 0
	LINear = 1
	OFF = 2
	POLYnomial = 3
	POWer = 4
	TABLe = 5


# noinspection SpellCheckingInspection
class IqOutEnvTerm(Enum):
	"""2 Members, GROund ... WIRE"""
	GROund = 0
	WIRE = 1


# noinspection SpellCheckingInspection
class IqOutEnvVrEf(Enum):
	"""2 Members, VCC ... VOUT"""
	VCC = 0
	VOUT = 1


# noinspection SpellCheckingInspection
class IqOutMode(Enum):
	"""3 Members, FIXed ... VATTenuated"""
	FIXed = 0
	VARiable = 1
	VATTenuated = 2


# noinspection SpellCheckingInspection
class IqOutType(Enum):
	"""2 Members, DIFFerential ... SINGle"""
	DIFFerential = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class IqSour(Enum):
	"""3 Members, ANALog ... DIFFerential"""
	ANALog = 0
	BASeband = 1
	DIFFerential = 2


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
class LfBwidth(Enum):
	"""2 Members, BW0M2 ... BW10m"""
	BW0M2 = 0
	BW10m = 1


# noinspection SpellCheckingInspection
class LfFreqMode(Enum):
	"""3 Members, CW ... SWEep"""
	CW = 0
	FIXed = 1
	SWEep = 2


# noinspection SpellCheckingInspection
class LfShapeBfAmily(Enum):
	"""5 Members, PULSe ... TRIangle"""
	PULSe = 0
	SINE = 1
	SQUare = 2
	TRAPeze = 3
	TRIangle = 4


# noinspection SpellCheckingInspection
class LfSource(Enum):
	"""17 Members, AM ... NOISe"""
	AM = 0
	AMA = 1
	AMB = 2
	EXT1 = 3
	EXT2 = 4
	FMPM = 5
	FMPMA = 6
	FMPMB = 7
	LF1 = 8
	LF1A = 9
	LF1B = 10
	LF2 = 11
	LF2A = 12
	LF2B = 13
	NOISA = 14
	NOISB = 15
	NOISe = 16


# noinspection SpellCheckingInspection
class LinkDir(Enum):
	"""4 Members, DOWN ... UP"""
	DOWN = 0
	FORWard = 1
	REVerse = 2
	UP = 3


# noinspection SpellCheckingInspection
class LinkDir2(Enum):
	"""3 Members, DOWN ... UP"""
	DOWN = 0
	SIDE = 1
	UP = 2


# noinspection SpellCheckingInspection
class LmodRunMode(Enum):
	"""2 Members, LEARned ... LIVE"""
	LEARned = 0
	LIVE = 1


# noinspection SpellCheckingInspection
class LocationModel(Enum):
	"""3 Members, HIL ... STATic"""
	HIL = 0
	MOVing = 1
	STATic = 2


# noinspection SpellCheckingInspection
class LogFmtSat(Enum):
	"""1 Members, CSV ... CSV"""
	CSV = 0


# noinspection SpellCheckingInspection
class LogMode(Enum):
	"""2 Members, OFFLine ... RT"""
	OFFLine = 0
	RT = 1


# noinspection SpellCheckingInspection
class LogRes(Enum):
	"""7 Members, R02S ... R5S"""
	R02S = 0
	R04S = 1
	R08S = 2
	R10S = 3
	R1S = 4
	R2S = 5
	R5S = 6


# noinspection SpellCheckingInspection
class LoModeW(Enum):
	"""6 Members, AOFF ... INTernal"""
	AOFF = 0
	BOFF = 1
	COUPled = 2
	ECOupled = 3
	EXTernal = 4
	INTernal = 5


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
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class LteCrsCarrierBwAll(Enum):
	"""6 Members, N100 ... N75"""
	N100 = 0
	N15 = 1
	N25 = 2
	N50 = 3
	N6 = 4
	N75 = 5


# noinspection SpellCheckingInspection
class MappingType(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MarkConf(Enum):
	"""2 Members, FRAM ... UNCH"""
	FRAM = 0
	UNCH = 1


# noinspection SpellCheckingInspection
class MarkMode(Enum):
	"""1 Members, RESTart ... RESTart"""
	RESTart = 0


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
class MarkModeB(Enum):
	"""15 Members, CSPeriod ... USER"""
	CSPeriod = 0
	DPC = 1
	DPCC = 2
	EDCH = 3
	HACK = 4
	HFE = 5
	LPP = 6
	PCQI = 7
	PMP = 8
	RATio = 9
	RFRame = 10
	SFNR = 11
	SLOT = 12
	TRIGger = 13
	USER = 14


# noinspection SpellCheckingInspection
class MarkModeGnss(Enum):
	"""6 Members, PATTern ... RATio"""
	PATTern = 0
	PP2S = 1
	PPS = 2
	PPS10 = 3
	PULSe = 4
	RATio = 5


# noinspection SpellCheckingInspection
class MatProp(Enum):
	"""2 Members, PERM ... PLOSS"""
	PERM = 0
	PLOSS = 1


# noinspection SpellCheckingInspection
class MaxCbgaLl(Enum):
	"""5 Members, DISabled ... G8"""
	DISabled = 0
	G2 = 1
	G4 = 2
	G6 = 3
	G8 = 4


# noinspection SpellCheckingInspection
class MaxNrofPorts(Enum):
	"""2 Members, P1 ... P2"""
	P1 = 0
	P2 = 1


# noinspection SpellCheckingInspection
class MccwCrestFactMode(Enum):
	"""3 Members, CHIRp ... SLOW"""
	CHIRp = 0
	OFF = 1
	SLOW = 2


# noinspection SpellCheckingInspection
class McsTable(Enum):
	"""3 Members, QAM256 ... QAM64LSE"""
	QAM256 = 0
	QAM64 = 1
	QAM64LSE = 2


# noinspection SpellCheckingInspection
class McsTablePdsch(Enum):
	"""4 Members, QAM1024 ... QAM64LSE"""
	QAM1024 = 0
	QAM256 = 1
	QAM64 = 2
	QAM64LSE = 3


# noinspection SpellCheckingInspection
class MinPrEv(Enum):
	"""2 Members, _2 ... _8"""
	_2 = 0
	_8 = 1


# noinspection SpellCheckingInspection
class MobStatType(Enum):
	"""4 Members, UE1 ... UE4"""
	UE1 = 0
	UE2 = 1
	UE3 = 2
	UE4 = 3


# noinspection SpellCheckingInspection
class Mode(Enum):
	"""2 Members, DRAT ... FDR"""
	DRAT = 0
	FDR = 1


# noinspection SpellCheckingInspection
class ModType(Enum):
	"""10 Members, BPSK ... QPSK"""
	BPSK = 0
	BPSK2 = 1
	NSQAM2048 = 2
	NSQAM4096 = 3
	PSK8 = 4
	QAM1024 = 5
	QAM16 = 6
	QAM256 = 7
	QAM64 = 8
	QPSK = 9


# noinspection SpellCheckingInspection
class ModTypeRmc(Enum):
	"""3 Members, QAM256 ... QPSK"""
	QAM256 = 0
	QAM64 = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class ModulationA(Enum):
	"""2 Members, QAM16 ... QPSK"""
	QAM16 = 0
	QPSK = 1


# noinspection SpellCheckingInspection
class ModulationB(Enum):
	"""4 Members, QAM16 ... QPSK"""
	QAM16 = 0
	QAM256 = 1
	QAM64 = 2
	QPSK = 3


# noinspection SpellCheckingInspection
class ModulationC(Enum):
	"""3 Members, QAM16 ... QPSK"""
	QAM16 = 0
	QAM64 = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class ModulationD(Enum):
	"""5 Members, QAM1024 ... QPSK"""
	QAM1024 = 0
	QAM16 = 1
	QAM256 = 2
	QAM64 = 3
	QPSK = 4


# noinspection SpellCheckingInspection
class ModulationDevMode(Enum):
	"""3 Members, RATio ... UNCoupled"""
	RATio = 0
	TOTal = 1
	UNCoupled = 2


# noinspection SpellCheckingInspection
class ModulationF(Enum):
	"""6 Members, BPSK ... QPSK"""
	BPSK = 0
	CCK = 1
	DBPSK = 2
	DQPSK = 3
	PBCC = 4
	QPSK = 5


# noinspection SpellCheckingInspection
class MonitorDisplayType(Enum):
	"""7 Members, ATTitude ... TRAJectory"""
	ATTitude = 0
	CHANnels = 1
	MAP = 2
	POWer = 3
	SKY = 4
	TRACks = 5
	TRAJectory = 6


# noinspection SpellCheckingInspection
class MsMode(Enum):
	"""5 Members, DPCDch ... PRACh"""
	DPCDch = 0
	PCPCh = 1
	PPCPch = 2
	PPRach = 3
	PRACh = 4


# noinspection SpellCheckingInspection
class MultiInstrMsMode(Enum):
	"""2 Members, PRIMary ... SECondary"""
	PRIMary = 0
	SECondary = 1


# noinspection SpellCheckingInspection
class MultInstSyncState(Enum):
	"""2 Members, NOSYnc ... SYNC"""
	NOSYnc = 0
	SYNC = 1


# noinspection SpellCheckingInspection
class NavDataFormat(Enum):
	"""2 Members, CNAV ... LNAV"""
	CNAV = 0
	LNAV = 1


# noinspection SpellCheckingInspection
class NavMsgCtrl(Enum):
	"""3 Members, AUTO ... OFF"""
	AUTO = 0
	EDIT = 1
	OFF = 2


# noinspection SpellCheckingInspection
class NetMode(Enum):
	"""2 Members, AUTO ... STATic"""
	AUTO = 0
	STATic = 1


# noinspection SpellCheckingInspection
class NetModeStaticOnly(Enum):
	"""1 Members, STATic ... STATic"""
	STATic = 0


# noinspection SpellCheckingInspection
class NetProtocol(Enum):
	"""2 Members, TCP ... UDP"""
	TCP = 0
	UDP = 1


# noinspection SpellCheckingInspection
class NetProtocolUdpOnly(Enum):
	"""1 Members, UDP ... UDP"""
	UDP = 0


# noinspection SpellCheckingInspection
class NfcAckNack(Enum):
	"""2 Members, ACK ... NACK"""
	ACK = 0
	NACK = 1


# noinspection SpellCheckingInspection
class NfcAcssAttrib(Enum):
	"""2 Members, AARO ... AARW"""
	AARO = 0
	AARW = 1


# noinspection SpellCheckingInspection
class NfcApgEnericFrameType(Enum):
	"""3 Members, BOSDd ... STANdard"""
	BOSDd = 0
	SHORt = 1
	STANdard = 2


# noinspection SpellCheckingInspection
class NfcAppDataCod(Enum):
	"""2 Members, CRCB ... PROP"""
	CRCB = 0
	PROP = 1


# noinspection SpellCheckingInspection
class NfcAtnTmot(Enum):
	"""2 Members, ATN ... TOUT"""
	ATN = 0
	TOUT = 1


# noinspection SpellCheckingInspection
class NfcBitFrmSdd(Enum):
	"""6 Members, SDD0 ... SDD8"""
	SDD0 = 0
	SDD1 = 1
	SDD16 = 2
	SDD2 = 3
	SDD4 = 4
	SDD8 = 5


# noinspection SpellCheckingInspection
class NfcBlockType(Enum):
	"""3 Members, TPI ... TPS"""
	TPI = 0
	TPR = 1
	TPS = 2


# noinspection SpellCheckingInspection
class NfcCmdType(Enum):
	"""63 Members, ACK ... WRES"""
	ACK = 0
	ALAQ = 1
	ALBQ = 2
	ATBQ = 3
	ATBS = 4
	ATRQ = 5
	ATRS = 6
	ATSS = 7
	BLNK = 8
	CHKQ = 9
	CHKS = 10
	DEPQ = 11
	DEPS = 12
	DSLQ = 13
	DSLS = 14
	GENE = 15
	IDLE = 16
	NACK = 17
	PSLQ = 18
	PSLS = 19
	RATQ = 20
	RD8Q = 21
	RD8S = 22
	RDAQ = 23
	RDAS = 24
	RLAQ = 25
	RLAS = 26
	RLSQ = 27
	RLSS = 28
	RSGQ = 29
	RSGS = 30
	SDAQ = 31
	SDAS = 32
	SLAQ = 33
	SLAS = 34
	SMAR = 35
	SNAQ = 36
	SNAS = 37
	SNBQ = 38
	SNBS = 39
	SNFQ = 40
	SNFS = 41
	SPAQ = 42
	SPBQ = 43
	SPBS = 44
	SSLQ = 45
	T1RQ = 46
	T1RS = 47
	T2RQ = 48
	T2RS = 49
	T2WQ = 50
	T4AD = 51
	T4BD = 52
	UPDQ = 53
	UPDS = 54
	WE8Q = 55
	WE8S = 56
	WN8Q = 57
	WN8S = 58
	WNEQ = 59
	WNES = 60
	WREQ = 61
	WRES = 62


# noinspection SpellCheckingInspection
class NfcConfigType(Enum):
	"""8 Members, _0 ... T4A"""
	_0 = 0
	_1 = 1
	DT4A = 2
	NDEP = 3
	OFF = 4
	ON = 5
	T2 = 6
	T4A = 7


# noinspection SpellCheckingInspection
class NfcDeselWtx(Enum):
	"""2 Members, DSEL ... WTX"""
	DSEL = 0
	WTX = 1


# noinspection SpellCheckingInspection
class NfcDivForMod(Enum):
	"""2 Members, DIV2 ... DIV4"""
	DIV2 = 0
	DIV4 = 1


# noinspection SpellCheckingInspection
class NfcDivisor(Enum):
	"""4 Members, DIV1 ... DIV8"""
	DIV1 = 0
	DIV2 = 1
	DIV4 = 2
	DIV8 = 3


# noinspection SpellCheckingInspection
class NfcDsiDri(Enum):
	"""7 Members, D1 ... D8"""
	D1 = 0
	D16 = 1
	D2 = 2
	D32 = 3
	D4 = 4
	D64 = 5
	D8 = 6


# noinspection SpellCheckingInspection
class NfcFsc(Enum):
	"""9 Members, F128 ... F96"""
	F128 = 0
	F16 = 1
	F24 = 2
	F256 = 3
	F32 = 4
	F40 = 5
	F48 = 6
	F64 = 7
	F96 = 8


# noinspection SpellCheckingInspection
class NfcLength(Enum):
	"""2 Members, LEN2 ... LEN3"""
	LEN2 = 0
	LEN3 = 1


# noinspection SpellCheckingInspection
class NfcLenReduct(Enum):
	"""4 Members, LR128 ... LR64"""
	LR128 = 0
	LR192 = 1
	LR254 = 2
	LR64 = 3


# noinspection SpellCheckingInspection
class NfcMinTr0(Enum):
	"""3 Members, TR00 ... TR02"""
	TR00 = 0
	TR01 = 1
	TR02 = 2


# noinspection SpellCheckingInspection
class NfcMinTr1(Enum):
	"""3 Members, TR10 ... TR12"""
	TR10 = 0
	TR11 = 1
	TR12 = 2


# noinspection SpellCheckingInspection
class NfcMinTr2(Enum):
	"""4 Members, TR20 ... TR23"""
	TR20 = 0
	TR21 = 1
	TR22 = 2
	TR23 = 3


# noinspection SpellCheckingInspection
class NfcNack(Enum):
	"""4 Members, NCK0 ... NCK5"""
	NCK0 = 0
	NCK1 = 1
	NCK4 = 2
	NCK5 = 3


# noinspection SpellCheckingInspection
class NfcNfcid1Sz(Enum):
	"""3 Members, DOUBle ... TRIPle"""
	DOUBle = 0
	SINGle = 1
	TRIPle = 2


# noinspection SpellCheckingInspection
class NfcNfcid2FmtTp(Enum):
	"""2 Members, NDEP ... TT3"""
	NDEP = 0
	TT3 = 1


# noinspection SpellCheckingInspection
class NfcNumOfSlots(Enum):
	"""5 Members, S1 ... S8"""
	S1 = 0
	S16 = 1
	S2 = 2
	S4 = 3
	S8 = 4


# noinspection SpellCheckingInspection
class NfcPcktSelect(Enum):
	"""2 Members, PCK1 ... PCK2"""
	PCK1 = 0
	PCK2 = 1


# noinspection SpellCheckingInspection
class NfcPfbType(Enum):
	"""3 Members, ANACk ... SUPer"""
	ANACk = 0
	INFO = 1
	SUPer = 2


# noinspection SpellCheckingInspection
class NfcPredef(Enum):
	"""5 Members, APA ... FPS"""
	APA = 0
	APS = 1
	BPA = 2
	BPS = 3
	FPS = 4


# noinspection SpellCheckingInspection
class NfcProtocolMode(Enum):
	"""5 Members, EMVA ... NFCF"""
	EMVA = 0
	EMVB = 1
	NFCA = 2
	NFCB = 3
	NFCF = 4


# noinspection SpellCheckingInspection
class NfcRc(Enum):
	"""3 Members, APFS ... SCIR"""
	APFS = 0
	NSCI = 1
	SCIR = 2


# noinspection SpellCheckingInspection
class NfcSelCmd(Enum):
	"""3 Members, CL1 ... CL3"""
	CL1 = 0
	CL2 = 1
	CL3 = 2


# noinspection SpellCheckingInspection
class NfcSlotNumber(Enum):
	"""15 Members, SN10 ... SN9"""
	SN10 = 0
	SN11 = 1
	SN12 = 2
	SN13 = 3
	SN14 = 4
	SN15 = 5
	SN16 = 6
	SN2 = 7
	SN3 = 8
	SN4 = 9
	SN5 = 10
	SN6 = 11
	SN7 = 12
	SN8 = 13
	SN9 = 14


# noinspection SpellCheckingInspection
class NfcTransMode(Enum):
	"""2 Members, LISTen ... POLL"""
	LISTen = 0
	POLL = 1


# noinspection SpellCheckingInspection
class NfcTsn(Enum):
	"""5 Members, TSN1 ... TSN8"""
	TSN1 = 0
	TSN16 = 1
	TSN2 = 2
	TSN4 = 3
	TSN8 = 4


# noinspection SpellCheckingInspection
class NidSource(Enum):
	"""3 Members, CELL ... PCRS"""
	CELL = 0
	DMRS = 1
	PCRS = 2


# noinspection SpellCheckingInspection
class NoisAwgnDispMode(Enum):
	"""10 Members, BBMM1 ... RFB"""
	BBMM1 = 0
	BBMM2 = 1
	FADER1 = 2
	FADER2 = 3
	FADER3 = 4
	FADER4 = 5
	IQOUT1 = 6
	IQOUT2 = 7
	RFA = 8
	RFB = 9


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
class NoisDistrib(Enum):
	"""4 Members, EQUal ... UNIForm"""
	EQUal = 0
	GAUSs = 1
	NORMal = 2
	UNIForm = 3


# noinspection SpellCheckingInspection
class NormalInverted(Enum):
	"""2 Members, INVerted ... NORMal"""
	INVerted = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class Nprs(Enum):
	"""4 Members, _1 ... _6"""
	_1 = 0
	_2 = 1
	_4 = 2
	_6 = 3


# noinspection SpellCheckingInspection
class Nr5Gbsp(Enum):
	"""8 Members, BS10 ... BS80"""
	BS10 = 0
	BS160 = 1
	BS20 = 2
	BS320 = 3
	BS40 = 4
	BS5 = 5
	BS640 = 6
	BS80 = 7


# noinspection SpellCheckingInspection
class Nr5GcarDep(Enum):
	"""10 Members, BT36 ... LT3"""
	BT36 = 0
	BT37125 = 1
	FR1GT3 = 2
	FR1LT3 = 3
	FR2 = 4
	FR2_1 = 5
	FR2_2 = 6
	GT6 = 7
	GT7125 = 8
	LT3 = 9


# noinspection SpellCheckingInspection
class Nr5Gcbw(Enum):
	"""22 Members, BW10 ... BW90"""
	BW10 = 0
	BW100 = 1
	BW15 = 2
	BW1600 = 3
	BW20 = 4
	BW200 = 5
	BW2000 = 6
	BW25 = 7
	BW30 = 8
	BW35 = 9
	BW40 = 10
	BW400 = 11
	BW4000 = 12
	BW45 = 13
	BW5 = 14
	BW50 = 15
	BW60 = 16
	BW70 = 17
	BW80 = 18
	BW800 = 19
	BW8000 = 20
	BW90 = 21


# noinspection SpellCheckingInspection
class Nr5Gcontent(Enum):
	"""11 Members, COReset ... SRS"""
	COReset = 0
	CSIRs = 1
	DUMRe = 2
	LTECrs = 3
	PDSCh = 4
	PRACh = 5
	PRS = 6
	PUCCh = 7
	PUSCh = 8
	SPBCh = 9
	SRS = 10


# noinspection SpellCheckingInspection
class Nr5GcontentB(Enum):
	"""18 Members, COReset ... SSSPbch"""
	COReset = 0
	CSIRs = 1
	DUMRe = 2
	LTECrs = 3
	PDSCh = 4
	PRACh = 5
	PRS = 6
	PSBCh = 7
	PSCCh = 8
	PSCSs = 9
	PSFCh = 10
	PSSCh = 11
	PUCCh = 12
	PUNCturing = 13
	PUSCh = 14
	SPBCh = 15
	SRS = 16
	SSSPbch = 17


# noinspection SpellCheckingInspection
class Nr5GmarkConfigMode(Enum):
	"""3 Members, AUTO ... ULDL"""
	AUTO = 0
	MAN = 1
	ULDL = 2


# noinspection SpellCheckingInspection
class Nr5GmarkMode(Enum):
	"""7 Members, FRAM ... ULDL"""
	FRAM = 0
	PERiod = 1
	RATio = 2
	RESTart = 3
	SFNRestart = 4
	SUBFram = 5
	ULDL = 6


# noinspection SpellCheckingInspection
class Nr5GpbschCase(Enum):
	"""7 Members, A ... G"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	G = 6


# noinspection SpellCheckingInspection
class Nr5GpdschAp(Enum):
	"""12 Members, AP1000 ... AP1011"""
	AP1000 = 0
	AP1001 = 1
	AP1002 = 2
	AP1003 = 3
	AP1004 = 4
	AP1005 = 5
	AP1006 = 6
	AP1007 = 7
	AP1008 = 8
	AP1009 = 9
	AP1010 = 10
	AP1011 = 11


# noinspection SpellCheckingInspection
class Nr5GpdschConfigType(Enum):
	"""2 Members, T1 ... T2"""
	T1 = 0
	T2 = 1


# noinspection SpellCheckingInspection
class Nr5GpuschAp(Enum):
	"""12 Members, AP0 ... AP9"""
	AP0 = 0
	AP1 = 1
	AP10 = 2
	AP11 = 3
	AP2 = 4
	AP3 = 5
	AP4 = 6
	AP5 = 7
	AP6 = 8
	AP7 = 9
	AP8 = 10
	AP9 = 11


# noinspection SpellCheckingInspection
class NrsIdAll(Enum):
	"""2 Members, CID ... PUID"""
	CID = 0
	PUID = 1


# noinspection SpellCheckingInspection
class NumApsCsiRs(Enum):
	"""3 Members, N1 ... N4"""
	N1 = 0
	N2 = 1
	N4 = 2


# noinspection SpellCheckingInspection
class NumberA(Enum):
	"""4 Members, _1 ... _4"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3


# noinspection SpellCheckingInspection
class NumberOfPorts(Enum):
	"""3 Members, AP1 ... AP4"""
	AP1 = 0
	AP2 = 1
	AP4 = 2


# noinspection SpellCheckingInspection
class NumbersB(Enum):
	"""3 Members, _1 ... _4"""
	_1 = 0
	_2 = 1
	_4 = 2


# noinspection SpellCheckingInspection
class NumbersC(Enum):
	"""7 Members, _1 ... _8"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3
	_5 = 4
	_6 = 5
	_8 = 6


# noinspection SpellCheckingInspection
class NumbersD(Enum):
	"""2 Members, _2 ... _4"""
	_2 = 0
	_4 = 1


# noinspection SpellCheckingInspection
class NumbersE(Enum):
	"""32 Members, _0 ... _9"""
	_0 = 0
	_1 = 1
	_10 = 2
	_11 = 3
	_12 = 4
	_13 = 5
	_14 = 6
	_15 = 7
	_16 = 8
	_17 = 9
	_18 = 10
	_19 = 11
	_2 = 12
	_20 = 13
	_21 = 14
	_22 = 15
	_23 = 16
	_24 = 17
	_25 = 18
	_26 = 19
	_27 = 20
	_28 = 21
	_29 = 22
	_3 = 23
	_30 = 24
	_31 = 25
	_4 = 26
	_5 = 27
	_6 = 28
	_7 = 29
	_8 = 30
	_9 = 31


# noinspection SpellCheckingInspection
class NumbersG(Enum):
	"""4 Members, _0 ... _3"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3


# noinspection SpellCheckingInspection
class NumbersI(Enum):
	"""2 Members, _0 ... _1"""
	_0 = 0
	_1 = 1


# noinspection SpellCheckingInspection
class NumbersJ(Enum):
	"""13 Members, _10 ... _9"""
	_10 = 0
	_11 = 1
	_12 = 2
	_13 = 3
	_14 = 4
	_2 = 5
	_3 = 6
	_4 = 7
	_5 = 8
	_6 = 9
	_7 = 10
	_8 = 11
	_9 = 12


# noinspection SpellCheckingInspection
class NumbOfBasebands(Enum):
	"""5 Members, _0 ... _4"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	_4 = 4


# noinspection SpellCheckingInspection
class NumbSystAntenna(Enum):
	"""5 Members, ANT01 ... ANT08"""
	ANT01 = 0
	ANT02 = 1
	ANT03 = 2
	ANT04 = 3
	ANT08 = 4


# noinspection SpellCheckingInspection
class Numerology(Enum):
	"""8 Members, N120 ... X60"""
	N120 = 0
	N15 = 1
	N240 = 2
	N30 = 3
	N480 = 4
	N60 = 5
	N960 = 6
	X60 = 7


# noinspection SpellCheckingInspection
class NumerologyPrs(Enum):
	"""7 Members, N120 ... X60"""
	N120 = 0
	N15 = 1
	N30 = 2
	N480 = 3
	N60 = 4
	N960 = 5
	X60 = 6


# noinspection SpellCheckingInspection
class NumerologyRmc(Enum):
	"""3 Members, N15 ... N60"""
	N15 = 0
	N30 = 1
	N60 = 2


# noinspection SpellCheckingInspection
class NumPrbs(Enum):
	"""3 Members, PRB2 ... PRB8"""
	PRB2 = 0
	PRB4 = 1
	PRB8 = 2


# noinspection SpellCheckingInspection
class ObscEnvModel(Enum):
	"""7 Members, FULL ... VOBS"""
	FULL = 0
	GSR = 1
	LMM = 2
	LOS = 3
	MPATh = 4
	RPL = 5
	VOBS = 6


# noinspection SpellCheckingInspection
class ObscModelFullObsc(Enum):
	"""8 Members, BR1 ... USER"""
	BR1 = 0
	BR2 = 1
	LTUNnel = 2
	MTUNnel = 3
	P10M = 4
	P1H = 5
	P1M = 6
	USER = 7


# noinspection SpellCheckingInspection
class ObscModelSideBuil(Enum):
	"""4 Members, CUTTing ... USER"""
	CUTTing = 0
	HIGHway = 1
	SUB1 = 2
	USER = 3


# noinspection SpellCheckingInspection
class ObscModelVertObst(Enum):
	"""3 Members, URB1 ... USER"""
	URB1 = 0
	URB2 = 1
	USER = 2


# noinspection SpellCheckingInspection
class ObscPhysModel(Enum):
	"""2 Members, OBSCuration ... OMPath"""
	OBSCuration = 0
	OMPath = 1


# noinspection SpellCheckingInspection
class OcnsMode(Enum):
	"""4 Members, HSDP2 ... STANdard"""
	HSDP2 = 0
	HSDPa = 1
	M3I = 2
	STANdard = 3


# noinspection SpellCheckingInspection
class OffsetFactorN(Enum):
	"""3 Members, OFN_1 ... OFN_3"""
	OFN_1 = 0
	OFN_2 = 1
	OFN_3 = 2


# noinspection SpellCheckingInspection
class OffsetRelativeAll(Enum):
	"""2 Members, POINta ... TXBW"""
	POINta = 0
	TXBW = 1


# noinspection SpellCheckingInspection
class OneWebAckNackMode(Enum):
	"""1 Members, MUX ... MUX"""
	MUX = 0


# noinspection SpellCheckingInspection
class OneWebBfaNtSet(Enum):
	"""10 Members, AP5 ... AP8"""
	AP5 = 0
	AP7 = 1
	AP710 = 2
	AP711 = 3
	AP712 = 4
	AP713 = 5
	AP714 = 6
	AP78 = 7
	AP79 = 8
	AP8 = 9


# noinspection SpellCheckingInspection
class OneWebCcIndex(Enum):
	"""2 Members, PC ... SC1"""
	PC = 0
	SC1 = 1


# noinspection SpellCheckingInspection
class OneWebConfMode(Enum):
	"""2 Members, PREDefined ... USER"""
	PREDefined = 0
	USER = 1


# noinspection SpellCheckingInspection
class OneWebCyclicPrefixGs(Enum):
	"""1 Members, NORMal ... NORMal"""
	NORMal = 0


# noinspection SpellCheckingInspection
class OneWebDciFormat(Enum):
	"""7 Members, F0 ... F3OW"""
	F0 = 0
	F1A = 1
	F1OW = 2
	F2OW = 3
	F3 = 4
	F3A = 5
	F3OW = 6


# noinspection SpellCheckingInspection
class OneWebDlChannelBandwidth(Enum):
	"""1 Members, BW250_00 ... BW250_00"""
	BW250_00 = 0


# noinspection SpellCheckingInspection
class OneWebDlDataSourceUser(Enum):
	"""16 Members, DLISt ... ZERO"""
	DLISt = 0
	MIB = 1
	ONE = 2
	PATTern = 3
	PN11 = 4
	PN15 = 5
	PN16 = 6
	PN20 = 7
	PN21 = 8
	PN23 = 9
	PN9 = 10
	USER1 = 11
	USER2 = 12
	USER3 = 13
	USER4 = 14
	ZERO = 15


# noinspection SpellCheckingInspection
class OneWebDlModulation(Enum):
	"""3 Members, PSK8 ... QPSK"""
	PSK8 = 0
	QAM16 = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class OneWebDuplexModeRange(Enum):
	"""1 Members, FDD ... FDD"""
	FDD = 0


# noinspection SpellCheckingInspection
class OneWebGlobMimoConf(Enum):
	"""1 Members, TX1 ... TX1"""
	TX1 = 0


# noinspection SpellCheckingInspection
class OneWebOrthSequ(Enum):
	"""3 Members, ORS0 ... ORS2"""
	ORS0 = 0
	ORS1 = 1
	ORS2 = 2


# noinspection SpellCheckingInspection
class OneWebPdccFmt2(Enum):
	"""1 Members, VAR ... VAR"""
	VAR = 0


# noinspection SpellCheckingInspection
class OneWebPdcchCfg(Enum):
	"""8 Members, NONE ... USER4"""
	NONE = 0
	PRNTi = 1
	RARNti = 2
	SIRNti = 3
	USER1 = 4
	USER2 = 5
	USER3 = 6
	USER4 = 7


# noinspection SpellCheckingInspection
class OneWebPdcchType(Enum):
	"""1 Members, PDCCh ... PDCCh"""
	PDCCh = 0


# noinspection SpellCheckingInspection
class OneWebPuaChanCodMode(Enum):
	"""1 Members, ULSChonly ... ULSChonly"""
	ULSChonly = 0


# noinspection SpellCheckingInspection
class OneWebResBlckMap(Enum):
	"""2 Members, V80 ... V81"""
	V80 = 0
	V81 = 1


# noinspection SpellCheckingInspection
class OneWebSearchSpace(Enum):
	"""5 Members, _1 ... UE"""
	_1 = 0
	AUTO = 1
	COMMon = 2
	ON = 3
	UE = 4


# noinspection SpellCheckingInspection
class OneWebSimAnt(Enum):
	"""1 Members, ANT1 ... ANT1"""
	ANT1 = 0


# noinspection SpellCheckingInspection
class OneWebTxMode(Enum):
	"""3 Members, M1OW ... M3OW"""
	M1OW = 0
	M2OW = 1
	M3OW = 2


# noinspection SpellCheckingInspection
class OneWebUlChannelBandwidth(Enum):
	"""1 Members, BW20_00 ... BW20_00"""
	BW20_00 = 0


# noinspection SpellCheckingInspection
class OneWebUlContentType(Enum):
	"""3 Members, PUACh ... PUSCh"""
	PUACh = 0
	PUCCh = 1
	PUSCh = 2


# noinspection SpellCheckingInspection
class OutpConnBbSignal(Enum):
	"""36 Members, BGATA ... TRIGD"""
	BGATA = 0
	BGATB = 1
	BGATC = 2
	BGATD = 3
	CWMODA = 4
	CWMODB = 5
	CWMODC = 6
	CWMODD = 7
	HOPA = 8
	HOPB = 9
	HOPC = 10
	HOPD = 11
	LATTA = 12
	LATTB = 13
	LATTC = 14
	LATTD = 15
	MARKA1 = 16
	MARKA2 = 17
	MARKA3 = 18
	MARKB1 = 19
	MARKB2 = 20
	MARKB3 = 21
	MARKC1 = 22
	MARKC2 = 23
	MARKC3 = 24
	MARKD1 = 25
	MARKD2 = 26
	MARKD3 = 27
	SCLA = 28
	SCLB = 29
	SCLC = 30
	SCLD = 31
	TRIGA = 32
	TRIGB = 33
	TRIGC = 34
	TRIGD = 35


# noinspection SpellCheckingInspection
class OutpConnGlbSignal(Enum):
	"""33 Members, BERCLKOUT ... VIDEOB"""
	BERCLKOUT = 0
	BERDATENOUT = 1
	BERDATOUT = 2
	BERRESTOUT = 3
	HIGH = 4
	LOW = 5
	MARKA1 = 6
	MARKA2 = 7
	MARKA3 = 8
	MARKB1 = 9
	MARKB2 = 10
	MARKB3 = 11
	MARKC1 = 12
	MARKC2 = 13
	MARKC3 = 14
	MARKD1 = 15
	MARKD2 = 16
	MARKD3 = 17
	MTRigger = 18
	NONE = 19
	OPULSA = 20
	OPULSB = 21
	RTRIGA = 22
	RTRIGB = 23
	SVALA = 24
	SVALANegated = 25
	SVALB = 26
	SVALBNegated = 27
	SYNCA = 28
	SYNCB = 29
	SYNCOUT = 30
	VIDEOA = 31
	VIDEOB = 32


# noinspection SpellCheckingInspection
class Output(Enum):
	"""3 Members, NONE ... RFB"""
	NONE = 0
	RFA = 1
	RFB = 2


# noinspection SpellCheckingInspection
class PackFormat(Enum):
	"""8 Members, L1M ... QHSP6"""
	L1M = 0
	L2M = 1
	LCOD = 2
	QHSP2 = 3
	QHSP3 = 4
	QHSP4 = 5
	QHSP5 = 6
	QHSP6 = 7


# noinspection SpellCheckingInspection
class PageInd(Enum):
	"""4 Members, D144 ... D72"""
	D144 = 0
	D18 = 1
	D36 = 2
	D72 = 3


# noinspection SpellCheckingInspection
class PanelCbN1(Enum):
	"""8 Members, N1 ... N8"""
	N1 = 0
	N12 = 1
	N16 = 2
	N2 = 3
	N3 = 4
	N4 = 5
	N6 = 6
	N8 = 7


# noinspection SpellCheckingInspection
class PanelCbN2(Enum):
	"""4 Members, N1 ... N4"""
	N1 = 0
	N2 = 1
	N3 = 2
	N4 = 3


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class Parity(Enum):
	"""3 Members, EVEN ... ODD"""
	EVEN = 0
	NONE = 1
	ODD = 2


# noinspection SpellCheckingInspection
class PathUniCodBbin(Enum):
	"""3 Members, A ... B"""
	A = 0
	AB = 1
	B = 2


# noinspection SpellCheckingInspection
class PbchSfnRestPeriod(Enum):
	"""2 Members, PER3gpp ... PERSlength"""
	PER3gpp = 0
	PERSlength = 1


# noinspection SpellCheckingInspection
class PcmOdeAll(Enum):
	"""5 Members, _0 ... OFF"""
	_0 = 0
	_1 = 1
	AUTO = 2
	MANual = 3
	OFF = 4


# noinspection SpellCheckingInspection
class PdccFmt2(Enum):
	"""6 Members, _0 ... VAR"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	_minus1 = 4
	VAR = 5


# noinspection SpellCheckingInspection
class PdschSchedMode(Enum):
	"""3 Members, ASEQuence ... MANual"""
	ASEQuence = 0
	AUTO = 1
	MANual = 2


# noinspection SpellCheckingInspection
class PdscPowA(Enum):
	"""8 Members, _0 ... _minus6_dot_02"""
	_0 = 0
	_0_dot_97 = 1
	_2_dot_04 = 2
	_3_dot_01 = 3
	_minus1_dot_77 = 4
	_minus3_dot_01 = 5
	_minus4_dot_77 = 6
	_minus6_dot_02 = 7


# noinspection SpellCheckingInspection
class PhichNg(Enum):
	"""5 Members, NG1 ... NGCustom"""
	NG1 = 0
	NG1_2 = 1
	NG1_6 = 2
	NG2 = 3
	NGCustom = 4


# noinspection SpellCheckingInspection
class PhichPwrMode(Enum):
	"""2 Members, CONSt ... IND"""
	CONSt = 0
	IND = 1


# noinspection SpellCheckingInspection
class PilLen(Enum):
	"""5 Members, BIT0 ... BIT8"""
	BIT0 = 0
	BIT16 = 1
	BIT2 = 2
	BIT4 = 3
	BIT8 = 4


# noinspection SpellCheckingInspection
class PmMode(Enum):
	"""3 Members, HBANdwidth ... LNOise"""
	HBANdwidth = 0
	HDEViation = 1
	LNOise = 2


# noinspection SpellCheckingInspection
class PositionFormat(Enum):
	"""2 Members, DECimal ... DMS"""
	DECimal = 0
	DMS = 1


# noinspection SpellCheckingInspection
class PowAlcDetSensitivity(Enum):
	"""5 Members, AUTO ... MEDium"""
	AUTO = 0
	FIXed = 1
	HIGH = 2
	LOW = 3
	MEDium = 4


# noinspection SpellCheckingInspection
class PowAlcDriverAmp(Enum):
	"""5 Members, AUTO ... ONMG"""
	AUTO = 0
	FIX = 1
	OFF = 2
	ON = 3
	ONMG = 4


# noinspection SpellCheckingInspection
class PowAlcSampleLev(Enum):
	"""3 Members, ATTenuated ... MINimum"""
	ATTenuated = 0
	FULL = 1
	MINimum = 2


# noinspection SpellCheckingInspection
class PowAttModeSzu(Enum):
	"""3 Members, AUTO ... MANual"""
	AUTO = 0
	FIXed = 1
	MANual = 2


# noinspection SpellCheckingInspection
class PowAttRfOffMode(Enum):
	"""3 Members, FATTenuation ... UNCHanged"""
	FATTenuation = 0
	RECeive = 1
	UNCHanged = 2


# noinspection SpellCheckingInspection
class PowcLevRef(Enum):
	"""4 Members, DRMS ... URMS"""
	DRMS = 0
	FRMS = 1
	UEBurst = 2
	URMS = 3


# noinspection SpellCheckingInspection
class PowCntrlSelect(Enum):
	"""8 Members, SENS1 ... SENSor4"""
	SENS1 = 0
	SENS2 = 1
	SENS3 = 2
	SENS4 = 3
	SENSor1 = 4
	SENSor2 = 5
	SENSor3 = 6
	SENSor4 = 7


# noinspection SpellCheckingInspection
class PowContAssMode(Enum):
	"""2 Members, FDPCh ... NORMal"""
	FDPCh = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class PowContMode(Enum):
	"""3 Members, EXTernal ... TPC"""
	EXTernal = 0
	MANual = 1
	TPC = 2


# noinspection SpellCheckingInspection
class PowContStepMan(Enum):
	"""2 Members, MAN0 ... MAN1"""
	MAN0 = 0
	MAN1 = 1


# noinspection SpellCheckingInspection
class PowcRefChan(Enum):
	"""6 Members, NF ... SRS"""
	NF = 0
	PRACH = 1
	PUCCH = 2
	PUCPUS = 3
	PUSCH = 4
	SRS = 5


# noinspection SpellCheckingInspection
class PowerAttMode(Enum):
	"""5 Members, AUTO ... NORMal"""
	AUTO = 0
	FIXed = 1
	HPOWer = 2
	MANual = 3
	NORMal = 4


# noinspection SpellCheckingInspection
class PowerModeAll(Enum):
	"""4 Members, ACTvsf ... PSDConst"""
	ACTvsf = 0
	AVG = 1
	BURSt = 2
	PSDConst = 3


# noinspection SpellCheckingInspection
class PowerRampClocMode(Enum):
	"""2 Members, MULTisample ... SAMPle"""
	MULTisample = 0
	SAMPle = 1


# noinspection SpellCheckingInspection
class PowerRampMarkMode(Enum):
	"""5 Members, PRESweep ... UNCHanged"""
	PRESweep = 0
	RFBLanking = 1
	STARt = 2
	STOP = 3
	UNCHanged = 4


# noinspection SpellCheckingInspection
class PowerRampShape(Enum):
	"""3 Members, LINear ... TRIangle"""
	LINear = 0
	STAir = 1
	TRIangle = 2


# noinspection SpellCheckingInspection
class PowerRampSlope(Enum):
	"""2 Members, ASCending ... DESCending"""
	ASCending = 0
	DESCending = 1


# noinspection SpellCheckingInspection
class PowLevBehaviour(Enum):
	"""7 Members, AUTO ... USER"""
	AUTO = 0
	CONStant = 1
	CPHase = 2
	CVSWr = 3
	MONotone = 4
	UNINterrupted = 5
	USER = 6


# noinspection SpellCheckingInspection
class PowLevMode(Enum):
	"""3 Members, LOWDistortion ... NORMal"""
	LOWDistortion = 0
	LOWNoise = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class PowPreContLen(Enum):
	"""2 Members, S0 ... S8"""
	S0 = 0
	S8 = 1


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
class PrachFormatAll(Enum):
	"""13 Members, F0 ... FC2"""
	F0 = 0
	F1 = 1
	F2 = 2
	F3 = 3
	FA1 = 4
	FA2 = 5
	FA3 = 6
	FB1 = 7
	FB2 = 8
	FB3 = 9
	FB4 = 10
	FC0 = 11
	FC2 = 12


# noinspection SpellCheckingInspection
class PrachNumAll(Enum):
	"""8 Members, N1_25 ... N960"""
	N1_25 = 0
	N120 = 1
	N15 = 2
	N30 = 3
	N480 = 4
	N5 = 5
	N60 = 6
	N960 = 7


# noinspection SpellCheckingInspection
class PrachRestrictedSetAll(Enum):
	"""3 Members, ARES ... URES"""
	ARES = 0
	BRES = 1
	URES = 2


# noinspection SpellCheckingInspection
class PrachSeqLengthAll(Enum):
	"""4 Members, L1151 ... L839"""
	L1151 = 0
	L139 = 1
	L571 = 2
	L839 = 3


# noinspection SpellCheckingInspection
class PrbBundleSizeSet1(Enum):
	"""4 Members, N2WB ... WIDeband"""
	N2WB = 0
	N4 = 1
	N4WB = 2
	WIDeband = 3


# noinspection SpellCheckingInspection
class PrbBundleSizeSet2(Enum):
	"""2 Members, N4 ... WIDeband"""
	N4 = 0
	WIDeband = 1


# noinspection SpellCheckingInspection
class PrbBundlingType(Enum):
	"""3 Members, DYNamic ... STATic"""
	DYNamic = 0
	NOTC = 1
	STATic = 2


# noinspection SpellCheckingInspection
class PrecMode(Enum):
	"""2 Members, CB ... RDM"""
	CB = 0
	RDM = 1


# noinspection SpellCheckingInspection
class PrecoderGranularityAll(Enum):
	"""2 Members, ACRB ... REG"""
	ACRB = 0
	REG = 1


# noinspection SpellCheckingInspection
class PropagCond(Enum):
	"""15 Members, AWGN ... TDLC300D600"""
	AWGN = 0
	HST1NR350 = 1
	HST1NR500 = 2
	HST3NR350 = 3
	HST3NR500 = 4
	MPX = 5
	MPY = 6
	MPZ = 7
	TDLA30D10 = 8
	TDLA30D300 = 9
	TDLA30D75 = 10
	TDLB100D400 = 11
	TDLC300D100 = 12
	TDLC300D1200 = 13
	TDLC300D600 = 14


# noinspection SpellCheckingInspection
class PrsCombSize(Enum):
	"""4 Members, C12 ... C6"""
	C12 = 0
	C2 = 1
	C4 = 2
	C6 = 3


# noinspection SpellCheckingInspection
class PrsNumSymbols(Enum):
	"""4 Members, S12 ... S6"""
	S12 = 0
	S2 = 1
	S4 = 2
	S6 = 3


# noinspection SpellCheckingInspection
class PrsPeriodicity(Enum):
	"""16 Members, SL10 ... SL8"""
	SL10 = 0
	SL10240 = 1
	SL1280 = 2
	SL16 = 3
	SL160 = 4
	SL20 = 5
	SL2560 = 6
	SL32 = 7
	SL320 = 8
	SL4 = 9
	SL40 = 10
	SL5 = 11
	SL5120 = 12
	SL64 = 13
	SL640 = 14
	SL8 = 15


# noinspection SpellCheckingInspection
class PrsRepFactor(Enum):
	"""6 Members, REP1 ... REP8"""
	REP1 = 0
	REP16 = 1
	REP2 = 2
	REP32 = 3
	REP4 = 4
	REP8 = 5


# noinspection SpellCheckingInspection
class PrsTimeGap(Enum):
	"""6 Members, TG1 ... TG8"""
	TG1 = 0
	TG16 = 1
	TG2 = 2
	TG32 = 3
	TG4 = 4
	TG8 = 5


# noinspection SpellCheckingInspection
class PseudorangeMode(Enum):
	"""4 Members, CONStant ... PROFile"""
	CONStant = 0
	FILE = 1
	FSBas = 2
	PROFile = 3


# noinspection SpellCheckingInspection
class PtrsEpreRatio(Enum):
	"""2 Members, RAT0 ... RAT1"""
	RAT0 = 0
	RAT1 = 1


# noinspection SpellCheckingInspection
class PtrsFreqDensity(Enum):
	"""2 Members, FD2 ... FD4"""
	FD2 = 0
	FD4 = 1


# noinspection SpellCheckingInspection
class PtrsPower(Enum):
	"""2 Members, P00 ... P01"""
	P00 = 0
	P01 = 1


# noinspection SpellCheckingInspection
class PtrsReOffset(Enum):
	"""4 Members, RE00 ... RE11"""
	RE00 = 0
	RE01 = 1
	RE10 = 2
	RE11 = 3


# noinspection SpellCheckingInspection
class PtrsTmeDensity(Enum):
	"""3 Members, TD1 ... TD4"""
	TD1 = 0
	TD2 = 1
	TD4 = 2


# noinspection SpellCheckingInspection
class PtrsTpNumberOfPtrsGrpsAll(Enum):
	"""3 Members, G2 ... G8"""
	G2 = 0
	G4 = 1
	G8 = 2


# noinspection SpellCheckingInspection
class PtrsTpTimeDensityAll(Enum):
	"""2 Members, TD1 ... TD2"""
	TD1 = 0
	TD2 = 1


# noinspection SpellCheckingInspection
class PucchFmt2OccLength(Enum):
	"""3 Members, L1 ... L4"""
	L1 = 0
	L2 = 1
	L4 = 2


# noinspection SpellCheckingInspection
class PucchFmt4OccLength(Enum):
	"""2 Members, L2 ... L4"""
	L2 = 0
	L4 = 1


# noinspection SpellCheckingInspection
class PucchFormatAll(Enum):
	"""5 Members, F0 ... F4"""
	F0 = 0
	F1 = 1
	F2 = 2
	F3 = 3
	F4 = 4


# noinspection SpellCheckingInspection
class PucchGrpHoppingAll(Enum):
	"""3 Members, DIS ... N"""
	DIS = 0
	ENA = 1
	N = 2


# noinspection SpellCheckingInspection
class PucchNumAp(Enum):
	"""2 Members, AP1 ... AP2"""
	AP1 = 0
	AP2 = 1


# noinspection SpellCheckingInspection
class PulsMode(Enum):
	"""4 Members, DOUBle ... SINGle"""
	DOUBle = 0
	PHOPptrain = 1
	PTRain = 2
	SINGle = 3


# noinspection SpellCheckingInspection
class PulsTransType(Enum):
	"""2 Members, FAST ... SMOothed"""
	FAST = 0
	SMOothed = 1


# noinspection SpellCheckingInspection
class PulsTrigMode(Enum):
	"""4 Members, AUTO ... EXTernal"""
	AUTO = 0
	EGATe = 1
	ESINgle = 2
	EXTernal = 3


# noinspection SpellCheckingInspection
class PuschGrpSeqAll(Enum):
	"""3 Members, GRP ... SEQuence"""
	GRP = 0
	NEITher = 1
	SEQuence = 2


# noinspection SpellCheckingInspection
class PuschPrecScheme(Enum):
	"""2 Members, NONE ... SPM"""
	NONE = 0
	SPM = 1


# noinspection SpellCheckingInspection
class PuschTxMode(Enum):
	"""2 Members, M1 ... M2"""
	M1 = 0
	M2 = 1


# noinspection SpellCheckingInspection
class PuschUciAlphaAll(Enum):
	"""4 Members, A0_5 ... A1_0"""
	A0_5 = 0
	A0_65 = 1
	A0_8 = 2
	A1_0 = 3


# noinspection SpellCheckingInspection
class PuschUciModeAll(Enum):
	"""2 Members, UCIonly ... UCLSch"""
	UCIonly = 0
	UCLSch = 1


# noinspection SpellCheckingInspection
class PwrUpdMode(Enum):
	"""2 Members, CONTinuous ... MANual"""
	CONTinuous = 0
	MANual = 1


# noinspection SpellCheckingInspection
class QckSettingsModType(Enum):
	"""5 Members, BPSK2 ... QPSK"""
	BPSK2 = 0
	QAM16 = 1
	QAM256 = 2
	QAM64 = 3
	QPSK = 4


# noinspection SpellCheckingInspection
class QucjSettingsScsAll(Enum):
	"""12 Members, N120 ... SCS960"""
	N120 = 0
	N15 = 1
	N240 = 2
	N30 = 3
	N60 = 4
	SCS120 = 5
	SCS15 = 6
	SCS240 = 7
	SCS30 = 8
	SCS480 = 9
	SCS60 = 10
	SCS960 = 11


# noinspection SpellCheckingInspection
class QuickSetSlotLenAll(Enum):
	"""2 Members, S10 ... S5"""
	S10 = 0
	S5 = 1


# noinspection SpellCheckingInspection
class QuickSetStateAll(Enum):
	"""3 Members, DIS ... EN"""
	DIS = 0
	DRSK = 1
	EN = 2


# noinspection SpellCheckingInspection
class RampFunc(Enum):
	"""2 Members, COSine ... LINear"""
	COSine = 0
	LINear = 1


# noinspection SpellCheckingInspection
class RateMatchGrpIdAll(Enum):
	"""3 Members, G1 ... N"""
	G1 = 0
	G2 = 1
	N = 2


# noinspection SpellCheckingInspection
class RateMatchPeriodictyAll(Enum):
	"""8 Members, _1 ... _8"""
	_1 = 0
	_10 = 1
	_2 = 2
	_20 = 3
	_4 = 4
	_40 = 5
	_5 = 6
	_8 = 7


# noinspection SpellCheckingInspection
class ReadOutMode(Enum):
	"""3 Members, CYCLic ... RTRip"""
	CYCLic = 0
	OWAY = 1
	RTRip = 2


# noinspection SpellCheckingInspection
class RecScpiCmdMode(Enum):
	"""4 Members, AUTO ... OFF"""
	AUTO = 0
	DAUTo = 1
	MANual = 2
	OFF = 3


# noinspection SpellCheckingInspection
class RefFrame(Enum):
	"""2 Members, PZ90 ... WGS84"""
	PZ90 = 0
	WGS84 = 1


# noinspection SpellCheckingInspection
class ReflMaterial(Enum):
	"""6 Members, DRY ... WET"""
	DRY = 0
	MDRY = 1
	SEA = 2
	USER = 3
	WATER = 4
	WET = 5


# noinspection SpellCheckingInspection
class RefScale(Enum):
	"""2 Members, DISTance ... TIME"""
	DISTance = 0
	TIME = 1


# noinspection SpellCheckingInspection
class RefStream(Enum):
	"""4 Members, S1 ... S4"""
	S1 = 0
	S2 = 1
	S3 = 2
	S4 = 3


# noinspection SpellCheckingInspection
class RefVehicle(Enum):
	"""2 Members, V1 ... V2"""
	V1 = 0
	V2 = 1


# noinspection SpellCheckingInspection
class RegObj(Enum):
	"""13 Members, _1 ... ALL"""
	_1 = 0
	_10 = 1
	_11 = 2
	_12 = 3
	_2 = 4
	_3 = 5
	_4 = 6
	_5 = 7
	_6 = 8
	_7 = 9
	_8 = 10
	_9 = 11
	ALL = 12


# noinspection SpellCheckingInspection
class RegObjDir(Enum):
	"""2 Members, APPRoaching ... DEParting"""
	APPRoaching = 0
	DEParting = 1


# noinspection SpellCheckingInspection
class RegObjOne(Enum):
	"""12 Members, _1 ... _9"""
	_1 = 0
	_10 = 1
	_11 = 2
	_12 = 3
	_2 = 4
	_3 = 5
	_4 = 6
	_5 = 7
	_6 = 8
	_7 = 9
	_8 = 10
	_9 = 11


# noinspection SpellCheckingInspection
class RegObjPowDedicStartRang(Enum):
	"""3 Members, ALL ... STARt"""
	ALL = 0
	END = 1
	STARt = 2


# noinspection SpellCheckingInspection
class RegObjSimMode(Enum):
	"""3 Members, CYCLic ... ROUNdtrip"""
	CYCLic = 0
	ONEWay = 1
	ROUNdtrip = 2


# noinspection SpellCheckingInspection
class RegObjType(Enum):
	"""4 Members, MOVing ... STATic"""
	MOVing = 0
	OFF = 1
	SMOVing = 2
	STATic = 3


# noinspection SpellCheckingInspection
class RegPrevDiagrType(Enum):
	"""3 Members, POLar ... VELocity"""
	POLar = 0
	POWer = 1
	VELocity = 2


# noinspection SpellCheckingInspection
class RegRadarPowRefFswStatus(Enum):
	"""4 Members, INValid ... VALid"""
	INValid = 0
	NCONected = 1
	UPDated = 2
	VALid = 3


# noinspection SpellCheckingInspection
class RegRadarPowSett(Enum):
	"""2 Members, MANual ... REQuation"""
	MANual = 0
	REQuation = 1


# noinspection SpellCheckingInspection
class RegRadarTestSetup(Enum):
	"""2 Members, CONDucted ... OTA"""
	CONDucted = 0
	OTA = 1


# noinspection SpellCheckingInspection
class RegRcsModel(Enum):
	"""5 Members, SWE0 ... SWE4"""
	SWE0 = 0
	SWE1 = 1
	SWE2 = 2
	SWE3 = 3
	SWE4 = 4


# noinspection SpellCheckingInspection
class RegSimCalibrationMode(Enum):
	"""2 Members, AUTomatic ... MANual"""
	AUTomatic = 0
	MANual = 1


# noinspection SpellCheckingInspection
class RegSimCalibrationState(Enum):
	"""2 Members, FAILed ... SUCCess"""
	FAILed = 0
	SUCCess = 1


# noinspection SpellCheckingInspection
class RegSimFreqRefFswState(Enum):
	"""2 Members, UPDated ... VALid"""
	UPDated = 0
	VALid = 1


# noinspection SpellCheckingInspection
class RegSimRange(Enum):
	"""1 Members, L74K ... L74K"""
	L74K = 0


# noinspection SpellCheckingInspection
class RegTrigMode(Enum):
	"""2 Members, AAUTo ... AUTO"""
	AAUTo = 0
	AUTO = 1


# noinspection SpellCheckingInspection
class Release(Enum):
	"""2 Members, REL15 ... REL16"""
	REL15 = 0
	REL16 = 1


# noinspection SpellCheckingInspection
class ReleaseNbiotDl(Enum):
	"""3 Members, EMTC ... R89"""
	EMTC = 0
	NIOT = 1
	R89 = 2


# noinspection SpellCheckingInspection
class RepAggrFactor(Enum):
	"""3 Members, F2 ... F8"""
	F2 = 0
	F4 = 1
	F8 = 2


# noinspection SpellCheckingInspection
class RepTypeAll(Enum):
	"""6 Members, CUSTom ... TA"""
	CUSTom = 0
	FRAMe = 1
	OFF = 2
	SLOT = 3
	SUBFrame = 4
	TA = 5


# noinspection SpellCheckingInspection
class RequestAll(Enum):
	"""3 Members, R1 ... RNON"""
	R1 = 0
	R2 = 1
	RNON = 2


# noinspection SpellCheckingInspection
class ResMcsTableAll(Enum):
	"""5 Members, T1 ... TTP2"""
	T1 = 0
	T2 = 1
	T3 = 2
	TTP1 = 3
	TTP2 = 4


# noinspection SpellCheckingInspection
class ResourceAllocAll(Enum):
	"""3 Members, DS ... T1"""
	DS = 0
	T0 = 1
	T1 = 2


# noinspection SpellCheckingInspection
class ResPoolScSizeAll(Enum):
	"""7 Members, R10 ... R75"""
	R10 = 0
	R12 = 1
	R15 = 2
	R20 = 3
	R25 = 4
	R50 = 5
	R75 = 6


# noinspection SpellCheckingInspection
class RestartDataAll(Enum):
	"""3 Members, COAL ... OFF"""
	COAL = 0
	FRAMe = 1
	OFF = 2


# noinspection SpellCheckingInspection
class RestrictedSet(Enum):
	"""2 Members, ARES ... BRES"""
	ARES = 0
	BRES = 1


# noinspection SpellCheckingInspection
class RfBand(Enum):
	"""3 Members, L1 ... L5"""
	L1 = 0
	L2 = 1
	L5 = 2


# noinspection SpellCheckingInspection
class RmcIdAll(Enum):
	"""51 Members, F215 ... TS38176_FR2A353"""
	F215 = 0
	F230 = 1
	F260 = 2
	F615 = 3
	F630 = 4
	F660 = 5
	FQ15 = 6
	FQ30 = 7
	FQ60 = 8
	FR2T2120 = 9
	FR2T260 = 10
	FR2T6120 = 11
	FR2T660 = 12
	FR2TQ120 = 13
	FR2TQ60 = 14
	T215 = 15
	T230 = 16
	T260 = 17
	T615 = 18
	T630 = 19
	T660 = 20
	TQ15 = 21
	TQ30 = 22
	TQ60 = 23
	TS38176_FR1A311 = 24
	TS38176_FR1A312 = 25
	TS38176_FR1A313 = 26
	TS38176_FR1A314 = 27
	TS38176_FR1A315 = 28
	TS38176_FR1A321 = 29
	TS38176_FR1A331 = 30
	TS38176_FR1A341 = 31
	TS38176_FR1A342 = 32
	TS38176_FR1A343 = 33
	TS38176_FR1A351 = 34
	TS38176_FR1A352 = 35
	TS38176_FR1A353 = 36
	TS38176_FR1A354 = 37
	TS38176_FR1A355 = 38
	TS38176_FR1A356 = 39
	TS38176_FR2A311 = 40
	TS38176_FR2A312 = 41
	TS38176_FR2A313 = 42
	TS38176_FR2A321 = 43
	TS38176_FR2A322 = 44
	TS38176_FR2A341 = 45
	TS38176_FR2A342 = 46
	TS38176_FR2A343 = 47
	TS38176_FR2A351 = 48
	TS38176_FR2A352 = 49
	TS38176_FR2A353 = 50


# noinspection SpellCheckingInspection
class Rosc1GoUtpFreqMode(Enum):
	"""3 Members, DER1G ... OFF"""
	DER1G = 0
	LOOPthrough = 1
	OFF = 2


# noinspection SpellCheckingInspection
class RoscFreqExt(Enum):
	"""6 Members, _100MHZ ... VARiable"""
	_100MHZ = 0
	_10MHZ = 1
	_13MHZ = 2
	_1GHZ = 3
	_5MHZ = 4
	VARiable = 5


# noinspection SpellCheckingInspection
class RoscOutpFreqMode(Enum):
	"""5 Members, DER100M ... SAME"""
	DER100M = 0
	DER10M = 1
	LOOPthrough = 2
	OFF = 3
	SAME = 4


# noinspection SpellCheckingInspection
class RoscSourSetup(Enum):
	"""3 Members, ELOop ... INTernal"""
	ELOop = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class Rs232BdRate(Enum):
	"""7 Members, _115200 ... _9600"""
	_115200 = 0
	_19200 = 1
	_2400 = 2
	_38400 = 3
	_4800 = 4
	_57600 = 5
	_9600 = 6


# noinspection SpellCheckingInspection
class RsrcBlockSize(Enum):
	"""2 Members, C1 ... C2"""
	C1 = 0
	C2 = 1


# noinspection SpellCheckingInspection
class RxaNt(Enum):
	"""4 Members, ANT1 ... ANT8"""
	ANT1 = 0
	ANT2 = 1
	ANT4 = 2
	ANT8 = 3


# noinspection SpellCheckingInspection
class SamplesPerPtrsGrpAll(Enum):
	"""2 Members, S2 ... S4"""
	S2 = 0
	S4 = 1


# noinspection SpellCheckingInspection
class SampRateFifoStatus(Enum):
	"""3 Members, OFLow ... URUN"""
	OFLow = 0
	OK = 1
	URUN = 2


# noinspection SpellCheckingInspection
class SampRateModeRange(Enum):
	"""2 Members, FFT ... MIN"""
	FFT = 0
	MIN = 1


# noinspection SpellCheckingInspection
class SarMode(Enum):
	"""3 Members, LRLM ... SRLM"""
	LRLM = 0
	SPARe = 1
	SRLM = 2


# noinspection SpellCheckingInspection
class SatNavClockMode(Enum):
	"""2 Members, MSYMbol ... SYMBol"""
	MSYMbol = 0
	SYMBol = 1


# noinspection SpellCheckingInspection
class SbasCorrMode(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	SYNC = 1
	USER = 2


# noinspection SpellCheckingInspection
class SbasSystem(Enum):
	"""5 Members, EGNOS ... WAAS"""
	EGNOS = 0
	GAGAN = 1
	MSAS = 2
	NONE = 3
	WAAS = 4


# noinspection SpellCheckingInspection
class ScalingAll(Enum):
	"""4 Members, F1 ... FP8"""
	F1 = 0
	FP5 = 1
	FP65 = 2
	FP8 = 3


# noinspection SpellCheckingInspection
class ScheduleMode(Enum):
	"""1 Members, AUTO ... AUTO"""
	AUTO = 0


# noinspection SpellCheckingInspection
class ScrCodeMode(Enum):
	"""3 Members, LONG ... SHORt"""
	LONG = 0
	OFF = 1
	SHORt = 2


# noinspection SpellCheckingInspection
class ScscOmmon(Enum):
	"""2 Members, N15_60 ... N30_120"""
	N15_60 = 0
	N30_120 = 1


# noinspection SpellCheckingInspection
class SelCriteria(Enum):
	"""3 Members, ELEVation ... VISibility"""
	ELEVation = 0
	MANual = 1
	VISibility = 2


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
class SeqGrpHoppingAll(Enum):
	"""3 Members, GRP ... SEQ"""
	GRP = 0
	N = 1
	SEQ = 2


# noinspection SpellCheckingInspection
class SigmaGuiDeviceAccessibility(Enum):
	"""3 Members, BUSY ... ONL"""
	BUSY = 0
	OFFL = 1
	ONL = 2


# noinspection SpellCheckingInspection
class SignalOutputs(Enum):
	"""2 Members, ALL ... HSAL"""
	ALL = 0
	HSAL = 1


# noinspection SpellCheckingInspection
class SimAnt(Enum):
	"""4 Members, ANT1 ... ANT4"""
	ANT1 = 0
	ANT2 = 1
	ANT3 = 2
	ANT4 = 3


# noinspection SpellCheckingInspection
class SimMode2(Enum):
	"""2 Members, NAVigation ... TRACking"""
	NAVigation = 0
	TRACking = 1


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
class SiriusLayer(Enum):
	"""2 Members, LEGacy ... OVERlay"""
	LEGacy = 0
	OVERlay = 1


# noinspection SpellCheckingInspection
class SiriusPhysLayer(Enum):
	"""3 Members, SAT1 ... TERR"""
	SAT1 = 0
	SAT2 = 1
	TERR = 2


# noinspection SpellCheckingInspection
class SiriusSatMarkMode(Enum):
	"""6 Members, FRAMe ... USER"""
	FRAMe = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	TRIGger = 4
	USER = 5


# noinspection SpellCheckingInspection
class SiriusSatMod(Enum):
	"""3 Members, P8INV ... QPSK"""
	P8INV = 0
	PSK8 = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class SiriusTerrMarkMode(Enum):
	"""6 Members, FRAMe ... USER"""
	FRAMe = 0
	RATio = 1
	SFRame = 2
	SYMBol = 3
	TRIGger = 4
	USER = 5


# noinspection SpellCheckingInspection
class SiriusTerrMod(Enum):
	"""1 Members, COFDM ... COFDM"""
	COFDM = 0


# noinspection SpellCheckingInspection
class SlopeRiseFall(Enum):
	"""2 Members, FALLing ... RISing"""
	FALLing = 0
	RISing = 1


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
class SpsInt(Enum):
	"""10 Members, S10 ... S80"""
	S10 = 0
	S128 = 1
	S160 = 2
	S20 = 3
	S32 = 4
	S320 = 5
	S40 = 6
	S64 = 7
	S640 = 8
	S80 = 9


# noinspection SpellCheckingInspection
class SrsConfig(Enum):
	"""2 Members, IE ... IER16"""
	IE = 0
	IER16 = 1


# noinspection SpellCheckingInspection
class SrsPtrsPortIdx(Enum):
	"""2 Members, P0 ... P1"""
	P0 = 0
	P1 = 1


# noinspection SpellCheckingInspection
class SrsRsNumSymbolsAll(Enum):
	"""5 Members, SYM1 ... SYM8"""
	SYM1 = 0
	SYM12 = 1
	SYM2 = 2
	SYM4 = 3
	SYM8 = 4


# noinspection SpellCheckingInspection
class SrsRsPeriodicityAll(Enum):
	"""21 Members, SL1 ... SL81920"""
	SL1 = 0
	SL10 = 1
	SL10240 = 2
	SL1280 = 3
	SL16 = 4
	SL160 = 5
	SL2 = 6
	SL20 = 7
	SL2560 = 8
	SL32 = 9
	SL320 = 10
	SL4 = 11
	SL40 = 12
	SL40960 = 13
	SL5 = 14
	SL5120 = 15
	SL64 = 16
	SL640 = 17
	SL8 = 18
	SL80 = 19
	SL81920 = 20


# noinspection SpellCheckingInspection
class SrsRsRepFactorAll(Enum):
	"""3 Members, REP1 ... REP4"""
	REP1 = 0
	REP2 = 1
	REP4 = 2


# noinspection SpellCheckingInspection
class SrsRsSetRsTypeAll(Enum):
	"""3 Members, APER ... SP"""
	APER = 0
	PER = 1
	SP = 2


# noinspection SpellCheckingInspection
class SrsRsSetUsageAll(Enum):
	"""4 Members, ASW ... NCB"""
	ASW = 0
	BM = 1
	CB = 2
	NCB = 3


# noinspection SpellCheckingInspection
class SrsRsTransComboAll(Enum):
	"""3 Members, TC2 ... TC8"""
	TC2 = 0
	TC4 = 1
	TC8 = 2


# noinspection SpellCheckingInspection
class SspBchBitLengthAll(Enum):
	"""5 Members, L10 ... L8"""
	L10 = 0
	L20 = 1
	L4 = 2
	L64 = 3
	L8 = 4


# noinspection SpellCheckingInspection
class SsSpsbchBlocksAll(Enum):
	"""7 Members, B1 ... B8"""
	B1 = 0
	B16 = 1
	B2 = 2
	B32 = 3
	B4 = 4
	B64 = 5
	B8 = 6


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
class SubType(Enum):
	"""2 Members, S1 ... S2"""
	S1 = 0
	S2 = 1


# noinspection SpellCheckingInspection
class Svid(Enum):
	"""201 Members, _1 ... ALL"""
	_1 = 0
	_10 = 1
	_100 = 2
	_101 = 3
	_102 = 4
	_103 = 5
	_104 = 6
	_105 = 7
	_106 = 8
	_107 = 9
	_108 = 10
	_109 = 11
	_11 = 12
	_110 = 13
	_111 = 14
	_112 = 15
	_113 = 16
	_114 = 17
	_115 = 18
	_116 = 19
	_117 = 20
	_118 = 21
	_119 = 22
	_12 = 23
	_120 = 24
	_121 = 25
	_122 = 26
	_123 = 27
	_124 = 28
	_125 = 29
	_126 = 30
	_127 = 31
	_128 = 32
	_129 = 33
	_13 = 34
	_130 = 35
	_131 = 36
	_132 = 37
	_133 = 38
	_134 = 39
	_135 = 40
	_136 = 41
	_137 = 42
	_138 = 43
	_139 = 44
	_14 = 45
	_140 = 46
	_141 = 47
	_142 = 48
	_143 = 49
	_144 = 50
	_145 = 51
	_146 = 52
	_147 = 53
	_148 = 54
	_149 = 55
	_15 = 56
	_150 = 57
	_151 = 58
	_152 = 59
	_153 = 60
	_154 = 61
	_155 = 62
	_156 = 63
	_157 = 64
	_158 = 65
	_159 = 66
	_16 = 67
	_160 = 68
	_161 = 69
	_162 = 70
	_163 = 71
	_164 = 72
	_165 = 73
	_166 = 74
	_167 = 75
	_168 = 76
	_169 = 77
	_17 = 78
	_170 = 79
	_171 = 80
	_172 = 81
	_173 = 82
	_174 = 83
	_175 = 84
	_176 = 85
	_177 = 86
	_178 = 87
	_179 = 88
	_18 = 89
	_180 = 90
	_181 = 91
	_182 = 92
	_183 = 93
	_184 = 94
	_185 = 95
	_186 = 96
	_187 = 97
	_188 = 98
	_189 = 99
	_19 = 100
	_190 = 101
	_191 = 102
	_192 = 103
	_193 = 104
	_194 = 105
	_195 = 106
	_196 = 107
	_197 = 108
	_198 = 109
	_199 = 110
	_2 = 111
	_20 = 112
	_200 = 113
	_21 = 114
	_22 = 115
	_23 = 116
	_24 = 117
	_25 = 118
	_26 = 119
	_27 = 120
	_28 = 121
	_29 = 122
	_3 = 123
	_30 = 124
	_31 = 125
	_32 = 126
	_33 = 127
	_34 = 128
	_35 = 129
	_36 = 130
	_37 = 131
	_38 = 132
	_39 = 133
	_4 = 134
	_40 = 135
	_41 = 136
	_42 = 137
	_43 = 138
	_44 = 139
	_45 = 140
	_46 = 141
	_47 = 142
	_48 = 143
	_49 = 144
	_5 = 145
	_50 = 146
	_51 = 147
	_52 = 148
	_53 = 149
	_54 = 150
	_55 = 151
	_56 = 152
	_57 = 153
	_58 = 154
	_59 = 155
	_6 = 156
	_60 = 157
	_61 = 158
	_62 = 159
	_63 = 160
	_64 = 161
	_65 = 162
	_66 = 163
	_67 = 164
	_68 = 165
	_69 = 166
	_7 = 167
	_70 = 168
	_71 = 169
	_72 = 170
	_73 = 171
	_74 = 172
	_75 = 173
	_76 = 174
	_77 = 175
	_78 = 176
	_79 = 177
	_8 = 178
	_80 = 179
	_81 = 180
	_82 = 181
	_83 = 182
	_84 = 183
	_85 = 184
	_86 = 185
	_87 = 186
	_88 = 187
	_89 = 188
	_9 = 189
	_90 = 190
	_91 = 191
	_92 = 192
	_93 = 193
	_94 = 194
	_95 = 195
	_96 = 196
	_97 = 197
	_98 = 198
	_99 = 199
	ALL = 200


# noinspection SpellCheckingInspection
class SweCyclMode(Enum):
	"""2 Members, SAWTooth ... TRIangle"""
	SAWTooth = 0
	TRIangle = 1


# noinspection SpellCheckingInspection
class SymbRate(Enum):
	"""15 Members, D120k ... D960k"""
	D120k = 0
	D15K = 1
	D1920k = 2
	D240k = 3
	D2880k = 4
	D2X1920K = 5
	D2X960K2X1920K = 6
	D30K = 7
	D3840k = 8
	D4800k = 9
	D480k = 10
	D5760k = 11
	D60K = 12
	D7K5 = 13
	D960k = 14


# noinspection SpellCheckingInspection
class SyncModulationScheme(Enum):
	"""2 Members, IQFile ... QPSK"""
	IQFile = 0
	QPSK = 1


# noinspection SpellCheckingInspection
class SystConfBbBandwidth(Enum):
	"""14 Members, BB040 ... BBOUTDEF"""
	BB040 = 0
	BB050 = 1
	BB080 = 2
	BB100 = 3
	BB120 = 4
	BB160 = 5
	BB1G = 6
	BB200 = 7
	BB240 = 8
	BB2G = 9
	BB400 = 10
	BB500 = 11
	BB800 = 12
	BBOUTDEF = 13


# noinspection SpellCheckingInspection
class SystConfBbConf(Enum):
	"""3 Members, COUPled ... SEParate"""
	COUPled = 0
	CPENtity = 1
	SEParate = 2


# noinspection SpellCheckingInspection
class SystConfFadConf(Enum):
	"""58 Members, FAABFBAB ... SISO8X1X1"""
	FAABFBAB = 0
	FAABFBN = 1
	FAAFBA = 2
	FAAFBB = 3
	FAAFBNone = 4
	FABFBB = 5
	FANFBAB = 6
	FANFBB = 7
	MIMO1X2 = 8
	MIMO1X3 = 9
	MIMO1X4 = 10
	MIMO1X8 = 11
	MIMO2X1 = 12
	MIMO2X1X2 = 13
	MIMO2X1X3 = 14
	MIMO2X1X4 = 15
	MIMO2X2 = 16
	MIMO2X2X1 = 17
	MIMO2X2X2 = 18
	MIMO2X2X3 = 19
	MIMO2X2X4 = 20
	MIMO2X3 = 21
	MIMO2X3X1 = 22
	MIMO2X3X2 = 23
	MIMO2X3X3 = 24
	MIMO2X3X4 = 25
	MIMO2X4 = 26
	MIMO2X4X1 = 27
	MIMO2X4X2 = 28
	MIMO2X4X3 = 29
	MIMO2X4X4 = 30
	MIMO2X8 = 31
	MIMO3X1 = 32
	MIMO3X1X2 = 33
	MIMO3X2 = 34
	MIMO3X2X1 = 35
	MIMO3X2X2 = 36
	MIMO3X3 = 37
	MIMO3X4 = 38
	MIMO4X1 = 39
	MIMO4X1X2 = 40
	MIMO4X2 = 41
	MIMO4X2X1 = 42
	MIMO4X2X2 = 43
	MIMO4X3 = 44
	MIMO4X4 = 45
	MIMO4X8 = 46
	MIMO8X1 = 47
	MIMO8X2 = 48
	MIMO8X4 = 49
	MIMO8X8 = 50
	SISO2X1X1 = 51
	SISO3X1X1 = 52
	SISO4X1X1 = 53
	SISO5X1X1 = 54
	SISO6X1X1 = 55
	SISO7X1X1 = 56
	SISO8X1X1 = 57


# noinspection SpellCheckingInspection
class SystConfFadEntOutp(Enum):
	"""5 Members, R01 ... R08"""
	R01 = 0
	R02 = 1
	R03 = 2
	R04 = 3
	R08 = 4


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
class SystConfMode(Enum):
	"""7 Members, ADVanced ... STANdard"""
	ADVanced = 0
	BWEXtension = 1
	EFADing = 2
	ESEQuencer = 3
	GNSS = 4
	REGenerator = 5
	STANdard = 6


# noinspection SpellCheckingInspection
class SystConfOutpMapMatMode(Enum):
	"""3 Members, ADD ... SINGle"""
	ADD = 0
	MULTiplex = 1
	SINGle = 2


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
class TbAlign(Enum):
	"""2 Members, EVEN ... ODD"""
	EVEN = 0
	ODD = 1


# noinspection SpellCheckingInspection
class TbScalingAll(Enum):
	"""3 Members, S1 ... S5"""
	S1 = 0
	S25 = 1
	S5 = 2


# noinspection SpellCheckingInspection
class TchCrc(Enum):
	"""5 Members, _12 ... NONE"""
	_12 = 0
	_16 = 1
	_24 = 2
	_8 = 3
	NONE = 4


# noinspection SpellCheckingInspection
class TchTranTimInt(Enum):
	"""4 Members, _10MS ... _80MS"""
	_10MS = 0
	_20MS = 1
	_40MS = 2
	_80MS = 3


# noinspection SpellCheckingInspection
class TcwDip(Enum):
	"""2 Members, SET1 ... SET2"""
	SET1 = 0
	SET2 = 1


# noinspection SpellCheckingInspection
class TcwfEedbackMode(Enum):
	"""2 Members, S3X8 ... SERial"""
	S3X8 = 0
	SERial = 1


# noinspection SpellCheckingInspection
class TcwpRachFormat(Enum):
	"""7 Members, F0 ... FC2"""
	F0 = 0
	FA1 = 1
	FA2 = 2
	FA3 = 3
	FB4 = 4
	FC0 = 5
	FC2 = 6


# noinspection SpellCheckingInspection
class TcwpRachNum(Enum):
	"""5 Members, N1_25 ... N60"""
	N1_25 = 0
	N120 = 1
	N15 = 2
	N30 = 3
	N60 = 4


# noinspection SpellCheckingInspection
class TdscdmaChanType(Enum):
	"""23 Members, DPCH_8PSQ ... UP_DPCH_QPSK"""
	DPCH_8PSQ = 0
	DPCH_QPSQ = 1
	E_PUCH_16QAM = 2
	E_PUCH_QPSK = 3
	E_RUCCH = 4
	EAGCH = 5
	EHICH = 6
	FPACH = 7
	HS_PDS_16QAM = 8
	HS_PDS_64QAM = 9
	HS_PDS_QPSK = 10
	HS_SCCH1 = 11
	HS_SCCH2 = 12
	HS_SICH = 13
	P_CCPCH1 = 14
	P_CCPCH2 = 15
	PDSCH = 16
	PLCCH = 17
	PUSCH = 18
	S_CCPCH1 = 19
	S_CCPCH2 = 20
	UP_DPCH_8PSK = 21
	UP_DPCH_QPSK = 22


# noinspection SpellCheckingInspection
class TdscdmaChipRate(Enum):
	"""1 Members, R1M28 ... R1M28"""
	R1M28 = 0


# noinspection SpellCheckingInspection
class TdscdmaDchCoding(Enum):
	"""16 Members, HRMC526K ... USER"""
	HRMC526K = 0
	HRMC730K = 1
	HS_SICH = 2
	HSDPA = 3
	HSUPA = 4
	PLCCH = 5
	RMC12K2 = 6
	RMC144K = 7
	RMC2048K = 8
	RMC384K = 9
	RMC64K = 10
	UP_RMC12K2 = 11
	UP_RMC144K = 12
	UP_RMC384K = 13
	UP_RMC64K = 14
	USER = 15


# noinspection SpellCheckingInspection
class TdscdmaEnhHsFrcMode(Enum):
	"""5 Members, _1 ... USER"""
	_1 = 0
	_2 = 1
	_3 = 2
	_4 = 3
	USER = 4


# noinspection SpellCheckingInspection
class TdscdmaEnhHsRmcMode(Enum):
	"""13 Members, HRMC_0M5_QPSK ... USER"""
	HRMC_0M5_QPSK = 0
	HRMC_1M1_16QAM = 1
	HRMC_1M1_QPSK = 2
	HRMC_1M6_16QAM = 3
	HRMC_1M6_QPSK = 4
	HRMC_2M2_16QAM = 5
	HRMC_2M2_QPSK = 6
	HRMC_2M8_16QAM = 7
	HRMC_2M8_QPSK = 8
	HRMC_64QAM_16UE = 9
	HRMC_64QAM_19UE = 10
	HRMC_64QAM_22UE = 11
	USER = 12


# noinspection SpellCheckingInspection
class TdscdmaEnhHsTbsTableDn(Enum):
	"""8 Members, C10TO12 ... C7TO9"""
	C10TO12 = 0
	C13TO15 = 1
	C16TO18 = 2
	C19TO21 = 3
	C1TO3 = 4
	C22TO24 = 5
	C4TO6 = 6
	C7TO9 = 7


# noinspection SpellCheckingInspection
class TdscdmaEnhHsTbsTableUp(Enum):
	"""2 Members, C1TO2 ... C3TO6"""
	C1TO2 = 0
	C3TO6 = 1


# noinspection SpellCheckingInspection
class TdscdmaEnhTchTti(Enum):
	"""5 Members, _10MS ... _80MS"""
	_10MS = 0
	_20MS = 1
	_40MS = 2
	_5MS = 3
	_80MS = 4


# noinspection SpellCheckingInspection
class TdscdmaMarkMode(Enum):
	"""7 Members, CSPeriod ... USER"""
	CSPeriod = 0
	FACTive = 1
	RATio = 2
	RFRame = 3
	SFNR = 4
	TRIGger = 5
	USER = 6


# noinspection SpellCheckingInspection
class TdscdmaPhasRot(Enum):
	"""3 Members, AUTO ... S2"""
	AUTO = 0
	S1 = 1
	S2 = 2


# noinspection SpellCheckingInspection
class TdscdmaSlotModeUp(Enum):
	"""2 Members, DEDicated ... PRACh"""
	DEDicated = 0
	PRACh = 1


# noinspection SpellCheckingInspection
class TdscdmaSpreadFactor(Enum):
	"""5 Members, _1 ... _8"""
	_1 = 0
	_16 = 1
	_2 = 2
	_4 = 3
	_8 = 4


# noinspection SpellCheckingInspection
class TdscdmaSyncShiftLen(Enum):
	"""8 Members, _0 ... _8"""
	_0 = 0
	_16 = 1
	_2 = 2
	_3 = 3
	_32 = 4
	_4 = 5
	_48 = 6
	_8 = 7


# noinspection SpellCheckingInspection
class TdscdmaTfciLen(Enum):
	"""9 Members, _0 ... _8"""
	_0 = 0
	_12 = 1
	_16 = 2
	_24 = 3
	_32 = 4
	_4 = 5
	_48 = 6
	_6 = 7
	_8 = 8


# noinspection SpellCheckingInspection
class TdscdmaTotalUsers(Enum):
	"""8 Members, _10 ... _8"""
	_10 = 0
	_12 = 1
	_14 = 2
	_16 = 3
	_2 = 4
	_4 = 5
	_6 = 6
	_8 = 7


# noinspection SpellCheckingInspection
class Test(Enum):
	"""4 Members, _0 ... STOPped"""
	_0 = 0
	_1 = 1
	RUNning = 2
	STOPped = 3


# noinspection SpellCheckingInspection
class TestBbBncConn(Enum):
	"""27 Members, AUTO ... USER6"""
	AUTO = 0
	C1TM2 = 1
	C1TM3 = 2
	C1TMC1 = 3
	C2TM5 = 4
	C2TM6 = 5
	C2TMC4 = 6
	F1TM2 = 7
	F1TM3 = 8
	F1TMC1 = 9
	F2TM5 = 10
	F2TM6 = 11
	F2TMC4 = 12
	F3TM2 = 13
	F3TM3 = 14
	F3TMC1 = 15
	F4TM5 = 16
	F4TM6 = 17
	F4TMC4 = 18
	TRGA = 19
	TRGB = 20
	USER1 = 21
	USER2 = 22
	USER3 = 23
	USER4 = 24
	USER5 = 25
	USER6 = 26


# noinspection SpellCheckingInspection
class TestBbGenIqSour(Enum):
	"""4 Members, ARB ... TTONe"""
	ARB = 0
	CONStant = 1
	SINE = 2
	TTONe = 3


# noinspection SpellCheckingInspection
class TestCase(Enum):
	"""71 Members, TS381411_TC67 ... TS381412_TC841"""
	TS381411_TC67 = 0
	TS381411_TC72 = 1
	TS381411_TC73 = 2
	TS381411_TC741 = 3
	TS381411_TC742A = 4
	TS381411_TC742B = 5
	TS381411_TC75 = 6
	TS381411_TC77 = 7
	TS381411_TC78 = 8
	TS381411_TC821 = 9
	TS381411_TC8210 = 10
	TS381411_TC8211 = 11
	TS381411_TC822 = 12
	TS381411_TC823 = 13
	TS381411_TC824 = 14
	TS381411_TC825 = 15
	TS381411_TC826 = 16
	TS381411_TC827 = 17
	TS381411_TC828 = 18
	TS381411_TC829 = 19
	TS381411_TC831 = 20
	TS381411_TC8310 = 21
	TS381411_TC8321 = 22
	TS381411_TC8322 = 23
	TS381411_TC8331 = 24
	TS381411_TC8332 = 25
	TS381411_TC834 = 26
	TS381411_TC835 = 27
	TS381411_TC8361A = 28
	TS381411_TC8361B = 29
	TS381411_TC837 = 30
	TS381411_TC8381 = 31
	TS381411_TC8382 = 32
	TS381411_TC839 = 33
	TS381411_TC841 = 34
	TS381412_TC68 = 35
	TS381412_TC72 = 36
	TS381412_TC73 = 37
	TS381412_TC74 = 38
	TS381412_TC751 = 39
	TS381412_TC752A = 40
	TS381412_TC752B = 41
	TS381412_TC76 = 42
	TS381412_TC78 = 43
	TS381412_TC79 = 44
	TS381412_TC821 = 45
	TS381412_TC8210 = 46
	TS381412_TC8211 = 47
	TS381412_TC822 = 48
	TS381412_TC823 = 49
	TS381412_TC824 = 50
	TS381412_TC825 = 51
	TS381412_TC826 = 52
	TS381412_TC827 = 53
	TS381412_TC828 = 54
	TS381412_TC829 = 55
	TS381412_TC831 = 56
	TS381412_TC8310 = 57
	TS381412_TC8321 = 58
	TS381412_TC8322 = 59
	TS381412_TC8331 = 60
	TS381412_TC8332 = 61
	TS381412_TC834 = 62
	TS381412_TC835 = 63
	TS381412_TC8361A = 64
	TS381412_TC8361B = 65
	TS381412_TC837 = 66
	TS381412_TC8381 = 67
	TS381412_TC8382 = 68
	TS381412_TC839 = 69
	TS381412_TC841 = 70


# noinspection SpellCheckingInspection
class TestGenIqSour(Enum):
	"""3 Members, ARB ... SINE"""
	ARB = 0
	CIQ = 1
	SINE = 2


# noinspection SpellCheckingInspection
class TestModel(Enum):
	"""1 Members, TM1_1 ... TM1_1"""
	TM1_1 = 0


# noinspection SpellCheckingInspection
class TestModelType(Enum):
	"""2 Members, NR ... ORAN"""
	NR = 0
	ORAN = 1


# noinspection SpellCheckingInspection
class TestRequire(Enum):
	"""2 Members, BLPE ... COBS"""
	BLPE = 0
	COBS = 1


# noinspection SpellCheckingInspection
class TestRequirment(Enum):
	"""2 Members, HST ... NORM"""
	HST = 0
	NORM = 1


# noinspection SpellCheckingInspection
class TestSetup(Enum):
	"""2 Members, TS_1 ... TS_2"""
	TS_1 = 0
	TS_2 = 1


# noinspection SpellCheckingInspection
class TestSpec(Enum):
	"""2 Members, TS38141_1 ... TS38141_2"""
	TS38141_1 = 0
	TS38141_2 = 1


# noinspection SpellCheckingInspection
class TetraAachqMode(Enum):
	"""2 Members, AAPDu ... RELement"""
	AAPDu = 0
	RELement = 1


# noinspection SpellCheckingInspection
class TetraAcssParm(Enum):
	"""16 Members, AP23 ... AP53"""
	AP23 = 0
	AP25 = 1
	AP27 = 2
	AP29 = 3
	AP31 = 4
	AP33 = 5
	AP35 = 6
	AP37 = 7
	AP39 = 8
	AP41 = 9
	AP43 = 10
	AP45 = 11
	AP47 = 12
	AP49 = 13
	AP51 = 14
	AP53 = 15


# noinspection SpellCheckingInspection
class TetraBurstType(Enum):
	"""29 Members, BSHD ... TSCU"""
	BSHD = 0
	RSBurst = 1
	RSSBurst = 2
	RSV1 = 3
	RSV2 = 4
	RSV3 = 5
	SFD = 6
	SFU = 7
	SPF = 8
	SPHD = 9
	SPHU = 10
	SQD = 11
	SQHU = 12
	SQRA = 13
	SQU = 14
	SSCH = 15
	SSTCh = 16
	T108 = 17
	T24D = 18
	T24U = 19
	T48D = 20
	T48U = 21
	T72F = 22
	T72S = 23
	T72U = 24
	TPTD = 25
	TPTU = 26
	TSCD = 27
	TSCU = 28


# noinspection SpellCheckingInspection
class TetraCelSvLevel(Enum):
	"""4 Members, CLUNknown ... MCLoad"""
	CLUNknown = 0
	HCLoad = 1
	LCLoad = 2
	MCLoad = 3


# noinspection SpellCheckingInspection
class TetraChnnlType(Enum):
	"""17 Members, CH0 ... CH9"""
	CH0 = 0
	CH1 = 1
	CH10 = 2
	CH11 = 3
	CH2 = 4
	CH21 = 5
	CH22 = 6
	CH23 = 7
	CH24 = 8
	CH25 = 9
	CH26 = 10
	CH27 = 11
	CH3 = 12
	CH4 = 13
	CH7 = 14
	CH8 = 15
	CH9 = 16


# noinspection SpellCheckingInspection
class TetraCrrBndwdth(Enum):
	"""4 Members, C100 ... C50"""
	C100 = 0
	C150 = 1
	C25 = 2
	C50 = 3


# noinspection SpellCheckingInspection
class TetraDplxSpcing(Enum):
	"""8 Members, DS0 ... DS7"""
	DS0 = 0
	DS1 = 1
	DS2 = 2
	DS3 = 3
	DS4 = 4
	DS5 = 5
	DS6 = 6
	DS7 = 7


# noinspection SpellCheckingInspection
class TetraDwnBrstType(Enum):
	"""2 Members, CONTinuous ... DCONtinuous"""
	CONTinuous = 0
	DCONtinuous = 1


# noinspection SpellCheckingInspection
class TetraFreqBand(Enum):
	"""9 Members, F100 ... F900"""
	F100 = 0
	F200 = 1
	F300 = 2
	F400 = 3
	F500 = 4
	F600 = 5
	F700 = 6
	F800 = 7
	F900 = 8


# noinspection SpellCheckingInspection
class TetraLgChType(Enum):
	"""46 Members, B16H ... U64U"""
	B16H = 0
	B16U = 1
	B4H = 2
	B64H = 3
	B64M = 4
	B64U = 5
	BBNCh = 6
	BSHD = 7
	D16H = 8
	D16U = 9
	D4H = 10
	D4U = 11
	D64H = 12
	D64M = 13
	D64U = 14
	H16H = 15
	H16U = 16
	H4H = 17
	H64H = 18
	H64M = 19
	H64U = 20
	S4S8 = 21
	S8HD = 22
	S8HU = 23
	S8S4 = 24
	SBNCh = 25
	SCHF = 26
	SP8F = 27
	SQRA = 28
	SSHD = 29
	SSHU = 30
	SSTCh = 31
	STCH = 32
	T108 = 33
	T24 = 34
	T48 = 35
	T72 = 36
	TCHF = 37
	TCHH = 38
	U16H = 39
	U16U = 40
	U4H = 41
	U4U = 42
	U64H = 43
	U64M = 44
	U64U = 45


# noinspection SpellCheckingInspection
class TetraMarkMode(Enum):
	"""9 Members, FSTart ... TRIGger"""
	FSTart = 0
	HFSTart = 1
	MFSTart = 2
	PATTern = 3
	PULSe = 4
	RATio = 5
	RESTart = 6
	SSTart = 7
	TRIGger = 8


# noinspection SpellCheckingInspection
class TetraModulType(Enum):
	"""2 Members, PHASe ... QAM"""
	PHASe = 0
	QAM = 1


# noinspection SpellCheckingInspection
class TetraOffset(Enum):
	"""4 Members, M625 ... ZERO"""
	M625 = 0
	P125 = 1
	P625 = 2
	ZERO = 3


# noinspection SpellCheckingInspection
class TetraShrngMode(Enum):
	"""4 Members, CSHaring ... TCSHaring"""
	CSHaring = 0
	CTRansmission = 1
	MSHaring = 2
	TCSHaring = 3


# noinspection SpellCheckingInspection
class TetraSlotLevel(Enum):
	"""3 Members, ATTenuated ... OFF"""
	ATTenuated = 0
	FULL = 1
	OFF = 2


# noinspection SpellCheckingInspection
class TetraSysCode(Enum):
	"""8 Members, S0 ... S7"""
	S0 = 0
	S1 = 1
	S2 = 2
	S3 = 3
	S4 = 4
	S5 = 5
	S6 = 6
	S7 = 7


# noinspection SpellCheckingInspection
class TetraT2BurstType(Enum):
	"""16 Members, CU16 ... SDDB"""
	CU16 = 0
	CU4 = 1
	CU64 = 2
	CUB = 3
	NCDB = 4
	ND16 = 5
	ND4 = 6
	ND64 = 7
	NDDB = 8
	NU16 = 9
	NU4 = 10
	NU64 = 11
	NUB = 12
	RAB = 13
	SCDB = 14
	SDDB = 15


# noinspection SpellCheckingInspection
class TetraTestMode(Enum):
	"""5 Members, T1 ... USER"""
	T1 = 0
	T2 = 1
	T3 = 2
	T4 = 3
	USER = 4


# noinspection SpellCheckingInspection
class TetraTscSource(Enum):
	"""2 Members, DEFault ... UDEFined"""
	DEFault = 0
	UDEFined = 1


# noinspection SpellCheckingInspection
class TetraTsRsrvdFrm(Enum):
	"""8 Members, F1 ... F9"""
	F1 = 0
	F12 = 1
	F18 = 2
	F2 = 3
	F3 = 4
	F4 = 5
	F6 = 6
	F9 = 7


# noinspection SpellCheckingInspection
class TetraTxBurstType(Enum):
	"""2 Members, CUB ... NUB"""
	CUB = 0
	NUB = 1


# noinspection SpellCheckingInspection
class TetraTxOn(Enum):
	"""2 Members, RON ... TON"""
	RON = 0
	TON = 1


# noinspection SpellCheckingInspection
class TetraTxPwr(Enum):
	"""7 Members, M15 ... M45"""
	M15 = 0
	M20 = 1
	M25 = 2
	M30 = 3
	M35 = 4
	M40 = 5
	M45 = 6


# noinspection SpellCheckingInspection
class TimcNtAoffs(Enum):
	"""4 Members, _0 ... NTA624"""
	_0 = 0
	_624 = 1
	NTA0 = 2
	NTA624 = 3


# noinspection SpellCheckingInspection
class TimeBasis(Enum):
	"""6 Members, BDT ... UTC"""
	BDT = 0
	GLO = 1
	GPS = 2
	GST = 3
	NAV = 4
	UTC = 5


# noinspection SpellCheckingInspection
class TimingAdjustmentOffsetAll(Enum):
	"""4 Members, N0 ... N39936"""
	N0 = 0
	N13792 = 1
	N25600 = 2
	N39936 = 3


# noinspection SpellCheckingInspection
class TmastConn(Enum):
	"""11 Members, BBMM1 ... RFB"""
	BBMM1 = 0
	BBMM2 = 1
	DEF = 2
	FAD1 = 3
	FAD2 = 4
	FAD3 = 5
	FAD4 = 6
	IQOUT1 = 7
	IQOUT2 = 8
	RFA = 9
	RFB = 10


# noinspection SpellCheckingInspection
class TpcDataSour(Enum):
	"""4 Members, DLISt ... ZERO"""
	DLISt = 0
	ONE = 1
	PATTern = 2
	ZERO = 3


# noinspection SpellCheckingInspection
class TpcMode(Enum):
	"""2 Members, D2B ... D4B"""
	D2B = 0
	D4B = 1


# noinspection SpellCheckingInspection
class TpcReadMode(Enum):
	"""5 Members, CONTinuous ... S1A"""
	CONTinuous = 0
	S01A = 1
	S0A = 2
	S10A = 3
	S1A = 4


# noinspection SpellCheckingInspection
class TranRecFftLen(Enum):
	"""6 Members, LEN1024 ... LEN8192"""
	LEN1024 = 0
	LEN2048 = 1
	LEN256 = 2
	LEN4096 = 3
	LEN512 = 4
	LEN8192 = 5


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
	"""26 Members, BBA ... STRH"""
	BBA = 0
	BBB = 1
	BBC = 2
	BBD = 3
	BBE = 4
	BBF = 5
	BBG = 6
	BBH = 7
	BBIA = 8
	BBIB = 9
	DO1 = 10
	DO2 = 11
	IQO1 = 12
	IQO2 = 13
	RFA = 14
	RFB = 15
	RFC = 16
	RFD = 17
	STRA = 18
	STRB = 19
	STRC = 20
	STRD = 21
	STRE = 22
	STRF = 23
	STRG = 24
	STRH = 25


# noinspection SpellCheckingInspection
class TranRecSourMux(Enum):
	"""8 Members, STRA ... STRH"""
	STRA = 0
	STRB = 1
	STRC = 2
	STRD = 3
	STRE = 4
	STRF = 5
	STRG = 6
	STRH = 7


# noinspection SpellCheckingInspection
class TranRecTrigSour(Enum):
	"""2 Members, MARKer ... SOFTware"""
	MARKer = 0
	SOFTware = 1


# noinspection SpellCheckingInspection
class TranSource(Enum):
	"""2 Members, DATA ... DTX"""
	DATA = 0
	DTX = 1


# noinspection SpellCheckingInspection
class TrigConf(Enum):
	"""2 Members, AAUT ... UNCH"""
	AAUT = 0
	UNCH = 1


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
class TriggerSourceC(Enum):
	"""13 Members, BBSY ... OBASeband"""
	BBSY = 0
	BEXTernal = 1
	EGC1 = 2
	EGC2 = 3
	EGT1 = 4
	EGT2 = 5
	ELCLock = 6
	ELTRigger = 7
	EXTernal = 8
	INTA = 9
	INTB = 10
	INTernal = 11
	OBASeband = 12


# noinspection SpellCheckingInspection
class TrigRunMode(Enum):
	"""2 Members, RUN ... STOP"""
	RUN = 0
	STOP = 1


# noinspection SpellCheckingInspection
class TrigSourBerBler(Enum):
	"""2 Members, EGT1 ... INTernal"""
	EGT1 = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class TrigSourReg(Enum):
	"""3 Members, ERRTA ... INTernal"""
	ERRTA = 0
	ERRTB = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class TrigSourRest(Enum):
	"""4 Members, EGC1 ... EGT2"""
	EGC1 = 0
	EGC2 = 1
	EGT1 = 2
	EGT2 = 3


# noinspection SpellCheckingInspection
class TrigSweepSourNoHopExtAuto(Enum):
	"""5 Members, AUTO ... SINGle"""
	AUTO = 0
	BUS = 1
	EXTernal = 2
	IMMediate = 3
	SINGle = 4


# noinspection SpellCheckingInspection
class Tristate(Enum):
	"""6 Members, _0 ... ON"""
	_0 = 0
	_1 = 1
	_2 = 2
	NOvalue = 3
	OFF = 4
	ON = 5


# noinspection SpellCheckingInspection
class TropModel(Enum):
	"""3 Members, MOPS ... STANag"""
	MOPS = 0
	NONE = 1
	STANag = 2


# noinspection SpellCheckingInspection
class Ts25141Bler(Enum):
	"""4 Members, B0 ... B01"""
	B0 = 0
	B0001 = 1
	B001 = 2
	B01 = 3


# noinspection SpellCheckingInspection
class Ts25141BspOwClass(Enum):
	"""3 Members, LOCal ... WIDE"""
	LOCal = 0
	MEDium = 1
	WIDE = 2


# noinspection SpellCheckingInspection
class Ts25141EditMode(Enum):
	"""2 Members, STANdard ... USER"""
	STANdard = 0
	USER = 1


# noinspection SpellCheckingInspection
class Ts25141IfScen(Enum):
	"""10 Members, TM116 ... TM58"""
	TM116 = 0
	TM132 = 1
	TM164 = 2
	TM2 = 3
	TM316 = 4
	TM332 = 5
	TM4 = 6
	TM528 = 7
	TM538 = 8
	TM58 = 9


# noinspection SpellCheckingInspection
class Ts25141MarkerConf(Enum):
	"""2 Members, AUTO ... PRESet"""
	AUTO = 0
	PRESet = 1


# noinspection SpellCheckingInspection
class Ts25141ReqPd(Enum):
	"""2 Members, PD099 ... PD0999"""
	PD099 = 0
	PD0999 = 1


# noinspection SpellCheckingInspection
class Ts25141ScrCodeMode(Enum):
	"""4 Members, LONG ... SHORt"""
	LONG = 0
	OFF = 1
	ON = 2
	SHORt = 3


# noinspection SpellCheckingInspection
class Ts25141SigMod(Enum):
	"""4 Members, CW ... WCDMa"""
	CW = 0
	GMSK = 1
	QPSK = 2
	WCDMa = 3


# noinspection SpellCheckingInspection
class Ts25141Tc(Enum):
	"""24 Members, TC642 ... TC894"""
	TC642 = 0
	TC66 = 1
	TC72 = 2
	TC73 = 3
	TC74 = 4
	TC75 = 5
	TC76 = 6
	TC78 = 7
	TC821 = 8
	TC831 = 9
	TC832 = 10
	TC833 = 11
	TC834 = 12
	TC84 = 13
	TC85 = 14
	TC86 = 15
	TC881 = 16
	TC882 = 17
	TC883 = 18
	TC884 = 19
	TC891 = 20
	TC892 = 21
	TC893 = 22
	TC894 = 23


# noinspection SpellCheckingInspection
class Ts25141TpcRepeatPattSour(Enum):
	"""6 Members, AGGRegated ... ZERO"""
	AGGRegated = 0
	DLISt = 1
	ONE = 2
	PATTern = 3
	SINGle = 4
	ZERO = 5


# noinspection SpellCheckingInspection
class Ts25141TpcStartPattSour(Enum):
	"""2 Members, DLISt ... PMAX"""
	DLISt = 0
	PMAX = 1


# noinspection SpellCheckingInspection
class Ts25141TriggerConf(Enum):
	"""3 Members, AUTO ... SINGle"""
	AUTO = 0
	PRESet = 1
	SINGle = 2


# noinspection SpellCheckingInspection
class Ts25141WsbLkScen(Enum):
	"""3 Members, COLocated ... WIDE"""
	COLocated = 0
	NARRow = 1
	WIDE = 2


# noinspection SpellCheckingInspection
class Ts25141WsoPband(Enum):
	"""6 Members, I ... VI"""
	I = 0
	II = 1
	III = 2
	IV = 3
	V = 4
	VI = 5


# noinspection SpellCheckingInspection
class TxAntenna(Enum):
	"""2 Members, ANT1 ... ANT2"""
	ANT1 = 0
	ANT2 = 1


# noinspection SpellCheckingInspection
class TxAntennaGnss(Enum):
	"""6 Members, ALL ... NONE"""
	ALL = 0
	ANT1 = 1
	ANT2 = 2
	ANT3 = 3
	ANT4 = 4
	NONE = 5


# noinspection SpellCheckingInspection
class TxConfigAll(Enum):
	"""2 Members, CB ... NCB"""
	CB = 0
	NCB = 1


# noinspection SpellCheckingInspection
class TxDiv(Enum):
	"""4 Members, ANT1 ... SANT"""
	ANT1 = 0
	ANT2 = 1
	OFF = 2
	SANT = 3


# noinspection SpellCheckingInspection
class UciBits(Enum):
	"""2 Members, B_40 ... B_7"""
	B_40 = 0
	B_7 = 1


# noinspection SpellCheckingInspection
class UeCat(Enum):
	"""5 Members, C1 ... C5"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	C5 = 4


# noinspection SpellCheckingInspection
class UeMode(Enum):
	"""2 Members, PRACh ... STD"""
	PRACh = 0
	STD = 1


# noinspection SpellCheckingInspection
class UeRelease(Enum):
	"""4 Members, EMTC ... R89"""
	EMTC = 0
	LADV = 1
	NIOT = 2
	R89 = 3


# noinspection SpellCheckingInspection
class UlFormat(Enum):
	"""7 Members, F1 ... F3"""
	F1 = 0
	F1A = 1
	F1B = 2
	F2 = 3
	F2A = 4
	F2B = 5
	F3 = 6


# noinspection SpellCheckingInspection
class UlFrc(Enum):
	"""47 Members, A11 ... UE3"""
	A11 = 0
	A12 = 1
	A13 = 2
	A14 = 3
	A15 = 4
	A21 = 5
	A22 = 6
	A23 = 7
	A31 = 8
	A32 = 9
	A33 = 10
	A34 = 11
	A35 = 12
	A36 = 13
	A37 = 14
	A41 = 15
	A42 = 16
	A43 = 17
	A44 = 18
	A45 = 19
	A46 = 20
	A47 = 21
	A48 = 22
	A51 = 23
	A52 = 24
	A53 = 25
	A54 = 26
	A55 = 27
	A56 = 28
	A57 = 29
	A71 = 30
	A72 = 31
	A73 = 32
	A74 = 33
	A75 = 34
	A76 = 35
	A81 = 36
	A82 = 37
	A83 = 38
	A84 = 39
	A85 = 40
	A86 = 41
	UE11 = 42
	UE12 = 43
	UE21 = 44
	UE22 = 45
	UE3 = 46


# noinspection SpellCheckingInspection
class UlFreqHopMode(Enum):
	"""2 Members, INTer ... INTRa"""
	INTer = 0
	INTRa = 1


# noinspection SpellCheckingInspection
class UlfReqHopping(Enum):
	"""3 Members, DIS ... INTRA"""
	DIS = 0
	INTER = 1
	INTRA = 2


# noinspection SpellCheckingInspection
class UlFreqHopType(Enum):
	"""3 Members, NONE ... TP2"""
	NONE = 0
	TP1 = 1
	TP2 = 2


# noinspection SpellCheckingInspection
class UlModulation(Enum):
	"""5 Members, PSK8 ... QPSK"""
	PSK8 = 0
	QAM16 = 1
	QAM256 = 2
	QAM64 = 3
	QPSK = 4


# noinspection SpellCheckingInspection
class UnchOff(Enum):
	"""2 Members, OFF ... UNCHanged"""
	OFF = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class Unit(Enum):
	"""5 Members, FRAMe ... SUBFrame"""
	FRAMe = 0
	SAMPle = 1
	SEQuence = 2
	SLOT = 3
	SUBFrame = 4


# noinspection SpellCheckingInspection
class UnitAngle(Enum):
	"""3 Members, DEGree ... RADian"""
	DEGree = 0
	DEGRee = 1
	RADian = 2


# noinspection SpellCheckingInspection
class UnitLengthReg(Enum):
	"""4 Members, KM ... NM"""
	KM = 0
	M = 1
	MI = 2
	NM = 3


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
class UnitSlA(Enum):
	"""3 Members, CHIP ... SEQuence"""
	CHIP = 0
	FRAMe = 1
	SEQuence = 2


# noinspection SpellCheckingInspection
class UnitSlB(Enum):
	"""2 Members, SAMPle ... SEQuence"""
	SAMPle = 0
	SEQuence = 1


# noinspection SpellCheckingInspection
class UnitSlBto(Enum):
	"""3 Members, EVENt ... SEQuence"""
	EVENt = 0
	FRAMe = 1
	SEQuence = 2


# noinspection SpellCheckingInspection
class UnitSlDvb(Enum):
	"""2 Members, FRAMe ... SEQuence"""
	FRAMe = 0
	SEQuence = 1


# noinspection SpellCheckingInspection
class UnitSlEvdo(Enum):
	"""3 Members, CHIP ... SLOT"""
	CHIP = 0
	SEQuence = 1
	SLOT = 2


# noinspection SpellCheckingInspection
class UnitSlGsm(Enum):
	"""2 Members, FRAMe ... SYMBol"""
	FRAMe = 0
	SYMBol = 1


# noinspection SpellCheckingInspection
class UnitSlTetra(Enum):
	"""2 Members, MFRame ... SEQuence"""
	MFRame = 0
	SEQuence = 1


# noinspection SpellCheckingInspection
class UnitSlW3Gpp(Enum):
	"""4 Members, CHIP ... SLOT"""
	CHIP = 0
	FRAMe = 1
	SEQuence = 2
	SLOT = 3


# noinspection SpellCheckingInspection
class UnitSlXmRadio(Enum):
	"""3 Members, MCM ... TPL"""
	MCM = 0
	SAMPle = 1
	TPL = 2


# noinspection SpellCheckingInspection
class UnitSpeed(Enum):
	"""4 Members, KMH ... NMPH"""
	KMH = 0
	MPH = 1
	MPS = 2
	NMPH = 3


# noinspection SpellCheckingInspection
class UnitTimeSecMs(Enum):
	"""2 Members, MS ... S"""
	MS = 0
	S = 1


# noinspection SpellCheckingInspection
class Unknown(Enum):
	"""2 Members, DBM ... V"""
	DBM = 0
	V = 1


# noinspection SpellCheckingInspection
class UpDownDirection(Enum):
	"""2 Members, DOWN ... UP"""
	DOWN = 0
	UP = 1


# noinspection SpellCheckingInspection
class UpdPolicyMode(Enum):
	"""3 Members, CONFirm ... STRict"""
	CONFirm = 0
	IGNore = 1
	STRict = 2


# noinspection SpellCheckingInspection
class UtraTcwaCkNackBits(Enum):
	"""4 Members, ANB16 ... ANB64"""
	ANB16 = 0
	ANB24 = 1
	ANB4 = 2
	ANB64 = 3


# noinspection SpellCheckingInspection
class UtraTcwbSclass(Enum):
	"""4 Members, HOME ... WIDE"""
	HOME = 0
	LOCal = 1
	MEDium = 2
	WIDE = 3


# noinspection SpellCheckingInspection
class UtraTcwgsoPtion(Enum):
	"""2 Members, OPT1 ... OPT2"""
	OPT1 = 0
	OPT2 = 1


# noinspection SpellCheckingInspection
class UtraTcwgssUbtest(Enum):
	"""4 Members, STC1 ... STC4"""
	STC1 = 0
	STC2 = 1
	STC3 = 2
	STC4 = 3


# noinspection SpellCheckingInspection
class UtraTcwsPec(Enum):
	"""1 Members, TS36141 ... TS36141"""
	TS36141 = 0


# noinspection SpellCheckingInspection
class UtraTcwtMcodes(Enum):
	"""5 Members, COD16 ... COD8"""
	COD16 = 0
	COD32 = 1
	COD4 = 2
	COD64 = 3
	COD8 = 4


# noinspection SpellCheckingInspection
class V5GbfaNtSet(Enum):
	"""31 Members, AP0 ... AP9_13"""
	AP0 = 0
	AP0_1 = 1
	AP1 = 2
	AP10 = 3
	AP10_11 = 4
	AP10_14 = 5
	AP107 = 6
	AP107_109 = 7
	AP109 = 8
	AP11 = 9
	AP11_15 = 10
	AP12 = 11
	AP12_13 = 12
	AP13 = 13
	AP14 = 14
	AP14_15 = 15
	AP15 = 16
	AP2 = 17
	AP2_3 = 18
	AP3 = 19
	AP4 = 20
	AP4_5 = 21
	AP5 = 22
	AP6 = 23
	AP6_7 = 24
	AP7 = 25
	AP8 = 26
	AP8_12 = 27
	AP8_9 = 28
	AP9 = 29
	AP9_13 = 30


# noinspection SpellCheckingInspection
class V5GcSiRsNzpConfig(Enum):
	"""32 Members, C0 ... C9"""
	C0 = 0
	C1 = 1
	C10 = 2
	C11 = 3
	C12 = 4
	C13 = 5
	C14 = 6
	C15 = 7
	C16 = 8
	C17 = 9
	C18 = 10
	C19 = 11
	C2 = 12
	C20 = 13
	C21 = 14
	C22 = 15
	C23 = 16
	C24 = 17
	C25 = 18
	C26 = 19
	C27 = 20
	C28 = 21
	C29 = 22
	C3 = 23
	C30 = 24
	C31 = 25
	C4 = 26
	C5 = 27
	C6 = 28
	C7 = 29
	C8 = 30
	C9 = 31


# noinspection SpellCheckingInspection
class V5GcSiRsNzpqOffset(Enum):
	"""31 Members, M1 ... P8"""
	M1 = 0
	M10 = 1
	M12 = 2
	M14 = 3
	M16 = 4
	M18 = 5
	M2 = 6
	M20 = 7
	M22 = 8
	M24 = 9
	M3 = 10
	M4 = 11
	M5 = 12
	M6 = 13
	M8 = 14
	P0 = 15
	P1 = 16
	P10 = 17
	P12 = 18
	P14 = 19
	P16 = 20
	P18 = 21
	P2 = 22
	P20 = 23
	P22 = 24
	P24 = 25
	P3 = 26
	P4 = 27
	P5 = 28
	P6 = 29
	P8 = 30


# noinspection SpellCheckingInspection
class V5GdCiCbReq(Enum):
	"""2 Members, CSIRs ... NONE"""
	CSIRs = 0
	NONE = 1


# noinspection SpellCheckingInspection
class V5GdCiCbSym(Enum):
	"""3 Members, S12 ... S13"""
	S12 = 0
	S1213 = 1
	S13 = 2


# noinspection SpellCheckingInspection
class V5GdCiDlPcrs(Enum):
	"""4 Members, AP60 ... NONE"""
	AP60 = 0
	AP6061 = 1
	AP61 = 2
	NONE = 3


# noinspection SpellCheckingInspection
class V5GdCiFormat(Enum):
	"""4 Members, FA1 ... FB2"""
	FA1 = 0
	FA2 = 1
	FB1 = 2
	FB2 = 3


# noinspection SpellCheckingInspection
class V5GdCiPiOrBsi(Enum):
	"""4 Members, P0 ... P3"""
	P0 = 0
	P1 = 1
	P2 = 2
	P3 = 3


# noinspection SpellCheckingInspection
class V5GdCiSrsReq(Enum):
	"""4 Members, C0 ... NONE"""
	C0 = 0
	C1 = 1
	C2 = 2
	NONE = 3


# noinspection SpellCheckingInspection
class V5GdCiSrsSym(Enum):
	"""2 Members, S12 ... S13"""
	S12 = 0
	S13 = 1


# noinspection SpellCheckingInspection
class V5GdCiXpdscheNd(Enum):
	"""2 Members, S11 ... S13"""
	S11 = 0
	S13 = 1


# noinspection SpellCheckingInspection
class V5GdCiXpuschRange(Enum):
	"""3 Members, S12 ... S14"""
	S12 = 0
	S13 = 1
	S14 = 2


# noinspection SpellCheckingInspection
class V5GdlContentType(Enum):
	"""4 Members, CSI ... XPDSch"""
	CSI = 0
	XPBCh = 1
	XPDCch = 2
	XPDSch = 3


# noinspection SpellCheckingInspection
class V5GdlDataSourceUser(Enum):
	"""19 Members, DLISt ... ZERO"""
	DLISt = 0
	MCCH = 1
	MIB = 2
	MTCH = 3
	ONE = 4
	PATTern = 5
	PN11 = 6
	PN15 = 7
	PN16 = 8
	PN20 = 9
	PN21 = 10
	PN23 = 11
	PN9 = 12
	USER1 = 13
	USER2 = 14
	USER3 = 15
	USER4 = 16
	XPDCch = 17
	ZERO = 18


# noinspection SpellCheckingInspection
class V5GdlpRecMultAntScheme(Enum):
	"""4 Members, BF ... TXD"""
	BF = 0
	NONE = 1
	SMUX = 2
	TXD = 3


# noinspection SpellCheckingInspection
class V5GpDcchCfg(Enum):
	"""5 Members, NONE ... USER4"""
	NONE = 0
	USER1 = 1
	USER2 = 2
	USER3 = 3
	USER4 = 4


# noinspection SpellCheckingInspection
class V5GpuschChanCodCoderate(Enum):
	"""4 Members, R12 ... R56"""
	R12 = 0
	R23 = 1
	R34 = 2
	R56 = 3


# noinspection SpellCheckingInspection
class V5GpuschDmrs(Enum):
	"""2 Members, CELL ... DMRS"""
	CELL = 0
	DMRS = 1


# noinspection SpellCheckingInspection
class V5GpuschPcrs(Enum):
	"""2 Members, CELL ... PCRS"""
	CELL = 0
	PCRS = 1


# noinspection SpellCheckingInspection
class V5GpuschPrecScheme(Enum):
	"""2 Members, NONE ... SMUX"""
	NONE = 0
	SMUX = 1


# noinspection SpellCheckingInspection
class V5GtxMode(Enum):
	"""3 Members, M1 ... M3"""
	M1 = 0
	M2 = 1
	M3 = 2


# noinspection SpellCheckingInspection
class V5GuEcat(Enum):
	"""6 Members, C1 ... USER"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	C5 = 4
	USER = 5


# noinspection SpellCheckingInspection
class V5GulContentType(Enum):
	"""4 Members, PUCCh ... XPUSch"""
	PUCCh = 0
	PUSCh = 1
	XPUCch = 2
	XPUSch = 3


# noinspection SpellCheckingInspection
class ViewMode(Enum):
	"""2 Members, PRB ... VRB"""
	PRB = 0
	VRB = 1


# noinspection SpellCheckingInspection
class ViewType(Enum):
	"""2 Members, DISTance ... HEIGht"""
	DISTance = 0
	HEIGht = 1


# noinspection SpellCheckingInspection
class VrbToPrbInterleaverAll(Enum):
	"""3 Members, VP2 ... VPN"""
	VP2 = 0
	VP4 = 1
	VPN = 2


# noinspection SpellCheckingInspection
class WcdmaLevRef(Enum):
	"""7 Members, DPCC ... RMS"""
	DPCC = 0
	EDCH = 1
	HACK = 2
	LPP = 3
	PCQI = 4
	PMP = 5
	RMS = 6


# noinspection SpellCheckingInspection
class WcdmaSymbRateEdPdchOverallSymbRate(Enum):
	"""14 Members, D120k ... D960k"""
	D120k = 0
	D15K = 1
	D1920k = 2
	D240k = 3
	D2880k = 4
	D2X1920K = 5
	D2X960K2X1920K = 6
	D30K = 7
	D3840k = 8
	D4800k = 9
	D480k = 10
	D5760k = 11
	D60K = 12
	D960k = 13


# noinspection SpellCheckingInspection
class WcdmaUlDtxBurstLen(Enum):
	"""3 Members, _1 ... _5"""
	_1 = 0
	_2 = 1
	_5 = 2


# noinspection SpellCheckingInspection
class WcdmaUlDtxCycle(Enum):
	"""13 Members, _1 ... _80"""
	_1 = 0
	_10 = 1
	_128 = 2
	_16 = 3
	_160 = 4
	_20 = 5
	_32 = 6
	_4 = 7
	_40 = 8
	_5 = 9
	_64 = 10
	_8 = 11
	_80 = 12


# noinspection SpellCheckingInspection
class WcdmaUlDtxLongPreLen(Enum):
	"""3 Members, _15 ... _4"""
	_15 = 0
	_2 = 1
	_4 = 2


# noinspection SpellCheckingInspection
class WcdmaUlDtxMode(Enum):
	"""2 Members, UDTX ... USCH"""
	UDTX = 0
	USCH = 1


# noinspection SpellCheckingInspection
class WcdmaUlDtxThreshold(Enum):
	"""8 Members, _1 ... _8"""
	_1 = 0
	_128 = 1
	_16 = 2
	_256 = 3
	_32 = 4
	_4 = 5
	_64 = 6
	_8 = 7


# noinspection SpellCheckingInspection
class WlanadChCod(Enum):
	"""5 Members, LDPC ... RS9"""
	LDPC = 0
	RB12 = 1
	RB16 = 2
	RB8 = 3
	RS9 = 4


# noinspection SpellCheckingInspection
class WlanadCodRate(Enum):
	"""9 Members, CR13D14 ... CR7D8"""
	CR13D14 = 0
	CR13D16 = 1
	CR13D21 = 2
	CR13D28 = 3
	CR1D2 = 4
	CR3D4 = 5
	CR52D63 = 6
	CR5D8 = 7
	CR7D8 = 8


# noinspection SpellCheckingInspection
class WlanadDmgPhyMode(Enum):
	"""4 Members, CONTrol ... SINGle"""
	CONTrol = 0
	LPOW = 1
	OFDM = 2
	SINGle = 3


# noinspection SpellCheckingInspection
class WlanadFrameType(Enum):
	"""2 Members, BEACon ... DATA"""
	BEACon = 0
	DATA = 1


# noinspection SpellCheckingInspection
class WlanadGrpPrIdx(Enum):
	"""42 Members, GPI0 ... GPI9"""
	GPI0 = 0
	GPI1 = 1
	GPI10 = 2
	GPI11 = 3
	GPI12 = 4
	GPI13 = 5
	GPI14 = 6
	GPI15 = 7
	GPI16 = 8
	GPI17 = 9
	GPI18 = 10
	GPI19 = 11
	GPI2 = 12
	GPI20 = 13
	GPI21 = 14
	GPI22 = 15
	GPI23 = 16
	GPI24 = 17
	GPI25 = 18
	GPI26 = 19
	GPI27 = 20
	GPI28 = 21
	GPI29 = 22
	GPI3 = 23
	GPI30 = 24
	GPI31 = 25
	GPI32 = 26
	GPI33 = 27
	GPI34 = 28
	GPI35 = 29
	GPI36 = 30
	GPI37 = 31
	GPI38 = 32
	GPI39 = 33
	GPI4 = 34
	GPI40 = 35
	GPI41 = 36
	GPI5 = 37
	GPI6 = 38
	GPI7 = 39
	GPI8 = 40
	GPI9 = 41


# noinspection SpellCheckingInspection
class WlanadLastRssi(Enum):
	"""16 Members, M42 ... NA"""
	M42 = 0
	M43 = 1
	M45 = 2
	M47 = 3
	M49 = 4
	M51 = 5
	M53 = 6
	M55 = 7
	M57 = 8
	M59 = 9
	M61 = 10
	M63 = 11
	M65 = 12
	M67 = 13
	M68 = 14
	NA = 15


# noinspection SpellCheckingInspection
class WlanadMarkMode(Enum):
	"""8 Members, FAPart ... TRIGger"""
	FAPart = 0
	FIPart = 1
	FRAMe = 2
	PATTern = 3
	PULSe = 4
	RATio = 5
	RESTart = 6
	TRIGger = 7


# noinspection SpellCheckingInspection
class WlanadModType(Enum):
	"""9 Members, DBPSK ... SQPSK"""
	DBPSK = 0
	P2BPSK = 1
	P2QAM16 = 2
	P2QAM64 = 3
	P2QPSK = 4
	QAM16 = 5
	QAM64 = 6
	QPSK = 7
	SQPSK = 8


# noinspection SpellCheckingInspection
class WlanadPackType(Enum):
	"""2 Members, TRNR ... TRNT"""
	TRNR = 0
	TRNT = 1


# noinspection SpellCheckingInspection
class WlanadTonePairType(Enum):
	"""2 Members, DYNamic ... STATic"""
	DYNamic = 0
	STATic = 1


# noinspection SpellCheckingInspection
class WlannDataSource(Enum):
	"""12 Members, AMPDU ... ZERO"""
	AMPDU = 0
	DLISt = 1
	ONE = 2
	PATTern = 3
	PN11 = 4
	PN15 = 5
	PN16 = 6
	PN20 = 7
	PN21 = 8
	PN23 = 9
	PN9 = 10
	ZERO = 11


# noinspection SpellCheckingInspection
class WlannFbChBwInNonHt(Enum):
	"""5 Members, B160 ... OFF"""
	B160 = 0
	B20 = 1
	B40 = 2
	B80 = 3
	OFF = 4


# noinspection SpellCheckingInspection
class WlannFbCodRate(Enum):
	"""4 Members, CR1D2 ... CR5D6"""
	CR1D2 = 0
	CR2D3 = 1
	CR3D4 = 2
	CR5D6 = 3


# noinspection SpellCheckingInspection
class WlannFbCodType(Enum):
	"""3 Members, BCC ... OFF"""
	BCC = 0
	LDPC = 1
	OFF = 2


# noinspection SpellCheckingInspection
class WlannFbDynBwInNonHt(Enum):
	"""3 Members, DYN ... STAT"""
	DYN = 0
	OFF = 1
	STAT = 2


# noinspection SpellCheckingInspection
class WlannFbEncoder(Enum):
	"""12 Members, E1 ... E9"""
	E1 = 0
	E10 = 1
	E11 = 2
	E12 = 3
	E2 = 4
	E3 = 5
	E4 = 6
	E5 = 7
	E6 = 8
	E7 = 9
	E8 = 10
	E9 = 11


# noinspection SpellCheckingInspection
class WlannFbGuard(Enum):
	"""5 Members, GD08 ... SHORt"""
	GD08 = 0
	GD16 = 1
	GD32 = 2
	LONG = 3
	SHORt = 4


# noinspection SpellCheckingInspection
class WlannFbMcs(Enum):
	"""77 Members, MCS0 ... MCS9"""
	MCS0 = 0
	MCS1 = 1
	MCS10 = 2
	MCS11 = 3
	MCS12 = 4
	MCS13 = 5
	MCS14 = 6
	MCS15 = 7
	MCS16 = 8
	MCS17 = 9
	MCS18 = 10
	MCS19 = 11
	MCS2 = 12
	MCS20 = 13
	MCS21 = 14
	MCS22 = 15
	MCS23 = 16
	MCS24 = 17
	MCS25 = 18
	MCS26 = 19
	MCS27 = 20
	MCS28 = 21
	MCS29 = 22
	MCS3 = 23
	MCS30 = 24
	MCS31 = 25
	MCS32 = 26
	MCS33 = 27
	MCS34 = 28
	MCS35 = 29
	MCS36 = 30
	MCS37 = 31
	MCS38 = 32
	MCS39 = 33
	MCS4 = 34
	MCS40 = 35
	MCS41 = 36
	MCS42 = 37
	MCS43 = 38
	MCS44 = 39
	MCS45 = 40
	MCS46 = 41
	MCS47 = 42
	MCS48 = 43
	MCS49 = 44
	MCS5 = 45
	MCS50 = 46
	MCS51 = 47
	MCS52 = 48
	MCS53 = 49
	MCS54 = 50
	MCS55 = 51
	MCS56 = 52
	MCS57 = 53
	MCS58 = 54
	MCS59 = 55
	MCS6 = 56
	MCS60 = 57
	MCS61 = 58
	MCS62 = 59
	MCS63 = 60
	MCS64 = 61
	MCS65 = 62
	MCS66 = 63
	MCS67 = 64
	MCS68 = 65
	MCS69 = 66
	MCS7 = 67
	MCS70 = 68
	MCS71 = 69
	MCS72 = 70
	MCS73 = 71
	MCS74 = 72
	MCS75 = 73
	MCS76 = 74
	MCS8 = 75
	MCS9 = 76


# noinspection SpellCheckingInspection
class WlannFbMod(Enum):
	"""7 Members, BPSK ... QPSK"""
	BPSK = 0
	QAM1024 = 1
	QAM16 = 2
	QAM256 = 3
	QAM4096 = 4
	QAM64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class WlannFbPhyMode(Enum):
	"""3 Members, GFIeld ... MIXed"""
	GFIeld = 0
	LEGacy = 1
	MIXed = 2


# noinspection SpellCheckingInspection
class WlannFbPilotType(Enum):
	"""2 Members, FIXed ... TRAVeling"""
	FIXed = 0
	TRAVeling = 1


# noinspection SpellCheckingInspection
class WlannFbPpduFormat(Enum):
	"""4 Members, MU ... TRIG"""
	MU = 0
	SU = 1
	SUEXt = 2
	TRIG = 3


# noinspection SpellCheckingInspection
class WlannFbPpduHeLtfSymbDuraion(Enum):
	"""3 Members, SD128 ... SD64"""
	SD128 = 0
	SD32 = 1
	SD64 = 2


# noinspection SpellCheckingInspection
class WlannFbPpduPeDuraion(Enum):
	"""3 Members, PE0 ... PE8"""
	PE0 = 0
	PE16 = 1
	PE8 = 2


# noinspection SpellCheckingInspection
class WlannFbPpduPreamblePuncturingBw(Enum):
	"""4 Members, _4 ... _7"""
	_4 = 0
	_5 = 1
	_6 = 2
	_7 = 3


# noinspection SpellCheckingInspection
class WlannFbPpduRuAlloc(Enum):
	"""87 Members, RU0 ... RU9"""
	RU0 = 0
	RU1 = 1
	RU10 = 2
	RU11 = 3
	RU12 = 4
	RU13 = 5
	RU14 = 6
	RU15 = 7
	RU16 = 8
	RU17 = 9
	RU18 = 10
	RU19 = 11
	RU2 = 12
	RU20 = 13
	RU21 = 14
	RU22 = 15
	RU23 = 16
	RU24 = 17
	RU25 = 18
	RU26 = 19
	RU27 = 20
	RU28 = 21
	RU29 = 22
	RU3 = 23
	RU30 = 24
	RU31 = 25
	RU32 = 26
	RU33 = 27
	RU34 = 28
	RU35 = 29
	RU36 = 30
	RU37 = 31
	RU38 = 32
	RU39 = 33
	RU4 = 34
	RU40 = 35
	RU41 = 36
	RU42 = 37
	RU43 = 38
	RU44 = 39
	RU45 = 40
	RU46 = 41
	RU47 = 42
	RU48 = 43
	RU49 = 44
	RU5 = 45
	RU50 = 46
	RU51 = 47
	RU52 = 48
	RU53 = 49
	RU54 = 50
	RU55 = 51
	RU56 = 52
	RU57 = 53
	RU58 = 54
	RU59 = 55
	RU6 = 56
	RU60 = 57
	RU61 = 58
	RU62 = 59
	RU63 = 60
	RU64 = 61
	RU65 = 62
	RU66 = 63
	RU67 = 64
	RU68 = 65
	RU69 = 66
	RU7 = 67
	RU70 = 68
	RU71 = 69
	RU72 = 70
	RU73 = 71
	RU74 = 72
	RU75 = 73
	RU76 = 74
	RU77 = 75
	RU78 = 76
	RU79 = 77
	RU8 = 78
	RU80 = 79
	RU81 = 80
	RU82 = 81
	RU83 = 82
	RU84 = 83
	RU85 = 84
	RU86 = 85
	RU9 = 86


# noinspection SpellCheckingInspection
class WlannFbPpduRuSel(Enum):
	"""39 Members, RU0 ... RU9"""
	RU0 = 0
	RU1 = 1
	RU10 = 2
	RU11 = 3
	RU12 = 4
	RU13 = 5
	RU14 = 6
	RU15 = 7
	RU16 = 8
	RU17 = 9
	RU18 = 10
	RU19 = 11
	RU2 = 12
	RU20 = 13
	RU21 = 14
	RU22 = 15
	RU23 = 16
	RU24 = 17
	RU25 = 18
	RU26 = 19
	RU27 = 20
	RU28 = 21
	RU29 = 22
	RU3 = 23
	RU30 = 24
	RU31 = 25
	RU32 = 26
	RU33 = 27
	RU34 = 28
	RU35 = 29
	RU36 = 30
	RU37 = 31
	RU38 = 32
	RU4 = 33
	RU5 = 34
	RU6 = 35
	RU7 = 36
	RU8 = 37
	RU9 = 38


# noinspection SpellCheckingInspection
class WlannFbPpduUserMruIdx(Enum):
	"""12 Members, MRU1 ... MRU9"""
	MRU1 = 0
	MRU10 = 1
	MRU11 = 2
	MRU12 = 3
	MRU2 = 4
	MRU3 = 5
	MRU4 = 6
	MRU5 = 7
	MRU6 = 8
	MRU7 = 9
	MRU8 = 10
	MRU9 = 11


# noinspection SpellCheckingInspection
class WlannFbPpduUserRuType(Enum):
	"""15 Members, RU106 ... RUC26"""
	RU106 = 0
	RU242 = 1
	RU26 = 2
	RU2996 = 3
	RU2996_484 = 4
	RU3996 = 5
	RU3996_484 = 6
	RU484 = 7
	RU484_242 = 8
	RU4996 = 9
	RU52 = 10
	RU996 = 11
	RU996_484 = 12
	RU996_484_242 = 13
	RUC26 = 14


# noinspection SpellCheckingInspection
class WlannFbScrMode(Enum):
	"""5 Members, OFF ... USER"""
	OFF = 0
	ON = 1
	PREamble = 2
	RANDom = 3
	USER = 4


# noinspection SpellCheckingInspection
class WlannFbSegment(Enum):
	"""3 Members, BOTH ... SEG1"""
	BOTH = 0
	SEG0 = 1
	SEG1 = 2


# noinspection SpellCheckingInspection
class WlannFbSpatMapMode(Enum):
	"""5 Members, BEAMforming ... OFF"""
	BEAMforming = 0
	DIRect = 1
	EXPansion = 2
	INDirect = 3
	OFF = 4


# noinspection SpellCheckingInspection
class WlannFbStbcState(Enum):
	"""2 Members, ACTive ... INACtive"""
	ACTive = 0
	INACtive = 1


# noinspection SpellCheckingInspection
class WlannFbStd(Enum):
	"""8 Members, USER ... WPJ"""
	USER = 0
	WAC = 1
	WAG = 2
	WAX = 3
	WBE = 4
	WBG = 5
	WN = 6
	WPJ = 7


# noinspection SpellCheckingInspection
class WlannFbTrigFrmType(Enum):
	"""3 Members, BASIC ... MURTS"""
	BASIC = 0
	BSRP = 1
	MURTS = 2


# noinspection SpellCheckingInspection
class WlannFbTxMode(Enum):
	"""33 Members, CCK ... V8080"""
	CCK = 0
	EHT160 = 1
	EHT160160 = 2
	EHT20 = 3
	EHT320 = 4
	EHT40 = 5
	EHT80 = 6
	EHT8080 = 7
	HE160 = 8
	HE20 = 9
	HE40 = 10
	HE80 = 11
	HE8080 = 12
	HT20 = 13
	HT40 = 14
	HTDup = 15
	HTLow = 16
	HTUP = 17
	L10 = 18
	L20 = 19
	LDUP = 20
	LLOW = 21
	LUP = 22
	PBCC = 23
	S1 = 24
	S16 = 25
	S2 = 26
	S4 = 27
	V160 = 28
	V20 = 29
	V40 = 30
	V80 = 31
	V8080 = 32


# noinspection SpellCheckingInspection
class WlannFbType(Enum):
	"""4 Members, BEACon ... TRIGger"""
	BEACon = 0
	DATA = 1
	SOUNding = 2
	TRIGger = 3


# noinspection SpellCheckingInspection
class WlannFbUserIdx(Enum):
	"""4 Members, UIDX0 ... UIDX3"""
	UIDX0 = 0
	UIDX1 = 1
	UIDX2 = 2
	UIDX3 = 3


# noinspection SpellCheckingInspection
class WlannMarkMode(Enum):
	"""9 Members, FAPart ... TRIGger"""
	FAPart = 0
	FBLock = 1
	FIPart = 2
	FRAMe = 3
	PATTern = 4
	PULSe = 5
	RATio = 6
	RESTart = 7
	TRIGger = 8


# noinspection SpellCheckingInspection
class WlannMcs(Enum):
	"""39 Members, MCS0 ... MCS91"""
	MCS0 = 0
	MCS1 = 1
	MCS10 = 2
	MCS11 = 3
	MCS12 = 4
	MCS121 = 5
	MCS122 = 6
	MCS123 = 7
	MCS124 = 8
	MCS125 = 9
	MCS126 = 10
	MCS13 = 11
	MCS14 = 12
	MCS15 = 13
	MCS16 = 14
	MCS17 = 15
	MCS18 = 16
	MCS19 = 17
	MCS2 = 18
	MCS20 = 19
	MCS21 = 20
	MCS22 = 21
	MCS23 = 22
	MCS24 = 23
	MCS25 = 24
	MCS26 = 25
	MCS27 = 26
	MCS28 = 27
	MCS29 = 28
	MCS3 = 29
	MCS30 = 30
	MCS31 = 31
	MCS4 = 32
	MCS5 = 33
	MCS6 = 34
	MCS7 = 35
	MCS8 = 36
	MCS9 = 37
	MCS91 = 38


# noinspection SpellCheckingInspection
class WlannTxAnt(Enum):
	"""8 Members, A1 ... A8"""
	A1 = 0
	A2 = 1
	A3 = 2
	A4 = 3
	A5 = 4
	A6 = 5
	A7 = 6
	A8 = 7


# noinspection SpellCheckingInspection
class WlannTxBw(Enum):
	"""5 Members, BW160 ... BW80"""
	BW160 = 0
	BW20 = 1
	BW320 = 2
	BW40 = 3
	BW80 = 4


# noinspection SpellCheckingInspection
class WlannTxNumBb(Enum):
	"""5 Members, NBB1 ... NBB8"""
	NBB1 = 0
	NBB2 = 1
	NBB3 = 2
	NBB4 = 3
	NBB8 = 4


# noinspection SpellCheckingInspection
class WlannTxOutpDest(Enum):
	"""10 Members, BB ... OFF"""
	BB = 0
	BB_B = 1
	BB_C = 2
	BB_D = 3
	BB_E = 4
	BB_F = 5
	BB_G = 6
	BB_H = 7
	FILE = 8
	OFF = 9


# noinspection SpellCheckingInspection
class XmRadioMarkMode(Enum):
	"""7 Members, MCM ... USER"""
	MCM = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	TPL = 4
	TRIGger = 5
	USER = 6


# noinspection SpellCheckingInspection
class XmRadioPhysLayer(Enum):
	"""6 Members, SAT1A ... TERRB"""
	SAT1A = 0
	SAT1B = 1
	SAT2A = 2
	SAT2B = 3
	TERRA = 4
	TERRB = 5


# noinspection SpellCheckingInspection
class XoverheadAll(Enum):
	"""4 Members, N0 ... N6"""
	N0 = 0
	N12 = 1
	N18 = 2
	N6 = 3


# noinspection SpellCheckingInspection
class YesNoStatus(Enum):
	"""2 Members, NO ... YES"""
	NO = 0
	YES = 1
