# external modules
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation

def array(robo):
    """
    Transforms the current state of robo into a numpy-array which can be plotted.

    Args:
        robo (Robo): the roboter

    Returns:
        numpy.array: a numpy-array which can be plotted
    """
    
    # magic number!
    cellstate_goal = 12
    
    arr = np.array(robo.grid.cells)
    arr[robo.position[0],robo.position[1]] = robo.orientation.to_int()
    arr[robo.grid.goal_position[0],robo.grid.goal_position[1]] = cellstate_goal
    return arr

    # ROBO = 0,1,2,3
    # STONE = 4
    # LEAF = 9
    # Empty 19
    # WALL = 16

class ArrayRecorder:
    """
    An observer of robo that gets informed (if it is registered) if the state of robo changes.
    It gathers a list of numpy arrays one for each state change.
    """
    def __init__(self):
        self._frames = []
        self._active = False

    def notify(self, robo) -> None:
        """Notify the observer. This will be called by the observable.

        Args:
            robo (Robo): the roboter
        """
        if self._active:
            self._frames.append(array(robo))

    def __repr__(self) -> str:
        return self.__class__.__name__

    def pause(self) -> None:
        """Pauses the recording."""
        self._active = False

    def resume(self) -> None:
        """Resumes the recording."""
        self._active = True

    def clear(self) -> None:
        self._frames.clear()

    @property
    def frames(self):
        return self._frames

class MatplotVisualizer:
    """
    A helper class that generates a displayable representation of the robo world.
    """

    def animate(self, recorder, interval:int=150, save:bool=False, dpi:int=60, scale=0.5, path:str=None) -> animation.FuncAnimation:
        """
        Returns a displayable animation of the movement of the roboter.
        Note that this call will clear the animation stack such that the next anmiation starts with the current situation.  

        Args:
            recorder: the recorder that recorded the animation 
            interval (int, optional): delay between animation frames in milliseconds. Defaults to 150.
            save (bool, optional): if True a gif will be saved at a default path or path specified. Defaults to False.
            dpi (int, optional): controls the dots per inch for the movie frames. Together with the figure's size in inches, this controls the size of the movie. Defaults to 60.
            scale (float, optional): scale of the figure. Defaults to 0.5.
            path (str, optional): relative path, i.e. the location of the saved figure. Defaults to None.

        Raises:
            Exception: _description_

        Returns:
            animation.FuncAnimation: _description_
        """
       
        if len(recorder.frames) <= 0:
            raise Exception("Recording is to short to generate an animation.")

        matplt, fig = self.plot(recorder.frames[0], dpi, scale)
        

        i = {'index': -1}  # trick to enforce sideeffect

        def updatefig(*args):
            i['index'] += 1
            if i['index'] >= len(recorder.frames):
                i['index'] = 0
            matplt.set_array(recorder.frames[i['index']])
            return matplt,

        anim = animation.FuncAnimation(fig, func=updatefig, init_func=lambda :matplt, interval=interval, blit=False, save_count=len(recorder.frames))
        
        if save:
            if path == None:
                anim.save('robo-world-animation.gif',dpi=dpi)
            else:
                anim.save(path, dpi=dpi)
        return anim

    def plot(self, frame, dpi=80, scale=0.5):
        """
        Transforms a frame of the recording, i.e., a numpy array into a figure.

        Args:
            matrix (numpy.array): the frame
            dpi (int, optional): dpi of the resulting figure. Defaults to 80.
            scale (float, optional): scale of the figure. Defaults to 0.5.

        Returns:
            Axis, Figure: (axis and) figure representing the frame
        """
        nrows, ncols = frame.shape
        fig = plt.figure(figsize=(ncols * scale, nrows * scale), dpi=dpi)
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(which='both')
        matplt = ax.matshow(frame, interpolation='nearest', vmin=0, vmax=len(plt.get_cmap('tab20c').colors), cmap=plt.get_cmap('tab20c'))
        x_ticks = np.arange(-0.5, ncols+1, 1)
        y_ticks = np.arange(-0.5, nrows+1, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticks(x_ticks, minor=True)
        ax.set_yticks(y_ticks, minor=True)
        ax.set_xlim(-0.5, ncols-0.5)
        ax.set_ylim(-0.5, nrows-0.5)
        plt.close()
        return matplt, fig

    def show(self, robo, dpi=80, scale=0.5) -> Figure:
        """Returns a displayabel representation of the world, i.e. a figure.

        Args:
            robo (Robo): the roboter
            dpi (int, optional): dpi of the resulting figure. Defaults to 80.
            scale (float, optional): scale of the figure. Defaults to 0.5.

        Returns:
            Figure: figure representing the frame
        """
        _, fig = self.plot(array(robo), dpi=dpi, scale=scale)
        return fig