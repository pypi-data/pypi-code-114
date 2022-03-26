import copy
from numpy import array, zeros, dot, transpose, allclose, diag, identity
from numpy.linalg import svd, eigh
import math
import sys
import logging

#
from natorbs.moldata import MolData, filter_orbitals
from natorbs.natural import NaturalOrbitals
##import natorbs_error

class Promolecule(MolData):
    """Construct a promolecule from fragments.
    Fragments can be restricted or unrestricted, or mixed (which will
    result in unrestricted promolecule).
    """
    def __init__(self, fragments, logname="Promolecule", loglevel=logging.INFO):
        """
        `fragments' is a list of MolData objects (molecular fragments)
        """
        self._setup_logger(logname, loglevel)
        attributes = {}

        self.logger.info("this is Promolecule")
        self.logger.info("concat.: atoms & basis set")
        # (1) atoms and basis set
        for key in "atoms", "gbasis": # FIXME: `sbasis' as an alt. still TODO!
            attributes[key] = []
            for fragment in fragments:
                attributes[key] += getattr(fragment, key)

        attributes["spherical"] = fragments[0].spherical
        for fragment in fragments:
            if fragment.spherical != attributes["spherical"]:
                s = "All fragments must have the same spherical settings."
                self.logger.error(s)
                raise RuntimeError(s)



        # (2) orbitals: occupations, energies, symmetries
        self.logger.info("concat.: MO occupations, energies and symmetries")
        
        # if at least one fragment is unresticted,
        # the orbitals for all restricted should be doubled,
        # what we do here in a very tricky way.
        max_spin = max(map(lambda _: len(_.mooccups), fragments))
        # ^^^^ this is either one or two, depending whether we need
        # restricted or unresticted promolecule.

        for key in "mooccups", "moenergies", "mosyms":
            promol_attr = []
            for s in range(0, max_spin):
                l = []
                for fragment in fragments:
                    fragm_attr = getattr(fragment, key)
                    l += list(fragm_attr[s % len(fragm_attr)])
                    # ^^^^^^ to 'double' restr. fragm. in unrestr. promol.
                    # (% in [] makes this index either s (unrestr. fragm.)
                    # or 0 (restr. fragm.)

                if key in ("mooccups", "moenergies"): promol_attr.append(array(l))
                else: promol_attr.append(l)
                # ^^^^ FIXME: this should be done by MolData.__init__()...(?)

            promol_attr = tuple(promol_attr)
            attributes[key] = promol_attr

        # FIXME: symmety labels for fragment orbitals should be ignored
        # or modified, because molecular and fragment symmetries are
        # ussually different...
        

        # (3) orbitals: coefficients
        self.logger.info("concat.: MO coefficients")
        attributes["mocoeffs"] = []
        for s in range(0, max_spin):
            n_orb, n_bas = 0, 0
            for fragment in fragments:
                # FIXME: why "s % len(fragment.mocoeffs)" instead of "s" here?
                fragm_shape = fragment.mocoeffs[s % len(fragment.mocoeffs)].shape
                n_orb += fragm_shape[0]
                n_bas += fragm_shape[1]
            attributes["mocoeffs"].append(
                zeros((n_orb, n_bas), "d"))
            i, j = 0, 0
            for fragment in fragments:
                C = fragment.mocoeffs[s % len(fragment.mocoeffs)]
                attributes["mocoeffs"][s][i:i+C.shape[0], j:j+C.shape[1]] = C
                i += C.shape[0]
                j += C.shape[1]
        attributes["mocoeffs"] = tuple(attributes["mocoeffs"])
        
        MolData.__init__(self, attributes)

class DiffDensOrbitals(Promolecule):
    """Eigenvectors/ eigenvalues of the differential density of the
    same molecule between two electronic states"""
    def __init__(self, molecule, fragments, logname="DiffDens", loglevel=logging.INFO):

        # obtain natural orbitals on fragments and molecule, if needed
        # convert fragments to promolecule
        Promolecule.__init__(self, list(map(lambda _: NaturalOrbitals(_), fragments)))
        mol = NaturalOrbitals(molecule)

        C0 = transpose(self.mocoeffs[0])
        C = transpose(mol.mocoeffs[0])
        U, w, Vt = svd(C)
        U1 = U[:,0:w.shape[0]]
        T = dot(dot(dot(transpose(Vt), diag(1/w)), transpose(U1)), C0)
        check_unit = abs(dot(transpose(T), T)-identity(T.shape[1])).max()
        self.logger.debug("checking norm(T*T-1) to test if T is orthogonal: %s"
                          %(allclose(1+check_unit,1)
                            and "ok"
                            or "failed (error=%g) -- continuing anyway (don't care if you believe T is `enough' orthogonal)" %check_unit))
        P0 = dot(dot(T,diag(mol.mooccups[0])), transpose(T))
        P = diag(self.mooccups[0])

        v, X = eigh(P - P0)

        ddocoeffs = [], []
        ddoenergies = [], []
        ddooccups = [], []
        ddosyms = [], []

        # Transform DDO back to the AO basis and
        # convert negative occupations to beta
        
        for c,o in zip(array(transpose(dot(C, X))), v):
            if o >= 0: s = 0
            else: s = 1
            ddocoeffs[s].append(c)
            ddooccups[s].append(abs(o))
            ddoenergies[s].append(0.)
            ddosyms[s].append("A")               
            
        self.mooccups = map(array, ddooccups)
        self.moenergies = map(array, ddoenergies)
        self.mocoeffs = map(array, ddocoeffs)
        self.mosyms = map(array, ddosyms)
        
    
class NOCV(Promolecule):
    """NOCV analysis for RHF-type wavefuntion
    """
    def __init__(self, molecule, fragments, logname="NOCV", loglevel=logging.INFO):

        self._setup_logger(logname, loglevel)

        # Contruct a promolecule only from the occupied fragment orbitals.
        self.logger.info("Constructing promolecule")
        filtered_fragments = list(map(
            lambda _: filter_orbitals(_, [lambda o,s,c: o != 0]),
            fragments))
        Promolecule.__init__(self, filtered_fragments)

        # Check if all occupation numbers are 2 (RHF) or 1 (UHF)
        if len(self.mooccups) == 1 and not allclose(self.mooccups[0],2):
            self.logger.error("The promolecule is not described by RHF wf")
            raise natorbs_error.NatorbsAssumptionError()
        elif len(self.mooccups) == 2 and not (allclose(self.mooccups[0],1) and allclose(self.mooccups[1],1)):
            self.logger.error("The promolecule is not described by UHF wf")
            raise natorbs_error.NatorbsAssumptionError()

        if len(molecule.mooccups) == 1 and ( \
            not allclose(list(filter(lambda x: x>1, molecule.mooccups[0])), 2) or \
            not allclose(list(filter(lambda x: x<1, molecule.mooccups[0])), 0)):
            self.logger.error("The molecule is not described by RHF wf")
            raise natorbs_error.NatorbsAssumptionError()
        elif len(molecule.mooccups) == 2 and (  \
            not (allclose(list(filter(lambda x: x>1, molecule.mooccups[0])), 1) and \
                 allclose(list(filter(lambda x: x>1, molecule.mooccups[1])), 1)) or \
            not (allclose(list(filter(lambda x: x<1, molecule.mooccups[0])), 0) and \
                 allclose(list(filter(lambda x: x<1, molecule.mooccups[1])), 0))):
            self.logger.error("The molecule is not described by UHF wf")
            raise natorbs_error.NatorbsAssumptionError()

        if not len(molecule.mocoeffs) == len(self.mocoeffs):
            self.logger.error("Molecule and Promolecule must have the same wf type: either RHF or UHF.")
            raise natorbs_error.NatorbsAssumptionError()

        if len(molecule.mocoeffs) == 1:
            NOCV_mooccups = [False]
            NOCV_mocoeffs = [False]
            NOCV_mosyms = [False]
            NOCV_moenergies = [False]
        else:
            NOCV_mooccups = [False, False]
            NOCV_mocoeffs = [False, False]
            NOCV_mosyms = [False, False]
            NOCV_moenergies = [False, False]
        
        for spin in range(0, len(molecule.mocoeffs)):
            self.logger.info("Calculating NOCV for spin %d of %d." %(spin+1,len(molecule.mocoeffs)))
            # Overlap integrals for AO basis
            C = transpose(molecule.mocoeffs[spin])
            U, w, Vt = svd(C)
            U1 = U[:,0:w.shape[0]]
            C_inv = dot(transpose(Vt), dot(diag(1/w), transpose(U1)))
            S = dot(transpose(C_inv), C_inv)
            test = dot(transpose(C), dot(S, C))
            self.logger.debug("checking... %s"
                         %((allclose(test, identity(test.shape[0])) and "ok")
                           or "failed"))

            # Obtain Loewdin ortogonalized promolecular orbitals
            C0_raw = transpose(self.mocoeffs[spin])
            G = dot(transpose(C0_raw), dot(S, C0_raw))
            g, L = eigh(G) # G=LgL^t
            inv_sqrt_G = dot(L, dot(
                diag(list(map(lambda x: 1 / math.sqrt(x), g))),
                transpose(L)))
            self.logger.debug("checking Loewdin transformation (test 1)... %s."
                         %(allclose(dot(dot(inv_sqrt_G, inv_sqrt_G), G),
                                    identity(G.shape[0])) and "ok" or "failed"))
            C0 = dot(C0_raw, inv_sqrt_G)
            self.logger.debug("checking Loewdin transformation (test 2)... %s."
                         %(allclose(dot(dot(transpose(C0), S), C0),
                                    identity(C0.shape[1])) and "ok" or "failed"))

            # Transform to common basis (MO), obtain diff. density matrix
            # and NOCV
            self.logger.debug("obtaining NOCV from diff. density matrix")
            T = dot(C_inv, C0)
            factor = len(molecule.mooccups) == 1 and 2.0 or 1.0
            delta_P = diag(molecule.mooccups[spin]) - dot(factor * T, transpose(T))
            v, X = eigh(delta_P)

            # Transform NOCV back to AO basis
            NOCV_mocoeffs[spin] = transpose(dot(C, X)) #bce of our convention!
            NOCV_moenergies[spin] = zeros(v.shape[0])
            NOCV_mooccups[spin] = v
            NOCV_mosyms[spin] = array(list(map(lambda _: 'A', v)))

        self.mocoeffs = tuple(NOCV_mocoeffs)
        self.moenergies = tuple(NOCV_moenergies)
        self.mooccups = tuple(NOCV_mooccups)
        self.mosyms = tuple(NOCV_mosyms)

    
class FragmentMullikenAnalysis(Promolecule):

    def __init__(self, molecule, fragments, spin=False, simple=True, logname="FMA", loglevel=logging.INFO):

        self._setup_logger(logname, loglevel)
        
        self.logger.info("this is Fragment Mulliken Analysis (experimental)")
        
        fragments_natural = list(map(lambda _: NaturalOrbitals(_, spin, loglevel),
                                fragments))
        Promolecule.__init__(self, fragments_natural)

        molecule_natural = NaturalOrbitals(molecule, spin, loglevel)

        for s in range(0, len(molecule_natural.mocoeffs)):
            self.logger.info("for spin %s" % ((s == 0 and "alpha") or "beta"))
            C  = transpose(molecule_natural.mocoeffs[s]) # bcse of our convention!
            n = molecule_natural.mooccups[s]
            C0 = transpose(self.mocoeffs[s]) # bcse of our convention!
            n0 = self.mooccups[s]

            #logger.debug("|n| = %f" %sum(n))
            #logger.debug("|n0| =%f" %sum(n0))

            self.logger.debug("overlap integrals in AO basis")
            # FIXME: repetition could be avoided here
            #(do it only once for s == 0)
            U, w, Vt = la.svd(C)
            U1 = U[:,0:w.shape[0]]
            C_inv = dot(transpose(Vt), dot(diag(1/w), transpose(U1)))
            S = dot(transpose(C_inv), C_inv)
            test = dot(transpose(C), dot(S, C))
            self.logger.debug("checking... %s"
                              %((allclose(test, identity(test.shape[0])) and "ok")
                                or "failed"))
            
            self.logger.debug("overlap integrals in the basis of fragment orbitals")
            G = dot(transpose(C0), dot(S, C0))

            self.logger.debug("transforming MO to the basis of fragment orbitals")
            U, w, Vt = la.svd(C0)
            U1 = U[:,0:w.shape[0]]
            C0_inv = dot(transpose(Vt), dot(diag(1/w), transpose(U1)))
            T = dot(C0_inv, C)
            #test = dot(transpose(T), dot(G, T))
            #logger.debug("checking... %s"
            #             %((allclose(test, identity(test.shape[0])) and "ok")
            #               or "failed"))

            self.logger.debug(
                "obtaining molecular dens. matrix in the basis of fragment orbs.")
            P = dot(dot(T, diag(n)), transpose(T))
            #logger.debug("Tr(PG)=%f" %trace(dot(P,G)))

            if simple:
                # trivial calcs of Mulliken charges
                self.logger.debug("calculating populations")
                for i in range(0, P.shape[0]):
                    pop = P[i,i]
                    for j in range(0, P.shape[1]):
                        if j == i: continue
                        pop += P[i,j]*G[j,i]
                    self.moenergies[s][i] = pop - self.mooccups[s][i]
                    self.mooccups[s][i] = pop

            else:
                # more advanced and experimental: diagonal. of diff fragment PS matrices
                start = 0
                new_MOs = zeros_like(transpose(self.mocoeffs[s]))
                new_flows = zeros_like(self.mooccups[s])
                for frag_nat in fragments_natural:
                    size = frag_nat.mooccups[s].shape[0] # only for "1st spin" bcos ts'r spinless MOs...
                    PG_fragm = dot( P[start:start+size, :], G[:, start:start+size])
                    flows, orbs = la.eigh(PG_fragm - diag(frag_nat.mooccups[s]))
                    #print 'PG_fragm:', PG_fragm.shape
                    #print 'flows:', flows.shape
                    #print 'orbs:', orbs.shape
                    #print 'self.mocoeffs[s]', self.mocoeffs[s].shape
                    #print start, size
                    new_MOs[:, start:start+size] = dot(transpose(self.mocoeffs[s])[:, start:start+size], orbs)
                    new_flows[start:start+size] = flows
                    start += size


                self.mocoeffs[s][:,:] = transpose(new_MOs)
                self.mooccups[s][:] = new_flows
                self.moenergies[s][:] = zeros_like(self.moenergies[s])
            
