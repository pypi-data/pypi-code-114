"""This example shows how to easily make a plot with optimeed"""
from optimeed.visualize import plot

x = [2, 3, 5, 2]
y = [1, 3, 2, 6, 7]

plot(x, y, hold=False, legend="Plot 1")  # hold = False means the program won't be blocking ... but the window won't be displayed either ;)

x = []  # Empty list is automatically converted to range(y) :)
y = [3, 2, 4, 4, 5]

plot(x, y, hold=True, legend="Plot 2", is_scattered=True)  # display the window

# Tips:
# Use right clic to zoom in or out
# If you are "lost" in the graph -> right click "View All"

# Do not hesitate to try the "export button".
# You can specify the file type (.txt, .png, .svg, or .pdf (it requires inkscape))
# You can also export to tikz for publication-quality graphs. In this case use the extension ".tikz", that will create a folder. Go inside and compile "generate_figure.tex" and tada ;)
# You can export to all file types if you do not write any extension.

