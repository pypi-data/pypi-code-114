# mu32autotest.py python program example for MegaMicro Mu32 transceiver 
#
# Copyright (c) 2022 DistalSense
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
Run autotest for MEMs detecting

Documentation is available on https://distalsense.io

Please, note that the following packages should be installed before using this program:
	> pip install libusb1
"""

welcome_msg = '-'*20 + '\n' + 'Mu32 Autotest program\n \
Copyright (C) 2022  DistalSense\n \
This program comes with ABSOLUTELY NO WARRANTY; for details see the source code\'.\n \
This is free software, and you are welcome to redistribute it\n \
under certain conditions; see the source code for details.\n' + '-'*20

import argparse
import numpy as np
from mu32.core import Mu32, mu32log, logging


mu32log.setLevel( logging.INFO )

def main():

	parser = argparse.ArgumentParser()
	parser.parse_args()

	print( welcome_msg )

	try:
		mu32 = Mu32()
		mu32.run( 
			post_callback_fn=my_autotest_function, 		# the user defined data processing function
			mems=[i for i in range(32)],				# activated mems: all
		)
	except :
		print( 'aborting' )


def my_autotest_function( mu32: Mu32 ):

	"""
	get queued signals from Mu32
	"""
	q_size = mu32.signal_q.qsize()
	signal = mu32.signal_q.get()
	while not mu32.signal_q.empty():
		signal = np.append( signal, mu32.signal_q.get(), axis=1 )

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

if __name__ == "__main__":
	main()