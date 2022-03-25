import numpy as np
import trimesh
from compas.colors import Color
from compas.datastructures import Mesh
from compas.datastructures import Network
from compas.geometry import Shape
from typing import Union, Dict


class App(trimesh.Scene):

    def add(self, item, **kwargs):
        geometries = self.to_trimesh_geometries(item, **kwargs)
        for geometry in geometries:
            super().add_geometry(geometry)

    def convert_shape(self, shape: Shape, **kwargs):
        mesh = Mesh.from_shape(shape)
        return self.convert_mesh(mesh, **kwargs)

    def convert_network(self, network: Network,
                        pointcolor: Union[Dict[str, Color], Color] = Color.black(), linecolor: Union[Dict[str, Color], Color] = Color.grey(),
                        show_points: bool = True, show_lines: bool = True,
                        pointsize: float = 0.1):

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

    def convert_mesh(self, mesh: Mesh,
                     facecolor: Union[Dict[str, Color], Color] = Color.white(),
                     pointcolor: Union[Dict[str, Color], Color] = Color.black(),
                     linecolor: Union[Dict[str, Color], Color] = Color.grey(),
                     show_points: bool = False, show_lines: bool = True, show_faces: bool = True,
                     pointsize: float = 0.1):

        geometries = []

        vertices, faces = mesh.to_vertices_and_faces()
        if show_faces:

            if isinstance(facecolor, dict):
                facecolor = [facecolor[face] for face in mesh.faces()]
            else:
                facecolor = [facecolor for _ in mesh.faces()]

            tri_vertices = []
            tri_faces = []
            tri_face_colors = []
            vi = 0
            for i, face in enumerate(faces):
                if len(face) == 4:
                    tri_vertices.append(vertices[face[0]])
                    tri_vertices.append(vertices[face[1]])
                    tri_vertices.append(vertices[face[2]])
                    tri_vertices.append(vertices[face[2]])
                    tri_vertices.append(vertices[face[3]])
                    tri_vertices.append(vertices[face[0]])
                    tri_faces.append([vi, vi+1, vi+2])
                    tri_faces.append([vi+3, vi+4, vi+5])
                    tri_face_colors.append(facecolor[i])
                    tri_face_colors.append(facecolor[i])
                    vi += 6
                elif len(face) == 3:
                    tri_vertices.append(vertices[face[0]])
                    tri_vertices.append(vertices[face[1]])
                    tri_vertices.append(vertices[face[2]])
                    tri_faces.append([vi, vi+1, vi+2])
                    tri_face_colors.append(facecolor[i])
                    vi += 3
                else:
                    raise NotImplementedError("Only triangular and quad faces are supported.")

            tri_face_colors += tri_face_colors
            tri_face_colors = trimesh.visual.to_rgba(tri_face_colors)
            tri_faces = np.array(tri_faces, dtype=int)
            tri_faces_backside = np.flip(tri_faces, axis=1)
            tri_faces = np.concatenate((tri_faces, tri_faces_backside), axis=0)
            _faces = trimesh.Trimesh(vertices=tri_vertices, faces=tri_faces, process=False)
            _faces.visual.face_colors = tri_face_colors

            geometries.append(_faces)

        if show_lines:
            lines = []
            if isinstance(linecolor, dict):
                pass
            else:
                linecolor = {edge: linecolor for edge in mesh.edges()}
            linecolors = []
            for v1, v2 in mesh.edges():
                line = trimesh.path.entities.Line(points=[v1, v2])
                lines.append(line)
                linecolors.append(linecolor[(v1, v2)])
            path = trimesh.path.Path3D(vertices=vertices, entities=lines, process=False)
            path.colors = linecolors
            geometries.append(path)

        if show_points:
            if isinstance(pointcolor, dict):
                pass
            else:
                pointcolor = {vertex: pointcolor for vertex in mesh.vertices()}
            for vertex in mesh.vertices():
                xyz = mesh.vertex_attributes(vertex, "xyz")
                sphere = trimesh.creation.uv_sphere(radius=pointsize)
                sphere.apply_translation(xyz)
                sphere.visual.vertex_colors = trimesh.visual.to_rgba(pointcolor[vertex])
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
