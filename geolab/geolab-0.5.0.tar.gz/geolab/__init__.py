from geolab import utilities

from geolab.mesh.iomesh import read_mesh_obj, save_mesh_obj, read_mesh, \
    save_mesh

from geolab.mesh.counting import number_of_faces, number_of_vertices, \
    number_of_edges

from geolab.mesh.navigate import navigate_halfedges, halfedges_origin, \
    halfedges_face, halfedges_next, halfedges_edge, halfedges_previous, \
    halfedges_twin

from geolab.mesh.halfedges import halfedges, orient_faces

from geolab.mesh.globalconnectivity import vertices_ring_ordered_halfedges, \
    vertices_ring_vertices, edges, faces_ordered_halfedges, \
    faces_edge_vertices, faces_vertices, vertices_ring_faces, \
    vertices_ring_edges, faces_edges, edges_vertices, edges_faces, \
    edges_halfedges, vertices_edge_map, faces_size, vertices_valence, \
    faces_list

from geolab.mesh.editconnectivity import join_meshes

from geolab.mesh.boundary import mesh_corners, boundary_contiguous_vertices, \
    boundary_contiguous_halfedges, boundary_faces, boundary_halfedges, \
    boundary_vertices, boundary_edges, label_contiguous_boundaries, \
    fill_boundaries, are_boundary_vertices, extract_boundary_faces, \
    double_boundary_vertices

from geolab.mesh.curves import mesh_curves

from geolab.mesh.geometry import faces_vector_area, faces_centroid, faces_area, \
    faces_normal, closest_vertices, vertices_normal, vertices_ring_area, \
    edges_mid_point, mesh_area, mean_edge_length, vertices_ring_barycenter, \
    edges_length, snap_vertices, feature_edges

from geolab.mesh.subdivision import explode_faces, face_triangles, \
    catmull_clark_subdivision, loop_subdivision, dual_mesh, delete_edges, \
    delete_unconnected_vertices, delete_faces, collapse_edge, flip_edge, \
    split_edge, collapse_threshold_edges, split_threshold_edges, \
    triangular_remesh, weld_faces, remesh_test, equalize_valences

from geolab.mesh.meshprimitives import mesh_plane, mesh_torus, mesh_sphere, \
    mesh_cylinder, mesh_icosahedron, mesh_rectangular_pipe, mesh_circular_pipe

from geolab.geometry.frame import make_frame, rotate_frame

from geolab.geometry.circle import circle_three_points, sample_circle

from geolab.geometry.polyline import polyline_vertex_frame, refine_polyline, \
    read_polyline, polyline_pipe_frame, polyline_bishop_frame, polyline_corners, \
    save_polyline, polyline_edges_length


from geolab.transform.reframe import rigid_transformation, \
    mesh_rigid_transformation

from geolab.utilities.arrayutilities import sum_repeated


try:
    from geolab.plot.viewer import plotter
    from geolab.plot.figure import figure
except ImportError:
    print('Mayavi not found')
    pass

try:
    from geolab.gui.geolabgui import geolab_gui
    from geolab.gui.geolabcomponent import GeolabComponent as geolab_component
except ImportError:
    pass
