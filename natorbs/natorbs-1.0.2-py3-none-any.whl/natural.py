"""Core routines related to natural/spin orbitals"""

from numpy import dot, transpose, array, allclose, diag, identity
#from numpy import *
from numpy import linalg as la
import logging
import sys
import functools

#
from natorbs.moldata import MolData
##import natorbs_error

class NaturalOrbitals(MolData):
    """Calculate natural/spin orbitals
    
    mocoeffs, mooccups --- nat./spin orbitals
    by definition: moenergies[]=0
    """
    def __init__(self, data, spin = False, logname="NaturalOrbitals", loglevel=logging.INFO, ignore_symmetry = False):

        self._setup_logger(logname, loglevel)
        
        # Firstly, determine whether we have restricted
        # or unrestricted case. The restricted case is trivial,
        # but it must be properly hadled as well as the unrestricted one!
        if len(data.mocoeffs) == 1:
            self.logger.info("This is restricted (trivial) case")
            MolData.__init__(self, data.__dict__)
            if spin: #FIXME: maybe these lists should be just empty?
                self.mooccups = (zeros(data.mocoeffs[0].shape[0], "d"),)
                self.mocoeffs = (data.mocoeffs[0],)
            return
        # End of restricted case --- below is the generic one.

        if spin:
            mooccups = [], []
            mocoeffs = [], []
            mosyms = [], []
            moenergies = [], [] # experimental!
            # overlaps of spinorbs with the original MOs (alpha and beta)
            # element [s][i, j] is  the overlap of the
            # i-th spinorb of spin s with the j-th original MO
            overlaps_alpha = [], []
            overlaps_beta = [], []
        else:
            mooccups = [],
            mocoeffs = [],
            mosyms = [],
            moenergies = [], # experimental!
            # overlaps of natorbs with the original MOs (alpha and beta)
            # element [i, j] is the overlap of the i-th natorb with the j-th original MO
            overlaps_alpha = [],
            overlaps_beta  = [],

        if not spin:
            radical_index_per_symmetry = []

        if ignore_symmetry:
            for s in 0, 1:
                data.mosyms[s] = list(map(lambda _: 'A1', data.mosyms[s]))

        for sym, ((n_a, n_b), (e_a, e_b), (C_a, C_b)) in self._get_by_symmetry(
            data.mosyms, data.mooccups, data.moenergies, data.mocoeffs):

            C_a, C_b = tuple(map(transpose, (C_a, C_b)))
            # (because in cclib the 1st dim is a number of MO...)
            
            self.logger.debug("SVD of the first MO set")
            U, w, Vt = la.svd(C_a, full_matrices=False)
            self.logger.debug("checking SVD: %s"
                              %(allclose(C_a, dot(U, dot(diag(w), Vt)))
                                and "ok" or "failed"))

            self.logger.debug("MO transformation")
            T = dot(dot(dot(transpose(Vt), diag(1/w)), transpose(U)), C_b)
            
            check_unit = abs(dot(transpose(T), T)-identity(T.shape[1])).max()
            THRESH_CHECK_UNIT = 0.0001  # FIXME: tune this value
            if allclose(1+check_unit,1):
                check_unit_s = 'ok'
            elif abs(check_unit)< THRESH_CHECK_UNIT:
                check_unit_s = 'acceptable (%g)' %check_unit
            else:
                check_unit_s = 'failed (%g)' %check_unit
            self.logger.debug("checking norm(T*T-1) to test if T is orthogonal: " + check_unit_s)
            if 'failed' in check_unit_s:
                self.logger.warning(
                    "transformation matrix C_a->C_b is significantly not orthogonal, deviation is %g" %check_unit)
            elif 'acceptable' in check_unit_s:
                self.logger.info(
                    "transformation matrix C_a->C_b deviates from orthogonality, deviation is %g (acceptable %g)" %(check_unit,THRESH_CHECK_UNIT))

            P_a = diag(n_a)
            P_b = dot(dot(T, diag(n_b)), transpose(T))

            # fock operator (in the basis of C_a)
            # to calculate energies -- experimental
            F = (diag(e_a) + dot(dot(T, diag(e_b)), transpose(T))) / 2
            
            if spin:
                self.logger.info(
                    "Computing spin orbitals for symmetry %s" %sym)
                v, X = la.eigh(P_a - P_b)
            else:
                self.logger.info(
                    "Computing natural orbitals for symmetry %s" %sym)
                v, X = la.eigh(P_a + P_b)
                radical_index = 0
                for vi in v:
                    radical_index += vi * (2.-vi)
                radical_index_per_symmetry.append(radical_index)
                
            # X contains eigenvectors in columns

            # --------------------------------------------------------------
            # compute expectation values of F and sort orbitals
            # in each symmetry by occupation numbers
            sorted_orbital_list = sorted(
                zip(v, map(lambda _: dot(_, dot(F, _)),
                           transpose(X)),
                    transpose(X)),
                key=functools.cmp_to_key(lambda x, y: x[0]-y[0] < 0 and 1 or -1))
            # [(v_i, X_i)], sorted by v_i
            close_to_one = lambda o: allclose([o], [1.])
            # filter singly occupied orbitals
            singly_occupied_mos = list(filter(lambda _: close_to_one(_[1][0]),
                                         enumerate(sorted_orbital_list)))
            if len(singly_occupied_mos) > 1:
                C1 = array(list(map(lambda _: _[1][2], singly_occupied_mos)))
                F1 = dot(C1, dot(F, transpose(C1)))
                e1, U1 = la.eigh(F1)
                #print (C1.shape, U1.shape)
                for i,e,u in zip(map(lambda _: _[0], singly_occupied_mos),
                             e1, transpose(U1)):
                    sorted_orbital_list[i] = (1., e, dot(u, C1))
            # --------------------------------------------------------------
            
#            # in each symmetry sort orbitals by energies
#            sorted_orbital_list = sorted(
#                zip(
#                v, map(lambda _: dot(_, dot(F, _)),
#                       transpose(X)),
#                transpose(dot(C_a, X))),
#                lambda x, y: x[1]-y[1] > 0 and 1 or -1)
#            # { the list is of form: [(occ, energy, coeff)] }

            for occup, energy, coeff in sorted_orbital_list:
                if spin and occup < 0: s = 1
                else: s = 0
                mosyms[s].append(sym)
                mooccups[s].append(abs(occup))
                moenergies[s].append(energy)
#                mocoeffs[s].append(coeff)
                mocoeffs[s].append(dot(C_a, coeff))
                overlaps_alpha[s].append(coeff)
                overlaps_beta[s].append(dot(transpose(T), coeff)) #?

        MolData.__init__(self, data.__dict__)
        self.mooccups = tuple(map(array, mooccups))
        self.moenergies = tuple(map(array, moenergies))
        self.mocoeffs = tuple(map(array, mocoeffs))
        self.overlaps_alpha = overlaps_alpha
        self.overlaps_beta  = overlaps_beta


        if not spin:
            print("Radical index (Davidson): %f\n" %sum(radical_index_per_symmetry))
        #self.moenergies = map(lambda _: zeros(_.shape, 'd'), self.mooccups)


    def _get_by_symmetry(self, mosyms, mooccups, moenergies, mocoeffs):
        """Get MOs by symmetry.

            << mosyms = ([syms_a], [syms_b])
            << mooccups = ([occups_a], [occups_b])
            << mocoeffs = (array(coeffs_a), array(coeffs_b))

            >> [(sym, ([occups_a], [occups_b]), ([coeffs_a], [coeffs_b])), ...]
        """
        # group by orbital:
        # >>  [[(sym_a, occup_a, coeff_a), ... ],
        #      [(sym_b, occup_b, coeff_b), ... ]] 
        if len(mooccups) < len(mocoeffs):
            corrected_mooccups = [0.5 * array(mooccups[0]), 0.5 * array(mooccups[0])]
        else:
            corrected_mooccups = mooccups
        # group by spin:
        # >>  [ ( [syms_a], [occups_a], array(coeffs_a) ),
        #       ( [syms_b], [occups_b], array(coeffs_b) ) ]
        # no longer works in Python3:
        #mos = map(lambda (syms, occups, energies, coeffs): zip(syms, occups, energies, coeffs),
        #          zip(mosyms, corrected_mooccups, moenergies, mocoeffs))
        # was replaced by
        mos = []
        for (syms, occups, energies, coeffs) in zip(mosyms, corrected_mooccups, moenergies, mocoeffs):
            mos.append(zip(syms, occups, energies, coeffs))
        mos_by_sym = {}
        for spin in (0, 1):
            for sym, occup, energy, coeff in mos[spin]:
                if not sym in mos_by_sym:  mos_by_sym[sym] = [[[], []], [[], []], [[], []]]
                mos_by_sym[sym][0][spin].append(occup)
                mos_by_sym[sym][1][spin].append(energy)
                mos_by_sym[sym][2][spin].append(coeff)

        for sym in mos_by_sym.keys():
            mos_by_sym[sym][0] = tuple(map(array, mos_by_sym[sym][0]))#occups
            mos_by_sym[sym][1] = tuple(map(array, mos_by_sym[sym][1]))#energies
            mos_by_sym[sym][2] = tuple(map(array, mos_by_sym[sym][2]))#coeffs
            mos_by_sym[sym] = tuple(mos_by_sym[sym])

        return mos_by_sym.items()
