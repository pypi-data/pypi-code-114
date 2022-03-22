"""
利用ffmpeg推流
"""
import os


class DmFFMPEG(object):
	def __init__(self):
		pass

	def push_stream(
			self, source, ip='127.0.0.1', port='1935', stream_type='rtmp', key=None,
			vcodec='h264', acodec=None,
			):
		key = f'/{key}' if key else ''
		vcodec = f'-vcodec {vcodec}' if vcodec else ''
		acodec = f'-acodec {acodec}' if acodec else ''
		code = f'ffmpeg -i {source} {vcodec} {acodec} -f flv {stream_type}://{ip}:{port}/live{key}'
		# print('xxx', code)
		os.system(code)

	def show_stream(self, source=None, stream_type='rtmp', ip='127.0.0.1', port='1935', key=None):
		key = f'/{key}' if key else ''
		source = source if source else f'{stream_type}://{ip}:{port}/live{key}'
		code = f'ffplay {source}'
		os.system(code)





