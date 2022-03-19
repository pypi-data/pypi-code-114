from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bbncht:
	"""Bbncht commands group definition. 26 total commands, 0 Subgroups, 26 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbncht", core, parent)

	# noinspection PyTypeChecker
	def get_aparameter(self) -> enums.TetraAcssParm:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:APARameter \n
		Snippet: value: enums.TetraAcssParm = driver.source.bb.tetra.bbncht.get_aparameter() \n
		Sets the value of the ACCESS_PARAMETER information field. This parameter is used for subsequent power adjustments for the
		mobile station. This protocol information field can takes values from -53 dBm to -23 dBm in 2 dB steps. \n
			:return: aparameter: AP53| AP51| AP49| AP47| AP45| AP43| AP41| AP39| AP37| AP35| AP33| AP31| AP29| AP27| AP25| AP23
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:APARameter?')
		return Conversions.str_to_scalar_enum(response, enums.TetraAcssParm)

	def set_aparameter(self, aparameter: enums.TetraAcssParm) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:APARameter \n
		Snippet: driver.source.bb.tetra.bbncht.set_aparameter(aparameter = enums.TetraAcssParm.AP23) \n
		Sets the value of the ACCESS_PARAMETER information field. This parameter is used for subsequent power adjustments for the
		mobile station. This protocol information field can takes values from -53 dBm to -23 dBm in 2 dB steps. \n
			:param aparameter: AP53| AP51| AP49| AP47| AP45| AP43| AP41| AP39| AP37| AP35| AP33| AP31| AP29| AP27| AP25| AP23
		"""
		param = Conversions.enum_scalar_to_str(aparameter, enums.TetraAcssParm)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:APARameter {param}')

	def get_bc_code(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:BCCode \n
		Snippet: value: int = driver.source.bb.tetra.bbncht.get_bc_code() \n
		Sets the colour code. The base color code is the number of subscriber group in a network. See Table 'Building of
		scrambling code' for information on how the scrambling code is calculated. \n
			:return: bc_code: integer Range: 1 to 63
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:BCCode?')
		return Conversions.str_to_int(response)

	def set_bc_code(self, bc_code: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:BCCode \n
		Snippet: driver.source.bb.tetra.bbncht.set_bc_code(bc_code = 1) \n
		Sets the colour code. The base color code is the number of subscriber group in a network. See Table 'Building of
		scrambling code' for information on how the scrambling code is calculated. \n
			:param bc_code: integer Range: 1 to 63
		"""
		param = Conversions.decimal_value_to_str(bc_code)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:BCCode {param}')

	# noinspection PyTypeChecker
	def get_cbandwidth(self) -> enums.TetraCrrBndwdth:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:CBANdwidth \n
		Snippet: value: enums.TetraCrrBndwdth = driver.source.bb.tetra.bbncht.get_cbandwidth() \n
		Selects the carrier bandwidth, i.e. determines the carrier spacing. The default value for all standard test modes is
		25kHz; carrier spacing of 50, 100 and 150 kHz is enabled for 'Test Mode' set to User Defined or T4. \n
			:return: cbandwidth: C25| C50| C100| C150
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:CBANdwidth?')
		return Conversions.str_to_scalar_enum(response, enums.TetraCrrBndwdth)

	def set_cbandwidth(self, cbandwidth: enums.TetraCrrBndwdth) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:CBANdwidth \n
		Snippet: driver.source.bb.tetra.bbncht.set_cbandwidth(cbandwidth = enums.TetraCrrBndwdth.C100) \n
		Selects the carrier bandwidth, i.e. determines the carrier spacing. The default value for all standard test modes is
		25kHz; carrier spacing of 50, 100 and 150 kHz is enabled for 'Test Mode' set to User Defined or T4. \n
			:param cbandwidth: C25| C50| C100| C150
		"""
		param = Conversions.enum_scalar_to_str(cbandwidth, enums.TetraCrrBndwdth)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:CBANdwidth {param}')

	def get_cr_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:CRFRequency \n
		Snippet: value: float = driver.source.bb.tetra.bbncht.get_cr_frequency() \n
		Displays the resulting RF frequency, calculated from the previous settings. The frequency is calculated from the
		'Frequency Band', 'Main Carrier Number', 'Offset', 'Duplex Spacing' and 'Reverse Operation' and transmitted in message
		channel BNCH/T when Downlink MS V+D Testing is selected. The 'Coded RF Frequency' is calculated as described in Table
		'Calculation of coded RF frequency'. \n
			:return: cr_frequency: float Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:CRFRequency?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_cs_level(self) -> enums.TetraCelSvLevel:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:CSLevel \n
		Snippet: value: enums.TetraCelSvLevel = driver.source.bb.tetra.bbncht.get_cs_level() \n
		Sets the cell service level information element, i.e. define the level of service a MS may receive in a cell.
		It may relate to the traffic loading in a cell. \n
			:return: cs_level: CLUNknown| LCLoad| MCLoad| HCLoad CLUNknown Cell load unknown LCLoad Low cell load MCLoad Medium cell load HCLoad High cell load
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:CSLevel?')
		return Conversions.str_to_scalar_enum(response, enums.TetraCelSvLevel)

	def set_cs_level(self, cs_level: enums.TetraCelSvLevel) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:CSLevel \n
		Snippet: driver.source.bb.tetra.bbncht.set_cs_level(cs_level = enums.TetraCelSvLevel.CLUNknown) \n
		Sets the cell service level information element, i.e. define the level of service a MS may receive in a cell.
		It may relate to the traffic loading in a cell. \n
			:param cs_level: CLUNknown| LCLoad| MCLoad| HCLoad CLUNknown Cell load unknown LCLoad Low cell load MCLoad Medium cell load HCLoad High cell load
		"""
		param = Conversions.enum_scalar_to_str(cs_level, enums.TetraCelSvLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:CSLevel {param}')

	def get_dnb_broadcast(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:DNBBroadcast \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_dnb_broadcast() \n
		Enables/disables support of the D-NWRK-BROADCAST PDU. \n
			:return: dnb_broadcast: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:DNBBroadcast?')
		return Conversions.str_to_bool(response)

	def set_dnb_broadcast(self, dnb_broadcast: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:DNBBroadcast \n
		Snippet: driver.source.bb.tetra.bbncht.set_dnb_broadcast(dnb_broadcast = False) \n
		Enables/disables support of the D-NWRK-BROADCAST PDU. \n
			:param dnb_broadcast: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dnb_broadcast)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:DNBBroadcast {param}')

	def get_dnb_enquiry(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:DNBenquiry \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_dnb_enquiry() \n
		Enables/disables support of the D-NWRK-BROADCAST enquiry. \n
			:return: dnb_enquiry: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:DNBenquiry?')
		return Conversions.str_to_bool(response)

	def set_dnb_enquiry(self, dnb_enquiry: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:DNBenquiry \n
		Snippet: driver.source.bb.tetra.bbncht.set_dnb_enquiry(dnb_enquiry = False) \n
		Enables/disables support of the D-NWRK-BROADCAST enquiry. \n
			:param dnb_enquiry: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dnb_enquiry)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:DNBenquiry {param}')

	# noinspection PyTypeChecker
	def get_dspacing(self) -> enums.TetraDplxSpcing:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:DSPacing \n
		Snippet: value: enums.TetraDplxSpcing = driver.source.bb.tetra.bbncht.get_dspacing() \n
		(for Uplink direction only) The 'Duplex Spacing' and 'Reverse Operation' parameters in the BNCH/T indicate the required
		uplink frequency with respect to the indicated downlink frequency. These parameters are defined in ETSI 300 392-2. \n
			:return: dspacing: DS0| DS1| DS2| DS3| DS4| DS5| DS6| DS7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:DSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.TetraDplxSpcing)

	def set_dspacing(self, dspacing: enums.TetraDplxSpcing) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:DSPacing \n
		Snippet: driver.source.bb.tetra.bbncht.set_dspacing(dspacing = enums.TetraDplxSpcing.DS0) \n
		(for Uplink direction only) The 'Duplex Spacing' and 'Reverse Operation' parameters in the BNCH/T indicate the required
		uplink frequency with respect to the indicated downlink frequency. These parameters are defined in ETSI 300 392-2. \n
			:param dspacing: DS0| DS1| DS2| DS3| DS4| DS5| DS6| DS7
		"""
		param = Conversions.enum_scalar_to_str(dspacing, enums.TetraDplxSpcing)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:DSPacing {param}')

	def get_ecorrection(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:ECORrection \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_ecorrection() \n
		Enables/disables error correction. \n
			:return: ecorrection: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:ECORrection?')
		return Conversions.str_to_bool(response)

	def set_ecorrection(self, ecorrection: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:ECORrection \n
		Snippet: driver.source.bb.tetra.bbncht.set_ecorrection(ecorrection = False) \n
		Enables/disables error correction. \n
			:param ecorrection: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ecorrection)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:ECORrection {param}')

	# noinspection PyTypeChecker
	def get_fband(self) -> enums.TetraFreqBand:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:FBANd \n
		Snippet: value: enums.TetraFreqBand = driver.source.bb.tetra.bbncht.get_fband() \n
		Sets the Frequency Band. This setting has an effect on the calculation of the transmission frequency. The Frequency Band
		Information is inserted only in the TETRA BSCH protocol channel. \n
			:return: fband: F100| F200| F300| F400| F500| F600| F700| F800| F900
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:FBANd?')
		return Conversions.str_to_scalar_enum(response, enums.TetraFreqBand)

	def set_fband(self, fband: enums.TetraFreqBand) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:FBANd \n
		Snippet: driver.source.bb.tetra.bbncht.set_fband(fband = enums.TetraFreqBand.F100) \n
		Sets the Frequency Band. This setting has an effect on the calculation of the transmission frequency. The Frequency Band
		Information is inserted only in the TETRA BSCH protocol channel. \n
			:param fband: F100| F200| F300| F400| F500| F600| F700| F800| F900
		"""
		param = Conversions.enum_scalar_to_str(fband, enums.TetraFreqBand)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:FBANd {param}')

	def get_fe_extension(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:FEEXtension \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_fe_extension() \n
		Enables/disables the frame 18 extension element, i.e. indicates whether an MS is allowed to receive downlink information
		on all slots of the frame 18. If extension is allowed, only MSs which are capable of receiving consecutive slots are able
		to perform this function. \n
			:return: fe_extension: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:FEEXtension?')
		return Conversions.str_to_bool(response)

	def set_fe_extension(self, fe_extension: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:FEEXtension \n
		Snippet: driver.source.bb.tetra.bbncht.set_fe_extension(fe_extension = False) \n
		Enables/disables the frame 18 extension element, i.e. indicates whether an MS is allowed to receive downlink information
		on all slots of the frame 18. If extension is allowed, only MSs which are capable of receiving consecutive slots are able
		to perform this function. \n
			:param fe_extension: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(fe_extension)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:FEEXtension {param}')

	def get_lback(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:LBACk \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_lback() \n
		Enables/disables loop back for test purposes. If enabled, the mobile station should set up a loop and return the data
		when requested by the Tx_burst_type. \n
			:return: lback: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:LBACk?')
		return Conversions.str_to_bool(response)

	def set_lback(self, lback: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:LBACk \n
		Snippet: driver.source.bb.tetra.bbncht.set_lback(lback = False) \n
		Enables/disables loop back for test purposes. If enabled, the mobile station should set up a loop and return the data
		when requested by the Tx_burst_type. \n
			:param lback: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(lback)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:LBACk {param}')

	def get_lentry(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:LENTry \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_lentry() \n
		Sets the value of the late entry supported information element, used to indicate to the MS whether or not late entry can
		be supported by the cell. \n
			:return: lentry: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:LENTry?')
		return Conversions.str_to_bool(response)

	def set_lentry(self, lentry: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:LENTry \n
		Snippet: driver.source.bb.tetra.bbncht.set_lentry(lentry = False) \n
		Sets the value of the late entry supported information element, used to indicate to the MS whether or not late entry can
		be supported by the cell. \n
			:param lentry: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(lentry)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:LENTry {param}')

	def get_mccode(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MCCode \n
		Snippet: value: int = driver.source.bb.tetra.bbncht.get_mccode() \n
		Sets the Mobile Country Code. The MCC is the number of the country in which the unit is operated. See Table 'Building of
		scrambling code' for information on how the scrambling code is calculated. \n
			:return: mccode: integer Range: 0 to 1023
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:MCCode?')
		return Conversions.str_to_int(response)

	def set_mccode(self, mccode: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MCCode \n
		Snippet: driver.source.bb.tetra.bbncht.set_mccode(mccode = 1) \n
		Sets the Mobile Country Code. The MCC is the number of the country in which the unit is operated. See Table 'Building of
		scrambling code' for information on how the scrambling code is calculated. \n
			:param mccode: integer Range: 0 to 1023
		"""
		param = Conversions.decimal_value_to_str(mccode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:MCCode {param}')

	def get_mc_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MCNumber \n
		Snippet: value: int = driver.source.bb.tetra.bbncht.get_mc_number() \n
		The 'Main Carrier Number' divides the TETRA band into carriers with a spacing as set with the parameter 'Carrier
		Bandwidth'. The range is 0 to 4095 (12 bits) . The Main Carrier Frequency is calculated as follow: Main Carrier Frequency,
		kHz = 'Main Carrier Number' * 'Carrier Bandwidth' \n
			:return: mc_number: integer Range: 0 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:MCNumber?')
		return Conversions.str_to_int(response)

	def set_mc_number(self, mc_number: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MCNumber \n
		Snippet: driver.source.bb.tetra.bbncht.set_mc_number(mc_number = 1) \n
		The 'Main Carrier Number' divides the TETRA band into carriers with a spacing as set with the parameter 'Carrier
		Bandwidth'. The range is 0 to 4095 (12 bits) . The Main Carrier Frequency is calculated as follow: Main Carrier Frequency,
		kHz = 'Main Carrier Number' * 'Carrier Bandwidth' \n
			:param mc_number: integer Range: 0 to 4095
		"""
		param = Conversions.decimal_value_to_str(mc_number)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:MCNumber {param}')

	def get_mncode(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MNCode \n
		Snippet: value: int = driver.source.bb.tetra.bbncht.get_mncode() \n
		Sets the Mobile Network Code (MNC) . The MNC is the number of the TETRA network operator. See Table 'Building of
		scrambling code' for information on how the scrambling code is calculated. \n
			:return: mncode: integer Range: 0 to 16383
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:MNCode?')
		return Conversions.str_to_int(response)

	def set_mncode(self, mncode: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MNCode \n
		Snippet: driver.source.bb.tetra.bbncht.set_mncode(mncode = 1) \n
		Sets the Mobile Network Code (MNC) . The MNC is the number of the TETRA network operator. See Table 'Building of
		scrambling code' for information on how the scrambling code is calculated. \n
			:param mncode: integer Range: 0 to 16383
		"""
		param = Conversions.decimal_value_to_str(mncode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:MNCode {param}')

	# noinspection PyTypeChecker
	def get_mtm_cell(self) -> enums.TetraTxPwr:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MTMCell \n
		Snippet: value: enums.TetraTxPwr = driver.source.bb.tetra.bbncht.get_mtm_cell() \n
		Sets the protocol information on the maximum transmission power for the mobile station. Allowed are values from 15 dBm to
		45 dBm in 5 dB steps. The MS_TXPWR_MAX_CELL paramer is used for cell selection and reselection, and for power adjustments. \n
			:return: mtm_cell: M15| M20| M25| M30| M35| M40| M45
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:MTMCell?')
		return Conversions.str_to_scalar_enum(response, enums.TetraTxPwr)

	def set_mtm_cell(self, mtm_cell: enums.TetraTxPwr) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:MTMCell \n
		Snippet: driver.source.bb.tetra.bbncht.set_mtm_cell(mtm_cell = enums.TetraTxPwr.M15) \n
		Sets the protocol information on the maximum transmission power for the mobile station. Allowed are values from 15 dBm to
		45 dBm in 5 dB steps. The MS_TXPWR_MAX_CELL paramer is used for cell selection and reselection, and for power adjustments. \n
			:param mtm_cell: M15| M20| M25| M30| M35| M40| M45
		"""
		param = Conversions.enum_scalar_to_str(mtm_cell, enums.TetraTxPwr)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:MTMCell {param}')

	# noinspection PyTypeChecker
	def get_offset(self) -> enums.TetraOffset:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:OFFSet \n
		Snippet: value: enums.TetraOffset = driver.source.bb.tetra.bbncht.get_offset() \n
		Set the 'Offset' to shifft the center frequency in the channel spacing. The allowed offsets are +6.25, 0,–6.25 and +12.50
		kHz. \n
			:return: offset: ZERO| P625| M625| P125
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:OFFSet?')
		return Conversions.str_to_scalar_enum(response, enums.TetraOffset)

	def set_offset(self, offset: enums.TetraOffset) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:OFFSet \n
		Snippet: driver.source.bb.tetra.bbncht.set_offset(offset = enums.TetraOffset.M625) \n
		Set the 'Offset' to shifft the center frequency in the channel spacing. The allowed offsets are +6.25, 0,–6.25 and +12.50
		kHz. \n
			:param offset: ZERO| P625| M625| P125
		"""
		param = Conversions.enum_scalar_to_str(offset, enums.TetraOffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:OFFSet {param}')

	def get_roperation(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:ROPeration \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_roperation() \n
		(for Uplink direction only) Enables/disables reverse operation. Reverse operation is used to fix the uplink frequency
		relative to the downlink frequency. In normal operation, the uplink frequency is lower than the downlink frequency and in
		reverse operation, the uplink frequency is higher than the downlink frequency. \n
			:return: roperation: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:ROPeration?')
		return Conversions.str_to_bool(response)

	def set_roperation(self, roperation: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:ROPeration \n
		Snippet: driver.source.bb.tetra.bbncht.set_roperation(roperation = False) \n
		(for Uplink direction only) Enables/disables reverse operation. Reverse operation is used to fix the uplink frequency
		relative to the downlink frequency. In normal operation, the uplink frequency is lower than the downlink frequency and in
		reverse operation, the uplink frequency is higher than the downlink frequency. \n
			:param roperation: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(roperation)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:ROPeration {param}')

	# noinspection PyTypeChecker
	def get_scode(self) -> enums.TetraSysCode:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:SCODe \n
		Snippet: value: enums.TetraSysCode = driver.source.bb.tetra.bbncht.get_scode() \n
		Indicate whether the system is a TETRA V+D system or whether this is a Direct Mode transmission. \n
			:return: scode: S0| S1| S2| S3| S4| S5| S6| S7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:SCODe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraSysCode)

	def set_scode(self, scode: enums.TetraSysCode) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:SCODe \n
		Snippet: driver.source.bb.tetra.bbncht.set_scode(scode = enums.TetraSysCode.S0) \n
		Indicate whether the system is a TETRA V+D system or whether this is a Direct Mode transmission. \n
			:param scode: S0| S1| S2| S3| S4| S5| S6| S7
		"""
		param = Conversions.enum_scalar_to_str(scode, enums.TetraSysCode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:SCODe {param}')

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.TetraShrngMode:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:SMODe \n
		Snippet: value: enums.TetraShrngMode = driver.source.bb.tetra.bbncht.get_smode() \n
		The sharing mode field indicates whether the BS is using continuous transmission, carrier sharing, MCCH sharing or
		traffic carrier sharing. \n
			:return: smode: CTRansmission| CSHaring| MSHaring| TCSHaring
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraShrngMode)

	def set_smode(self, smode: enums.TetraShrngMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:SMODe \n
		Snippet: driver.source.bb.tetra.bbncht.set_smode(smode = enums.TetraShrngMode.CSHaring) \n
		The sharing mode field indicates whether the BS is using continuous transmission, carrier sharing, MCCH sharing or
		traffic carrier sharing. \n
			:param smode: CTRansmission| CSHaring| MSHaring| TCSHaring
		"""
		param = Conversions.enum_scalar_to_str(smode, enums.TetraShrngMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:SMODe {param}')

	# noinspection PyTypeChecker
	def get_tb_type(self) -> enums.TetraTxBurstType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TBTYpe \n
		Snippet: value: enums.TetraTxBurstType = driver.source.bb.tetra.bbncht.get_tb_type() \n
		Sets the parameter Tx_burst_type and determines whether the MS under test transmit either a normal uplink burst or
		control uplink burst. \n
			:return: tb_type: NUB| CUB NUB The mobile station should transmit using normal uplink burst. CUB The mobile station should transmit using control uplink burst.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:TBTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.TetraTxBurstType)

	def set_tb_type(self, tb_type: enums.TetraTxBurstType) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TBTYpe \n
		Snippet: driver.source.bb.tetra.bbncht.set_tb_type(tb_type = enums.TetraTxBurstType.CUB) \n
		Sets the parameter Tx_burst_type and determines whether the MS under test transmit either a normal uplink burst or
		control uplink burst. \n
			:param tb_type: NUB| CUB NUB The mobile station should transmit using normal uplink burst. CUB The mobile station should transmit using control uplink burst.
		"""
		param = Conversions.enum_scalar_to_str(tb_type, enums.TetraTxBurstType)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:TBTYpe {param}')

	# noinspection PyTypeChecker
	def get_tr_frames(self) -> enums.TetraTsRsrvdFrm:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TRFRames \n
		Snippet: value: enums.TetraTsRsrvdFrm = driver.source.bb.tetra.bbncht.get_tr_frames() \n
		Determines the number of frames reserved over two multiframes period. The way this field is processed, depends on the
		selected [:SOURce<hw>]:BB:TETRa:BBNCht:SMODe. If MCCH sharing is indicated, the TS reserved frames field shall indicate
		which frames are reserved in this mode of operation. For the other values of sharing mode, the contents of the TS
		reserved frames field shall be ignored. \n
			:return: tr_frames: F1| F2| F3| F4| F6| F9| F12| F18
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:TRFRames?')
		return Conversions.str_to_scalar_enum(response, enums.TetraTsRsrvdFrm)

	def set_tr_frames(self, tr_frames: enums.TetraTsRsrvdFrm) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TRFRames \n
		Snippet: driver.source.bb.tetra.bbncht.set_tr_frames(tr_frames = enums.TetraTsRsrvdFrm.F1) \n
		Determines the number of frames reserved over two multiframes period. The way this field is processed, depends on the
		selected [:SOURce<hw>]:BB:TETRa:BBNCht:SMODe. If MCCH sharing is indicated, the TS reserved frames field shall indicate
		which frames are reserved in this mode of operation. For the other values of sharing mode, the contents of the TS
		reserved frames field shall be ignored. \n
			:param tr_frames: F1| F2| F3| F4| F6| F9| F12| F18
		"""
		param = Conversions.enum_scalar_to_str(tr_frames, enums.TetraTsRsrvdFrm)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:TRFRames {param}')

	# noinspection PyTypeChecker
	def get_ttb_type(self) -> enums.TetraBurstType:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TTBType \n
		Snippet: value: enums.TetraBurstType = driver.source.bb.tetra.bbncht.get_ttb_type() \n
		Sets the value of the special parameter T1_T4_Burst_Type, i.e. determines the logical channel the BS is expecting to
		receive. \n
			:return: ttb_type: T72F| T72S| SFD| BSHD| T24D| RSV1| RSV2| T72U| SFU| SSTCh| T24U| SSCH| RSV3| RSBurst| RSSBurst| TPTD| TPTU| T48D| T48U| TSCD| TSCU| T108| SPHD| SPHU| SPF| SQHU| SQU| SQD| SQRA
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:TTBType?')
		return Conversions.str_to_scalar_enum(response, enums.TetraBurstType)

	def set_ttb_type(self, ttb_type: enums.TetraBurstType) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TTBType \n
		Snippet: driver.source.bb.tetra.bbncht.set_ttb_type(ttb_type = enums.TetraBurstType.BSHD) \n
		Sets the value of the special parameter T1_T4_Burst_Type, i.e. determines the logical channel the BS is expecting to
		receive. \n
			:param ttb_type: T72F| T72S| SFD| BSHD| T24D| RSV1| RSV2| T72U| SFU| SSTCh| T24U| SSCH| RSV3| RSBurst| RSSBurst| TPTD| TPTU| T48D| T48U| TSCD| TSCU| T108| SPHD| SPHU| SPF| SQHU| SQU| SQD| SQRA
		"""
		param = Conversions.enum_scalar_to_str(ttb_type, enums.TetraBurstType)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:TTBType {param}')

	# noinspection PyTypeChecker
	def get_txon(self) -> enums.TetraTxOn:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TXON \n
		Snippet: value: enums.TetraTxOn = driver.source.bb.tetra.bbncht.get_txon() \n
		Determines the value of the Tx_on parameter, i.e. selects the test mode the MS operates in, 'Reception ON' or
		'Transmission ON'. This parameter is neccessary for the generation of test signal T1 or T4 transmitted by the test system. \n
			:return: txon: RON| TON RON The mobile station is requested to recept. TON The mobile station is requested to transmit.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:TXON?')
		return Conversions.str_to_scalar_enum(response, enums.TetraTxOn)

	def set_txon(self, txon: enums.TetraTxOn) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:TXON \n
		Snippet: driver.source.bb.tetra.bbncht.set_txon(txon = enums.TetraTxOn.RON) \n
		Determines the value of the Tx_on parameter, i.e. selects the test mode the MS operates in, 'Reception ON' or
		'Transmission ON'. This parameter is neccessary for the generation of test signal T1 or T4 transmitted by the test system. \n
			:param txon: RON| TON RON The mobile station is requested to recept. TON The mobile station is requested to transmit.
		"""
		param = Conversions.enum_scalar_to_str(txon, enums.TetraTxOn)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:TXON {param}')

	def get_updtx(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:UPDTx \n
		Snippet: value: bool = driver.source.bb.tetra.bbncht.get_updtx() \n
		The 'U-plane DTX' element indicates whether or not the BS supports discontinuous traffic transmission by the MS. \n
			:return: updtx: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:BBNCht:UPDTx?')
		return Conversions.str_to_bool(response)

	def set_updtx(self, updtx: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:BBNCht:UPDTx \n
		Snippet: driver.source.bb.tetra.bbncht.set_updtx(updtx = False) \n
		The 'U-plane DTX' element indicates whether or not the BS supports discontinuous traffic transmission by the MS. \n
			:param updtx: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(updtx)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:BBNCht:UPDTx {param}')
