# mu32.core.py python program interface for MegaMicro Mu32 transceiver 
#
# Copyright (c) 2022 Distalsense
# Author: bruno.gas@distalsense.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Mu32 documentation is available on https://distalsense.io
See documentation on usb device programming with libusb on https://pypi.org/project/libusb1/1.3.0/#documentation
Examples are available on https://github.com/vpelletier/python-libusb1

Please, note that the following packages should be installed before using this program:
	> pip install libusb1
"""


__VERSION__ = 1.0

import sys
import logging
import libusb1
import usb1
import time
from ctypes import byref, sizeof, create_string_buffer, CFUNCTYPE
import numpy as np
from math import ceil as ceil
import queue

from .log import mu32log
from .exception import Mu32Exception

MU_BEAMS_NUMBER					= 4
MU_BEAM_MEMS_NUMBER				= 8
MU_ANALOG_CHANNELS				= 4
MU_LOGIC_CHANNELS				= 4
MU_USB2_BUS_ADDRESS				= 0x82
MU_USB3_BUS_ADDRESS				= 0x81
MU_VENDOR_ID					= 0xFE27
MU_VENDOR_PRODUCT				= 0xAC03

MU_DEFAULT_CLOCKDIV				= 0x09									# Default internal acquisition clock value
MU_DEFAULT_TIME_ACTIVATION		= 1										# Wainting time after MEMs powering in seconds
MU_DEFAULT_PACKET_SIZE			= 512*1024
MU_DEFAULT_PACKET_NUMBER		= 0
MU_DEFAULT_TIMEOUT				= 1000
MU_DEFAULT_DATATYPE				= "int32"								# Default receiver incoming data type ("int32" or "float32") 
MU_DEFAULT_ACTIVATED_MEMS		= (0, )									# Default activated MEMs
MU_DEFAULT_SAMPLING_FREQUENCY	= 500000 / ( MU_DEFAULT_CLOCKDIV + 1 )	# Default sampling frequency
MU_DEFAULT_ACTIVATED_ANALOG		= []									# Default activated analog channels
MU_DEFAULT_ACTIVATED_COUNTER	= True									# Counter channel activation flag
MU_DEFAULT_ACTIVATED_STATUS		= False									# Status channel activation flag
MU_DEFAULT_COUNTER_SKIPPING		= True									# Counter channel blocking 


LIBUSB_RECIPIENT_DEVICE			= 0x00
LIBUSB_REQUEST_TYPE_VENDOR		= 0x40
LIBUSB_ENDPOINT_OUT				= 0x00
LIBUSB_DEFAULT_TIMEOUT			= 1000

MU_CMD_ACTIVE					= b'\x05'
MU_DEFAULT_BUFFERS_NUMBER		= 8											# USB transfer buffer number
MU_TRANSFER_DATAWORDS_SIZE		= 4											# 
MU_TRANSFER_DATABYTES_SIZE		= MU_TRANSFER_DATAWORDS_SIZE * 8			# buffer length in bytes
MU_DEFAULT_BUFFER_LENGTH		= 512										# buffer length in samples number to be received by each microphone
MU_DEFAULT_DURATION				= 1											# Default acquisition time
MU_MAX_RETRY_ATTEMPT			= 5											# Maximal reset attempts when rebooting FX3 USB adapter
MU_TRANSFER_TIMEOUT				= 1000										# Waiting time of inconming receiver signals before acquisition is stoped

MU_MEMS_UQUANTIZATION			= 24										# MEMs unsigned quantization 
MU_MEMS_QUANTIZATION			= MU_MEMS_UQUANTIZATION - 1					# MEMs signed quantization 
MU_MEMS_AMPLITUDE				= 2**MU_MEMS_QUANTIZATION					# MEMs maximal amlitude value for "int32" data type
MU_MEMS_SENSIBILITY				= 1/(MU_MEMS_AMPLITUDE*10**(-26/20)/3.17)	# MEMs sensibility factor (-26dBFS for 104 dB that is 3.17 Pa)


class MegaMicro:
	pass

class Mu32( MegaMicro ):

	def __init__( self ):
		"""
		Set default values
		"""
		self._signal_q = queue.Queue()
		self._mems = MU_DEFAULT_ACTIVATED_MEMS
		self._mems_number = len( self._mems )
		self._analogs = MU_DEFAULT_ACTIVATED_ANALOG
		self._analogs_number = len( self._analogs )
		self._counter = MU_DEFAULT_ACTIVATED_COUNTER
		self._counter_skip = MU_DEFAULT_COUNTER_SKIPPING
		self._status = MU_DEFAULT_ACTIVATED_STATUS
		self._channels_number = self._mems_number + self._analogs_number + self._counter + self._status
		self._clockdiv = MU_DEFAULT_CLOCKDIV
		self._sampling_frequency = 500000 / ( MU_DEFAULT_CLOCKDIV + 1 )
		self._buffer_length = MU_DEFAULT_BUFFER_LENGTH
		self._buffers_number = MU_DEFAULT_BUFFERS_NUMBER
		self._duration = MU_DEFAULT_DURATION
		self._transfers_count = int( ( MU_DEFAULT_DURATION * ( 500000 / ( MU_DEFAULT_CLOCKDIV + 1 ) ) )//MU_DEFAULT_BUFFER_LENGTH )
		self._buffer_words_length = self._channels_number*self._buffer_length
		self._datatype = MU_DEFAULT_DATATYPE
		self._callback_fn = None
		self._transfer_index = 0
		self._recording = False
		self._restart_request = False
		self._restart_attempt = 0
		self._counter_state = 0
		self._previous_counter_state = 0

	def __del__( self ):
		mu32log.info( '-'*20 )
		mu32log.info('Mu32: end')

	@property
	def signal_q( self ):
		return self._signal_q

	@property
	def mems( self ):
		return self._mems

	@property
	def mems_number( self ):
		return self._mems_number

	@property
	def analogs( self ):
		return self._analogs

	@property
	def analogs_number( self ):
		return self._analogs_number

	@property
	def counter( self ):
		return self._counter

	@property
	def counter_skip( self ):
		return self._counter_skip

	@property
	def status( self ):
		return self._status

	@property
	def channels_number( self ):
		return self._channels_number

	@property
	def clockdiv( self ):
		return self._clockdiv

	@property
	def sampling_frequency( self ):
		return self._sampling_frequency

	@property
	def buffer_length( self ):
		return self._buffer_length

	@property
	def buffers_number( self ):
		return self._buffers_number

	@property
	def duration( self ):
		return self._duration

	@property
	def transfers_count( self ):
		return self._transfers_count

	@property
	def datatype( self ):
		return self._datatype

	@property
	def sensibility( self ):
		return MU_MEMS_SENSIBILITY

	def check_usb( self, vendor_id, vendor_pr, verbose=True ):
		"""
		check for Mu32 usb plug in verbose mode off
		"""
		if verbose==False:
			with usb1.USBContext() as context:
				handle = context.openByVendorIDAndProductID( 
					vendor_id,
					vendor_pr,
					skip_on_error=True,
				)
				if handle is None:
					raise Mu32Exception( 'Mu32 USB3 device is not present or user is not allowed to access device' )

				try:
					with handle.claimInterface( 0 ):
						pass
				except Exception as e:	
					raise Mu32Exception( f"Mu32 USB3 device buzy: cannot claim it: {e}" )

			return

		"""
		check for Mu32 usb plug in verbose mode on
		"""
		mu32log.info('Mu32::check_usb')

		Mu32_device = None
		mu32log.info( 'found following devices:' )
		with usb1.USBContext() as context:
			mu32log.info( '-'*20 )
			for device in context.getDeviceIterator( skip_on_error=True ):
				mu32log.info( 'ID %04x:%04x' % (device.getVendorID(), device.getProductID()), '->'.join(str(x) for x in ['Bus %03i' % (device.getBusNumber(), )] + device.getPortNumberList()), 'Device', device.getDeviceAddress() )
				if device.getVendorID() == vendor_id and device.getProductID() == vendor_pr:
					Mu32_device = device
			mu32log.info( '-'*20 )
			if Mu32_device is None:
				raise Mu32Exception( 'Mu32 USB3 device is not present or user is not allowed to access device' )
			else:
				mu32log.info( 'found MegaMicro device %04x:%04x ' % ( Mu32_device.getVendorID(), Mu32_device.getProductID() ) )

			"""
			open Usb device and claims interface
			"""	
			handle = context.openByVendorIDAndProductID( 
				vendor_id,
				vendor_pr,
				skip_on_error=True,
			)

			if handle is None:
				raise Mu32Exception( 'Mu32 USB3 device is not present or user is not allowed to access device' )

			try:
				with handle.claimInterface( 0 ):
					pass
			except Exception as e:	
				mu32log.info( f"Mu32 USB3 device buzy: cannot claim it: {e}" )
			
			mu32log.info( '-'*20 )
			mu32log.info( 'Found following device characteristics :' )
			mu32log.info( '  Bus number: ', Mu32_device.getBusNumber() )
			mu32log.info( '  ports number: ', Mu32_device.getPortNumber() )
			mu32log.info( '  device address: ', Mu32_device.getDeviceAddress() )
			deviceSpeed =  Mu32_device.getDeviceSpeed()
			if deviceSpeed  == libusb1.LIBUSB_SPEED_LOW:
				mu32log.info( '  device speed:  [LOW SPEED] (The OS doesn\'t report or know the device speed)' )
			elif deviceSpeed == libusb1.LIBUSB_SPEED_FULL:
				mu32log.info( '  device speed:  [FULL SPEED] (The device is operating at low speed (1.5MBit/s))' )
			elif deviceSpeed == libusb1.LIBUSB_SPEED_HIGH:
				mu32log.info( '  device speed:  [HIGH SPEED] (The device is operating at full speed (12MBit/s))' )
			elif deviceSpeed == libusb1.LIBUSB_SPEED_SUPER:
				mu32log.info( '  device speed:  [SUPER SPEED] (The device is operating at high speed (480MBit/s))' )
			elif deviceSpeed == libusb1.LIBUSB_SPEED_SUPER_PLUS:
				mu32log.info( '  device speed:  [SUPER PLUS SPEED] (The device is operating at super speed (5000MBit/s))' )
			elif deviceSpeed == libusb1.LIBUSB_SPEED_UNKNOWN:
				mu32log.info( '  device speed:  [LIBUSB_SPEED_UNKNOWN] (The device is operating at unknown speed)' )
			else:
				mu32log.info( '  device speed:  [?] (The device is operating at unknown speed)' )
			mu32log.info( '-'*20 )


	def ctrlWrite( self, handle, request, data, time_out=LIBUSB_DEFAULT_TIMEOUT ):
		"""
		Send a write command tp Mu32 FPGA through the usb interface
		"""
		ndata = handle.controlWrite(
						# command type
			LIBUSB_RECIPIENT_DEVICE | LIBUSB_REQUEST_TYPE_VENDOR | LIBUSB_ENDPOINT_OUT,
			request, 	# command
			0,			# command parameter value
			0,			# index
			data,		# data to send 
			time_out 
		)
		if ndata != sizeof( data ):
			mu32log.warning( 'Mu32::ctrlWrite(): command failed with ', ndata, ' data transfered against ', sizeof( data ), ' wanted ' )


	def ctrlWriteReset( self, handle, request, time_out=LIBUSB_DEFAULT_TIMEOUT ):
		"""
		Send a reset write command tp Mu32 FPGA through the usb interface.
		This command needs to perform a _controlTransfer() call instead of a controlWrite() call.
		This is because we have no data to transfer (0 length) while the buffer should not be empty.
		controlWrite() computes the data length on its own, that is something >0 conducting to a LIBUSB_ERROR_PIPE [-9] exception throwing
		"""
		data = create_string_buffer( 16 )
		try:
			ndata = handle._controlTransfer(
				LIBUSB_RECIPIENT_DEVICE | LIBUSB_REQUEST_TYPE_VENDOR | LIBUSB_ENDPOINT_OUT, 
				request, 
				0,
				0, 
				data, 
				0,
				time_out,
			)
		except Exception as e:
			mu32log.error( f"reset write failed on device: {e}" )
			raise

		if ndata != 0:
			mu32log.warning( 'Mu32::ctrlWrite(): command failed with ', ndata, ' data transfered against 0 wanted ' )


	def ctrlTixels( self, handle, samples_number ):
		"""
		Set the samples number to be sent by the Mu32 system 
		"""
		buf = create_string_buffer( 5 )
		buf[0] = b'\x04'  # commande COUNT
		buf[1] = bytes(( samples_number & 0x000000ff, ) )
		buf[2] = bytes( ( ( ( samples_number & 0x0000ff00 ) >> 8 ),) )
		buf[3] = bytes( ( ( ( samples_number & 0x00ff0000 ) >> 16 ),) )
		buf[4] = bytes( ( ( ( samples_number & 0xff000000 ) >> 24 ),) )
		self.ctrlWrite( handle, 0xB4, buf )


	def ctrlResetAcq32( self, handle ):
		"""
		Reset and purge fifo
		No documention found about the 0x06 code value. Use ctrlResetMu32() instead for a complete system reset
		"""
		buf = create_string_buffer( 1 )
		buf[0] = b'\x00'
		self.ctrlWrite( handle, 0xB0, buf )
		buf[0] = b'\x06'
		self.ctrlWrite( handle, 0xB0, buf )


	def ctrlResetFx3( self, handle ):
		"""
		Mu32 need a 0xC4 command instead of 0xC2 as viewed on other programs...
		Regarding the Mu32 documentation, this control seems incomplete. Use instead ctrlResetMu32()
		"""
		try:
			self.ctrlWriteReset( handle, 0xC0, time_out=1 )
			self.ctrlWriteReset( handle, 0xC4, time_out=1 )
		except Exception as e:
			mu32log.error( f"Fx3 reset failed: {e}" ) 
			raise

	def ctrlResetMu32( self, handle ):
		"""
		full reset of Mu32 receiver
		"""
		buf = create_string_buffer( 1 )
		buf[0] = 0x00
		try:
			self.ctrlWriteReset( handle, 0xC0, time_out=1 )
			self.ctrlWriteReset( handle, 0xC4, time_out=1 )
			self.ctrlWrite( handle, 0xB0, buf )
			self.ctrlWriteReset( handle, 0xC4, time_out=1 )
			self.ctrlWriteReset( handle, 0xC0, time_out=1 )
		except Exception as e:
			mu32log.error( f"Mu32 reset failed: {e}" ) 
			raise

	def ctrlResetFPGA( self, handle ):
		"""
		reset of FPGA
		"""
		buf = create_string_buffer( 1 )
		buf[0] = 0x00
		try:
			self.ctrlWrite( handle, 0xB0, buf )
		except Exception as e:
			mu32log.error( f"FPGA reset failed: {e}" ) 
			raise


	def ctrlClockdiv( self, handle, clockdiv=0x09, time_activation=MU_DEFAULT_TIME_ACTIVATION ):
		"""
		Init acq32: set sampling frequency and supplies power to microphones 
		"""
		buf = create_string_buffer( 2 )
		buf[0] = b'\x01'  # commande init
		buf[1] = clockdiv
		try:
			self.ctrlWrite( handle, 0xB1, buf )
		except Exception as e:
			mu32log.error( f"Mu32 clock setting and powerwing on microphones failed: {e}" ) 
			raise	

		"""
		wait for mems activation
		"""
		time.sleep( time_activation )


	def ctrlDatatype( self, handle, datatype='int32' ):
		"""
		Set datatype
		! note that float32 is not considered -> TO DO
		""" 
		buf = create_string_buffer( 2 )
		buf[0] = b'\x09'
		if datatype=='int32':
			buf[1] = b'\x00' 
		elif datatype=='float32':
			buf[1] = b'\x01'
		else:
			raise Mu32Exception( 'Mu32::ctrlDatatype(): Unknown data type [%s]. Please, use [int32] or [float32]' % datatype )

		try:
			self.ctrlWrite( handle, 0xB1, buf )
		except Exception as e:
			mu32log.error( f"Mu32 datatype setting failed: {e}" ) 
			raise	

	def ctrlMems( self, handle, request, mems='all' ):
		"""
		Activate or deactivate MEMs
		"""
		try:
			buf = create_string_buffer( 4 )
			buf[0] = MU_CMD_ACTIVE		# command
			buf[1] = 0x00				# module
			if mems == 'all':
				if request == 'activate':
					for beam in range( MU_BEAMS_NUMBER ):
						buf[2] = beam		# beam number
						buf[3] = 0xFF		# active MEMs map
						self.ctrlWrite( handle, 0xB3, buf )
				elif request == 'deactivate':
					for beam in range( MU_BEAMS_NUMBER ):
						buf[2] = beam		
						buf[3] = 0x00		
						self.ctrlWrite( handle, 0xB3, buf )
				else:
					raise Mu32Exception( 'In Mu32::ctrlMems(): Unknown parameter [%s]' % request )
			else:
				if request == 'activate':
					map_mems = [0 for _ in range( MU_BEAMS_NUMBER )]
					for mic in mems:
						mic_index = mic % MU_BEAM_MEMS_NUMBER
						beam_index = int( mic / MU_BEAM_MEMS_NUMBER )
						if beam_index >= MU_BEAMS_NUMBER:
							raise Mu32Exception( 'microphone index [%d] is out of range (should be less than %d)' % ( mic,  MU_BEAMS_NUMBER*MU_BEAM_MEMS_NUMBER ) )
						map_mems[beam_index] += ( 0x01 << mic_index )

					for beam in range( MU_BEAMS_NUMBER ):
						if map_mems[beam] != 0:
							buf[2] = beam
							buf[3] = map_mems[beam]				
							self.ctrlWrite( handle, 0xB3, buf )
				else:
					raise Mu32Exception( 'In Mu32::ctrlMems(): request [%s] is not implemented' % request )
		except Exception as e:
			mu32log.error( f"Mu32 microphones activating failed: {e}" ) 
			raise	


	def ctrlCSA( self, handle, counter, status, analogs ):
		"""
		Activate or deactivate analogic, status and counter channels
		"""		
		buf = create_string_buffer( 4 )
		buf[0] = MU_CMD_ACTIVE		# command
		buf[1] = 0x00				# module
		buf[2] = 0xFF				# counter, status and analogic channels

		map_csa = 0x00
		if len( analogs ) > 0:
			for anl_index in analogs:
				map_csa += ( 0x01 << anl_index ) 
		if status:
			map_csa += ( 0x01 << 6 )
		if counter:
			map_csa += ( 0x01 << 7 )

		buf[3] = map_csa

		try:
			self.ctrlWrite( handle, 0xB3, buf )
		except Exception as e:
			mu32log.error( f"Mu32 analogic channels and status activating failed: {e}" ) 
			raise	

	def ctrlStart( self, handle ):
		"""
		start acquiring by soft triggering
		"""
		buf = create_string_buffer( 2 )
		buf[0] = 0x02
		buf[1] = 0x00

		try:
			self.ctrlWrite( handle, 0xB1, buf )
		except Exception as e:
			mu32log.error( f"Mu32 starting failed: {e}" ) 
			raise	

	def ctrlStop( self, handle ):
		"""
		stop acquiring by soft triggering
		"""
		buf = create_string_buffer( 2 )
		buf[0] = 0x03
		buf[1] = 0x00

		try:
			self.ctrlWrite( handle, 0xB1, buf )
		except Exception as e:
			mu32log.error( f"Mu32 stop failed: {e}" ) 
			raise

	def ctrlPowerOffMic( self, handle ):
		"""
		powers off microphones
		"""
		buf = create_string_buffer( 2 )
		buf[0] = 0x00

		try:
			self.ctrlWrite( handle, 0xB0, buf )
		except Exception as e:
			mu32log.error( f"Mu32 microphones powering off failed: {e}" ) 
			raise	


	"""
	Callback flushing function: only intended to flush Mu32 internal buffers
	"""
	def processFlush( self, transfer ):
		if transfer.getActualLength() > 0:
			mu32log.info( f" .flushed {transfer.getActualLength()} data bytes from transfer buffer [{transfer.getUserData()}]" )


	def processRun( self, transfer ):
		"""
		Callback run function: check transfer error, call user callback function and submit next transfer
		"""

		if self._restart_request == True:
			"""
			A request for restart has been sent -> do nothing and do not submit new transfer
			"""
			return

		if transfer.getStatus() != usb1.TRANSFER_COMPLETED:
			"""
			Transfer not completed -> skip data transfer without runing user callback
			Data is lost, if anay
			"""
			if transfer.getStatus() == usb1.TRANSFER_CANCELLED:
				mu32log.info( f" .transfer [{transfer.getUserData()}] cancelled." )
			elif transfer.getStatus() == usb1.TRANSFER_NO_DEVICE:
				mu32log.critical( f"Mu32: transfer [{transfer.getUserData()}]: no device. Exit skiping callback run." )
			elif transfer.getStatus() == usb1.TRANSFER_ERROR:
				mu32log.error( f"Mu32: transfer [{transfer.getUserData()}] error. Exit skiping callback run." )
			elif transfer.getStatus() == usb1.TRANSFER_TIMED_OUT:
				mu32log.error( f"Mu32: transfer [{transfer.getUserData()}] timed out. Exit skiping callback run." )
			elif transfer.getStatus() == usb1.TRANSFER_STALL:
				mu32log.error( f"Mu32: transfer [{transfer.getUserData()}] stalled. Exit skiping callback run." )
			elif transfer.getStatus() == usb1.TRANSFER_OVERFLOW:
				mu32log.error( f"Mu32: transfer [{transfer.getUserData()}] overflow. Exit skiping callback run." )
			else:
				mu32log.error( f"Mu32: transfer [{transfer.getUserData()}] unknowb error. Exit skiping callback run." )
				
			self._recording = False
			return
				

		"""
		get data from buffer
		"""
		data = np.frombuffer( transfer.getBuffer()[:transfer.getActualLength()], dtype=np.int32 )

		if len( data ) != self._buffer_words_length:
			"""
			buffer is not fully completed. Some data are missing
			try again anyway but skip the user process callback call. Current data is lost
			"""
			mu32log.warning( f" .lost {self._buffer_words_length - len( data )} lost samples. Retry transfer" )
			if( self._recording ):
				try:
					transfer.submit()
				except Exception as e:
					mu32log.error( f"Mu32: transfer submit failed: {e}" )
					self._recording = False
			return

		if self._counter:
			"""
			counter flag is True: performs data control such as to know if some data have been lost
			This usually appears when user callback function takes too long.
			Control is done by substracting the frame last counter value with the frame first counter value. Result should be equal to the buffer size in samples number
			Beware that, if not, it means that samples have been lost or, whorst than that, data is no longer aligned in which case this difference no longer makes sense.
			Do not submit next transfer but leave the recording flag to True. 
			At the main loop level this will suggest to retry after having reset the FX3 (data Misalignement seems to come from the FX3 USB controler.)
			"""
			ctrl_buffer_length = data[self._buffer_words_length-self._channels_number] - data[0] + 1
			if ctrl_buffer_length != self._buffer_length:

				mu32log.warning( f"Mu32: from transfer[{transfer.getUserData()}]: data has been lost. Send a restart request...")
				mu32log.info( f" .last known counter value: {self._counter_state}")
				self._restart_request = True
				return

			"""
			All seems correct -> continue
			save current counter value and reset attempt counter if needed
			"""
			self._previous_counter_state = self._counter_state
			self._counter_state = data[self._buffer_words_length-self._channels_number]
			if self._counter_state - self._previous_counter_state > self._buffer_length and self._previous_counter_state != 0:
				mu32log.info( f" .{self._counter_state - self._previous_counter_state - self._buffer_length} samples lost it seems.")

			self._restart_attempt = 0

		data = np.reshape( data, ( self._buffer_length, self._channels_number ) ).T

		if self._counter and self._counter_skip:
			"""
			Remove counter signal
			"""
			data = data[1:,:]


		"""
		Call user callback processing function if any.
		Otherwise push data in the object signal queue
		"""
		if self._callback_fn != None:
			try:
				self._callback_fn( self, data )
			except KeyboardInterrupt as e:
				mu32log.info( ' .keyboard interrupt...' )
				self._recording = False
			except Exception as e:
				mu32log.critical( f"Mu32: unexpected error {e}. Aborting..." )
				self._recording = False
		else:
			self._signal_q.put( data )
		
		"""
		Resubmit transfer once data is processed and while recording mode is on
		"""
		if( self._recording ):
			try:
				transfer.submit()
			except Exception as e:
				mu32log.error( f"Mu32: transfer submit failed: {e}. Aborting..." )
				self._recording = False

		"""
		Control duration and stop acquisition if the transfer count is reach
		_transfers_count set to 0 means the acquisition is infinite loop
		"""
		self._transfer_index += 1
		if self._transfers_count != 0 and  self._transfer_index > self._transfers_count:
			self._recording = False
	

	def run( 
			self, 
			sampling_frequency=MU_DEFAULT_SAMPLING_FREQUENCY, 
			buffers_number=MU_DEFAULT_BUFFERS_NUMBER, 
			buffer_length=MU_DEFAULT_BUFFER_LENGTH, 
			duration=MU_DEFAULT_DURATION, 
			datatype=MU_DEFAULT_DATATYPE, 
			mems=MU_DEFAULT_ACTIVATED_MEMS,
			analogs = MU_DEFAULT_ACTIVATED_ANALOG,
			counter = MU_DEFAULT_ACTIVATED_COUNTER,
			counter_skip = MU_DEFAULT_COUNTER_SKIPPING,
			status = MU_DEFAULT_ACTIVATED_STATUS,
			post_callback_fn=None, 
			callback_fn=None 
		):
		"""
		Run is a generic acquisition method that get signals from the activated MEMs

		Parameters
		----------
		* clockdiv decide for the sampling frequency. The sampling frequency is given by int( 500000/( clockdiv+1 ) ).Ex: 0x09 set for 50kHz
		* buffers_number is the number of buffers used by the USB device for the data bulk transfer. It can be set from 1 to n>1 (default is given by MU_DEFAULT_BUFFERS_NUMBER).
		* buffer_length is the number of samples that will be sent for each microphone by the Mu32 system in each transfer buffer. buffers_number_number and buffer_length have effects on latence and real time capabilities. 
		* duration is the desired recording time in seconds
		Setting buffers_number to 1 should be used only for autotest purpose since it cannot ensure real time processing.
		The more buffers_number is the more real time can be ensured without timeout or data flow breaks problems.
		Conversely latency is increased.
		"""
		try:
			self._clockdiv = max( int( 500000 / sampling_frequency ) - 1, 9 )
			self._sampling_frequency = 500000 / ( self._clockdiv + 1 )
			self._buffer_length = buffer_length
			self._buffers_number = buffers_number
			self._duration = duration
			self._mems = mems
			self._mems_number = len( self._mems )
			self._analogs = analogs
			self._analogs_number = len( self._analogs )
			self._counter = counter
			self._counter_skip = counter_skip
			self._status = status
			self._channels_number = self._mems_number + self._analogs_number + self._counter + self._status
			self._buffer_words_length = self._channels_number*self._buffer_length
			self._transfers_count = int( ( self._duration * self._sampling_frequency ) // self._buffer_length )
			self._callback_fn = callback_fn

			"""
			Do some controls and print recording parameters
			"""
			if self._analogs_number > 0:
				mu32log.warning( f"Mu32: {self._analogs_number} analogs channels were activated while they are not supported on Mu32 device -> unselecting")
				self._analogs = []
				self._analogs_number = 0
				self._channels_number = self._mems_number + self._analogs_number + self._counter + self._status
				self._buffer_words_length = self._channels_number*self._buffer_length

			mu32log.info( 'Mu32: Start running recording...')
			mu32log.info( '-'*20 )

			if datatype != 'int32' and datatype != 'float32':
				raise Mu32Exception( 'Unknown datatype [%s]' % datatype )
			self._datatype = datatype

			if sampling_frequency > 50000:
				mu32log.warning( 'Mu32: desired sampling frequency [%s Hz] is greater than the max admissible sampling frequency. Adjusted to 50kHz' % sampling_frequency )
			else:
				mu32log.info( 'Mu32: sampling frequency: %d Hz' % self._sampling_frequency )

			if self._counter_skip and not self._counter:
				mu32log.warning( 'Mu32: cannot skip counter in the absence of counter (counter flag is off)' )

			mu32log.info( f" .desired recording duration: {self._duration} s" )
			mu32log.info( f" .minimal recording duration: {( self._transfers_count*self._buffer_length ) / self._sampling_frequency} s" )
			mu32log.info( f" .{self._mems_number} activated microphones" )
			mu32log.info( f" .activated microphones: {self._mems}" )
			mu32log.info( f" .{self._analogs_number} activated analogic channels" )
			mu32log.info( f" .activated analogic channels: {self._analogs }" )
			mu32log.info( f" .whether counter is activated: {self._counter}" )
			mu32log.info( f" .whether status is activated: {self._status}" )
			mu32log.info( f" .total channels number is {self._channels_number}" )
			mu32log.info( f" .datatype: {self._datatype}" )
			mu32log.info( f" .number of USB transfer buffers: {self._buffers_number}" )
			mu32log.info( f" .buffer length in samples number: {self._buffer_length} ({self._buffer_length*1000/self._sampling_frequency} ms duration)" )			
			mu32log.info( f" .buffer length in 32 bits words number: {self._buffer_length}x{self._channels_number}={self._buffer_words_length} ({self._buffer_words_length*MU_TRANSFER_DATAWORDS_SIZE} bytes)" )
			mu32log.info( f" .minimal transfers count: {self._transfers_count}" )

			with usb1.USBContext() as context:
				"""
				open Usb device and claims interface
				"""	
				handle = context.openByVendorIDAndProductID( 
					MU_VENDOR_ID,
					MU_VENDOR_PRODUCT,
					skip_on_error=True,
				)
				if handle is None:
					raise Mu32Exception( 'Mu32 USB3 device is not present or user is not allowed to access device' )

				try:
					with handle.claimInterface( 0 ):

						"""
						init Mu32 and send acquisition starting command
						Note that counter is always selected for control purpose. This channel won't be reported if user do not select COUNTER 
						"""
						self.ctrlResetMu32( handle)
						self.ctrlClockdiv( handle, self._clockdiv, MU_DEFAULT_TIME_ACTIVATION )
						self.ctrlTixels( handle, 0 )
						self.ctrlDatatype( handle, self._datatype )
						self.ctrlMems( handle, request='activate', mems=self._mems )
						self.ctrlCSA( handle, counter=self._counter, status=self._status, analogs=self._analogs )
						self.ctrlStart( handle )

						"""
						Allocate the list of transfer objects
						"""
						transfer_list = []
						for id in range( self.buffers_number ):
							transfer = handle.getTransfer()
							transfer.setBulk(
								usb1.ENDPOINT_IN | MU_USB3_BUS_ADDRESS,
								self._buffer_words_length*MU_TRANSFER_DATAWORDS_SIZE,
								callback=self.processRun,
								user_data = id,
								timeout=MU_TRANSFER_TIMEOUT
							)
							transfer_list.append( transfer )
							transfer.submit()
							
						"""
						Recording loop
						"""
						self._transfer_index = 0
						self._counter_state = self._previous_counter_state = 0
						self._recording = True
						self._restart_request = False

						mu32log.info( f" .start recording loop..." )
						while self._recording == True:
							"""
							Attemps loop while recording is open
							"""
							while any( x.isSubmitted() for x in transfer_list ):
								"""
								Main recording loop.
								Waits for pending tranfers while there are any.
								Once a transfer is finished, handleEvents() trigers callback  
								"""
								try:
									context.handleEvents()
								except KeyboardInterrupt:
									mu32log.info( f" .Keyboard interrupting..." )
									self._recording = False	
								except usb1.USBErrorInterrupted:
									mu32log.errort( f"Mu32: USB error interrupting..." )
									self._recording = False
								except Exception as e:
									mu32log.error( f"Mu32: unexpected error {e}. Aborting..." )
									self._recording = False
							
							if self._restart_request and self._recording:
								"""
								Exits loop while recording flag is still True.
								It means that packets have been lost (this is a restart request).
								Retry after having reset FX3
								"""
								self._restart_attempt += 1
								if self._restart_attempt == 1:
									mu32log.info( " .restart device..." )
								elif self._restart_attempt >1 and self._restart_attempt < MU_MAX_RETRY_ATTEMPT:
									mu32log.info( f" .restart device... [{self._restart_attempt} times]" )
								else:
									mu32log.error( f"Mu32: device restart failed {self._restart_attempt} times -> aborting..." )
									self._recording = False
									self._restart_request = False
									break
								
								self.ctrlResetFx3( handle )
								mu32log.info( " .transfer restarting..." )
								self._restart_request = False
								for transfer in transfer_list:
									transfer.submit()

							else:
								mu32log.info( f" .quitting recording loop" )

						"""
						After loop processing
						Attempt to cancel transfers that could be yet pending
						"""
						for transfer in transfer_list:
							if transfer.isSubmitted():
								mu32log.info( f" .cancelling transfer [{transfer.getUserData()}] (may takes a while) ..." )
								try:
									transfer.cancel()
								except:
									pass
						
						while any( x.isSubmitted() for x in transfer_list ):
							try:
								context.handleEvents()
							except:
								pass

						mu32log.info( f" .cancelling transfer [done]" )

						"""
						Send stop command to Mu32 FPGA
						"""
						self.ctrlStop( handle )

						"""
						Flush Mu32 remaining data from buffers
						"""
						mu32log.info( f" .flushing buffers..." )
						for id in range( self.buffers_number ):
							transfer = transfer_list[id]
							if not transfer.isSubmitted():
								transfer.setBulk(
									usb1.ENDPOINT_IN | MU_USB3_BUS_ADDRESS,
									self._buffer_words_length*MU_TRANSFER_DATAWORDS_SIZE,
									callback=self.processFlush,
									user_data = id,
									timeout=10
								)
								try:
									transfer.submit()
								except Exception as e:
									mu32log.info( f" .transfer [{transfer.getUserData()}] flushing failed: {e}" )

						while any( x.isSubmitted() for x in transfer_list ):
							try:
								context.handleEvents()
							except :
								pass

						mu32log.info( f" .flushing [done]" )
						
						"""
						Reset Mu32 and powers off microphones
						"""
						self.ctrlResetMu32( handle)

				except Exception as e:	
					raise Mu32Exception( 'Mu32 USB3 run failed: [%s]' % e )

			mu32log.info( ' .end of acquisition' )
			mu32log.info( ' .data post processing...' )

			"""
			Call the final callback user function if any 
			"""
			if post_callback_fn != None:
				post_callback_fn( self )

		except Mu32Exception as e:
			mu32log.critical( str( e ) )
			raise
		except Exception as e:
			mu32log.critical( f"Unexpected error:{e}" )
			raise


	def post_callback_autotest( self, mu32 ):
		""" 
		end processing callback function for autotesting the Mu32 system 
		"""

		q_size = self.signal_q.qsize()
		if q_size== 0:
			raise Mu32Exception( 'Processing autotest: No received data !' )		

		signal = self.signal_q.get()
		while not self.signal_q.empty():
			signal = np.append( signal, self.signal_q.get(), axis=1 )

		"""
		compute mean energy
		"""
		mic_power = np.sum( signal**2, axis=1 )
		n_samples = np.size( signal, 1 )
			
		print( 'Autotest results:')
		print( '-'*20 )
		print( f" .counted {q_size} recorded data buffers" )
		print( f" .equivalent recording time is: {n_samples / mu32.sampling_frequency} " )
		print( f" .detected {len( np.where( mic_power > 0 )[0] )} active MEMs: {np.where( mic_power > 0 )[0]}" )
		print( '-'*20 )


	def callback_power( self, mu32, data: np.ndarray ):
		""" 
		Compute energy (mean power) on transfered frame
		"""
		signal = data * self.sensibility
		mean_power = np.sum( signal**2, axis=1 ) / self.buffer_length

		self.signal_q.put( mean_power )



def main():
	print( 'This is the main function of the module Mu32. Performs autotest' )
	mu32 = Mu32()
	mu32.run( 
		mems=[i for i in range(32)],
		post_callback_fn=mu32.post_callback_autotest,
	)


def __main__():
	main()


if __name__ == "__main__":
	main()



