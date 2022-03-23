# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcgiscolor']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.6.3,<3.0.0']

setup_kwargs = {
    'name': 'arcgiscolor',
    'version': '1.0.1',
    'description': 'Toolset to apply coloring to a layer in an ArcGIS Pro map, using the greedy color method',
    'long_description': '# ArcGIS Pro Greedy Colorization\n\nToolbox applies the greedy color algorithm to polyline or polygon features. Goal is to symbolize the features with the fewest required colors.\n\nThis is best used in scenarios where there are a high cardinality column where individual colors do not matter. \n\n## Installation Requirements\n\nRequirements\n\n* ArcGIS Pro (Locally installed)\n* networkx [https://networkx.org/](https://networkx.org/)\n\nTo run, the networkx library must be installed in a cloned arcgis pro environment. \n\nClone the environment in your Python settings in ArcGIS Pro, or via the commandline and set this as the active python environment.\n\nonce cloned, install the networkx library.\n\n    pip install networkx\n\n\n## Usage\n\nWhen run in ArcGIS Pro, the tool will use the open map and active view. Based on the selected layer and field, the dataset will be colored with the fewest colors required to avoid color collisions.\n\nFeature symbology is updated in place. Data is unchanged.\n\nDefault search strategy is \'largest first\', but a different one can be specified. Full options available [here](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.coloring.greedy_color.html#networkx.algorithms.coloring.greedy_color).\n\n## Method\n\nTo calculate the minimum number of features, the toolbox must generate a graph representation of the dataset. As the graph represents a connected network, with nodes and links, the dataset is converted to this representation based on its spatial location.\n\nFor polyline feature, the expectation is that each end represents a connected location. For example, two lines that end on each other, are considered connected and will be linked together. This represented is with the lines as node element in a graph, linked with an arbitrary line. \n\nTo calculate the graph, the polyline feature is reduced to a point feature class with a point representing each end of the line. Each line will contain two points, sharing the input field value, which will then create the link in the networkx graph.\n\nA spatial join is completed to find the connected locations. The polygon features skips the previous step, and begins here. Similar assumption, in this case, if it touches, it is connected.\n\nFinally, the greedy color algorithm is applied to the graph and the layer is updated via the CIM in ArcGIS Pro.\n\n## Examples\n\n### Polygon Layer\n\n![Polygon](images/polygon_example.png)\n\n\n### Polyline Layer\n\n![Polyline](images/polyline_example.png)\n\n## Pypi\n\nLibrary is also installable with pip.\n\n    pip install arcgiscolor\n\nThen called with the following command.\n\n    from ArcGISColor import ColorPolyline, ColorPolygon\n\nIf using this as a standalone, the same parameters of needing to supply an ArcGIS Project and layer apply.\n    \n    project = arcpy.mp.ArcGISProject("C:\\\\path\\\\to\\\\project.aprx")\n    layer = project.listMaps(\'map_name\')[0].listLayers(\'polygon_layer_name\')[0]\n\n    cpoly = ColorPolygon()\n    cpoly.apply_colors(layer, \'field_name\', \'largest_first\')\n\n    project.save()\n\nAdditional options are available this way, such as saving a graph, re-using a graph, etc.',
    'author': 'Cody Scott',
    'author_email': 'jcodyscott@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
