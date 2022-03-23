from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import ConnectionPatch, Arc

from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

from matplotlib.image import NonUniformImage

import numpy as np
import pandas as pd

from todofcpy.visualization.graph import Sprintmap

def _is_ndarray(array):
	"""
	.. py:function:: lumache.get_random_ingredients(kind=None)

	   Return a list of random ingredients as strings.

	   :param kind: Optional "kind" of ingredients.
	   :type kind: list[str] or None
	   :return: The ingredients list.
	   :rtype: list[str]

	Returns True if is ndarray of size 2.

	Parameters
	----------
	np.array
	"""
	if type(array) is np.ndarray:
		if len(array.shape) == 2 and len(array[0]) == 2:
			return True
		else:
			return False
	else:
		return False

def _create_histogram(self,ax):
	"""
	Returns a matplotlib.pyplot with histogram2d & NonUniformImage added.

	Parameters
	----------
	self (self.data)
	ax = fig.subplot
	"""

	array = self.data
	x = array['x_pos'].to_numpy()
	y = array['y_pos'].to_numpy()

	if 'color' in self.__dict__:
		color = self.color
	else:
		color = 'gnuplot'

	# x, y = array[:,0], array[:,1]
	heatmap, xedges, yedges = np.histogram2d(x, y, bins=50, range=[[0, 105], [0, 68]])
	heatmap = heatmap.T
	im = NonUniformImage(ax, interpolation='bilinear', cmap=color)
	xcenters = (xedges[:-1] + xedges[1:]) / 2
	ycenters = (yedges[:-1] + yedges[1:]) / 2
	im.set_data(xcenters, ycenters,heatmap)
	ax.images.append(im)

	return plt

def _draw_pitch(ax):
	# focus on only half of the pitch
	#Pitch Outline & Centre Line
	Pitch = plt.Rectangle([0,0], width = 120, height = 80,color="white", fill = False)
	#Left, Right Penalty Area and midline
	LeftPenalty = plt.Rectangle([0,22.3], width = 14.6, height = 35.3, color="white",fill = False)
	RightPenalty = plt.Rectangle([105.4,22.3], width = 14.6, height = 35.3, color="white",fill = False)
	midline = ConnectionPatch([60,0], [60,80], "data", "data",color="white")

	#Left, Right 6-yard Box
	LeftSixYard = plt.Rectangle([0,32], width = 4.9, height = 16, color="white",fill = False)
	RightSixYard = plt.Rectangle([115.1,32], width = 4.9, height = 16, color="white",fill = False)

	#Prepare Circles
	centreCircle = plt.Circle((60,40),8.1,color="white", fill = False)
	centreSpot = plt.Circle((60,40),0.71,color="white")
	#Penalty spots and Arcs around penalty boxes
	leftPenSpot = plt.Circle((9.7,40),0.71,color="white")
	rightPenSpot = plt.Circle((110.3,40),0.71,color="white")
	leftArc = Arc((9.7,40),height=16.2,width=16.2,angle=0,theta1=310,theta2=50,color="white")
	rightArc = Arc((110.3,40),height=16.2,width=16.2,angle=0,theta1=130,theta2=230,color="white")

	element = [Pitch, LeftPenalty, RightPenalty, midline, LeftSixYard, RightSixYard, centreCircle,
			   centreSpot, rightPenSpot, leftPenSpot, leftArc, rightArc]
	for i in element:
		ax.add_patch(i)

def _create_frame(t,self):
	data = self.data
	array = self.__dict__['array_data']
	if 'sprintmap' in self.__dict__:
		if self.__dict__['sprintmap'] == 'on':
			plt = _create_sprintmap(data=array)
			ax = plt.gca()
			fig = plt.gcf()
		else:
			from matplotlib import pyplot as plt
			fig=plt.figure()
			fig.set_size_inches(7, 5)
			ax=fig.add_subplot(1,1,1)
			fig.set_facecolor('black')
			_draw_pitch(ax)
			plt.ylim(-2, 82)
			plt.xlim(-2, 122)
			plt.axis('off')
	else:
		from matplotlib import pyplot as plt
		fig=plt.figure()
		fig.set_size_inches(7, 5)
		ax=fig.add_subplot(1,1,1)
		fig.set_facecolor('black')
		_draw_pitch(ax)
		plt.ylim(-2, 82)
		plt.xlim(-2, 122)
		plt.axis('off')

	if 'heatmap' in self.__dict__:
		# turn heatmap on?
		if(self.__dict__['heatmap']=='on'):
			_create_histogram(self,ax)


	# set player color?
	if 'player_color' in self.__dict__:
		player_color = self.player_color
	else:
		player_color = 'gray'

	if 'fps' in self.__dict__:
		fps = self.fps
	else:
		fps =  20

	f = int(t*fps)
	data = data.loc[f]
	ax.add_artist(Ellipse((data['x_pos'],
							data['y_pos']),
							2/105*100, 2/68*100,
							edgecolor='white',
							linewidth=2,
							facecolor=player_color,
							alpha=1,
							zorder=20))

	return fig, ax, data

def _create_dataframe(self,kwargs):
	array = kwargs['data']
	self.__dict__['data'] = pd.DataFrame({'x_pos': array[:, 0], 'y_pos': array[:, 1]})
	self.__dict__['array_data'] = array

def _create_sprintmap(data):
	tsm = Sprintmap(data=data)
	plt = tsm.create_sprintmap_plot()

	return plt

def _set_clip_parameters(self,kwargs):
	# set fps
	if 'fps' in self.__dict__:
		pass
	elif 'fps' in kwargs:
		self.__dict__['fps'] = kwargs['fps']
	else:
		self.__dict__['fps'] = 20

	# set duration
	if 'duration' in self.__dict__:
		pass
	elif 'duration' in kwargs:
		self.__dict__['duration'] = kwargs['duration']
	else:
		self.__dict__['duration'] = 30

	# set start
	if 'start' in self.__dict__:
		pass
	elif 'start' in kwargs:
		self.__dict__['start'] = kwargs['start']
	else:
		self.__dict__['start'] = 0

	# check length error
	start_frames_count = self.__dict__['start'] * self.__dict__['fps']
	duration_frames_count = self.__dict__['duration'] * self.__dict__['fps']
	total_frames_count = start_frames_count + duration_frames_count
	if total_frames_count > len(self.__dict__['data'].index):
		raise ValueError("Clip length too long for data selected.")

	self.__dict__['data'] = self.__dict__['data'].drop(self.__dict__['data'].index[0:start_frames_count])
	self.__dict__['data'] = self.__dict__['data'].reset_index()



class Animation:
	def __init__(self,**kwargs):
		"""
		Set's Animations variables.

		Kwargs:
		   data (np.ndarray): 2d array of length 2.
		   color (Matplotlib.cm): (optional) Matplotlib.cm, ['viridis', 'plasma', 'inferno', 'magma', 'cividis'].
		   duration (int): Number of secods desired for clip.
		   player_color (rgba,string): Color for desired player to be.

		"""
		# error check data
		if 'data' in kwargs:
			try:
				ndarray = _is_ndarray(kwargs['data'])
				if(ndarray):
					pass
				else:
					raise ValueError()
			except ValueError:
				print("Sprintmap takes ndarray")
				sys.exit()

		self.__dict__.update(kwargs)

		_create_dataframe(self,kwargs)

	def animate(self,**kwargs):
		"""
		Animate saves a moviepy.editor.VideoClip in the current directory. The
			name of the file is the start minute and finish minute.

		Keyword Args:
			start (Optional[int]): The interger value of seconds where the clip
				is to start. Defaults to 0.
			duration (Optional[int]): The interger value of seconds that is the
				length of the clip. Defaults to 30 seconds.
			color (Optional[Matplotlib.cm]): ['viridis', 'plasma', 'inferno',
				'magma', 'cividis'].
			player_color (Optional[Color Name, Hex Value or RGB Value]): Color
				value of the player. Defaults to 'gray'.
			fps (Optional[int]): The number of frames per second the data was
				recorded in. Defaults to 20.
			heatmap (Optional[str]): If heatmap='on', a heatmap will show in
				background. Defaults to off.
			sprintmap (Optional[str]): If sprintmap='on', a sprintmap will show
				in background.
		"""

		self.__dict__.update(kwargs)
		_set_clip_parameters(self,kwargs)
		animation = VideoClip(lambda x: mplfig_to_npimage(_create_frame(x,self)[0]),duration=self.__dict__['duration'])
		end = self.__dict__['start'] + self.__dict__['duration']
		end = str(end)
		name = str(self.__dict__['start']) + '_to_' + end + '.mp4'
		animation.write_videofile(name,self.__dict__['fps'])
