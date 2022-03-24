import numpy as np
import trimesh
from compas.colors import Color
from compas.datastructures import Mesh
from compas.datastructures import Network
from compas.geometry import Shape


class App(trimesh.Scene):

    def add(self, item, **kwargs):
        geometries = self.to_trimesh_geometries(item, **kwargs)
        for geometry in geometries:
            super().add_geometry(geometry)

    def convert_shape(self, shape: Shape, **kwargs):
        mesh = Mesh.from_shape(shape)
        return self.convert_mesh(mesh, **kwargs)

    def convert_network(self, network: Network, pointcolor: Color = Color.black(), linecolor: Color = Color.grey(),
                        show_points: bool = True, show_lines: bool = True,
                        pointsize: float = 0.1, linewidth: float = 1):

        geometries = []

        vertices = []
        for node in network.nodes():
            vertices.append(network.node_attributes(node, 'xyz'))

        if show_lines:
            lines = []
            for v1, v2 in network.edges():
                line = trimesh.path.entities.Line(points=[v1, v2])
                lines.append(line)
            path = trimesh.path.Path3D(vertices=vertices, entities=lines, process=False)
            path.colors = [linecolor] * len(path.entities)
            geometries.append(path)

        if show_points:
            for vertex in vertices:
                sphere = trimesh.creation.uv_sphere(radius=pointsize)
                sphere.apply_translation(vertex)
                sphere.visual.vertex_colors = trimesh.visual.to_rgba(pointcolor)
                geometries.append(sphere)

        return geometries

    def convert_mesh(self, mesh: Mesh, facecolor: Color = Color.white(), pointcolor: Color = Color.black(), linecolor: Color = Color.grey(),
                     show_points: bool = False, show_lines: bool = True, show_faces: bool = True,
                     pointsize: float = 0.1, linewidth: float = 1):

        geometries = []

        vertices, faces = mesh.to_vertices_and_faces()
        if show_faces:
            faces = np.array(faces)
            faces_backside = np.flip(faces, axis=1)
            faces_backside = np.roll(faces_backside, 1, axis=1)
            faces = np.concatenate((faces, faces_backside), axis=0)
            _faces = trimesh.Trimesh(vertices=vertices, faces=faces)
            if facecolor:
                _faces.visual.face_colors = trimesh.visual.to_rgba(facecolor)

            geometries.append(_faces)

        if show_lines:
            lines = []
            for v1, v2 in mesh.edges():
                line = trimesh.path.entities.Line(points=[v1, v2])
                lines.append(line)
            path = trimesh.path.Path3D(vertices=vertices, entities=lines, process=False)
            path.colors = [linecolor] * len(path.entities)
            geometries.append(path)

        if show_points:
            for vertex in vertices:
                sphere = trimesh.creation.uv_sphere(radius=pointsize)
                sphere.apply_translation(vertex)
                sphere.visual.vertex_colors = trimesh.visual.to_rgba(pointcolor)
                geometries.append(sphere)

        return geometries

    def to_trimesh_geometries(self, item, **kwargs):

        if isinstance(item, Mesh):
            return self.convert_mesh(item, **kwargs)
        elif isinstance(item, Network):
            return self.convert_network(item, **kwargs)
        elif isinstance(item, Shape):
            return self.convert_shape(item, **kwargs)
        else:
            raise NotImplementedError
