"""Tutorials are getting harder !
Plots are fine but we would want them to 'hide' some data ...
Let's see how we combine both of them ;)
"""

# First we define the imports

from optimeed.core import ListDataStruct  # This will hold a 'list of data'
# Visuals imports
from optimeed.core.linkDataGraph import LinkDataGraph, HowToPlotGraph  # These classes will tell how the data is connected to the graphs
from optimeed.visualize.gui.widgets.widget_graphs_visual import widget_graphs_visual  # That will convert a "python data structure" to "a graph that will be displayed" (pyqtgraph)
from optimeed.visualize.gui.gui_mainWindow import gui_mainWindow  # That will spawn the GUI containing the widget_graphs_visual
# Graph visuals imports
from optimeed.visualize.gui.widgets.graphsVisualWidget.examplesActionOnClick import on_graph_click_showInfo, Repr_brut_attributes  # This is an action to perform when the graph will be clicked... there are many others;)
from optimeed.visualize.gui.widgets.graphsVisualWidget.examplesActionOnClick import on_graph_click_delete  # This is an other action to perform when the graph is clicked.
from optimeed.visualize.gui.widgets.graphsVisualWidget.smallGui import guiPyqtgraph  # That will add some GUI element to the widget_graphs_visual, like an export button


# Now that we have the imports, we define a data type.
# Our data type is simple, it contains the informations "length", "height" and "surface"
class MyDevice:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.surface = self.length * self.height


# Now we make a 'structure of data' out of the data: imagine we have many data (e.g., logs from an optimization)
theDataStruct = ListDataStruct()
for xi in range(10):
    for yi in range(10):
        theDataStruct.add_data(MyDevice(xi, yi))

# We would like to plot them. In other words, we will link data to graphs.
theDataLink = LinkDataGraph()
_ = theDataLink.add_collection(theDataStruct)  # Do not care for now about the return value.

# Now we tell what we need to plot:
howToPlot = HowToPlotGraph('length',  # We plot the attribute length on the x axis
                           'surface',  # we plot the attribuge "surface" on the y axis
                           {'x_label': "length [m]", 'y_label': "surface [m^2]", 'is_scattered': True})  # We use that last line to display the way we want
theDataLink.add_graph(howToPlot)

# Everything is ready. We ask theDataLink to generate the graphs
theGraphs = theDataLink.createGraphs()

# We also add additional actions to perform when the graph is clicked.
# This is what makes this software extremely powerful, because this action makes the graph interactive and could be anything.
theActionsOnClick = list()
theActionsOnClick.append(on_graph_click_showInfo(theDataLink, visuals=[Repr_brut_attributes()]))  # This action shows the content of the selected data
theActionsOnClick.append(on_graph_click_delete(theDataLink))  # This action shows the content of the selected data

# Now we make a GUI out of it. It is composed of three tings:
myWidgetGraphsVisuals = widget_graphs_visual(theGraphs, highlight_last=True, refresh_time=-1, is_light=True)  # The widget to display the graphs
guiPyqtgraph(myWidgetGraphsVisuals, actionsOnClick=theActionsOnClick)  # The GUI of the widget (that contains export buttons)
myWindow = gui_mainWindow([myWidgetGraphsVisuals])  # A Window (that will contain the widget)

# When everything is ready ... WE START IT! Dont hesitate to left click on some points to see what happens ;)
myWindow.run(True)

# Tips:
# You can select several points at once by holding shift and dragging the left mouse ... don't be greedy, this option is slow :D
# Try to change the action! The Delete action is so fun to hide outliers ;)
