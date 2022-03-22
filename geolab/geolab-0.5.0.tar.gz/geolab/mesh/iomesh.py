"""
A mesh obj reader
"""

__author__ = 'Davide Pellis'

import numpy as np

# -----------------------------------------------------------------------------

from geolab.utilities.stringutilities import make_filepath

from geolab.mesh.globalconnectivity import faces_list

from geolab.mesh.halfedges import are_halfedges


# -----------------------------------------------------------------------------
# GENERAL
# -----------------------------------------------------------------------------

def read_mesh(file_name, read_texture=False):
    if file_name.endswith('.obj'):
        return read_mesh_obj(file_name, read_texture)
    try:
        return read_mesh_npz(file_name)
    except FileNotFoundError:
        return read_mesh_obj(file_name, read_texture)


def save_mesh(vertices, connectivity, file_name='mesh.npz',
              overwrite=False, texture=None):
    if file_name.endswith('.obj'):
        return save_mesh_obj(vertices, connectivity, file_name=file_name,
                             overwrite=overwrite, texture=texture)
    else:
        return save_mesh_npz(vertices, connectivity, file_name, overwrite)


# -----------------------------------------------------------------------------
# OBJ
# -----------------------------------------------------------------------------

def read_mesh_obj(file_name, read_texture=False):
    """Read an OBJ mesh file.

    Parameters
    ----------
    file_name : str
        The path of the OBJ file to open.

    read_texture : bool
        If 'True', the uv coordinates are returned. Default is 'False.

    Returns
    -------
    v : np.array (V,3)
        The array of vertices [[x_0, y_0, z_0], ..., [x_V, y_V, z_V]].
    f : list
        The list of faces [[v_i, v_j, ...], ...]
    uv (optional): np.array (V, 2)
        The array of uv vertex coordinates [[u_0, v_0], ..., [u_V, v_V]].

    Notes
    -----
    Files must be written without line wrap (in many CAD software,
    line wrap can be disabled in the OBJ saving options).
    """
    if not file_name.endswith('.obj'):
        file_name = file_name + '.obj'
    file_name = str(file_name)
    obj_file = open(file_name, encoding='utf-8')
    vertices_list = []
    uv_list = []
    f = []
    for line in obj_file:
        split_line = line.split(' ')
        if split_line[0] == 'v':
            split_x = split_line[1].split('\n')
            x = float(split_x[0])
            split_y = split_line[2].split('\n')
            y = float(split_y[0])
            split_z = split_line[3].split('\n')
            try:
                z = float(split_z[0])
            except ValueError:
                print('WARNING: disable line wrap when saving .obj')
            vertices_list.append([x, y, z])
        elif split_line[0] == 'f':
            v_list = []
            L = len(split_line)
            try:
                for i in range(1, L):
                    split_face_data = split_line[i].split('/')
                    v_list.append(int(split_face_data[0]) - 1)
                f.append(v_list)
            except ValueError:
                v_list = []
                for i in range(1, L - 1):
                    v_list.append(int(split_line[i]) - 1)
                f.append(v_list)
        elif read_texture:
            if split_line[0] == 'vt':
                split_u = split_line[1].split('\n')
                u = float(split_u[0])
                split_v = split_line[2].split('\n')
                v = float(split_v[0])
                uv_list.append([u, v])
    v = np.array(vertices_list)
    try:
        f = np.array(f)
    except TypeError:
        pass
    if read_texture:
        uv = np.array(uv_list)
        return v, f, uv
    return v, f


def save_mesh_obj(vertices, connectivity, file_name='mesh',
                  overwrite=False, texture=None):
    """Save the mesh as OBJ file.

    Parameters
    ----------
    vertices : np.array (H, 3)
        The array of vertices.

    Optional Parameters
    -------------------
    connectivity : np.array (F, n) / list of lists / np.array (H, 6)
        The array or connectivity. Faces / faces list / halfedges.
    file_name : str
        The path of the OBJ file to be created.
    overwrite : bool
        If `False` (default), when the path already exists, a sequential
        number is added to file_name. If `True`, existing paths are
        overwritten.
    texture : np.array (V, 2)
        The uv vertex coordinates.

    Returns
    -------
    str
        The path of the saves OBJ file (without extension).
    """
    path = make_filepath(file_name, 'obj', overwrite)
    obj = open(path, 'w')
    line = 'o {}\n'.format(file_name)
    obj.write(line)
    if are_halfedges(vertices, connectivity):
        faces = faces_list(connectivity)
    else:
        faces = connectivity
    for v in range(len(vertices)):
        vi = vertices[v]
        line = 'v {} {} {}\n'.format(vi[0], vi[1], vi[2])
        obj.write(line)
    if texture is not None:
        for v in range(len(texture)):
            uv = texture[v]
            line = 'vt {} {}\n'.format(uv[0], uv[1])
            obj.write(line)
    for f in range(len(faces)):
        obj.write('f ')
        N = len(faces[f])
        for v in range(N - 1):
            vf = str(faces[f][v] + 1)
            obj.write(vf + ' ')
        vf = str(faces[f][N - 1] + 1)
        obj.write(vf + '\n')
    obj.close()
    out = 'OBJ saved in {}'.format(path)
    print(out)
    return path.split('.')[0]


# -----------------------------------------------------------------------------
# NPZ
# -----------------------------------------------------------------------------

def save_mesh_npz(vertices, connectivity, file_name, overwrite=False):
    path = make_filepath(file_name, 'npz', overwrite)
    np.savez(path, vertices, connectivity)
    out = 'NPZ saved in {}'.format(path)
    print(out)


def read_mesh_npz(file_name):
    if not file_name.endswith('.npz'):
        file_name = file_name + '.npz'
    npz = np.load(file_name)
    return npz['arr_0'], npz['arr_1']

