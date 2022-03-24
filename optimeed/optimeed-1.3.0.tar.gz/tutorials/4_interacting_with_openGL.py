"""That was fun, but how about I could have something more ... visual ?
If there is a length and a height, I am dealing with a square. Can I display it ?
Of course! Thanks to the use of openGL.
"""

# We already know these imports ...
from optimeed.core import ListDataStruct
from optimeed.core import LinkDataGraph, HowToPlotGraph
from optimeed.visualize import widget_graphs_visual, gui_mainWindow, guiPyqtgraph
# Now for the openGL imports:
from optimeed.visualize.gui.widgets.openGLWidget.DeviceDrawerInterface import DeviceDrawerInterface  # To tell how to draw the device
from optimeed.visualize.gui.widgets.openGLWidget.OpenGlFunctions_Library import *  # The OpenGL library
from optimeed.visualize.gui.widgets.openGLWidget.Materials_visual import Bronze_material  # Some predefined materials aspect (color, reflection, etc.)
from optimeed.visualize.gui.widgets.widget_openGL import widget_openGL  # And we put all of that inside a widget
from optimeed.visualize.gui.widgets.graphsVisualWidget.examplesActionOnClick import on_graph_click_showAnim, DataAnimationOpenGL  # And we put the widget inside an action


class MyDevice:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.surface = self.length * self.height


# The drawer class
class DeviceDrawer(DeviceDrawerInterface):
    """Drawer of the device"""
    def __init__(self):
        self.theDevice = None

    def draw(self, theDevice):
        glPushMatrix()  # Remove the previous matrices transformations
        glTranslate(-5, -5, 0)
        Bronze_material.activateMaterialProperties()  # Change colour aspect of the material, here it will look like bronze
        draw_simple_rectangle(theDevice.length, theDevice.height)  # Thats the interesting line
        glPopMatrix()  # Push back previous matrices transformations

    def get_init_camera(self, theDevice):
        tipAngle = 0
        viewAngle = 0
        zoomLevel = 0.1
        return tipAngle, viewAngle, zoomLevel


# From now on, that's the same as before
theDataStruct = ListDataStruct()
for xi in range(10):
    for yi in range(10):
        theDataStruct.add_data(MyDevice(xi, yi))

theDataLink = LinkDataGraph()
_ = theDataLink.add_collection(theDataStruct)

howToPlot = HowToPlotGraph('length', 'surface', {'x_label': "length [m]", 'y_label': "surface [m^2]", 'is_scattered': True})
theDataLink.add_graph(howToPlot)
theGraphs = theDataLink.createGraphs()

theActionsOnClick = list()

# That's where the fun begins !
openGlDrawing = widget_openGL()  # First we define the widget
openGlDrawing.set_deviceDrawer(DeviceDrawer())  # We set the drawer to the widget
theActionsOnClick.append(on_graph_click_showAnim(theDataLink, DataAnimationOpenGL(openGlDrawing)))  # And we create an action out of it !

# Same as before
myWidgetGraphsVisuals = widget_graphs_visual(theGraphs, highlight_last=True, refresh_time=-1)  # The widget to display the graphs
guiPyqtgraph(myWidgetGraphsVisuals, actionsOnClick=theActionsOnClick)  # The GUI of the widget (that contains export buttons)
myWindow = gui_mainWindow([myWidgetGraphsVisuals])  # A Window (that will contain the widget)
myWindow.run(True)

# Now click on a point.
# Click on "show all"
# Watch the graph and animation in parallel!
