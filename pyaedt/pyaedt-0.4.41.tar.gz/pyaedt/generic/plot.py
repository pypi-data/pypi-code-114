import csv
import os
import tempfile
import time
import warnings
from datetime import datetime

from pyaedt import pyaedt_function_handler
from pyaedt.generic.constants import AEDT_UNITS
from pyaedt.generic.constants import CSS4_COLORS
from pyaedt.generic.general_methods import convert_remote_object
from pyaedt.generic.general_methods import is_ironpython

if not is_ironpython:
    try:
        import numpy as np
    except ImportError:
        warnings.warn(
            "The NumPy module is required to run some functionalities of PostProcess.\n"
            "Install with \n\npip install numpy\n\nRequires CPython."
        )

    try:
        import pyvista as pv

        pyvista_available = True
    except ImportError:
        warnings.warn(
            "The PyVista module is required to run some functionalities of PostProcess.\n"
            "Install with \n\npip install pyvista\n\nRequires CPython."
        )

    try:
        import matplotlib.pyplot as plt
        from matplotlib.path import Path
        from matplotlib.patches import PathPatch
    except ImportError:
        warnings.warn(
            "The Matplotlib module is required to run some functionalities of PostProcess.\n"
            "Install with \n\npip install matplotlib\n\nRequires CPython."
        )
    except:
        pass


def is_notebook():
    """Check if pyaedt is running in Jupyter or not.

    Returns
    -------
    bool
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        else:
            return False
    except NameError:
        return False  # Probably standard Python interpreter


def is_float(istring):
    """Convert a string to a float.

    Parameters
    ----------
    istring : str
        String to convert to a float.

    Returns
    -------
    float
        Converted float when successful, ``0`` when when failed.
    """
    try:
        return float(istring.strip())
    except Exception:
        return 0


def plot_polar_chart(
    plot_data, size=(2000, 1000), show_legend=True, xlabel="", ylabel="", title="", snapshot_path=None
):
    """Create a matplotlib polar plot based on a list of data.

    Parameters
    ----------
    plot_data : list of list
        List of plot data. Every item has to be in the following format
        `[x points, y points, label]`.
    size : tuple, optional
        Image size in pixel (width, height).
    show_legend : bool
        Either to show legend or not.
    xlabel : str
        Plot X label.
    ylabel : str
        Plot Y label.
    title : str
        Plot Title label.
    snapshot_path : str
        Full path to image file if a snapshot is needed.
    """
    dpi = 100.0

    ax = plt.subplot(111, projection="polar")

    try:
        len(plot_data)
    except:
        plot_data = convert_remote_object(plot_data)

    label_id = 1
    legend = []
    for object in plot_data:
        if len(object) == 3:
            label = object[2]
        else:
            label = "Trace " + str(label_id)
        theta = np.array(object[0])
        r = np.array(object[1])
        ax.plot(theta, r)
        ax.grid(True)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        legend.append(label)
        label_id += 1

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    if show_legend:
        ax.legend(legend)

    fig = plt.gcf()
    fig.set_size_inches(size[0] / dpi, size[1] / dpi)
    if snapshot_path:
        fig.savefig(snapshot_path)
    else:
        fig.show()
    return True


def plot_3d_chart(plot_data, size=(2000, 1000), xlabel="", ylabel="", title="", snapshot_path=None):
    """Create a matplotlib 3D plot based on a list of data.

    Parameters
    ----------
    plot_data : list of list
        List of plot data. Every item has to be in the following format
        `[x points, y points, z points, label]`.
    size : tuple, optional
        Image size in pixel (width, height).
    xlabel : str
        Plot X label.
    ylabel : str
        Plot Y label.
    title : str
        Plot Title label.
    snapshot_path : str
        Full path to image file if a snapshot is needed.
    """
    dpi = 100.0
    dpi = 100.0

    ax = plt.subplot(111, projection="3d")

    try:
        len(plot_data)
    except:
        plot_data = convert_remote_object(plot_data)
    THETA, PHI = np.meshgrid(plot_data[0], plot_data[1])
    R = np.array(plot_data[2])
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("jet"), linewidth=0, antialiased=True, alpha=0.5)
    fig = plt.gcf()
    fig.set_size_inches(size[0] / dpi, size[1] / dpi)
    if snapshot_path:
        fig.savefig(snapshot_path)
    else:
        fig.show()
    return True


def plot_2d_chart(plot_data, size=(2000, 1000), show_legend=True, xlabel="", ylabel="", title="", snapshot_path=None):
    """Create a matplotlib plot based on a list of data.

    Parameters
    ----------
    plot_data : list of list
        List of plot data. Every item has to be in the following format
        `[x points, y points, label]`.
    size : tuple, optional
        Image size in pixel (width, height).
    show_legend : bool
        Either to show legend or not.
    xlabel : str
        Plot X label.
    ylabel : str
        Plot Y label.
    title : str
        Plot Title label.
    snapshot_path : str
        Full path to image file if a snapshot is needed.
    """
    dpi = 100.0
    figsize = (size[0] / dpi, size[1] / dpi)
    fig, ax = plt.subplots(figsize=figsize)
    try:
        len(plot_data)
    except:
        plot_data = convert_remote_object(plot_data)
    label_id = 1
    for object in plot_data:
        if len(object) == 3:
            label = object[2]
        else:
            label = "Trace " + str(label_id)
        ax.plot(np.array(object[0]), np.array(object[1]), label=label)
        label_id += 1

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    if show_legend:
        ax.legend()

    if snapshot_path:
        fig.savefig(snapshot_path)
    else:
        fig.show()
    return True


def plot_matplotlib(plot_data, size=(2000, 1000), show_legend=True, xlabel="", ylabel="", title="", snapshot_path=None):
    """Create a matplotlib plot based on a list of data.

    Parameters
    ----------
    plot_data : list of list
        List of plot data. Every item has to be in the following format
        `[x points, y points, color, alpha, label, type]`. type can be `fill` or `path`.
    size : tuple, optional
        Image size in pixel (width, height).
    show_legend : bool
        Either to show legend or not.
    xlabel : str
        Plot X label.
    ylabel : str
        Plot Y label.
    title : str
        Plot Title label.
    snapshot_path : str
        Full path to image file if a snapshot is needed.
    """
    dpi = 100.0
    figsize = (size[0] / dpi, size[1] / dpi)
    fig, ax = plt.subplots(figsize=figsize)
    try:
        len(plot_data)
    except:
        plot_data = convert_remote_object(plot_data)
    for object in plot_data:
        if object[-1] == "fill":
            plt.fill(object[0], object[1], c=object[2], label=object[3], alpha=object[4])
        elif object[-1] == "path":
            path = Path(object[0], object[1])
            patch = PathPatch(path, color=object[2], alpha=object[4], label=object[3])
            ax.add_patch(patch)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    if show_legend:
        ax.legend()
    ax.axis("equal")

    if snapshot_path:
        plt.savefig(snapshot_path)
    else:
        plt.show()


class ObjClass(object):
    """Class that manages mesh files to be plotted in pyvista.

    Parameters
    ----------
    path : str
        Full path to the file.
    color : str or tuple
        Can be a string with color name or a tuple with (r,g,b) values.
    opacity : float
        Value between 0 to 1 of opacity.
    units : str
        Model units.

    """

    def __init__(self, path, color, opacity, units):
        self.path = path
        self._color = (0, 0, 0)
        self.color = color
        self.opacity = opacity
        self.units = units
        self._cached_mesh = None
        self._cached_polydata = None
        self.name = os.path.splitext(os.path.basename(self.path))[0]

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, (tuple, list)):
            self._color = value
        elif value in CSS4_COLORS:
            h = CSS4_COLORS[value].lstrip("#")
            self._color = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


class FieldClass(object):
    """Class to manage Field data to be plotted in pyvista.

    Parameters
    ----------
    path : str
        Full path to the file.
    log_scale : bool, optional
        Either if the field has to be plotted log or not. The default value is ``True``.
    coordinate_units : str, optional
        Fields coordinates units. The default value is ``"meter"``.
    opacity : float, optional
        Value between 0 to 1 of opacity. The default value is ``1``.
    color_map : str, optional
        Color map of field plot. The default value is ``"rainbow"``.
    label : str, optional
        Name of the field. The default value is ``"Field"``.
    tolerance : float, optional
        Delauny tolerance value used for interpolating points. The default value is ``1e-3``.
    headers : int, optional
        Number of lines to of the file containing header info that has to be removed.
        The default value is ``2``.
    """

    def __init__(
        self,
        path,
        log_scale=True,
        coordinate_units="meter",
        opacity=1,
        color_map="rainbow",
        label="Field",
        tolerance=1e-3,
        headers=2,
        show_edge=True,
    ):
        self.path = path
        self.log_scale = log_scale
        self.units = coordinate_units
        self.opacity = opacity
        self.color_map = color_map
        self._cached_mesh = None
        self._cached_polydata = None
        self.label = label
        self.name = os.path.splitext(os.path.basename(self.path))[0]
        self.color = (255, 0, 0)
        self.surface_mapping_tolerance = tolerance
        self.header_lines = headers
        self.show_edge = show_edge
        self._is_frame = False


class ModelPlotter(object):
    """Class that manage the plot data.

    Examples
    --------
    This Class can be instantiated within Pyaedt (with plot_model_object or different field plots
    and standalone.
    Here an example of standalone project

    >>> model = ModelPlotter()
    >>> model.add_object(r'D:\Simulation\antenna.obj', (200,20,255), 0.6, "in")
    >>> model.add_object(r'D:\Simulation\helix.obj', (0,255,0), 0.5, "in")
    >>> model.add_field_from_file(r'D:\Simulation\helic_antenna.csv', True, "meter", 1)
    >>> model.background_color = (0,0,0)
    >>> model.plot()

    And here an example of animation:

    >>> model = ModelPlotter()
    >>> model.add_object(r'D:\Simulation\antenna.obj', (200,20,255), 0.6, "in")
    >>> model.add_object(r'D:\Simulation\helix.obj', (0,255,0), 0.5, "in")
    >>> frames = [r'D:\Simulation\helic_antenna.csv', r'D:\Simulation\helic_antenna_10.fld',
    >>>           r'D:\Simulation\helic_antenna_20.fld', r'D:\Simulation\helic_antenna_30.fld',
    >>>           r'D:\Simulation\helic_antenna_40.fld']
    >>> model.gif_file = r"D:\Simulation\animation.gif"
    >>> model.animate()
    """

    def __init__(self):
        self._objects = []
        self._fields = []
        self._frames = []
        self.show_axes = True
        self.show_legend = True
        self.show_grid = True
        self.is_notebook = is_notebook()
        self.gif_file = None
        self._background_color = (255, 255, 255)
        self.off_screen = False
        self.windows_size = [1024, 768]
        self.pv = None
        self._orientation = ["xy", 0, 0, 0]
        self.units = "meter"
        self.frame_per_seconds = 3
        self._plot_meshes = []
        self.range_min = None
        self.range_max = None
        self.image_file = None
        self._camera_position = "yz"
        self._roll_angle = 0
        self._azimuth_angle = 45
        self._elevation_angle = 20
        self._zoom = 1
        self._isometric_view = True
        self.bounding_box = True
        self.color_bar = True

    @property
    def isometric_view(self):
        """Enable or disable the default iso view.

        Parameters
        ----------
        value : bool
            Either if iso view is enabled or disabled.

        Returns
        -------
        bool
        """
        return self._isometric_view

    @isometric_view.setter
    def isometric_view(self, value=True):
        self._isometric_view = value

    @property
    def camera_position(self):
        """Get/Set the camera position value. It disables the default iso view.

        Parameters
        ----------
        value : str
            Value of camera position. One of `"xy"`, `"xz"`,`"yz"`.

        Returns
        -------
        str
        """
        return self._camera_position

    @camera_position.setter
    def camera_position(self, value):
        self._camera_position = value
        self.isometric_view = False

    @property
    def roll_angle(self):
        """Get/Set the roll angle value. It disables the default iso view.

        Parameters
        ----------
        value : float
            Value of roll angle in degrees.

        Returns
        -------
        float
        """
        return self._roll_angle

    @roll_angle.setter
    def roll_angle(self, value=20):
        self._roll_angle = value
        self.isometric_view = False

    @property
    def azimuth_angle(self):
        """Get/Set the azimuth angle value. It disables the default iso view.

        Parameters
        ----------
        value : float
            Value of azimuth angle in degrees.

        Returns
        -------
        float
        """
        return self._azimuth_angle

    @azimuth_angle.setter
    def azimuth_angle(self, value=45):
        self._azimuth_angle = value
        self.use_default_iso_view = False

    @property
    def elevation_angle(self):
        """Get/Set the elevation angle value. It disables the default iso view.

        Parameters
        ----------
        value : float
            Value of elevation angle in degrees.

        Returns
        -------
        float
        """
        return self._elevation_angle

    @elevation_angle.setter
    def elevation_angle(self, value=45):
        self._elevation_angle = value
        self.use_default_iso_view = False

    @property
    def zoom(self):
        """Get/Set the zoom value.

        Parameters
        ----------
        value : float
            Value of zoom in degrees.

        Returns
        -------
        float
        """
        return self._zoom

    @zoom.setter
    def zoom(self, value=1):
        self._zoom = value

    @pyaedt_function_handler()
    def set_orientation(self, camera_position="xy", roll_angle=0, azimuth_angle=45, elevation_angle=20):
        """Change the plot default orientation.

        Parameters
        ----------
        camera_position : str
            Camera view. Default is `"xy"`. Options are `"xz"` and `"yz"`.
        roll_angle : int, float
            Roll camera angle on the specified the camera_position.
        azimuth_angle : int, float
            Azimuth angle of camera on the specified the camera_position.
        elevation_angle : int, float
            Elevation camera angle on the specified the camera_position.

        Returns
        -------
        bool
        """
        if camera_position in ["xy", "yz", "xz"]:
            self.camera_position = camera_position
        else:
            warnings.warn("Plane has to be one of xy, xz, yz.")
        self.roll_angle = roll_angle
        self.azimuth_angle = azimuth_angle
        self.elevation_angle = elevation_angle
        self.use_default_iso_view = False
        return True

    @property
    def background_color(self):
        """Get/Set Backgroun Color.
        It can be a tuple of (r,g,b)  or color name."""
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if isinstance(value, (tuple, list)):
            self._background_color = value
        elif value in CSS4_COLORS:
            h = CSS4_COLORS[value].lstrip("#")
            self._background_color = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    @property
    def fields(self):
        """List of fields object.

        Returns
        -------
        list of :class:`pyaedt.modules.AdvancedPostProcessing.FieldClass`
        """
        return self._fields

    @property
    def frames(self):
        """Frames list for animation.

        Returns
        -------
        list of :class:`pyaedt.modules.AdvancedPostProcessing.FieldClass`
        """
        return self._frames

    @property
    def objects(self):
        """List of class objects.

        Returns
        -------
        list of :class:`pyaedt.modules.AdvancedPostProcessing.ObjClass`
        """
        return self._objects

    @pyaedt_function_handler()
    def add_object(self, cad_path, cad_color="dodgerblue", opacity=1, units="mm"):
        """Add an mesh file to the scenario. It can be obj or any of pyvista supported files.

        Parameters
        ----------
        cad_path : str
            Full path to the file.
        cad_color : str or tuple
            Can be a string with color name or a tuple with (r,g,b) values.
            The default value is ``"dodgerblue"``.
        opacity : float
            Value between 0 to 1 of opacity. The default value is ``1``.
        units : str
            Model units. The default value is ``"mm"``.

        Returns
        -------
        bool
        """
        self._objects.append(ObjClass(cad_path, cad_color, opacity, units))
        self.units = units
        return True

    @pyaedt_function_handler()
    def add_field_from_file(
        self,
        field_path,
        log_scale=True,
        coordinate_units="meter",
        opacity=1,
        color_map="rainbow",
        label_name="Field",
        surface_mapping_tolerance=1e-3,
        header_lines=2,
        show_edges=True,
    ):
        """Add a field file to the scenario.
        It can be aedtplt, fld or csv file or any txt file with 4 column [x,y,z,field].
        If text file they have to be space separated column.

        Parameters
        ----------
        field_path : str
            Full path to the file.
        log_scale : bool
            Either if the field has to be plotted log or not.
        coordinate_units : str
            Fields coordinates units.
        opacity : float
            Value between 0 to 1 of opacity.
        color_map : str
            Color map of field plot. Default rainbow.
        label_name : str, optional
            Name of the field.
        surface_mapping_tolerance : float, optional
            Delauny tolerance value used for interpolating points.
        header_lines : int
            Number of lines to of the file containing header info that has to be removed.

        Returns
        -------
        bool
        """
        self._fields.append(
            FieldClass(
                field_path,
                log_scale,
                coordinate_units,
                opacity,
                color_map,
                label_name,
                surface_mapping_tolerance,
                header_lines,
                show_edges,
            )
        )

    @pyaedt_function_handler()
    def add_frames_from_file(
        self,
        field_files,
        log_scale=True,
        coordinate_units="meter",
        opacity=1,
        color_map="rainbow",
        label_name="Field",
        surface_mapping_tolerance=1e-3,
        header_lines=2,
    ):
        """Add a field file to the scenario. It can be aedtplt, fld or csv file.

        Parameters
        ----------
        field_files : list
            List of full path to frame file.
        log_scale : bool
            Either if the field has to be plotted log or not.
        coordinate_units : str
            Fields coordinates units.
        opacity : float
            Value between 0 to 1 of opacity.
        color_map : str
            Color map of field plot. Default rainbow.
        label_name : str, optional
            Name of the field.
        surface_mapping_tolerance : float, optional
            Delauny tolerance value used for interpolating points.
        header_lines : int
            Number of lines to of the file containing header info that has to be removed.
        Returns
        -------
        bool
        """
        for field in field_files:
            self._frames.append(
                FieldClass(
                    field,
                    log_scale,
                    coordinate_units,
                    opacity,
                    color_map,
                    label_name,
                    surface_mapping_tolerance,
                    header_lines,
                    False,
                )
            )
            self._frames[-1]._is_frame = True

    @pyaedt_function_handler()
    def add_field_from_data(
        self,
        coordinates,
        fields_data,
        log_scale=True,
        coordinate_units="meter",
        opacity=1,
        color_map="rainbow",
        label_name="Field",
        surface_mapping_tolerance=1e-3,
        show_edges=True,
    ):
        """Add field data to the scenario.

        Parameters
        ----------
        coordinates : list of list
            List of list [x,y,z] coordinates.
        fields_data : list
            List of list Fields Value.
        log_scale : bool
            Either if the field has to be plotted log or not.
        coordinate_units : str
            Fields coordinates units.
        opacity : float
            Value between 0 to 1 of opacity.
        color_map : str
            Color map of field plot. Default rainbow.
        label_name : str, optional
            Name of the field.
        surface_mapping_tolerance : float, optional
            Delauny tolerance value used for interpolating points.

        Returns
        -------
        bool
        """
        self._fields.append(
            FieldClass(
                None, log_scale, coordinate_units, opacity, color_map, label_name, surface_mapping_tolerance, show_edges
            )
        )
        vertices = np.array(coordinates)
        filedata = pv.PolyData(vertices)
        filedata = filedata.delaunay_2d(tol=surface_mapping_tolerance)
        filedata.point_data[self.fields[-1].label] = np.array(fields_data)
        self.fields[-1]._cached_polydata = filedata

    @pyaedt_function_handler()
    def _triangle_vertex(self, elements_nodes, num_nodes_per_element, take_all_nodes=True):
        trg_vertex = []
        if num_nodes_per_element == 10 and take_all_nodes:
            for e in elements_nodes:
                trg_vertex.append([e[0], e[1], e[3]])
                trg_vertex.append([e[1], e[2], e[4]])
                trg_vertex.append([e[1], e[4], e[3]])
                trg_vertex.append([e[3], e[4], e[5]])

                trg_vertex.append([e[9], e[6], e[8]])
                trg_vertex.append([e[6], e[0], e[3]])
                trg_vertex.append([e[6], e[3], e[8]])
                trg_vertex.append([e[8], e[3], e[5]])

                trg_vertex.append([e[9], e[7], e[8]])
                trg_vertex.append([e[7], e[2], e[4]])
                trg_vertex.append([e[7], e[4], e[8]])
                trg_vertex.append([e[8], e[4], e[5]])

                trg_vertex.append([e[9], e[7], e[6]])
                trg_vertex.append([e[7], e[2], e[1]])
                trg_vertex.append([e[7], e[1], e[6]])
                trg_vertex.append([e[6], e[1], e[0]])
        elif num_nodes_per_element == 10 and not take_all_nodes:
            for e in elements_nodes:
                trg_vertex.append([e[0], e[2], e[5]])
                trg_vertex.append([e[9], e[0], e[5]])
                trg_vertex.append([e[9], e[2], e[0]])
                trg_vertex.append([e[9], e[2], e[5]])

        elif num_nodes_per_element == 6 and not take_all_nodes:
            for e in elements_nodes:
                trg_vertex.append([e[0], e[2], e[5]])

        elif num_nodes_per_element == 6 and take_all_nodes:
            for e in elements_nodes:
                trg_vertex.append([e[0], e[1], e[3]])
                trg_vertex.append([e[1], e[2], e[4]])
                trg_vertex.append([e[1], e[4], e[3]])
                trg_vertex.append([e[3], e[4], e[5]])

        elif num_nodes_per_element == 4 and take_all_nodes:
            for e in elements_nodes:
                trg_vertex.append([e[0], e[1], e[3]])
                trg_vertex.append([e[1], e[2], e[3]])
                trg_vertex.append([e[0], e[1], e[2]])
                trg_vertex.append([e[0], e[2], e[3]])

        elif num_nodes_per_element == 3:
            trg_vertex = elements_nodes

        return trg_vertex

    @pyaedt_function_handler()
    def _read_mesh_files(self, read_frames=False):
        for cad in self.objects:
            if not cad._cached_polydata:
                filedata = pv.read(cad.path)
                cad._cached_polydata = filedata
            color_cad = [i / 255 for i in cad.color]
            cad._cached_mesh = self.pv.add_mesh(cad._cached_polydata, color=color_cad, opacity=cad.opacity)
        obj_to_iterate = [i for i in self._fields]
        if read_frames:
            for i in self.frames:
                obj_to_iterate.append(i)
        for field in obj_to_iterate:
            if field.path and not field._cached_polydata:
                if ".aedtplt" in field.path:
                    lines = []
                    with open(field.path, "r") as f:
                        drawing_found = False
                        for line in f:
                            if "$begin Drawing" in line:
                                drawing_found = True
                                l_tmp = []
                                continue
                            if "$end Drawing" in line:
                                lines.append(l_tmp)
                                drawing_found = False
                                continue
                            if drawing_found:
                                l_tmp.append(line)
                                continue
                    surf = None
                    for drawing_lines in lines:
                        bounding = []
                        elements = []
                        nodes_list = []
                        solution = []
                        for l in drawing_lines:
                            if "BoundingBox(" in l:
                                bounding = l[l.find("(") + 1 : -2].split(",")
                                bounding = [i.strip() for i in bounding]
                            if "Elements(" in l:
                                elements = l[l.find("(") + 1 : -2].split(",")
                                elements = [int(i.strip()) for i in elements]
                            if "Nodes(" in l:
                                nodes_list = l[l.find("(") + 1 : -2].split(",")
                                nodes_list = [float(i.strip()) for i in nodes_list]
                            if "ElemSolution(" in l:
                                # convert list of strings to list of floats
                                sols = l[l.find("(") + 1 : -2].split(",")
                                sols = [is_float(value) for value in sols]

                                # sols = [float(i.strip()) for i in sols]
                                num_solution_per_element = int(sols[2])
                                sols = sols[3:]
                                sols = [
                                    sols[i : i + num_solution_per_element]
                                    for i in range(0, len(sols), num_solution_per_element)
                                ]
                                solution = [sum(i) / num_solution_per_element for i in sols]

                        nodes = [
                            [nodes_list[i], nodes_list[i + 1], nodes_list[i + 2]] for i in range(0, len(nodes_list), 3)
                        ]
                        num_nodes = elements[0]
                        num_elements = elements[1]
                        elements = elements[2:]
                        element_type = elements[0]
                        num_nodes_per_element = elements[4]
                        hl = 5  # header length
                        elements_nodes = []
                        for i in range(0, len(elements), num_nodes_per_element + hl):
                            elements_nodes.append([elements[i + hl + n] for n in range(num_nodes_per_element)])
                        if solution:
                            take_all_nodes = True  # solution case
                        else:
                            take_all_nodes = False  # mesh case
                        trg_vertex = self._triangle_vertex(elements_nodes, num_nodes_per_element, take_all_nodes)
                        # remove duplicates
                        nodup_list = [list(i) for i in list(set([frozenset(t) for t in trg_vertex]))]
                        sols_vertex = []
                        if solution:
                            sv = {}
                            for els, s in zip(elements_nodes, solution):
                                for el in els:
                                    if el in sv:
                                        sv[el] = (sv[el] + s) / 2
                                    else:
                                        sv[el] = s
                            sols_vertex = [sv[v] for v in sorted(sv.keys())]
                        array = [[3] + [j - 1 for j in i] for i in nodup_list]
                        faces = np.hstack(array)
                        vertices = np.array(nodes)
                        surf = pv.PolyData(vertices, faces)
                        if sols_vertex:
                            temps = np.array(sols_vertex)
                            mean = np.mean(temps)
                            std = np.std(temps)
                            if np.min(temps) > 0:
                                log = True
                            else:
                                log = False
                            surf.point_data[field.label] = temps
                    field.log = log
                    field._cached_polydata = surf
                else:
                    points = []
                    nodes = []
                    values = []
                    with open(field.path, "r") as f:
                        try:
                            lines = f.read().splitlines()[field.header_lines :]
                            if ".csv" in field.path:
                                sniffer = csv.Sniffer()
                                delimiter = sniffer.sniff(lines[0]).delimiter
                            else:
                                delimiter = " "
                            if len(lines) > 2000 and not field._is_frame:
                                lines = list(dict.fromkeys(lines))
                                # decimate = 2
                                # del lines[decimate - 1 :: decimate]
                        except:
                            lines = []
                        for line in lines:
                            tmp = line.split(delimiter)
                            nodes.append([float(tmp[0]), float(tmp[1]), float(tmp[2])])
                            values.append(float(tmp[3]))
                    if nodes:
                        try:
                            conv = 1 / AEDT_UNITS["Length"][self.units]
                        except:
                            conv = 1
                        vertices = np.array(nodes) * conv
                        filedata = pv.PolyData(vertices)
                        filedata = filedata.delaunay_2d(tol=field.surface_mapping_tolerance)
                        filedata.point_data[field.label] = np.array(values)
                        field._cached_polydata = filedata

    @pyaedt_function_handler()
    def _add_buttons(self):
        size = int(self.pv.window_size[1] / 40)
        startpos = self.pv.window_size[1] - 2 * size
        endpos = 100
        color = self.pv.background_color
        axes_color = [0 if i >= 0.5 else 1 for i in color]
        buttons = []
        texts = []
        max_elements = (startpos - endpos) // (size + (size // 10))

        class SetVisibilityCallback:
            """Helper callback to keep a reference to the actor being modified."""

            def __init__(self, actor):
                self.actor = actor

            def __call__(self, state):
                self.actor.SetVisibility(state)

        class ChangePageCallback:
            """Helper callback to keep a reference to the actor being modified."""

            def __init__(self, plot, actor, axes_color):
                self.plot = plot
                self.actors = actor
                self.id = 0
                self.endpos = 100
                self.size = int(plot.window_size[1] / 40)
                self.startpos = plot.window_size[1] - 2 * self.size
                self.max_elements = (self.startpos - self.endpos) // (self.size + (self.size // 10))
                self.i = self.max_elements
                self.axes_color = axes_color

            def __call__(self, state):
                self.plot.button_widgets = [self.plot.button_widgets[0]]
                self.id += 1
                k = 0
                startpos = self.startpos
                while k < self.max_elements:
                    if len(self.text) > k:
                        self.plot.remove_actor(self.text[k])
                    k += 1
                self.text = []
                k = 0

                while k < self.max_elements:
                    if self.i >= len(self.actors):
                        self.i = 0
                        self.id = 0
                    callback = SetVisibilityCallback(self.actors[self.i])
                    self.plot.add_checkbox_button_widget(
                        callback,
                        value=self.actors[self.i]._cached_mesh.GetVisibility() == 1,
                        position=(5.0, startpos),
                        size=self.size,
                        border_size=1,
                        color_on=[i / 255 for i in self.actors[self.i].color],
                        color_off="grey",
                        background_color=None,
                    )
                    self.text.append(
                        self.plot.add_text(
                            self.actors[self.i].name,
                            position=(25.0, startpos),
                            font_size=self.size // 3,
                            color=self.axes_color,
                        )
                    )
                    startpos = startpos - self.size - (self.size // 10)
                    k += 1
                    self.i += 1

        el = 1
        for actor in self.objects:
            if el < max_elements:
                callback = SetVisibilityCallback(actor._cached_mesh)
                buttons.append(
                    self.pv.add_checkbox_button_widget(
                        callback,
                        value=True,
                        position=(5.0, startpos + 50),
                        size=size,
                        border_size=1,
                        color_on=[i / 255 for i in actor.color],
                        color_off="grey",
                        background_color=None,
                    )
                )
                texts.append(
                    self.pv.add_text(actor.name, position=(50.0, startpos + 50), font_size=size // 3, color=axes_color)
                )
                startpos = startpos - size - (size // 10)
                el += 1
        for actor in self.fields:
            if actor._cached_mesh and el < max_elements:
                callback = SetVisibilityCallback(actor._cached_mesh)
                buttons.append(
                    self.pv.add_checkbox_button_widget(
                        callback,
                        value=True,
                        position=(5.0, startpos + 50),
                        size=size,
                        border_size=1,
                        color_on="blue",
                        color_off="grey",
                        background_color=None,
                    )
                )
                texts.append(
                    self.pv.add_text(actor.name, position=(50.0, startpos + 50), font_size=size // 3, color=axes_color)
                )
                startpos = startpos - size - (size // 10)
                el += 1
        actors = [i for i in self._fields if i._cached_mesh] + self._objects
        if texts and len(texts) >= max_elements:
            callback = ChangePageCallback(self.pv, actors, axes_color)
            self.pv.add_checkbox_button_widget(
                callback,
                value=True,
                position=(5.0, self.pv.window_size[1]),
                size=int(1.5 * size),
                border_size=2,
                color_on=axes_color,
                color_off=axes_color,
            )
            self.pv.add_text("Next", position=(50.0, self.pv.window_size[1]), font_size=size // 3, color="grey")
            self.pv.button_widgets.insert(
                0, self.pv.button_widgets.pop(self.pv.button_widgets.index(self.pv.button_widgets[-1]))
            )

    @pyaedt_function_handler()
    def plot(self, export_image_path=None):
        """Plot the current available Data. With `s` key a screenshot is saved in export_image_path or in tempdir.

        Parameters
        ----------

        export_image_path : str
            Path to image to save.

        Returns
        -------
        bool
        """
        start = time.time()
        self.pv = pv.Plotter(notebook=self.is_notebook, off_screen=self.off_screen, window_size=self.windows_size)
        self.pv.background_color = [i / 255 for i in self.background_color]
        self._read_mesh_files()

        axes_color = [0 if i >= 128 else 1 for i in self.background_color]
        if self.color_bar:
            sargs = dict(
                title_font_size=10,
                label_font_size=10,
                shadow=True,
                n_labels=9,
                italic=True,
                fmt="%.1f",
                font_family="arial",
                interactive=True,
                color=axes_color,
                vertical=False,
            )
        else:
            sargs = dict(
                position_x=2,
                position_y=2,
            )
        for field in self._fields:
            if self.range_max is not None and self.range_min is not None:
                field._cached_mesh = self.pv.add_mesh(
                    field._cached_polydata,
                    scalars=field.label,
                    log_scale=field.log_scale,
                    scalar_bar_args=sargs,
                    cmap=field.color_map,
                    clim=[self.range_min, self.range_max],
                    opacity=field.opacity,
                    show_edges=field.show_edge,
                )
            else:
                field._cached_mesh = self.pv.add_mesh(
                    field._cached_polydata,
                    scalars=field.label,
                    log_scale=field.log_scale,
                    scalar_bar_args=sargs,
                    cmap=field.color_map,
                    opacity=field.opacity,
                    show_edges=field.show_edge,
                )
        if self.show_legend:
            self._add_buttons()
        end = time.time() - start
        files_list = []
        if self.show_axes:
            self.pv.show_axes()
        if self.show_grid and not self.is_notebook:
            self.pv.show_grid(color=tuple(axes_color))
        if self.bounding_box:
            self.pv.add_bounding_box(color=tuple(axes_color))
        self.pv.set_focus(self.pv.mesh.center)

        if not self.isometric_view:
            self.pv.camera_position = self.camera_position
            self.pv.camera.azimuth += self.azimuth_angle
            self.pv.camera.roll += self.roll_angle
            self.pv.camera.elevation += self.elevation_angle
        else:
            self.pv.isometric_view()
        self.pv.camera.zoom(self.zoom)
        if export_image_path:
            path_image = os.path.dirname(export_image_path)
            root_name, format = os.path.splitext(os.path.basename(export_image_path))
        else:
            path_image = tempfile.gettempdir()  # pragma: no cover
            format = ".png"  # pragma: no cover
            root_name = "Image"  # pragma: no cover

        def s_callback():  # pragma: no cover
            """save screenshots"""
            exp = os.path.join(
                path_image, "{}{}{}".format(root_name, datetime.now().strftime("%Y_%M_%d_%H-%M-%S"), format)
            )
            self.pv.screenshot(exp, return_img=False)

        self.pv.add_key_event("s", s_callback)
        if export_image_path:
            self.pv.show(screenshot=export_image_path, full_screen=True)
        elif self.is_notebook:  # pragma: no cover
            self.pv.show()  # pragma: no cover
        else:
            self.pv.show(full_screen=True)  # pragma: no cover

        self.image_file = export_image_path
        return True

    @pyaedt_function_handler()
    def clean_cache_and_files(self, remove_objs=True, remove_fields=True, clean_cache=False):
        """Clean downloaded files, and, on demand, also the cached meshes.

        Parameters
        ----------
        remove_objs : bool
        remove_fields : bool
        clean_cache : bool

        Returns
        -------
        bool
        """
        if remove_objs:
            for el in self.objects:
                if os.path.exists(el.path):
                    os.remove(el.path)
                if clean_cache:
                    el._cached_mesh = None
                    el._cached_polydata = None
        if remove_fields:
            for el in self.fields:
                if os.path.exists(el.path):
                    os.remove(el.path)
                if clean_cache:
                    el._cached_mesh = None
                    el._cached_polydata = None
        return True

    @pyaedt_function_handler()
    def animate(self):
        """Animate the current field plot.

        Returns
        -------
        bool
        """
        start = time.time()
        assert len(self.frames) > 0, "Number of Fields have to be greater than 1 to do an animation."
        if self.is_notebook:
            self.pv = pv.Plotter(notebook=self.is_notebook, off_screen=True, window_size=self.windows_size)
        else:
            self.pv = pv.Plotter(notebook=self.is_notebook, off_screen=self.off_screen, window_size=self.windows_size)

        self.pv.background_color = [i / 255 for i in self.background_color]
        self._read_mesh_files(read_frames=True)
        end = time.time() - start
        files_list = []
        axes_color = [0 if i >= 128 else 1 for i in self.background_color]

        if self.show_axes:
            self.pv.show_axes()
        if self.show_grid and not self.is_notebook:
            self.pv.show_grid(color=tuple(axes_color))
        if self.bounding_box:
            self.pv.add_bounding_box(color=tuple(axes_color))
        if self.show_legend:
            labels = []
            for m in self.objects:
                labels.append([m.name, [i / 255 for i in m.color]])
            for m in self.fields:
                labels.append([m.name, "red"])
            self.pv.add_legend(labels=labels, bcolor=None, face="circle", size=[0.15, 0.15])
        if not self.isometric_view:
            self.pv.camera_position = self.camera_position
            self.pv.camera.azimuth += self.azimuth_angle
            self.pv.camera.roll += self.roll_angle
            self.pv.camera.elevation += self.elevation_angle
        else:
            self.pv.isometric_view()
        self.pv.zoom = self.zoom
        self._animating = True

        if self.gif_file:
            self.pv.open_gif(self.gif_file)

        def q_callback():
            """exit when user wants to leave"""
            self._animating = False

        self._pause = False

        def p_callback():
            """exit when user wants to leave"""
            self._pause = not self._pause

        self.pv.add_text(
            "Press p for Play/Pause, Press q to exit ", font_size=8, position="upper_left", color=tuple(axes_color)
        )
        self.pv.add_text(" ", font_size=10, position=[0, 0], color=tuple(axes_color))
        self.pv.add_key_event("q", q_callback)
        self.pv.add_key_event("p", p_callback)
        if self.color_bar:
            sargs = dict(
                title_font_size=10,
                label_font_size=10,
                shadow=True,
                n_labels=9,
                italic=True,
                fmt="%.1f",
                font_family="arial",
            )
        else:
            sargs = dict(
                position_x=2,
                position_y=2,
            )

        for field in self._fields:
            field._cached_mesh = self.pv.add_mesh(
                field._cached_polydata,
                scalars=field.label,
                log_scale=field.log_scale,
                scalar_bar_args=sargs,
                cmap=field.color_map,
                opacity=field.opacity,
            )
        # run until q is pressed
        if self.pv.mesh:
            self.pv.set_focus(self.pv.mesh.center)

        cpos = self.pv.show(interactive=False, auto_close=False, interactive_update=not self.off_screen)

        if self.range_min is not None and self.range_max is not None:
            mins = self.range_min
            maxs = self.range_max
        else:
            mins = 1e20
            maxs = -1e20
            for el in self.frames:
                if np.min(el._cached_polydata.point_data[el.label]) < mins:
                    mins = np.min(el._cached_polydata.point_data[el.label])
                if np.max(el._cached_polydata.point_data[el.label]) > maxs:
                    maxs = np.max(el._cached_polydata.point_data[el.label])

        self.frames[0]._cached_mesh = self.pv.add_mesh(
            self.frames[0]._cached_polydata,
            scalars=self.frames[0].label,
            log_scale=self.frames[0].log_scale,
            scalar_bar_args=sargs,
            cmap=self.frames[0].color_map,
            clim=[mins, maxs],
            show_edges=False,
            pickable=True,
            smooth_shading=True,
            name="FieldPlot",
            opacity=self.frames[0].opacity,
        )
        start = time.time()

        self.pv.update(1, force_redraw=True)
        if self.gif_file:
            first_loop = True
            self.pv.write_frame()
        else:
            first_loop = False
        i = 1
        while self._animating:
            if self._pause:
                time.sleep(1)
                self.pv.update(1, force_redraw=True)
                continue
            # p.remove_actor("FieldPlot")
            if i >= len(self.frames):
                if self.off_screen or self.is_notebook:
                    break
                i = 0
                first_loop = False
            scalars = self.frames[i]._cached_polydata.point_data[self.frames[i].label]
            self.pv.update_scalars(scalars, render=False)
            if not hasattr(self.pv, "ren_win"):
                break
            time.sleep(max(0, (1 / self.frame_per_seconds) - (time.time() - start)))
            start = time.time()
            if self.off_screen:
                self.pv.render()
            else:
                self.pv.update(1, force_redraw=True)
            if first_loop:
                self.pv.write_frame()
            i += 1
        self.pv.close()
        if self.gif_file:
            return self.gif_file
        else:
            return True
