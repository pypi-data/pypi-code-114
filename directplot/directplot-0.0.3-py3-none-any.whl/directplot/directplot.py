"""Direct Plot

This is a simple plot library to generate plots "directly point by point"
with instantaneous update of the plot window after every point.

ATTENTION: This library is slow and not suited for production use!

It has been developed for educational purpose, especially 
to visualize numerical algorithms e.g. for simulation or plotting measurement data.


This modules requires `numpy` and `matplotlib` to be installed 
within the Python environment you are running this script in.

It wraps matplotlib and pyplot commands in even simpler commands:

```
import math
import directplot as dp

dp.init()

for i in range(51):
    x = i*2*math.pi/50
    y = math.sin(x)
    dp.add(0, x, y)

dp.waitforclose()
```

The following functions are provided:

* `init()` Initializes and opens a Direct Plot window
* `add()` Adds a single point to a plot line
* `showMarker()` Shows or hides marker points on a plot line or on all plot lines
* `label()` Changes the label of a plot line used in the legend
* `title()` Changes the title of a sub-plot
* `xylabel()` Changes the axis lables of a sub-plot
* `refresh()` Refreshes the contents of the plot window
* `close()` Closes the Direct Plot window
* `clear()` Deletes the contents of the plot window
* `waitforclose()` Displays a new window title on the plot window and
                   blocks execution until user closes the window.
"""

__version__ = '0.1'
__author__ = 'Georg Braun'

#import numpy as _np
import matplotlib.pyplot as _plt
import inspect as _inspect
from typing import Sequence as _Sequence


def init(titles: _Sequence[str] = ["Direct-Plot"], linesPerSubplot: int = 4, showMarker: bool = True) -> None:
    """Initializes and opens a Direct Plot window.

    Parameters:
    -----------
    * titles: A list or tuple containing 1 to 3 strings, resulting in 1 to 3 sub-plots on the plot window. Optional with a default title for a single sub-plot.
    * linesPerSubplot: Number of lines (data series) per sub-plot. Optional with default 4
    * showMarker: Determines if data points are emphasized with a little dot. Optional with default True

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.init()
    dp.init(["Results"])
    dp.init(["Height", "Speed", "Forces"], 2, False)
    ```
    """

    global __dp
    if __dp is not None:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): YOU HAVE CALLED {_inspect.currentframe().f_code.co_name}() TOO OFTEN!")
    __dp = __DirectPlot(titles, linesPerSubplot, showMarker)



def close() -> None:
    """Closes the Direct Plot window.

    Example:
    --------
    ```
    dp.close()
    ```
    """
    global __dp
    try:
        __dp.close()
        del(__dp)
        __dp = None
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def clear() -> None:
    """Deletes the contents of the plot window.

    Keeps the number of sub-plots, the number of lines per sub-plot and the titles of the sub-plots. Everything else is reset/deleted.

    Example:
    --------
    ```
    dp.clear()
    ```
    """
    
    global __dp
    try:
        __dp.clear()
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def waitforclose(msg: str = None) -> None:
    """Displays a new window title on the plot window and blocks execution until user closes the window.

    Parameters:
    -----------
    * msg: A string to be shown on the window title. Optional with default None resulting in a standard title

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.waitforclose()
    dp.waitforclose("PLEASE CLOSE THIS WINDOW")
    ```
    """

    global __dp
    try:
        __dp.waitforclose(msg)
        del(__dp)
        __dp = None
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def add(id: int, x: float, y: float, refresh: bool = True) -> None:
    """Adds a single point to a plot line.

    Parameters:
    -----------
    * id: The id of the target plot line
    * x: x value
    * y: y value
    * refresh: Determines if the plot is refreshed immediately resulting in slower plotting speed. Optional with default True

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.add(0, 0.1, 2.7)
    dp.add(1, 1.1, 7.3, False)
    dp.add(1, 1.2, 7.2)
    ```
    """

    global __dp
    try:
        __dp.add(id, x, y, refresh)
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def refresh() -> None:
    """Refreshes the contents of the plot window.

    Mostly used in conjunction with add() and refresh=False.

    Example:
    --------
    ```
    dp.add(0, 0.1, 7.3, False)
    dp.add(0, 0.2, 6.9, False)
    dp.add(0, 0.3, 2.1, False)
    dp.refresh()
    ```
    """

    global __dp
    try:
        __dp.refresh()
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def showMarker(show: bool = True, id: int = None) -> None:
    """Shows or hides marker points on a plot line or on all plot lines.

    Parameters:
    -----------
    * show: Show or hide markes. Optional with default True
    * id: The id of the target plot line. Optional with default None resulting in a change of markers on all plot lines.

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.showMarker()
    dp.showMarker(False, 1)
    ```
    """

    global __dp
    try:
        __dp.showMarker(show, id)
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def label(id: int, label: str) -> None:
    """Changes the label of a plot line used in the legend.

    Parameters:
    -----------
    * id: The id of the target plot line
    * label: The new label text

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.label(0, "mass in kg")
    ```
    """

    global __dp
    try:
        __dp.label(id, label)
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def title(id: int, title: str) -> None:
    """Changes the title of a sub-plot

    Parameters:
    -----------
    * id: The id of the target plot line used to determine the corresponding sub-plot
    * title: The new title text

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.title(0, "Simulated Values")
    ```
    """
    
    global __dp
    try:
        __dp.title(id, title)
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")



def xylabel(id: int, xlabel: str, ylabel: str) -> None:
    """Changes the axis lables of a sub-plot

    Parameters:
    -----------
    * id: The id of the target plot line used to determine the corresponding sub-plot
    * xlabel: New label for the x axis
    * ylabel: New label for the y axis

    Returns:
    --------
    None

    Examples:
    ---------
    ```
    dp.xylabel(0, "time in s", "force in N")
    ```
    """
    
    global __dp
    try:
        __dp.xylabel(id, xlabel, ylabel)
    except AttributeError:
        raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO MORE PLOT-WINDOW - DID YOU CLOSE IT ALREADY?")




def dp_selftest() -> None:
    """Runs some tests and quits."""

    import time

    print()
    print("Welcome to directplot. We will run some tests for you. Have fun...")
    print()

    print("test1:", _test1.__doc__)
    _test1()
    print("test2:", _test2.__doc__)
    _test2()
    print("test3:", _test3.__doc__)
    _test3()

    print()
    print("Done with testing. Bye bye ...")
    for i in range(3, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print()



def _test1() -> None:
    """Plots a sine curve"""

    import math
    import time

    time.sleep(0.2)
    points=51
    init()
    for i in range(points):
        x = i*2*math.pi/(points-1)
        y = math.sin(x)
        add(0, x, y)
    time.sleep(2)
    close()



def _test2() -> None:
    """Combines sine and cosine to a circle in two sub-plots"""

    import math
    import time

    time.sleep(0.2)
    points=51
    init(["Sinus, Cosinus", "Circle"], 2, False)
    label(0, "Cosinus")
    label(1, "Sinus")
    for i in range(points):
        t = i*2*math.pi/(points-1)
        x = math.cos(t)
        y = math.sin(t)
        add(0, t, x, False)
        add(1, t, y, False)
        add(2, x, y, False)
        refresh()
    time.sleep(2)
    close()



def _test3() -> None:
    """Combines sine and cosine to a circle in two sub-plots and plots sinc() in a third one."""

    import math
    import time
    import numpy as _np

    time.sleep(0.2)
    points=51
    init(["Sinus, Cosinus", "Circle", "sinc()"], 2)
    label(0, "Cosinus")
    label(1, "Sinus")
    label(4, "sinc()")
    for i in range(points):
        t = i*2*math.pi/(points-1)
        x = math.cos(t)
        y = math.sin(t)
        add(0, t, x, False)
        add(1, t, y, False)
        add(2, x, y, False)
        add(4, t, _np.sinc(t-math.pi), False)
        refresh()
    time.sleep(3)
    close()





class __DirectPlot:
    """Internal class used for the internal singleton object __dp"""

    def __init__(self, titles: _Sequence[str], linesPerSubplot: int = 4, showMarker: bool = True) -> None:
        self._create(titles, linesPerSubplot, showMarker)

    # Besser keinen Destructor. Der löst bei Programm-Ende durch Exceptions weitere Exceptions aus...
    # def __del__(self) -> None:
    #     self.close()

    def _create(self, titles: _Sequence[str], linesPerSubplot: int = 4, showMarker: bool = True) -> None:
        if isinstance(titles, str):
            titles = (titles, )
        
        self.titles = titles
        self.linesPerSubplot = linesPerSubplot

        self.subPlotCount = len(titles)
        if self.subPlotCount<1 or self.subPlotCount>3:
            raise ValueError(f"ERROR in directplot: YOU PROVIDED {self.subPlotCount} PLOT-TITLES. ONLY 1...3 ARE ALLOWED!")

        if not (_plt.isinteractive()): 
            _plt.ion()

        self.xLists=[[]]
        self.yLists=[[]]
        self.lines2d=[]

        self.fig, self.axs = _plt.subplots(1, self.subPlotCount, figsize=(4*self.subPlotCount, 3.5))
        # self.axs soll auch bei nur einem Plot ein Interable sein:
        if self.subPlotCount==1: self.axs = (self.axs, )

        for i, title in enumerate(titles):
            self.axs[i].set_title(title)
            self.axs[i].set_xlabel("xlabel")
            self.axs[i].set_ylabel("ylabel")

            for plot_idx in range(linesPerSubplot):
                newXlist = []
                self.xLists.append(newXlist)
                newYlist = []
                self.yLists.append(newYlist)
                line2d, = self.axs[i].plot(newXlist, newYlist, label=f"id {i*linesPerSubplot+plot_idx}", marker="." if showMarker else "") # marker='o',
                self.lines2d.append(line2d)

            self.axs[i].legend(loc='upper right')
        
        _plt.tight_layout()
        _plt.pause(0.001)
        # self.fig.canvas.draw_idle()
        # self.fig.canvas.start_event_loop(0.001)

    def close(self) -> None:
        try:
            _plt.close(self.fig)
            del(self.xLists)
            del(self.yLists)
            del(self.lines2d)
            del(self.fig)
            del(self.axs)
        except AttributeError:
            raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO PLOT-WINDOW AVAILABLE. DID YOU ALREADY CLOSE IT?")

    def waitforclose(self, msg: str = None) -> None:
        self.fig.canvas.set_window_title(msg or " "+5*" ===== DONE - PLEASE CLOSE THIS WINDOW "+"=====")
        _plt.pause(0.001)
        _plt.ioff()
        _plt.show()
        del(self.xLists)
        del(self.yLists)
        del(self.lines2d)
        del(self.fig)
        del(self.axs)

    def clear(self) -> None:
        self.close()
        self._create(self.titles, self.linesPerSubplot)

    def add(self, id: int, x: float, y: float, refresh: bool = True) -> None:
        if id<0 or id>=self.subPlotCount*self.linesPerSubplot:
            raise ValueError(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): YOUR id VALUE {id} IS OUT OF THE ALLOWED RANGE OF [0...{len(self.lines2d)-1}]!")

        self.xLists[id].append(x)
        self.yLists[id].append(y)
        self.lines2d[id].set_data(self.xLists[id], self.yLists[id])
        if refresh:
            ax_idx = id // self.linesPerSubplot
            self.axs[ax_idx].relim()
            self.axs[ax_idx].autoscale_view()
            _plt.pause(0.001)
            # self.fig.canvas.draw_idle()
            # self.fig.canvas.start_event_loop(0.001)

    def refresh(self) -> None:
        try:
            for ax in self.axs:
                ax.relim()
                ax.autoscale_view()
            _plt.pause(0.001)
            # self.fig.canvas.draw_idle()
            # self.fig.canvas.start_event_loop(0.001)
        except AttributeError:
            raise Exception(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): NO PLOT-WINDOW AVAILABLE. DID YOU ALREADY CLOSE IT?")
    
    def showMarker(self, show: bool = True, id: int = None) -> None:
        if id is None:
            # Alle Linien/Datenserien aktualisieren:
            for line in self.lines2d:
                line.set_marker("." if show else "")
            # Alle Legenden aktualisieren:
            for ax in self.axs:
                ax.legend(loc='upper right')
        else:
            # Nur eine Linie/Datenserie mit Legende aktualisieren:
            if id<0 or id>=len(self.lines2d):
                raise ValueError(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): YOUR id VALUE {id} IS OUT OF THE ALLOWED RANGE OF [0...{len(self.lines2d)-1}]!")
            self.lines2d[id].set_marker("." if show else "")
            ax_idx = id // self.linesPerSubplot
            self.axs[ax_idx].legend(loc='upper right')
        # Der Einfachheit halber den ganzen Plot aktualisieren:
        _plt.pause(0.001)

    def label(self, id: int, label: str) -> None:
        if id<0 or id>=len(self.lines2d):
            raise ValueError(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): YOUR id VALUE {id} IS OUT OF THE ALLOWED RANGE OF [0...{len(self.lines2d)-1}]!")
        self.lines2d[id].set_label(label)
        ax_idx = id // self.linesPerSubplot
        self.axs[ax_idx].legend(loc='upper right')
        _plt.pause(0.001)

    def title(self, id: int, title: str) -> None:
        if id<0 or id>=len(self.lines2d):
            raise ValueError(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): YOUR id VALUE {id} IS OUT OF THE ALLOWED RANGE OF [0...{len(self.lines2d)-1}]!")
        ax_idx = id // self.linesPerSubplot
        self.axs[ax_idx].set_title(title)
        self.titles[ax_idx] = title
        _plt.pause(0.001)

    def xylabel(self, id: int, xlabel: str, ylabel: str) -> None:
        if id<0 or id>=len(self.lines2d):
            raise ValueError(f"ERROR in directplot.{_inspect.currentframe().f_code.co_name}(): YOUR id VALUE {id} IS OUT OF THE ALLOWED RANGE OF [0...{len(self.lines2d)-1}]!")
        ax_idx = id // self.linesPerSubplot
        self.axs[ax_idx].set_xlabel(xlabel)
        self.axs[ax_idx].set_ylabel(ylabel)
        _plt.pause(0.001)

__dp = None

if __name__=="__main__":
    dp_selftest()
