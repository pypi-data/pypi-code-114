"""Now that you have optimized (tutorial 7), how about analyzing the optimization ?
Don't worry ... That is insanely easy.
This tutorial can be seen as a mix between 6bis and 4."""

from optimeed.visualize import ViewOptimizationResults  # This is new. High-level interface to load saved optimization results.

# This is for the visualization, you are already familiar with that.
from optimeed.visualize.gui.widgets.graphsVisualWidget.examplesActionOnClick import *
from optimeed.visualize.gui.widgets.widget_openGL import widget_openGL
from optimeed.visualize.gui.widgets.openGLWidget.DeviceDrawerInterface import DeviceDrawerInterface
from optimeed.visualize.gui.widgets.openGLWidget.OpenGlFunctions_Library import *
from optimeed.visualize.gui.widgets.openGLWidget.Materials_visual import *


class Drawer(DeviceDrawerInterface):
    def __init__(self):
        self.theDevice = None

    def draw(self, theDevice):
        self.theDevice = theDevice
        glPushMatrix()
        Bronze_material.activateMaterialProperties()
        draw_simple_rectangle(theDevice.x, theDevice.y)
        glPopMatrix()

    def get_init_camera(self, theDevice):
        return 0, 0, 0.4


foldername = 'Workspace/opti/'  # This folder and files are automatically created once you have run 7_your_first_optimization.

theViewer = ViewOptimizationResults()  # Create an optimization viewer
theViewer.add_opti_project(foldername)  # Add the opti project to it (you can load several, here we only load one)

# Let's start the visualisation! Set the actions on click
theActionsOnClick = list()
theDataLink = theViewer.get_data_link()

openGlDrawing = widget_openGL()
openGlDrawing.set_deviceDrawer(Drawer())

theActionsOnClick.append(on_graph_click_showAnim(theDataLink, DataAnimationOpenGL(openGlDrawing)))
theActionsOnClick.append(on_graph_click_showInfo(theDataLink, visuals=[Repr_brut_attributes()]))
theActionsOnClick.append(on_click_extract_pareto(theDataLink, max_x=False, max_y=False))
theActionsOnClick.append(on_graph_click_delete(theDataLink))
theActionsOnClick.append(On_click_tojson(theDataLink))
theActionsOnClick.append(on_graph_click_export_trace(theDataLink))
theActionsOnClick.append(On_click_export_to_txtfile(theDataLink, attributes_master=["x", "y"], attributes_slave=["objectives[0]", "objectives[1]"]))

# And now we display the graphs ...
theViewer.display_graphs(theActionsOnClick=theActionsOnClick, max_nb_points_convergence=None)
# TADA! Nothing easier :D
