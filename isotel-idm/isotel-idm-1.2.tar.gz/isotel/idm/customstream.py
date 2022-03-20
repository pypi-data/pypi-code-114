"""ISOTEL IDM support to decode signals from user defined custom streams into IDM Streams
"""
import socket

class CustomStream():
    """Open and Decode Stream from Custom/User Protocol of either endianness and sizes.

    :param stream_hostport: a tuple returned by gateway.Device.get_stream_hostport()
    :param packet_format: specifies one or more variables after the first packet time specs in the format as
           [('t [s]', packet_size, packet_interval), ('val [V]', start_byte, end_byte, scale, post_offset), ..],
           where if start_byte < end_byte denotes little endian, 
           if either start or end byte is negative value determines signed othewise unsigned
    :param start_func: is lambda function executed at start
    :param stop_func: is lambda function executed before starting the transfer and at the end
    :param packet_timeout: denotes tcp/ip socket timeout to retrieve the data
    """
    def __init__(self, stream_hostport, packet_format, start_func, stop_func, packet_timeout=0.1):
        self.packet_format = packet_format
        self.start_func = start_func
        self.stop_func = stop_func

        self.stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stream_socket.connect(stream_hostport)
        self.stream_socket.settimeout(packet_timeout)

    """
    Is a generator yielding the IDM signal.stream compatible output to be used with scope.

    :param N: number of samples (packets) to fetch
    """
    def fetch(self, N=10):
        self.stop_func()
        while True:
            try:
                self.stream_socket.recv(1024)
            except socket.timeout:
                break
        try:
            yield ((self.packet_format[0][0], tuple([i[0] for i in self.packet_format[1:]])),)
            self.start_func()
            for t in range(N):
                pckt = self.stream_socket.recv( self.packet_format[0][1] )
                vals = []
                for i in range(1,len(self.packet_format)):
                    st  = self.packet_format[i][1]
                    end = self.packet_format[i][2]
                    signed = True if st < 0 or end < 0 else False
                    st  = abs(st)
                    end = abs(end)
                    if end > st:
                        vals += [self.packet_format[i][3] * int.from_bytes(pckt[st:end], byteorder='little', signed=signed) - self.packet_format[i][4]]
                    else:
                        vals += [self.packet_format[i][3] * int.from_bytes(pckt[end:st], byteorder='big', signed=signed) - self.packet_format[i][4]]

                yield ((t*self.packet_format[0][2], tuple(vals)),)

            self.stop_func()

        except KeyboardInterrupt:
            self.stop_func()

        except (GeneratorExit, socket.timeout):
            self.stop_func()
            raise
