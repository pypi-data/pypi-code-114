import numpy as np
from scipy.sparse import coo_matrix
from pyNastran.bdf.bdf import read_bdf
from pyfe3d import (BeamLR, BeamLRData, BeamLRProbe, Quad4R, Quad4RData,
        Quad4RProbe, Tria3R, Tria3RData, Tria3RProbe, DOF, INT, DOUBLE)
from pyfe3d.beamprop import BeamProp
from pyfe3d.shellprop_utils import isotropic_plate
import sectionproperties.pre.library.primitive_sections as primitive_sections
from sectionproperties.analysis.section import Section
import pyvista as pv


def conm2_on_rbe3(mesh, conm2, rbe3):
    assert rbe3.type == 'RBE3'
    assert len(rbe3.dependent_nodes) == 1
    xyz = []
    weights = []
    nids = []
    for weight, Gijs in zip(rbe3.weights, rbe3.Gijs_node_ids):
        for nid in Gijs:
            xyz.append(mesh.nodes[nid].xyz)
            weights.append(weight)
            nids.append(nid)
    weights = np.array(weights)
    rCG = np.mean(xyz, axis=0)
    r_i = xyz - rCG
    r_iXY = r_i.copy()
    r_iXZ = r_i.copy()
    r_iYZ = r_i.copy()

    r_iXY[:, 2] = 0
    r_iXZ[:, 1] = 0
    r_iYZ[:, 0] = 0

    mass = conm2.mass
    I11, I21, I22, I31, I32, I33 = conm2.I

    dnode_id = rbe3.dependent_nodes[0]
    dnode = mesh.nodes[dnode_id]
    r_d = dnode.xyz - rCG
    #NOTE from reference node to CG
    ICG11 = I11 + (r_d[1]**2 + r_d[2]**2)*mass
    ICG22 = I22 + (r_d[0]**2 + r_d[2]**2)*mass
    ICG33 = I33 + (r_d[0]**2 + r_d[1]**2)*mass
    #TODO what about the off-diagonal terms?

    #NOTE assuming no moments applied at RBE3
    #M[DOF*pos+3, DOF*pos+3] += -I11
    #M[DOF*pos+3, DOF*pos+4] += -I21
    #M[DOF*pos+3, DOF*pos+5] += -I31
    #M[DOF*pos+4, DOF*pos+3] += -I21
    #M[DOF*pos+4, DOF*pos+4] += -I22
    #M[DOF*pos+4, DOF*pos+5] += -I32
    #M[DOF*pos+5, DOF*pos+3] += -I31
    #M[DOF*pos+5, DOF*pos+4] += -I32
    #M[DOF*pos+5, DOF*pos+5] += -I33

    #NOTE from CG to independent_nodes

    factor_i = weights/weights.sum()
    I11_i = (ICG11 + mass*(r_i[:, 1]**2 + r_i[:, 2]**2))*factor_i
    I22_i = (ICG22 + mass*(r_i[:, 0]**2 + r_i[:, 2]**2))*factor_i
    I33_i = (ICG33 + mass*(r_i[:, 0]**2 + r_i[:, 1]**2))*factor_i
    mass_i = mass*factor_i
    assert np.isclose(mass_i.sum(), mass)

    #TODO how to treat the off-diagonal terms?

    return nids, mass_i, I11_i, I22_i, I33_i


class ModelPyfe3D(object):
    r"""
    Attributes
    ----------
    TODO

    """
    __slots__ = [
            'ncoords', 'nids', 'nid_pos',
            'list_Tria3R', 'list_Quad4R', 'list_Beam',
            'beamLRProbe',
            'quad4RProbe',
            'tria3RProbe',
            'N',
            'dict_prop',
            'bu', 'bk',
            'KC0', 'M',
            'K6ROT',
            ]

    def __init__(self):
        self.K6ROT = 100.

    def read_nastran(self, input_file, spcid=1):
        mesh = read_bdf(input_file, debug=False)
        num_cbeam = 0
        num_cquad4 = 0
        num_ctria3 = 0
        unique_nids = set()
        dict_prop = {}
        self.dict_prop = dict_prop
        for eid, elem in mesh.elements.items():
            unique_nids.update(elem.node_ids)
            if elem.type == 'CBEAM':
                num_cbeam += 1
            if elem.type == 'CQUAD4':
                num_cquad4 += 1
            if elem.type == 'CTRIA3':
                num_ctria3 += 1
            prop = elem.pid_ref
            mat = prop.mid_ref
            if prop.pid not in dict_prop:
                if prop.type == 'PBEAML':
                    if prop.beam_type == 'BAR':
                        dim_z, dim_y = prop.dim[0]
                        geometry = primitive_sections.rectangular_section(d=dim_z, b=dim_y)
                        geometry.create_mesh(mesh_sizes=[min(dim_z/10, dim_y/10)])
                        A, Iyy, Izz, Iyz, J, phi = Section(geometry).calculate_frame_properties()
                        #TODO warping constants not yet supported by pyfe3d
                    p = BeamProp()
                    p.A = A
                    p.E = mat.e
                    scf = 5/6.
                    p.G = scf*mat.e/2/(1+mat.nu)
                    p.Iyy = Iyy
                    p.Izz = Izz
                    p.Iyz = Iyz
                    p.J = J
                    p.intrho = mat.rho*prop.Area()
                    p.intrhoz2 = mat.rho*Iyy
                    p.intrhoy2 = mat.rho*Izz
                    p.intrhoyz = mat.rho*Iyz
                    dict_prop[prop.pid] = p
                elif prop.type == 'PSHELL':
                    p = isotropic_plate(thickness=prop.t, E=mat.e, nu=mat.nu,
                            calc_scf=True, rho=mat.rho)
                    dict_prop[prop.pid] = p
                else:
                    raise NotImplementedError('TODO add more properties')

        beamLRData = BeamLRData()
        beamLRProbe = BeamLRProbe()
        quad4RData = Quad4RData()
        quad4RProbe = Quad4RProbe()
        tria3RData = Tria3RData()
        tria3RProbe = Tria3RProbe()
        self.beamLRProbe = beamLRProbe
        self.quad4RProbe = quad4RProbe
        self.tria3RProbe = tria3RProbe

        size_KC0 = (beamLRData.KC0_SPARSE_SIZE*num_cbeam +
                    quad4RData.KC0_SPARSE_SIZE*num_cquad4 +
                    tria3RData.KC0_SPARSE_SIZE*num_ctria3)
        size_M = (beamLRData.M_SPARSE_SIZE*num_cbeam +
                  quad4RData.M_SPARSE_SIZE*num_cquad4 +
                  tria3RData.M_SPARSE_SIZE*num_ctria3)
        KC0r = np.zeros(size_KC0, dtype=INT)
        KC0c = np.zeros(size_KC0, dtype=INT)
        KC0v = np.zeros(size_KC0, dtype=DOUBLE)
        Mr = np.zeros(size_M, dtype=INT)
        Mc = np.zeros(size_M, dtype=INT)
        Mv = np.zeros(size_M, dtype=DOUBLE)

        N = DOF*len(unique_nids)
        self.N = N
        print('# number of CBEAM elements:', num_cbeam)
        print('# number of CQUAD4 elements:', num_cquad4)
        print('# number of CTRIA3 elements:', num_ctria3)
        print('# degrees-of-freedom:', N)
        nids = sorted(list(unique_nids))
        nid_pos = dict(zip(nids, np.arange(len(nids))))

        ncoords = np.array([mesh.nodes[nid].xyz for nid in nids])
        ncoords_flatten = ncoords.flatten()
        self.ncoords = ncoords
        self.nids = nids
        self.nid_pos = nid_pos

        # creating elements and populating global stiffness
        init_k_KC0 = 0
        init_k_M = 0
        for eid, elem in mesh.elements.items():
            if elem.type != 'CBEAM':
                continue
            n1, n2 = elem.node_ids
            pos1 = nid_pos[n1]
            pos2 = nid_pos[n2]
            beam = BeamLR(beamLRProbe)
            beam.init_k_KC0 = init_k_KC0
            beam.init_k_M = init_k_M
            beam.n1 = n1
            beam.n2 = n2
            beam.c1 = DOF*pos1
            beam.c2 = DOF*pos2
            vec = elem.get_x_g0_defaults()
            beam.update_rotation_matrix(vec[0], vec[1], vec[2], ncoords_flatten)
            beam.update_probe_xe(ncoords_flatten)
            prop = dict_prop[elem.pid]
            beam.update_KC0(KC0r, KC0c, KC0v, prop)
            beam.update_M(Mr, Mc, Mv, prop)
            init_k_KC0 += beamLRData.KC0_SPARSE_SIZE
            init_k_M += beamLRData.M_SPARSE_SIZE

        self.list_Quad4R = []
        for eid, elem in mesh.elements.items():
            if elem.type != 'CQUAD4':
                continue
            n1, n2, n3, n4 = elem.node_ids
            pos1 = nid_pos[n1]
            pos2 = nid_pos[n2]
            pos3 = nid_pos[n3]
            pos4 = nid_pos[n4]
            r1 = ncoords[pos1]
            r2 = ncoords[pos2]
            r3 = ncoords[pos3]
            prop = dict_prop[elem.pid]
            quad = Quad4R(quad4RProbe)
            quad.alphat = self.K6ROT*1e-6/prop.A66*prop.h
            quad.n1 = n1
            quad.n2 = n2
            quad.n3 = n3
            quad.n4 = n4
            quad.c1 = DOF*nid_pos[n1]
            quad.c2 = DOF*nid_pos[n2]
            quad.c3 = DOF*nid_pos[n3]
            quad.c4 = DOF*nid_pos[n4]
            quad.init_k_KC0 = init_k_KC0
            quad.init_k_M = init_k_M
            quad.update_rotation_matrix(ncoords_flatten)
            quad.update_probe_xe(ncoords_flatten)
            quad.update_KC0(KC0r, KC0c, KC0v, prop)
            quad.update_M(Mr, Mc, Mv, prop)
            init_k_KC0 += quad4RData.KC0_SPARSE_SIZE
            init_k_M += quad4RData.M_SPARSE_SIZE
            self.list_Quad4R.append(quad)

        self.list_Tria3R = []
        for eid, elem in mesh.elements.items():
            if elem.type != 'CTRIA3':
                continue
            n1, n2, n3 = elem.node_ids
            pos1 = nid_pos[n1]
            pos2 = nid_pos[n2]
            pos3 = nid_pos[n3]
            r1 = ncoords[pos1]
            r2 = ncoords[pos2]
            r3 = ncoords[pos3]
            prop = dict_prop[elem.pid]
            tria = Tria3R(tria3RProbe)
            tria.alphat = self.K6ROT*1e-6/prop.A66*prop.h
            tria.n1 = n1
            tria.n2 = n2
            tria.n3 = n3
            tria.c1 = DOF*nid_pos[n1]
            tria.c2 = DOF*nid_pos[n2]
            tria.c3 = DOF*nid_pos[n3]
            tria.init_k_KC0 = init_k_KC0
            tria.init_k_M = init_k_M
            tria.update_rotation_matrix(ncoords_flatten)
            tria.update_probe_xe(ncoords_flatten)
            tria.update_KC0(KC0r, KC0c, KC0v, prop)
            tria.update_M(Mr, Mc, Mv, prop)
            init_k_KC0 += tria3RData.KC0_SPARSE_SIZE
            init_k_M += tria3RData.M_SPARSE_SIZE
            self.list_Tria3R.append(tria)


        KC0 = coo_matrix((KC0v, (KC0r, KC0c)), shape=(N, N)).tocsc()
        M = coo_matrix((Mv, (Mr, Mc)), shape=(N, N)).tocsc()
        self.KC0 = KC0
        self.M = M


        for conm in mesh.masses.values():
            if conm.cid != 0:
                raise NotImplementedError('TODO')
            if conm.type != 'CONM2':
                raise NotImplementedError('TODO')
            pos = nid_pos.get(conm.nid)
            if pos is None:
                flag = False
                for rbe3 in mesh.rigid_elements.values():
                    if rbe3.dependent_nodes[0] == conm.nid:
                        flag = True
                        break
                if not flag:
                    print(conm.nid)
                    raise NotImplementedError('TODO')
                nids, mass_i, I11_i, I22_i, I33_i = conm2_on_rbe3(mesh, conm, rbe3)
            else:
                nids = [conm.nid]
                mass_i = [conm.mass]
                I11, I21, I22, I31, I32, I33 = conm.I
                I11_i, I22_i, I33_i = [I11], [I22], [I33]

            for nid, mass, I11, I22, I33 in zip(nids, mass_i, I11_i, I22_i, I33_i):
                pos = nid_pos[nid]
                for i in range(3):
                    M[DOF*pos+i, DOF*pos+i] += mass
                #TODO out-of-diagonal terms
                #M[DOF*pos+3, DOF*pos+3] += I11
                #M[DOF*pos+3, DOF*pos+4] += I21
                #M[DOF*pos+3, DOF*pos+5] += I31
                #M[DOF*pos+4, DOF*pos+3] += I21
                #M[DOF*pos+4, DOF*pos+4] += I22
                #M[DOF*pos+4, DOF*pos+5] += I32
                #M[DOF*pos+5, DOF*pos+3] += I31
                #M[DOF*pos+5, DOF*pos+4] += I32
                #M[DOF*pos+5, DOF*pos+5] += I33

        print('# structural matrices created')

        # applying boundary conditions
        bk = np.zeros(N, dtype=bool) #array to store known DOFs
        for spc in mesh.spcs[spcid]:
            for component in spc.components:
                component = int(component)-1
                for nid in spc.node_ids:
                    pos = nid_pos.get(nid)
                    if pos is not None:
                        bk[DOF*pos + component] = True
        bu = ~bk
        self.bu = bu
        self.bk = bk
        print('# applied boundary conditions')

        return self

def plot3d(model, displ_vec=None, contour_vec=None, contour_label='vec', background='white'):
    #NOTE needs ipygany and pythreejs packages (pip install pyvista pythreejs ipygany --upgrade)
    nid_pos = model.nid_pos
    ncoords = model.ncoords
    plotter = pv.Plotter(off_screen=False)
    faces_quad = []
    for q in model.list_Quad4R:
        faces_quad.append([4, nid_pos[q.n1], nid_pos[q.n2], nid_pos[q.n3], nid_pos[q.n4]])
    faces_quad = np.array(faces_quad)
    quad_plot = pv.PolyData(ncoords, faces_quad)
    if contour_vec is not None:
        quad_plot[contour_label] = contour_vec
        plotter.add_mesh(quad_plot, scalars=contour_label, cmap='coolwarm',
                edge_color='black', show_edges=True, line_width=1.)
    else:
        plotter.add_mesh(quad_plot, edge_color='black', show_edges=True,
                line_width=1.)
    faces_tria = []
    for t in model.list_Tria3R:
        faces_tria.append([3, nid_pos[t.n1], nid_pos[t.n2], nid_pos[t.n3]])
    faces_tria = np.array(faces_tria)
    tria_plot = pv.PolyData(ncoords, faces_tria)
    if contour_vec is not None:
        tria_plot[contour_label] = contour_vec
        plotter.add_mesh(tria_plot, scalars=contour_label, cmap='coolwarm',
                edge_color='black', show_edges=True, line_width=1.)
    else:
        plotter.add_mesh(tria_plot, edge_color='black', show_edges=True,
                line_width=1.)
    if displ_vec is not None:
        quad_plot = pv.PolyData(ncoords + displ_vec, faces_quad)
        plotter.add_mesh(quad_plot, edge_color='red', show_edges=True,
                line_width=1., opacity=0.5)
        tria_plot = pv.PolyData(ncoords + displ_vec, faces_tria)
        plotter.add_mesh(tria_plot, edge_color='red', show_edges=True,
                line_width=1., opacity=0.5)
    plotter.set_background(background)
    plotter.parallel_projection = False
    return plotter

