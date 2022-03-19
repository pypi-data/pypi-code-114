from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MacHeader:
	"""MacHeader commands group definition. 31 total commands, 0 Subgroups, 31 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("macHeader", core, parent)

	def get_ar(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:AR \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_ar() \n
		Sets the bit in the AR field. \n
			:return: ar: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:AR?')
		return Conversions.str_to_int(response)

	def set_ar(self, ar: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:AR \n
		Snippet: driver.source.bb.huwb.macHeader.set_ar(ar = 1) \n
		Sets the bit in the AR field. \n
			:param ar: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(ar)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:AR {param}')

	def get_ctrl(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:CTRL \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_ctrl() \n
		Sets the input value of the frame control field. The value is an 8-bit or 16-bit value in hexadecimal representation. \n
			:return: frame_control: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:CTRL?')
		return Conversions.str_to_int(response)

	def set_ctrl(self, frame_control: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:CTRL \n
		Snippet: driver.source.bb.huwb.macHeader.set_ctrl(frame_control = 1) \n
		Sets the input value of the frame control field. The value is an 8-bit or 16-bit value in hexadecimal representation. \n
			:param frame_control: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(frame_control)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:CTRL {param}')

	def get_dad_2(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DAD2 \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_dad_2() \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:return: dest_addr_2: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:DAD2?')
		return Conversions.str_to_int(response)

	def set_dad_2(self, dest_addr_2: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DAD2 \n
		Snippet: driver.source.bb.huwb.macHeader.set_dad_2(dest_addr_2 = 1) \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:param dest_addr_2: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(dest_addr_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:DAD2 {param}')

	def get_dad_3(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DAD3 \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_dad_3() \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:return: dest_addr_3: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:DAD3?')
		return Conversions.str_to_int(response)

	def set_dad_3(self, dest_addr_3: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DAD3 \n
		Snippet: driver.source.bb.huwb.macHeader.set_dad_3(dest_addr_3 = 1) \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:param dest_addr_3: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(dest_addr_3)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:DAD3 {param}')

	def get_dad_4(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DAD4 \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_dad_4() \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:return: dest_addr_4: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:DAD4?')
		return Conversions.str_to_int(response)

	def set_dad_4(self, dest_addr_4: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DAD4 \n
		Snippet: driver.source.bb.huwb.macHeader.set_dad_4(dest_addr_4 = 1) \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:param dest_addr_4: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(dest_addr_4)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:DAD4 {param}')

	def get_dadd(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DADD \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_dadd() \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:return: destination_addr: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:DADD?')
		return Conversions.str_to_int(response)

	def set_dadd(self, destination_addr: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DADD \n
		Snippet: driver.source.bb.huwb.macHeader.set_dadd(destination_addr = 1) \n
		DADD requires destination address length of two or eight octets. DAD2, DAD3 and DAD4 require destination address length
		of eight octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LDADdress. Sets the first, second, third and fourth input value of
		the destination address field. \n
			:param destination_addr: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(destination_addr)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:DADD {param}')

	def get_dad_mode(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DADMode \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_dad_mode() \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets bits of the destination
		addressing mode. \n
			:return: dest_addr_mode: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:DADMode?')
		return Conversions.str_to_int(response)

	def set_dad_mode(self, dest_addr_mode: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DADMode \n
		Snippet: driver.source.bb.huwb.macHeader.set_dad_mode(dest_addr_mode = 1) \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets bits of the destination
		addressing mode. \n
			:param dest_addr_mode: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(dest_addr_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:DADMode {param}')

	def get_dpan_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DPANid \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_dpan_id() \n
		Sets the length and the input value of the destination PAN ID field. \n
			:return: destination_pan_id: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:DPANid?')
		return Conversions.str_to_int(response)

	def set_dpan_id(self, destination_pan_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:DPANid \n
		Snippet: driver.source.bb.huwb.macHeader.set_dpan_id(destination_pan_id = 1) \n
		Sets the length and the input value of the destination PAN ID field. \n
			:param destination_pan_id: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(destination_pan_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:DPANid {param}')

	def get_fpending(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:FPENding \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_fpending() \n
		Sets the bit in the frame pending field. \n
			:return: frame_pending: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:FPENding?')
		return Conversions.str_to_int(response)

	def set_fpending(self, frame_pending: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:FPENding \n
		Snippet: driver.source.bb.huwb.macHeader.set_fpending(frame_pending = 1) \n
		Sets the bit in the frame pending field. \n
			:param frame_pending: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(frame_pending)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:FPENding {param}')

	def get_ftype(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:FTYPe \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_ftype() \n
		Sets the bits in the frame type field. The value is a 3-bit value. \n
			:return: frame_type: integer Range: 0 to 7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:FTYPe?')
		return Conversions.str_to_int(response)

	def set_ftype(self, frame_type: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:FTYPe \n
		Snippet: driver.source.bb.huwb.macHeader.set_ftype(frame_type = 1) \n
		Sets the bits in the frame type field. The value is a 3-bit value. \n
			:param frame_type: integer Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(frame_type)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:FTYPe {param}')

	def get_fversion(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:FVERsion \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_fversion() \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bits in the frame
		version field. The value is a 2-bit value. \n
			:return: frame_version: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:FVERsion?')
		return Conversions.str_to_int(response)

	def set_fversion(self, frame_version: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:FVERsion \n
		Snippet: driver.source.bb.huwb.macHeader.set_fversion(frame_version = 1) \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bits in the frame
		version field. The value is a 2-bit value. \n
			:param frame_version: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(frame_version)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:FVERsion {param}')

	def get_ie_present(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:IEPResent \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_ie_present() \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bit in the
		information element (IE) present field. \n
			:return: ie_present: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:IEPResent?')
		return Conversions.str_to_int(response)

	def set_ie_present(self, ie_present: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:IEPResent \n
		Snippet: driver.source.bb.huwb.macHeader.set_ie_present(ie_present = 1) \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bit in the
		information element (IE) present field. \n
			:param ie_present: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(ie_present)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:IEPResent {param}')

	# noinspection PyTypeChecker
	def get_ld_address(self) -> enums.HrpUwbMacLenAddress:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LDADdress \n
		Snippet: value: enums.HrpUwbMacLenAddress = driver.source.bb.huwb.macHeader.get_ld_address() \n
		Sets the length of the destination address field. You can set lengths of zero octets, two octets or eight octets. \n
			:return: len_dest_addr: L0| L2| L8 L0 Sets destination address length to zero octets. L2 Sets destination address length to two octets. L8 Sets destination address length to eight octets.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:LDADdress?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMacLenAddress)

	def set_ld_address(self, len_dest_addr: enums.HrpUwbMacLenAddress) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LDADdress \n
		Snippet: driver.source.bb.huwb.macHeader.set_ld_address(len_dest_addr = enums.HrpUwbMacLenAddress.L0) \n
		Sets the length of the destination address field. You can set lengths of zero octets, two octets or eight octets. \n
			:param len_dest_addr: L0| L2| L8 L0 Sets destination address length to zero octets. L2 Sets destination address length to two octets. L8 Sets destination address length to eight octets.
		"""
		param = Conversions.enum_scalar_to_str(len_dest_addr, enums.HrpUwbMacLenAddress)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:LDADdress {param}')

	# noinspection PyTypeChecker
	def get_lde_pan_id(self) -> enums.HrpUwbMacLenPanId:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LDEPanid \n
		Snippet: value: enums.HrpUwbMacLenPanId = driver.source.bb.huwb.macHeader.get_lde_pan_id() \n
		Sets the length of the destination PAN ID field. You can set lengths of zero octets or two octets. \n
			:return: len_dest_pan_id: L0| L2 L0 Sets destination PAN ID length to zero octets. L2 Sets destination PAN ID length to two octets.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:LDEPanid?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMacLenPanId)

	def set_lde_pan_id(self, len_dest_pan_id: enums.HrpUwbMacLenPanId) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LDEPanid \n
		Snippet: driver.source.bb.huwb.macHeader.set_lde_pan_id(len_dest_pan_id = enums.HrpUwbMacLenPanId.L0) \n
		Sets the length of the destination PAN ID field. You can set lengths of zero octets or two octets. \n
			:param len_dest_pan_id: L0| L2 L0 Sets destination PAN ID length to zero octets. L2 Sets destination PAN ID length to two octets.
		"""
		param = Conversions.enum_scalar_to_str(len_dest_pan_id, enums.HrpUwbMacLenPanId)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:LDEPanid {param}')

	# noinspection PyTypeChecker
	def get_lfr_control(self) -> enums.HrpUwbMacLenFrameControl:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LFRControl \n
		Snippet: value: enums.HrpUwbMacLenFrameControl = driver.source.bb.huwb.macHeader.get_lfr_control() \n
		Sets the length of the frame control field. You can set lengths of one octet or two octets. \n
			:return: len_frame_control: L1| L2 L1 Sets frame control length to one octet. L2 Sets frame control length to two octets.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:LFRControl?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMacLenFrameControl)

	def set_lfr_control(self, len_frame_control: enums.HrpUwbMacLenFrameControl) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LFRControl \n
		Snippet: driver.source.bb.huwb.macHeader.set_lfr_control(len_frame_control = enums.HrpUwbMacLenFrameControl.L1) \n
		Sets the length of the frame control field. You can set lengths of one octet or two octets. \n
			:param len_frame_control: L1| L2 L1 Sets frame control length to one octet. L2 Sets frame control length to two octets.
		"""
		param = Conversions.enum_scalar_to_str(len_frame_control, enums.HrpUwbMacLenFrameControl)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:LFRControl {param}')

	# noinspection PyTypeChecker
	def get_ls_address(self) -> enums.HrpUwbMacLenAddress:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LSADdress \n
		Snippet: value: enums.HrpUwbMacLenAddress = driver.source.bb.huwb.macHeader.get_ls_address() \n
		Sets the length of the source address field. You can set lengths of zero octets, two octets or eight octets. \n
			:return: len_src_address: L0| L2| L8 L0 Sets source address length to zero octets. L2 Sets source address length to two octets. L8 Sets source address length to eight octets.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:LSADdress?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMacLenAddress)

	def set_ls_address(self, len_src_address: enums.HrpUwbMacLenAddress) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LSADdress \n
		Snippet: driver.source.bb.huwb.macHeader.set_ls_address(len_src_address = enums.HrpUwbMacLenAddress.L0) \n
		Sets the length of the source address field. You can set lengths of zero octets, two octets or eight octets. \n
			:param len_src_address: L0| L2| L8 L0 Sets source address length to zero octets. L2 Sets source address length to two octets. L8 Sets source address length to eight octets.
		"""
		param = Conversions.enum_scalar_to_str(len_src_address, enums.HrpUwbMacLenAddress)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:LSADdress {param}')

	# noinspection PyTypeChecker
	def get_lseq_number(self) -> enums.HrpUwbMacLenSeqNumber:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LSEQnumber \n
		Snippet: value: enums.HrpUwbMacLenSeqNumber = driver.source.bb.huwb.macHeader.get_lseq_number() \n
		Sets the length of the sequence number field. You can set zero octets or one octet. \n
			:return: len_seq_number: L0| L1 L0 Sets the sequence number length to zero octets. L1 Sets the sequence number length to one octet.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:LSEQnumber?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMacLenSeqNumber)

	def set_lseq_number(self, len_seq_number: enums.HrpUwbMacLenSeqNumber) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LSEQnumber \n
		Snippet: driver.source.bb.huwb.macHeader.set_lseq_number(len_seq_number = enums.HrpUwbMacLenSeqNumber.L0) \n
		Sets the length of the sequence number field. You can set zero octets or one octet. \n
			:param len_seq_number: L0| L1 L0 Sets the sequence number length to zero octets. L1 Sets the sequence number length to one octet.
		"""
		param = Conversions.enum_scalar_to_str(len_seq_number, enums.HrpUwbMacLenSeqNumber)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:LSEQnumber {param}')

	# noinspection PyTypeChecker
	def get_lso_pan_id(self) -> enums.HrpUwbMacLenPanId:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LSOPanid \n
		Snippet: value: enums.HrpUwbMacLenPanId = driver.source.bb.huwb.macHeader.get_lso_pan_id() \n
		Sets the length of the source PAN ID field. You can set lengths of zero octets or two octets. \n
			:return: len_source_pan_id: L0| L2 L0 Sets source PAN ID length to zero octets. L2 Sets source PAN ID length to two octets.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:LSOPanid?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMacLenPanId)

	def set_lso_pan_id(self, len_source_pan_id: enums.HrpUwbMacLenPanId) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:LSOPanid \n
		Snippet: driver.source.bb.huwb.macHeader.set_lso_pan_id(len_source_pan_id = enums.HrpUwbMacLenPanId.L0) \n
		Sets the length of the source PAN ID field. You can set lengths of zero octets or two octets. \n
			:param len_source_pan_id: L0| L2 L0 Sets source PAN ID length to zero octets. L2 Sets source PAN ID length to two octets.
		"""
		param = Conversions.enum_scalar_to_str(len_source_pan_id, enums.HrpUwbMacLenPanId)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:LSOPanid {param}')

	def get_pid_comp(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:PIDComp \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_pid_comp() \n
		Sets the bit in the PAN ID compression field. \n
			:return: pan_id_compress: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:PIDComp?')
		return Conversions.str_to_int(response)

	def set_pid_comp(self, pan_id_compress: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:PIDComp \n
		Snippet: driver.source.bb.huwb.macHeader.set_pid_comp(pan_id_compress = 1) \n
		Sets the bit in the PAN ID compression field. \n
			:param pan_id_compress: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(pan_id_compress)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:PIDComp {param}')

	def get_reserved(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:REServed \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_reserved() \n
		Sets a reserved bit for future use. \n
			:return: reserved: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:REServed?')
		return Conversions.str_to_int(response)

	def set_reserved(self, reserved: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:REServed \n
		Snippet: driver.source.bb.huwb.macHeader.set_reserved(reserved = 1) \n
		Sets a reserved bit for future use. \n
			:param reserved: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(reserved)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:REServed {param}')

	def get_sad_2(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SAD2 \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_sad_2() \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:return: source_address_2: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SAD2?')
		return Conversions.str_to_int(response)

	def set_sad_2(self, source_address_2: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SAD2 \n
		Snippet: driver.source.bb.huwb.macHeader.set_sad_2(source_address_2 = 1) \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:param source_address_2: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(source_address_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SAD2 {param}')

	def get_sad_3(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SAD3 \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_sad_3() \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:return: source_address_3: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SAD3?')
		return Conversions.str_to_int(response)

	def set_sad_3(self, source_address_3: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SAD3 \n
		Snippet: driver.source.bb.huwb.macHeader.set_sad_3(source_address_3 = 1) \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:param source_address_3: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(source_address_3)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SAD3 {param}')

	def get_sad_4(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SAD4 \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_sad_4() \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:return: source_address_4: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SAD4?')
		return Conversions.str_to_int(response)

	def set_sad_4(self, source_address_4: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SAD4 \n
		Snippet: driver.source.bb.huwb.macHeader.set_sad_4(source_address_4 = 1) \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:param source_address_4: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(source_address_4)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SAD4 {param}')

	def get_sadd(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SADD \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_sadd() \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:return: source_address: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SADD?')
		return Conversions.str_to_int(response)

	def set_sadd(self, source_address: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SADD \n
		Snippet: driver.source.bb.huwb.macHeader.set_sadd(source_address = 1) \n
		SADD requires source address length of two or eight octets. SAD2, SAD3 and SAD4 require source address lengths of eight
		octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LSADdress. Sets the first, second, third and fourth input value of the source
		address field. \n
			:param source_address: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(source_address)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SADD {param}')

	def get_sad_mode(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SADMode \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_sad_mode() \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bits in the source
		addressing mode field. The value is a 2-bit value. \n
			:return: src_addr_mode: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SADMode?')
		return Conversions.str_to_int(response)

	def set_sad_mode(self, src_addr_mode: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SADMode \n
		Snippet: driver.source.bb.huwb.macHeader.set_sad_mode(src_addr_mode = 1) \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bits in the source
		addressing mode field. The value is a 2-bit value. \n
			:param src_addr_mode: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(src_addr_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SADMode {param}')

	def get_se_enabled(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SEENabled \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_se_enabled() \n
		Sets the bit in the security enabled field. \n
			:return: security_enabled: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SEENabled?')
		return Conversions.str_to_int(response)

	def set_se_enabled(self, security_enabled: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SEENabled \n
		Snippet: driver.source.bb.huwb.macHeader.set_se_enabled(security_enabled = 1) \n
		Sets the bit in the security enabled field. \n
			:param security_enabled: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(security_enabled)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SEENabled {param}')

	def get_sen_supp(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SENSupp \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_sen_supp() \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bit in the sequence
		number suppression field. \n
			:return: seq_numb_suppr: integer Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SENSupp?')
		return Conversions.str_to_int(response)

	def set_sen_supp(self, seq_numb_suppr: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SENSupp \n
		Snippet: driver.source.bb.huwb.macHeader.set_sen_supp(seq_numb_suppr = 1) \n
		Requires frame control length of two octets. See [:SOURce<hw>]:BB:HUWB:MACHeader:LFRControl. Sets the bit in the sequence
		number suppression field. \n
			:param seq_numb_suppr: integer Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(seq_numb_suppr)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SENSupp {param}')

	def get_seq_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SEQNumber \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_seq_number() \n
		No command help available \n
			:return: sequence_number: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SEQNumber?')
		return Conversions.str_to_int(response)

	def set_seq_number(self, sequence_number: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SEQNumber \n
		Snippet: driver.source.bb.huwb.macHeader.set_seq_number(sequence_number = 1) \n
		No command help available \n
			:param sequence_number: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(sequence_number)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SEQNumber {param}')

	def get_span_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SPANid \n
		Snippet: value: int = driver.source.bb.huwb.macHeader.get_span_id() \n
		Sets the input value of the source PAN ID field. The value is a 16-bit value in hexadecimal representation. \n
			:return: source_pan_id: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:SPANid?')
		return Conversions.str_to_int(response)

	def set_span_id(self, source_pan_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:SPANid \n
		Snippet: driver.source.bb.huwb.macHeader.set_span_id(source_pan_id = 1) \n
		Sets the input value of the source PAN ID field. The value is a 16-bit value in hexadecimal representation. \n
			:param source_pan_id: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(source_pan_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:SPANid {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:STATe \n
		Snippet: value: bool = driver.source.bb.huwb.macHeader.get_state() \n
		Activates or deactivates MAC header information. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:STATe \n
		Snippet: driver.source.bb.huwb.macHeader.set_state(state = False) \n
		Activates or deactivates MAC header information. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:MACHeader:STATe {param}')

	def get_string(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:HUWB:MACHeader:STRing \n
		Snippet: value: str = driver.source.bb.huwb.macHeader.get_string() \n
		Queries the length of the MAC header and the MAC address in hexadecimal format. \n
			:return: string: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:MACHeader:STRing?')
		return trim_str_response(response)
