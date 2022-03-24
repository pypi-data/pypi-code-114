"""Ok, graphs linked to data are fun but now I would like to select a subset of my data and do something from it ...
 How could I do it ?
-> You need our special class 'GuiDataSelector' will do it for you ! """

# You already know these imports :)
from optimeed.visualize import widget_graphs_visual, guiPyqtgraph, gui_mainWindow
from optimeed.core import ListDataStruct, LinkDataGraph, HowToPlotGraph
from optimeed.visualize import DeviceDrawerInterface
from optimeed.visualize.gui.widgets.openGLWidget.OpenGlFunctions_Library import *
from optimeed.visualize.gui.widgets.openGLWidget.Materials_visual import Bronze_material
from optimeed.visualize.gui.widgets.widget_openGL import widget_openGL
from optimeed.visualize.gui.widgets.graphsVisualWidget.examplesActionOnClick import *

# But these ones are new ...
from optimeed.visualize import start_qt_mainloop  # That allows the GUI to refresh "manually"
from optimeed.visualize import GuiDataSelector  # This is the data selector we will cover
from optimeed.visualize import On_select_new_trace  # These are two examples of what we can do with the data selector

from random import random  # This just comes in handy to generate the data


# From now on, that's the same as before
class MyDevice:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.surface = self.length * self.height


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


theDataStruct = ListDataStruct()
for _ in range(100):
    theDataStruct.add_data(MyDevice(random()*10, random()*10))

theDataLink = LinkDataGraph()
_ = theDataLink.add_collection(theDataStruct)

howToPlot = HowToPlotGraph('length', 'surface', {'x_label': "length [m]", 'y_label': "surface [m^2]", 'is_scattered': True})
theDataLink.add_graph(howToPlot)
theGraphs = theDataLink.createGraphs()

theActionsOnClick = list()
openGlDrawing = widget_openGL()
openGlDrawing.set_deviceDrawer(DeviceDrawer())
theActionsOnClick.append(on_graph_click_showAnim(theDataLink, DataAnimationOpenGL(openGlDrawing)))
theActionsOnClick.append(on_graph_click_showInfo(theDataLink, visuals=[Repr_brut_attributes()]))
theActionsOnClick.append(on_graph_click_delete(theDataLink))
theActionsOnClick.append(on_graph_click_export_trace(theDataLink))

myWidgetGraphsVisuals = widget_graphs_visual(theGraphs, highlight_last=False, refresh_time=-1)
guiPyqtgraph(myWidgetGraphsVisuals, actionsOnClick=theActionsOnClick)
myWindow = gui_mainWindow([myWidgetGraphsVisuals])

# Now this is different !
myWindow.run(False)  # We run this window, but non-blocking (-> False) because we still have something to do ...

theDataSelector = GuiDataSelector([theDataStruct], [On_select_new_trace(theDataLink)])  # Spawn the data selector
theDataSelector.run()  # Run it
start_qt_mainloop()  # Display the gui "Manually"

# Now you have a new GUI (might be hidden behind the graphs)
# You can enter 1 to length (min) and 4 to length (max)
# Then click Update.
# A new trace with the selection appeared on the graph (because the action was "create new trace" (from selection)
# Now you can click on a point of this new trace ...
# Tada! You will only animate the subselection.
# This is extremely powerful as you can combine any "selection action" to any "click action".
# So that, for instance, you could export a specific subset of the data you need ...
# ;)
