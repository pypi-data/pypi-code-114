#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

from tvtk.api import tvtk

from mayavi.sources.vtk_data_source import VTKDataSource

from mayavi.modules.glyph import Glyph

import numpy as np

# -----------------------------------------------------------------------------

from geolab.plot import plotutilities

# -----------------------------------------------------------------------------

'''pointsource.py: Point plot source class, for meshes and arrays'''

__author__ = 'Davide Pellis'


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                   Points
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class Points(object):
    """The plot source for points.

    If added to a list, it can be displayed with geolab.plot.view()

    Parameters
    ----------
    points : np.array, (V, 3)
        An array with the x,y,z coordinates of the points to plot.

    **kwargs
        point_data : np.array, (V,)
            An array containing additional data corresponding to the points.
            The i-th entry of the array is associate with the i-th vertex row.
        vertex_indices : np.array of int, (N,)
            If specified, only the vertices with index contained in this
            array will be plotted.
        color : str / tuple / list of str and tuple
            The color of the plotted object. Colors can be specified as:
                - `(r,g,b)` tuples, with `r`, `g`, `b` in the interval [0,1]
                - a keyword color
                - a keyword for a color Lookup Table (LUT)
                - a list of `(r,g,b)` tuples and keyword colors
            Default is `cornflower`. If a keyword for a color Lookup Table
            (LUT) is specified, the points are colored according to a
            `point_data` -> color mapping.
        opacity : float / list of float
            a [0,1] float / a list of [0,1] floats of the same length of colors
        lut_range : str / list
            A keyword that specifies the range of the color Lookup Table
            (LUT) for data display.
                - `'-:0:+'` for symmetric LUT range, zero is the central color
                - `'0:+'` for positive LUT range, zero is the first color
                - `'-:0'` for negative LUT range, zero is the last color
                - `'-:+'` for min-max LUT range
                - `[min,max]` for user defined LUT range
            Default is `'-:0:+'`.
        glyph_type: str
            Specifies how the points are displayed. It can be
            `sphere`, `cube`, `axes`, `cone`, `wireframe`.
            Default is `sphere`

    """

    def __init__(self, points, **kwargs):
        # plotutilities.check_arguments(**kwargs)

        if hasattr(points, 'vertices'):
            self._points = points.vertices
        else:
            self._points = points

        self._geometry = None

        self._data_range = None

        self._vertex_data = kwargs.get('vertex_data', None)

        self._indices = kwargs.get('vertex_indices', None)

        self._color = kwargs.get('color', 'cornflower')

        self._opacity = kwargs.get('opacity', 1)

        self._line_width = kwargs.get('line_width', 1)

        self._scale_factor = kwargs.get('scale_factor', 1)

        self._glyph_type = kwargs.get('glyph_type', 'sphere')

        self._radius = kwargs.get('radius', 0.1)

        self._height = kwargs.get('height', 0.1)

        self._resolution = kwargs.get('resolution', 20)

        self._lut_range = kwargs.get('lut_range', '-:0:+')

        self._lut_expansion = kwargs.get('lut_expansion', 2)

        self._reverse_lut = kwargs.get('reverse_lut', False)

        self._shading = kwargs.get('shading', True)

        self._glossy = kwargs.get('glossy', 0.3)

        self._scaling = kwargs.get('scaling', False)

        self._data_points = kwargs.get('data_points', None)

        self.name = kwargs.get('name', 'points')

        self._force_opaque = kwargs.get('force_opaque', False)

        # --------------------------------------------------------------------------
        #                                 Pipeline
        # --------------------------------------------------------------------------
        # - .source =   VTKDataSource
        # - .data   =     \_Unstructured_grid
        # - .module =        \_Module_manager
        # - .glyph  =           \__Glyph
        # --------------------------------------------------------------------------

        self._make_data()

        self._module = plotutilities.make_module(self._color,
                                                 self._opacity,
                                                 self._lut_range,
                                                 self._lut_expansion,
                                                 self._reverse_lut,
                                                 self._data_range)

        self._make_glyph()

        self._assemble_pipeline()

        self.on_scene = False

        self.hidden = False

    @property
    def type(self):
        return 'Points-source'

    # --------------------------------------------------------------------------
    #                               Data Structure
    # --------------------------------------------------------------------------

    def _make_data(self):
        try:
            self._points.shape
        except AttributeError:
            self._points = np.array(self._points)
        if len(self._points.shape) == 1:
            self._points = np.array([self._points])
        if self._indices is not None:
            points = self._points[self._indices]
        else:
            points = self._points
        self._data = tvtk.PolyData(points=points)
        if self._data_points is not None:
            V = len(self._data_points)
            self._data.point_data.scalars = np.arange(V)
            self._data_range = [0, V]
        elif self._vertex_data is None:
            V = self._points.shape[0]
            self._data.point_data.scalars = np.zeros(V)
            self._data_range = [0, 0]
        else:
            scalars = np.array(self._vertex_data)
            self._data.point_data.scalars = scalars
            self._data_range = [np.min(scalars), np.max(scalars)]
        self._data.point_data.scalars.name = self.name

    # -------------------------------------------------------------------------
    #                                Glyph
    # -------------------------------------------------------------------------

    def _make_glyph(self):
        self._glyph = Glyph()
        if self._scaling:
            self._glyph.glyph.scale_mode = 'scale_by_scalar'
        else:
            self._glyph.glyph.scale_mode = 'data_scaling_off'
        self._glyph.actor.property.opacity = self._opacity
        # print(glyph.glyph.glyph_source.glyph_dict)

        if self._glyph_type == 'wireframe':
            self._glyph.actor.actor.property.representation = 'points'
            self._glyph.actor.actor.property.point_size = 1
            self._glyph.actor.actor.property.render_points_as_spheres = True
            g_src = self._glyph.glyph.glyph_source.glyph_dict['glyph_source2d']
            self._glyph.glyph.glyph_source.glyph_source.dash = True
            self._glyph.glyph.glyph_source.glyph_source.glyph_type = 'none'
            self._glyph.glyph.glyph_source.glyph_source.scale = 0
            self._glyph.actor.property.line_width = self._line_width

        elif self._glyph_type == 'cube':
            self._glyph.actor.actor.property.representation = 'surface'
            g_src = self._glyph.glyph.glyph_source.glyph_dict['cube_source']
            g_src.x_length = 2 * self._radius
            g_src.y_length = 2 * self._radius
            g_src.z_length = 2 * self._radius

        elif self._glyph_type == 'sphere':
            g_src = self._glyph.glyph.glyph_source.glyph_dict['sphere_source']
            g_src.radius = self._radius
            g_src.phi_resolution = self._resolution
            g_src.theta_resolution = self._resolution

        elif self._glyph_type == 'cone':
            self._glyph.actor.actor.property.representation = 'surface'
            g_src = self._glyph.glyph.glyph_source.glyph_dict['cone_source']
            g_src.resolution = self._resolution
            g_src.radius = self._radius
            g_src.height = self._height
            g_src.direction = np.array([0, 0, 1])
            g_src.center = np.array([0, 0, -self._height / 2])


        elif self._glyph_type == 'axes':
            g_src = self._glyph.glyph.glyph_source.glyph_dict['axes']
            self._glyph.actor.property.line_width = self._line_width

        self._glyph.glyph.glyph_source.glyph_source = g_src
        self._glyph.glyph.glyph.scale_factor = self._scale_factor

        if not self._shading:
            self._glyph.actor.actor.property.lighting = False

        self._glyph.actor.actor.property.specular = min(self._glossy, 1)
        sp = 21. * self._glossy + 0.001
        self._glyph.actor.actor.property.specular_power = sp

    # --------------------------------------------------------------------------
    #                                Pipeline
    # --------------------------------------------------------------------------

    def _assemble_pipeline(self):
        src = VTKDataSource(data=self._data)
        self._module.add_child(self._glyph)
        src.add_child(self._module)
        self.source = src

    # -------------------------------------------------------------------------
    #                                 Update
    # -------------------------------------------------------------------------

    def _update_data(self, **kwargs):
        self._points = kwargs.get('points', self._points)
        self._indices = kwargs.get('vertex_indices', self._indices)
        try:
            self._points.shape
        except AttributeError:
            self._points = np.array(self._points)
        if len(self._points.shape) == 1:
            self._points = np.array([self._points])
        if self._indices is not None:
            points = self._points[self._indices]
        else:
            points = self._points
        self._data.set(points=points)
        self._vertex_data = kwargs.get('vertex_data', self._vertex_data)
        if self._vertex_data is not None:
            if self._points.shape[0] != self._vertex_data.shape[0]:
                self._vertex_data = None
        if self._vertex_data is not None:
            scalars = np.array(self._vertex_data)
            self._data.point_data.scalars = scalars
            self._data.point_data.scalars.name = self.name
            self._data_range = [np.min(scalars), np.max(scalars)]
        else:
            V = points.shape[0]
            self._data.point_data.scalars = np.zeros(V)
            self._data.point_data.scalars.name = self.name
            self._data_range = [0, 0]
        self._data.modified()

    def _update_lut_range(self, **kwargs):
        self._lut_range = kwargs.get('lut_range', self._lut_range)
        lut_range = plotutilities.make_lut_range(self._lut_range, self._data_range)
        self._module.scalar_lut_manager.data_range = lut_range

    def _update_glossy(self, **kwargs):
        self._glossy = kwargs.get('glossy', self._glossy)
        self._glyph.actor.actor.property.specular = min(self._glossy, 1)
        sp = 21. * self._glossy + 0.001
        self._glyph.actor.actor.property.specular_power = sp

    def _update_radius(self, **kwargs):
        g_src = self._glyph.glyph.glyph_source.glyph_source
        if self._glyph_type == 'cube':
            g_src.x_length = 2 * self._radius
            g_src.y_length = 2 * self._radius
            g_src.z_length = 2 * self._radius
        elif self._glyph_type == 'sphere':
            self._radius = kwargs.get('radius', self._radius)
            g_src.radius = self._radius

    def _update_color(self, **kwargs):
        if 'color' in kwargs:
            if kwargs['color'] is not self._color:
                self._color = kwargs['color']
                plotutilities.make_lut_table(self._module,
                                             self._color,
                                             self._opacity,
                                             self._lut_expansion,
                                             self._reverse_lut)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    def update(self, **kwargs):
        self._update_data(**kwargs)
        self._update_lut_range(**kwargs)
        self._update_color(**kwargs)
        self._update_glossy(**kwargs)
        self._update_radius(**kwargs)
        # --------------------------- bug fix ---------------------------------
        # plot 2 times for updation of cone center
        if self._glyph_type == 'cone':
            g_src = self._glyph.glyph.glyph_source.glyph_source
            g_src.center = np.array([0, 0, -self._height / 2])
        # ---------------------------------------------------------------------
        self.source.update()

    def kwargs(self):
        kwargs = {}
        kwargs['name'] = self.name
        if hasattr(self._points, 'vertices'):
            if self._indices is None:
                kwargs['points'] = np.copy(self._points.vertices)
            else:
                kwargs['points'] = np.copy(self._points.vertices[self._indices])
        else:
            kwargs['points'] = np.copy(self._points)
        kwargs['vertex_data'] = np.copy(self._vertex_data)
        return kwargs

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------


'''
def _update_data(self, **kwargs):

        if 'points' in kwargs:
            points = kwargs['points']
            if type(points) == list:
                points = np.array(points)
            if hasattr(points, 'shape'):
                if len(points.shape) == 1:
                    points = np.array([points])
            elif points.type == 'Mesh':
                self._indices = kwargs.get('indices', self._indices)
                if self._indices is not None:
                    if type(self._indices) == list:
                        self._indices = np.array(self._indices)
                    points = self._geometry.vertices[self._indices,:]
                else:
                    points = self._geometry.vertices
            self._points = points
        else:
            points = self._points
        print(points)
        self._data.set(points=points)
        self._vertex_data = kwargs.get('vertex_data', self._vertex_data)
        if self._vertex_data is not None:
            scalars = np.array(self._vertex_data)
            self._data.point_data.scalars = scalars
            self._data.point_data.scalars.name = self.name
            self._data_range = [np.min(scalars), np.max(scalars)]
        else:
            V = points.shape[0]
            self._data.point_data.scalars = np.zeros(V)
            self._data.point_data.scalars.name = self.name
            self._data_range = [0,0]
        self._data.modified()
'''
