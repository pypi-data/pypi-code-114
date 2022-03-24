
def unit_test_ellipse():
    import numpy as np
    from optimeed.visualize.gui.widgets.graphsVisualWidget.pyqtgraph import TextItem
    from optimeed.core import get_ellipse_axes
    from optimeed.core import Data, Graphs
    from optimeed.visualize import widget_graphs_visual, gui_mainWindow
    from PyQt5.QtCore import QTimer
    from time import time

    theData = Data([], [])
    theGraphs = Graphs()
    g = theGraphs.add_graph()
    theGraphs.add_trace(g, theData)

    wgPlot = widget_graphs_visual(theGraphs)
    wgPlot.get_graph(g).axis_equal()
    textItem = TextItem("Test")
    wgPlot.get_graph(g).add_feature(textItem)

    win = gui_mainWindow([wgPlot])

    def change_data(a, b, phi):
        nTimesteps = 50
        x = np.linspace(0, 2 * np.pi, nTimesteps)
        bx = a * np.sin(x)
        by = b * np.sin(x + phi)
        theData.set_data(bx, by)
        maja, mina, phase = get_ellipse_axes(a, b, phi)
        textItem.setText("a:{:#.4g}\nb: {:#.4g}\nmaj: {:#.4g}\nmin: {:#.4g}\n phase: {:#.4g}".format(a, b, maja, mina, phase*180/np.pi))
        QTimer().singleShot(100, lambda: change_data(a, b, np.pi*np.sin(time())))

    change_data(1, 0.5, np.pi/2)
    win.run(hold=True)


def unit_test_fourrier():
    import numpy as np
    from optimeed.visualize.gui.widgets.graphsVisualWidget.pyqtgraph import TextItem
    from optimeed.core import my_fft, reconstitute_signal
    from optimeed.core import Data, Graphs
    from optimeed.visualize import widget_graphs_visual, gui_mainWindow
    from PyQt5.QtCore import QTimer
    from time import time

    theData = Data([], [])
    theGraphs = Graphs()
    g = theGraphs.add_graph()
    theGraphs.add_trace(g, theData)
    theData2 = Data([], [], is_scattered=True)
    theGraphs.add_trace(g, theData2)
    wgPlot = widget_graphs_visual(theGraphs)
    wgPlot.get_graph(g).axis_equal()
    textItem = TextItem("Test")
    wgPlot.get_graph(g).add_feature(textItem)

    win = gui_mainWindow([wgPlot])

    def change_data(a, b, phi):
        nTimesteps = 25
        x = np.linspace(0, 2 * np.pi, nTimesteps)
        y = a*np.sin(x) + b*np.sin(3*x + phi)
        theData.set_data(x, y)
        amplitudes, phase = my_fft(y)
        print(amplitudes)
        theData2.set_data(*reconstitute_signal(amplitudes, phase, x_points=x))
        textItem.setText("{:#.4g}\t:{:#.4g}\n{:#.4g}\t:{:#.4g}\n".format(a, amplitudes[1], b, amplitudes[3]))
        QTimer().singleShot(100, lambda: change_data(a, 0.5*np.sin(time()), phi))

    change_data(1, 0.5, np.pi/2)
    win.run(hold=True)


def unit_test_derivate_integrate():
    import numpy as np
    from optimeed.visualize.gui.widgets.graphsVisualWidget.pyqtgraph import TextItem
    from optimeed.core import derivate, integrate
    from optimeed.core import Data, Graphs
    from optimeed.visualize import widget_graphs_visual, gui_mainWindow
    from PyQt5.QtCore import QTimer
    from time import time

    theData = Data([], [])
    theGraphs = Graphs()
    g = theGraphs.add_graph()
    theGraphs.add_trace(g, theData)
    theData2 = Data([], [], is_scattered=True)

    theGraphs.add_trace(g, theData2)
    wgPlot = widget_graphs_visual(theGraphs)
    # textItem = TextItem("Test")
    # wgPlot.get_graph(g).add_feature(textItem)

    win = gui_mainWindow([wgPlot])

    def change_data(a, b, phi, order):
        nTimesteps = 50
        x = np.linspace(0, 2 * np.pi, nTimesteps)
        y = a*np.sin(x) + b*np.sin(order*x + phi)
        dydx = a*np.cos(x) + order*b*np.cos(order*x + phi)
        theData.set_data(x, dydx)

        derivative = derivate(x, y)

        theData2.set_data(x, derivative)
        # textItem.setText("{:#.4g}\t:{:#.4g}\n{:#.4g}\t:{:#.4g}\n".format(a, amplitudes[1], b, amplitudes[3]))
        QTimer().singleShot(100, lambda: change_data(a, b, phi, order+1))

    change_data(1, 0.5, np.pi/2, 3)
    win.run(hold=True)


unit_test_derivate_integrate()
