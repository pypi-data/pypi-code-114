"""This example shows how to make a 3D plot easily, using plotly.
The interest is only marginal, as optimeed is designed to work with 2D plots."""
from random import random
from optimeed.core.graphs3 import ScatterPlot3, convert_to_gridplot, SurfPlot
from optimeed.visualize import plot3d


# Generate 3D
x = list()
y = list()
z = list()
for i in range(100):
    x.append(random())
    y.append(random())
    z.append(x[-1] ** 2 * y[-1])

allPlots = list()
allPlots.append(ScatterPlot3(x, y, z, x_label="I am the X axis"))  # A scatter plot directly from the data
allPlots.append(SurfPlot(*convert_to_gridplot(x, y, z, x_interval=[0.1, 0.9], y_interval=[0.1, 0.9])))  # An interpolated surf plot from the data

plot3d(allPlots)
