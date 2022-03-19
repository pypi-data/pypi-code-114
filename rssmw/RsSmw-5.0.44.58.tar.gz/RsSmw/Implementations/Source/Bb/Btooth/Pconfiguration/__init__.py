from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconfiguration:
	"""Pconfiguration commands group definition. 23 total commands, 6 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pconfiguration", core, parent)

	@property
	def bdaLap(self):
		"""bdaLap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdaLap'):
			from .BdaLap import BdaLap
			self._bdaLap = BdaLap(self._core, self._cmd_group)
		return self._bdaLap

	@property
	def bdaNap(self):
		"""bdaNap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdaNap'):
			from .BdaNap import BdaNap
			self._bdaNap = BdaNap(self._core, self._cmd_group)
		return self._bdaNap

	@property
	def bdaUap(self):
		"""bdaUap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdaUap'):
			from .BdaUap import BdaUap
			self._bdaUap = BdaUap(self._core, self._cmd_group)
		return self._bdaUap

	@property
	def coDevice(self):
		"""coDevice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coDevice'):
			from .CoDevice import CoDevice
			self._coDevice = CoDevice(self._core, self._cmd_group)
		return self._coDevice

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def lfsWord(self):
		"""lfsWord commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lfsWord'):
			from .LfsWord import LfsWord
			self._lfsWord = LfsWord(self._core, self._cmd_group)
		return self._lfsWord

	# noinspection PyTypeChecker
	def get_acknowledgement(self) -> enums.BtoAckNldgmt:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:ACKNowledgement \n
		Snippet: value: enums.BtoAckNldgmt = driver.source.bb.btooth.pconfiguration.get_acknowledgement() \n
		Sets the ARQN bit of the packet header.. \n
			:return: acknowledgement: NAK| ACK NAK Request to retransmit the previous payload. ACK Previous payload has been received successfully.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:ACKNowledgement?')
		return Conversions.str_to_scalar_enum(response, enums.BtoAckNldgmt)

	def set_acknowledgement(self, acknowledgement: enums.BtoAckNldgmt) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:ACKNowledgement \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_acknowledgement(acknowledgement = enums.BtoAckNldgmt.ACK) \n
		Sets the ARQN bit of the packet header.. \n
			:param acknowledgement: NAK| ACK NAK Request to retransmit the previous payload. ACK Previous payload has been received successfully.
		"""
		param = Conversions.enum_scalar_to_str(acknowledgement, enums.BtoAckNldgmt)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:ACKNowledgement {param}')

	def get_dlength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DLENgth \n
		Snippet: value: int = driver.source.bb.btooth.pconfiguration.get_dlength() \n
		Sets the payload data length in bytes. \n
			:return: dlength: integer Range: 0 to depends on packet type
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DLENgth?')
		return Conversions.str_to_int(response)

	def set_dlength(self, dlength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DLENgth \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_dlength(dlength = 1) \n
		Sets the payload data length in bytes. \n
			:param dlength: integer Range: 0 to depends on packet type
		"""
		param = Conversions.decimal_value_to_str(dlength)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DLENgth {param}')

	# noinspection PyTypeChecker
	def get_dsf_packet(self) -> enums.BtoDataSourForPck:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DSFPacket \n
		Snippet: value: enums.BtoDataSourForPck = driver.source.bb.btooth.pconfiguration.get_dsf_packet() \n
		Selects the data source for the selected packet type. \n
			:return: dsf_packet: PEDit| ADATa PED Enables the 'Packet Editor'. All packet fields can be configured individually. ADAT Fills the generated packets with the selected data source. Useful if predefined data contents are loaded with a data list file or the data contents of the packet are not of interest.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DSFPacket?')
		return Conversions.str_to_scalar_enum(response, enums.BtoDataSourForPck)

	def set_dsf_packet(self, dsf_packet: enums.BtoDataSourForPck) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DSFPacket \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_dsf_packet(dsf_packet = enums.BtoDataSourForPck.ADATa) \n
		Selects the data source for the selected packet type. \n
			:param dsf_packet: PEDit| ADATa PED Enables the 'Packet Editor'. All packet fields can be configured individually. ADAT Fills the generated packets with the selected data source. Useful if predefined data contents are loaded with a data list file or the data contents of the packet are not of interest.
		"""
		param = Conversions.enum_scalar_to_str(dsf_packet, enums.BtoDataSourForPck)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DSFPacket {param}')

	def get_dwhitening(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DWHitening \n
		Snippet: value: bool = driver.source.bb.btooth.pconfiguration.get_dwhitening() \n
		Activates the 'Data Whitening'. \n
			:return: dwhitening: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DWHitening?')
		return Conversions.str_to_bool(response)

	def set_dwhitening(self, dwhitening: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:DWHitening \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_dwhitening(dwhitening = False) \n
		Activates the 'Data Whitening'. \n
			:param dwhitening: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dwhitening)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:DWHitening {param}')

	# noinspection PyTypeChecker
	def get_eir_packet_follows(self) -> enums.YesNoStatus:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:EIRPacketfollows \n
		Snippet: value: enums.YesNoStatus = driver.source.bb.btooth.pconfiguration.get_eir_packet_follows() \n
		Indicates that an extended inquiry response packet can follow. \n
			:return: eir_packet_follow: YES| NO YES Indicates that EIR packet follows. NO Indicates that EIR packet does not follow.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:EIRPacketfollows?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def set_eir_packet_follows(self, eir_packet_follow: enums.YesNoStatus) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:EIRPacketfollows \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_eir_packet_follows(eir_packet_follow = enums.YesNoStatus.NO) \n
		Indicates that an extended inquiry response packet can follow. \n
			:param eir_packet_follow: YES| NO YES Indicates that EIR packet follows. NO Indicates that EIR packet does not follow.
		"""
		param = Conversions.enum_scalar_to_str(eir_packet_follow, enums.YesNoStatus)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:EIRPacketfollows {param}')

	# noinspection PyTypeChecker
	def get_hf_control(self) -> enums.BtoFlowCtrl:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:HFControl \n
		Snippet: value: enums.BtoFlowCtrl = driver.source.bb.btooth.pconfiguration.get_hf_control() \n
		The command sets the FLOW bit in the header. This bit indicates start or stop of transmission of packets over the ACL
		logical transport. \n
			:return: hf_control: GO| STOP GO Allows the other devices to transmit new data. STOP Stops the other devices from transmitting data temporarily.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:HFControl?')
		return Conversions.str_to_scalar_enum(response, enums.BtoFlowCtrl)

	def set_hf_control(self, hf_control: enums.BtoFlowCtrl) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:HFControl \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_hf_control(hf_control = enums.BtoFlowCtrl.GO) \n
		The command sets the FLOW bit in the header. This bit indicates start or stop of transmission of packets over the ACL
		logical transport. \n
			:param hf_control: GO| STOP GO Allows the other devices to transmit new data. STOP Stops the other devices from transmitting data temporarily.
		"""
		param = Conversions.enum_scalar_to_str(hf_control, enums.BtoFlowCtrl)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:HFControl {param}')

	def get_lt_address(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:LTADdress \n
		Snippet: value: int = driver.source.bb.btooth.pconfiguration.get_lt_address() \n
		The command enters the logical transport address for the header. Each Peripheral active in a piconet is assigned a
		primary logical transport address (LT_ADDR) . The all-zero LT_ADDR is reserved for broadcast messages. \n
			:return: lt_address: integer Range: 0 to 7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:LTADdress?')
		return Conversions.str_to_int(response)

	def set_lt_address(self, lt_address: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:LTADdress \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_lt_address(lt_address = 1) \n
		The command enters the logical transport address for the header. Each Peripheral active in a piconet is assigned a
		primary logical transport address (LT_ADDR) . The all-zero LT_ADDR is reserved for broadcast messages. \n
			:param lt_address: integer Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(lt_address)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:LTADdress {param}')

	# noinspection PyTypeChecker
	def get_pf_control(self) -> enums.BtoFlowCtrl:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:PFControl \n
		Snippet: value: enums.BtoFlowCtrl = driver.source.bb.btooth.pconfiguration.get_pf_control() \n
		The command sets the FLOW bit in the payload (flow control per logical link) . \n
			:return: pf_control: GO| STOP GO Indicates the start of transmission of ACL packets after a new connection has been established. STOP Indicates the stop of transmission of ACL packets before an additional amount of payload data is sent.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:PFControl?')
		return Conversions.str_to_scalar_enum(response, enums.BtoFlowCtrl)

	def set_pf_control(self, pf_control: enums.BtoFlowCtrl) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:PFControl \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_pf_control(pf_control = enums.BtoFlowCtrl.GO) \n
		The command sets the FLOW bit in the payload (flow control per logical link) . \n
			:param pf_control: GO| STOP GO Indicates the start of transmission of ACL packets after a new connection has been established. STOP Indicates the stop of transmission of ACL packets before an additional amount of payload data is sent.
		"""
		param = Conversions.enum_scalar_to_str(pf_control, enums.BtoFlowCtrl)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:PFControl {param}')

	def get_plength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:PLENgth \n
		Snippet: value: int = driver.source.bb.btooth.pconfiguration.get_plength() \n
		Sets the packet length in symbols. \n
			:return: plength: integer Range: 1 to depends on packet type
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:PLENgth?')
		return Conversions.str_to_int(response)

	def set_plength(self, plength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:PLENgth \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_plength(plength = 1) \n
		Sets the packet length in symbols. \n
			:param plength: integer Range: 1 to depends on packet type
		"""
		param = Conversions.decimal_value_to_str(plength)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:PLENgth {param}')

	def get_slap(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:SLAP \n
		Snippet: value: bool = driver.source.bb.btooth.pconfiguration.get_slap() \n
		Activates synchronization of the lower address part (LAP) of the sync word and Bluetooth device address. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:SLAP?')
		return Conversions.str_to_bool(response)

	def set_slap(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:SLAP \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_slap(state = False) \n
		Activates synchronization of the lower address part (LAP) of the sync word and Bluetooth device address. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:SLAP {param}')

	def get_sns_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:SNSValue \n
		Snippet: value: int = driver.source.bb.btooth.pconfiguration.get_sns_value() \n
		Sets the start value of the header SEQN bit. The SEQN bit is present in the header to filter out retransmissions in the
		destination. The signal generator is altering this bit automatically on consecutive frames, if a sequence length of at
		least 2 frames is set. \n
			:return: sns_value: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:SNSValue?')
		return Conversions.str_to_int(response)

	def set_sns_value(self, sns_value: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:SNSValue \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_sns_value(sns_value = 1) \n
		Sets the start value of the header SEQN bit. The SEQN bit is present in the header to filter out retransmissions in the
		destination. The signal generator is altering this bit automatically on consecutive frames, if a sequence length of at
		least 2 frames is set. \n
			:param sns_value: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(sns_value)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:SNSValue {param}')

	# noinspection PyTypeChecker
	def get_sr_mode(self) -> enums.BtoScanReMode:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:SRMode \n
		Snippet: value: enums.BtoScanReMode = driver.source.bb.btooth.pconfiguration.get_sr_mode() \n
		The command indicates the interval between two consecutive page scan windows, determines the behavior of the paging
		device. \n
			:return: sr_mode: R0| R1| R2 R0 The scan interval is equal to the scan window T w page scan (continuous nscan) and maximal 1.28s. R1 The scan interval is maximal 1.28s. R2 The scan interval is maximal 2.56s.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:SRMode?')
		return Conversions.str_to_scalar_enum(response, enums.BtoScanReMode)

	def set_sr_mode(self, sr_mode: enums.BtoScanReMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:SRMode \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_sr_mode(sr_mode = enums.BtoScanReMode.R0) \n
		The command indicates the interval between two consecutive page scan windows, determines the behavior of the paging
		device. \n
			:param sr_mode: R0| R1| R2 R0 The scan interval is equal to the scan window T w page scan (continuous nscan) and maximal 1.28s. R1 The scan interval is maximal 1.28s. R2 The scan interval is maximal 2.56s.
		"""
		param = Conversions.enum_scalar_to_str(sr_mode, enums.BtoScanReMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:SRMode {param}')

	# noinspection PyTypeChecker
	def get_vdata(self) -> enums.DataSourceB:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:VDATa \n
		Snippet: value: enums.DataSourceB = driver.source.bb.btooth.pconfiguration.get_vdata() \n
		Selects the data source for the voice field. \n
			:return: vdata: ALL0| ALL1| PATTern| PN09| PN11| PN15| PN16| PN20| PN21| PN23| DLISt
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:PCONfiguration:VDATa?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceB)

	def set_vdata(self, vdata: enums.DataSourceB) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:VDATa \n
		Snippet: driver.source.bb.btooth.pconfiguration.set_vdata(vdata = enums.DataSourceB.ALL0) \n
		Selects the data source for the voice field. \n
			:param vdata: ALL0| ALL1| PATTern| PN09| PN11| PN15| PN16| PN20| PN21| PN23| DLISt
		"""
		param = Conversions.enum_scalar_to_str(vdata, enums.DataSourceB)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:VDATa {param}')

	def clone(self) -> 'Pconfiguration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pconfiguration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
