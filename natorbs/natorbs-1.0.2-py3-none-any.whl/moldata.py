from cclib.parser.utils import PeriodicTable
from cclib.parser.utils import convertor
from cclib.parser import ccopen

from numpy import *
import numpy as np
import re
import logging
import sys
import gzip
import os
import copy
import io

class MolData:
    """A general molecular data, such as orbitals, basis set, etc.

    Attributes:
    
       atoms = [(Z, (x,y,z)), ... ]
       spherical = (True, True, True)
       mocoeffs = like cclib
       mosyms = like cclib
       mooccups - analogous to moenergies, etc.
       moenergies = like cclib
       gbasis | sbasis = like cclib |  ??? document this feature -- FIXME
       
    """
    def __init__(self, attributes):
        """Creates MolData object from attributes dictionary
        """
        for attr in ["atoms", "spherical", "mocoeffs", "mosyms", "mooccups",
                     "moenergies"]:
            setattr(self, attr, attributes[attr])
        if "sbasis" in attributes:
            setattr(self, "sbasis", attributes["sbasis"])
        elif "gbasis" in attributes:
            setattr(self, "gbasis", attributes["gbasis"])
        else: raise KeyError("Missing `sbasis' or `gbasis' keys.")

        # Length unit string to be used when writing Molden Format
        self.MOLDEN_LENGTH_UNIT_STR = {
            'Angstrom': 'Angs',
            'bohr': 'AU',
            'Fractional': 'Fractional'}
            
        if "length_unit" in attributes:
            assert attributes["length_unit"] in self.MOLDEN_LENGTH_UNIT_STR, "Unknown lenght unit"
            self.length_unit = attributes["length_unit"]
        else:
            self.length_unit = "Angstrom"
            
        if "extensions" in attributes:
            setattr(self, "extensions", attributes["extensions"])

    def _setup_logger(self, logname, loglevel):
        """Initialize logger
        """
        if hasattr(self, "logger"): return
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(loglevel)
        if len(self.logger.handlers)==0:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(logging.Formatter("[%(name)s %(levelname)s] %(message)s"))
            self.logger.addHandler(handler)        
        
    def write_molden_format(self, outfile, mo_filter = lambda o, e: True):
        """Convert MolData to MoldenFormat and write to a file

        (*) mo_filter --- 2-argument function (taking the orbital
        occupation and energy as arguemens) to filter the mos (only those
        for which this function returns true will be written to the
        outfile. Default is to return true for all orbitals.
        """
        outfile.write("[Molden Format]\n")

        # print extensions for crystals
        if hasattr(self, "extensions") and self.extensions:
            for title, value in self.extensions:
                outfile.write('%s' %value)
        
        # atoms            
        outfile.write("[Atoms] (%s)\n" %(self.MOLDEN_LENGTH_UNIT_STR[self.length_unit]))
        pt = PeriodicTable()
        for i, (at_Z, (x, y, z)) in enumerate(self.atoms):
            outfile.write('%(element_name)3s %(i)4d %(atomic_number)3d %(x)10.6f %(y)10.6f %(z)10.6f\n' %
                          {'element_name': pt.element[int(at_Z)], 'i': i+1,
                           'atomic_number': at_Z,
                           'x': x, 'y': y, 'z': z})
        ## FIXME: int(at_Z) should not be needed, but
        ## it is necessary when using cclib-parsed Gaussian logs.

        # spherical or cartesian
        if self.spherical and len(self.spherical) >= 3: # FIXME: what to do with larger sizes? (h functions)
            if self.spherical[0]:
                if self.spherical[1]:
                    outfile.write("[5d7f]\n")
                else:
                    outfile.write("[5d10f]\n")
            elif self.spherical[1]:
                outfile.write("[6d7f]\n")
            if self.spherical[2]:
                outfile.write("[9g]\n")

            if hasattr(self, "sbasis"):
                outfile.write("[STO]\n")
                for (atom, kx, ky, kz, kr, alpha, norm) in self.sbasis:
                    outfile.write("%4d  %d %d %d %d %12.6f %12.6f\n" %(atom+1,kx,ky,kz,kr,alpha,norm))

        # basis
        if hasattr(self, "gbasis"):
            outfile.write("[GTO]\n")
            for i in range(0, len(self.atoms)):
                outfile.write("%d 0\n" %(i+1))
                for contraction in self.gbasis[i]:
                    outfile.write("%s %d 1.00\n" %(contraction[0], len(contraction[1])))
                    # (Number of contractions is not necessairly 1
                    # e.g. for 'sp' shells. However, all cases are
                    # handled together here.)
                    format = "%20.10e  "
                    nc = len(contraction[1][0]) - 1
                    for _ in range(0, nc): format += "  %20.10e"
                    format += "\n"
                    for ec in contraction[1]:
                        outfile.write(format % ec)
                outfile.write("\n")
            outfile.write("\n")

        # MOs
        outfile.write("[MO]\n")
        spin_name = ('Alpha', 'Beta')

        # determine if we have also overlaps to print
        has_overlaps = hasattr(self, "overlaps_alpha")
        for s in range(0, len(self.mocoeffs)):
            if has_overlaps:
                print("spin, occup, energy, max overlap alpha, max overlap beta:")

            for (i,(sym, e, o, lcao)) in enumerate(zip(self.mosyms[s], self.moenergies[s],
                                         self.mooccups[s], self.mocoeffs[s])):
                if not mo_filter(o, e): continue
                outfile.write("Sym= %s\n" %sym)
                outfile.write("Ene= %f\n" %e)
                outfile.write("Spin= %s\n" %spin_name[s])
                outfile.write("Occup = %f\n" %o)
                for j, x in enumerate(lcao):
                    outfile.write("%4d %20.10e\n" %(j+1, x))
                if has_overlaps:
                    s_a, s_b = self.overlaps_alpha[s][i], self.overlaps_beta[s][i]
                    abs_s_a = abs(s_a)
                    abs_s_b = abs(s_b)
                    s_a_imax = abs_s_a.argmax()
                    s_b_imax = abs_s_b.argmax()
                    print("%d   %.3f  %.6f  %d (%2.0f%%) %d (%2.0f%%)" %(
                        s,o,e,s_a_imax+1,100*abs_s_a[s_a_imax], s_b_imax+1,100*abs_s_b[s_b_imax]))
        outfile.write("\n")

        
class MolData_from_MoldenFormat(MolData):
            
    def __init__(self, inputfilename, logname="MolData_from_MoldenFormat", loglevel=logging.INFO, rebase_coeffs=None): 
        """
        set `rebase_coeffs' to True when parsing molden files generated by CRYSTAL (even for molecules) 
        in order to fix problem with numbering of AOs for BETA orbitals, see below.
        """
        self._setup_logger("%s %s" %(logname,inputfilename), loglevel)
        self._is_crystal = False
        self._rebase_coeffs = rebase_coeffs
        attributes = self._parse(open(inputfilename, "r"))
        MolData.__init__(self, attributes)

    def _parse(self, inputfile):
        attributes = {}
        attributes["spherical"] = [False, False, False]

        self.logger.debug("Mark sections in Molden Format.")
        sections = self._markSections(inputfile)

        self.logger.debug("Parsing Molden Format.")
        for (title, start, end) in sections:

            if title == 'molden': # ignore [Molden Format] section
                pass
            
            elif title == 'atoms':
                attributes["atoms"], attributes["length_unit"] = self._readAtoms(inputfile, start, end)

            # it does not work, because orbitals are given
            # for a different orientation!
            #
            #elif title == 'geometries':
            #    geometries = self._readGeometries(inputfile, start, end)

            elif title == '5d' or title == '5d7f':
                attributes["spherical"][0] = True
                attributes["spherical"][1] = True
            elif title == '5d10f':
                attributes["spherical"][0] = True
                attributes["spherical"][1] = False
            elif title == '7f':
                attributes["spherical"][1] = True
            elif title == '9g':
                attributes["spherical"][2] = True

            elif title == 'gto':
                attributes["gbasis"] = self._readGBasis(inputfile, start, end,
                                                        len(attributes["atoms"]))

            elif title == 'sto':
                attributes["sbasis"] = self._readSBasis(inputfile, start, end)

            elif title == 'mo':
                if self._rebase_coeffs == None:
                    if self._is_crystal: self._rebase_coeffs = True
                    else: self._rebase_coeffs = False
                    
                assert self._rebase_coeffs == True or self._rebase_coeffs == False
                mosyms, mocoeffs, mooccups, moenergies = self._readMOs(inputfile, start, end)
                attributes["mosyms"] = mosyms
                attributes["mocoeffs"] = mocoeffs
                attributes["mooccups"] = mooccups
                attributes["moenergies"] = moenergies

        # it does not work because orbitals are given for
        # a different orientation!
        
        ## If there are several geometries provided in the
        ## geometries section, this Molden files is from geometry
        ## optimization. In such a case use the last geometry,
        ## to make it consistent with the orbitals.
        ##n = len(geometries)
        ##if n > 1:
        ##    attributes["atoms"] = geometries[n-1]

            else: # all other sections, not defined by standard molden format
                if not "extensions" in attributes:
                    attributes["extensions"] = []
                attributes["extensions"].append(
                    (title, self._readOtherSectionVerbatim(inputfile, start, end))
                    )
                self.logger.info("Found non-standard section: %s" %title)
                # if this is looks like a crystal, save this information 
                if title == 'spacegroup': 
                    self._is_crystal = True
        
        return attributes

    def _markSections(self, inputfile):
        """read and mark sections in file"""
        sections = []
        title = False
        start = 0
        while True:
            pos = inputfile.tell()
            line = inputfile.readline()
            if not line: # EOF reached
                if title: sections.append((title, start, pos))
                break
            elif line.strip() and line.strip()[0] == '[': # new section found
                if title: sections.append((title, start, pos))
                title = line.split()[0].strip('[').strip(']').lower()
                if not title: raise SyntaxError("Error in MoldenFormat: empty section name")
                start = pos
        return sections
    

    def _readGeometries(self, inputfile, start, end):
        """parse geometries section"""
        inputfile.seek(start)
        line = inputfile.readline()
        if len(line.split()) > 1:
            assert line.split()[1].lower() == 'xyz'
        geometries = []
        pt = PeriodicTable()
        atoms = None
        while inputfile.tell() < end:
            line = inputfile.readline()
            broken = line.split()
            if len(broken) == 1:
                if atoms:
                    geometries.append(atoms)
                inputfile.readline()
                atoms = []
            elif len(broken) == 4:
                at_Z = pt.number[broken[0]]
                coords = array(list(map(float, broken[1:4])))
                atoms.append((at_Z, coords))
        geometries.append(atoms)
        #print (geometries)
        return geometries
        
    
    def _readAtoms(self, inputfile, start, end):
        """parse atoms section
        Return a tuple: atoms, length_units
        where length_units will be either 'Angstrom', 'bohr', or 'Fractional' (extension).
        (Presently this function converts AU to Angs, so 'bohr' is never returned.
        """

        # get units info -- in the title line
        inputfile.seek(start)
        line = inputfile.readline()
        if len(line.split()) > 1:
            unit = line.split()[1].lower().strip("(").strip(")")
            if unit.lower()[0:3] == "ang": unit = "Angstrom"
            elif unit.lower() == "au": unit = "bohr"
            elif unit.lower() == "fractional": unit = "Fractional"
            else: raise RuntimeError("Unknown lenght unit: %s" %unit)
        else: unit = "Angstrom"
        # convert bohr to Angstrom, other units (Angstrom, Fractional kept intact)
        if unit == "bohr":
            lconvert = lambda x: convertor(x, "bohr", "Angstrom")
            unit = "Angstrom"
        else:
            lconvert = lambda x: x
            
        # read all atoms
        atoms = []
        while inputfile.tell() < end:
            line = inputfile.readline()
            broken = line.split()
            if len(broken) == 6: # 6 items per line for correct entry
                at_Z = int(broken[2])
                coords = array(list(map(lconvert, map(lambda _: float(_.replace('D','E')), broken[3:6]))))
                atoms.append((at_Z, coords))
        return atoms, unit

    def _readOtherSectionVerbatim(self, inputfile, start, end):
        """read other sections (no parsing)

        Possibly extensions of the Molden Format. 
        For instance, sections added by Crystal.
        So far no attempt to parse, just verbatim storage of the original.
        """
        inputfile.seek(start)
        value = ''
        while inputfile.tell() < end:
            value += inputfile.readline()
        return value
        
    def _readGBasis(self, inputfile, start, end, nAtoms):
        inputfile.seek(start)
        line = inputfile.readline()

        gbasis = []

        for i in range(0, nAtoms):
            atomic_gbasis = []
            line = inputfile.readline()
            atom_no = list(map(int, line.split()))[0]
            line = inputfile.readline()
            while line.strip():
                shell_label, no_primitives = line.split()[0:2]
                contractions = []
                for i in range(0, int(no_primitives)):
                    contractions.append(tuple(map(lambda _: float(_.replace('D','E')), inputfile.readline().split())))
                atomic_gbasis.append((shell_label.upper(), contractions))
                line = inputfile.readline()
            gbasis.append(atomic_gbasis)
        return gbasis


    def _readSBasis(self, inputfile, start, end):
        inputfile.seek(start)
        line = inputfile.readline()

        sbasis = []

        while inputfile.tell() < end:
            atom, kx, ky, kz, kr, alpha, norm = inputfile.readline().split()
            atom = int(atom)-1
            kx = float(kx.replace('D','E'))
            ky = float(ky.replace('D','E'))
            kz = float(kz.replace('D','E'))
            kr = float(kr.replace('D','E'))
            alpha = float(alpha.replace('D','E'))
            norm = float(norm.replace('D','E'))
            sbasis.append((atom, kx, ky, kz, kr, alpha, norm))
            # FIXME: remove `atom' and group all contractions by atom
            # (like in `gbasis').
        return sbasis


    def _readMOs(self, inputfile, start, end):
        inputfile.seek(start)
        line = inputfile.readline()

        mocoeffs = [[], []]
        moenergies = [[], []]
        mooccups = [[], []]
        mosyms = [[], []]

        symmetry = "A" # FIXME: how it used to work before (without the default irrep)??
        line = inputfile.readline()
        parsing = True
        while parsing and line.strip():

            if line.strip().lower()[:3] == "sym":
                symmetry = self._normaliseSym(line.split("=")[1].strip())
                line = inputfile.readline()

            elif line.strip().lower()[:3] == "ene":
                energy = float(line.split("=")[1].strip())
                line = inputfile.readline()

            elif line.strip().lower()[:3] == "spi":
                spin_letter = line.split("=")[1].strip()[0].lower()
                # ^... just 'a' or 'b'
                if spin_letter == 'a': spin = 0
                elif spin_letter == 'b': spin = 1
                else: raise RuntimeError(
                    "Wrong spin (should be `alpha' or `beta', but `%s' found)." %spin)
                line = inputfile.readline()

            elif line.strip().lower()[:3] == "occ":
                occup = float(line.split("=")[1].strip().replace('D','E'))
                line = inputfile.readline()

            elif line.strip()[0] != "[": # FIXME
                # read MO coeffs
                coeffs = []
                while True:
                    try:
                        broken = line.split()
                        n, C = int(broken[0]), float(broken[1].replace('D','E'))
                        # FIXME:
                        # In Molden files from Crystal, the coeffs of BETA orbitals
                        # are numerated from s+1 (where s is size of the basis set);
                        # Don't know why; this seems to be incorrect, or at least misleading.
                        # In such a case, we should not add trailing zeros, as normally when
                        # the above n is larger ???
                        if not self._rebase_coeffs:     
                            for dummy in range(len(coeffs)+1, n):
                                coeffs.append(0.)
                        coeffs.append(C)
                    except ValueError: break
                    line = inputfile.readline()
                    if not line:
                        parsing=False
                        break

                # add the currect MO to the list
                mosyms[spin].append(symmetry)
                mocoeffs[spin].append(coeffs)
                moenergies[spin].append(energy)
                mooccups[spin].append(occup)

            else: break

        # Reorder MOs (occupied before virtual)
        for s in 0,1:

            occ_occups, virt_occups = [], []
            occ_syms, virt_syms = [], []
            occ_coeffs, virt_coeffs = [], []
            occ_energies, virt_energies = [], []
            
            for i in range(0, len(mooccups[s])):
                n = mooccups[s][i] 

                if allclose(n, 0): # virtual
                    virt_occups.append(n)
                    virt_syms.append(mosyms[s][i])
                    virt_coeffs.append(mocoeffs[s][i])
                    virt_energies.append(moenergies[s][i])

                else: # occupied: 1,2 or fractional
                    occ_occups.append(n)
                    occ_syms.append(mosyms[s][i])
                    occ_coeffs.append(mocoeffs[s][i])
                    occ_energies.append(moenergies[s][i])

            mooccups[s] = occ_occups + virt_occups
            mosyms[s] = occ_syms + virt_syms
            mocoeffs[s] = occ_coeffs + virt_coeffs
            moenergies[s] = occ_energies + virt_energies
            
        # filling empty MO coefficients with zeros
        # (needed for truncated Molden files produced e.g. by Jaguar)
        def max_or_zero(x):
            if x: return max(x)
            else: return 0
        N = max(map(lambda x: max_or_zero(list(map(len, x))), mocoeffs))
        for mos in mocoeffs:
            for C in mos:
                for dummy in range(len(C), N): C.append(0.)

        # Eliminate 2nd items of mocoeffs, moenergies, mosyms and mooccups
        # in case of restricted orbitals
        if len(mosyms[1]) == 0:
            mosyms = [mosyms[0]]
        if len(mooccups[1]) == 0:
            mooccups = [mooccups[0]]        
        if len(mocoeffs[1]) == 0:
            mocoeffs = [mocoeffs[0]]
        if len(moenergies[1]) == 0:
            moenergies = [moenergies[0]]
        #print ('len mocoeffs: ', len(mocoeffs))

        # Convert
        mocoeffs = list(map(array, mocoeffs))
        mooccups = list(map(array, mooccups))
        moenergies = list(map(array, moenergies))
        
        return mosyms, mocoeffs, mooccups, moenergies

        
    def _normaliseSym(self, label):
        """Normalize a symmetry label from MoldenFormat"""
        # strip number which often occur in molden format
        m = re.match("\d*\.?(?P<sym>[\w\._'\"]+)", label)
        if m:
            # it's very difficult to guess labels which might appear in molden format;
            # this is moreless consistent with cclib, however 'A.g' will remain unchanged
            # (it should have became 'Ag')
            sym = m.group("sym")
            sym = sym.lower()
            if sym[:3] == "aaa":
                sym = (sym.replace("aaa", "a") + '"')
            elif sym[:2] == "aa":
                sym = (sym.replace("aa", "a") + "'")
            sym = sym.replace("''", '"')
            sym = sym[0].upper() + sym[1:]
            sym = sym.replace("p", "'")
            sym = sym.replace("pp", '"')
            sym = sym.replace("Sigma", "sigma")
            sym = sym.replace("Sg", "sigma")
            sym = sym.replace("Pi", "pi")
            sym = sym.replace("Delta", "delta")
            sym = sym.replace("Dlta", "delta")
            sym = sym.replace("Dltu", "delta.u")
            sym = sym.replace("Dltg", "delta.g")
            sym = sym.replace("Phi", "phi")
            return sym
        else: raise RuntimeError(
            "A symmetry label has incorrect format: %s" %label)

class MolData_from_gzMoldenFormat(MolData_from_MoldenFormat):
    def __init__(self, inputfilename, logname="MolData_from_gzMoldenFormat", loglevel=logging.INFO, rebase_coeffs=None): 
        self._setup_logger("%s %s" %(logname,inputfilename), loglevel)
        self._is_crystal = False
        self._rebase_coeffs = rebase_coeffs
        attributes = self._parse(io.TextIOWrapper(gzip.open(inputfilename, "r")))
        MolData.__init__(self, attributes)

class MolData_via_cclib(MolData):     # FIXME: not functional yet!

    def __init__(self, inputfilename, logname="MolData_from_cclib", loglevel=logging.INFO):
        self._setup_logger("%s %s" %(logname,inputfilename), loglevel)
	#MR: to make it compatible with cclib 1.3.1
        #from cclib.progress import TextProgress 
        #data = ccopen(inputfilename, TextProgress(), logging.ERROR).parse()
        data = ccopen(inputfilename, loglevel=logging.ERROR).parse()
        if data.mult == 1 and len(data.mocoeffs) == 1:
            # standard restricted singlet
            n1 = (sum(data.atomnos) - data.charge) / 2
            n = int(n1)
            assert np.isclose(n, n1)
            mooccups = ([2. for i in range(0, n)] + \
                        [0. for i in range(n, len(data.moenergies[0]))], )
        else:
            # unrestricted singlet or higher multiplicity
            nb = (sum(data.atomnos) - data.charge - data.mult + 1)/2
            na = nb + data.mult - 1
            na=int(na)
            nb=int(nb)
            mooccups = ([1. for i in range(0,na)] + \
                        [0. for i in range(na,len(data.moenergies[0]))],
                        [1. for i in range(0,nb)] + \
                        [0. for i in range(nb,len(data.moenergies[1]))],)
        if not hasattr(data, "mosyms"):
            data.mosyms = [list(map(lambda _: "A", data.moenergies[0])),
                           list(map(lambda _: "A", data.moenergies[1]))]
                   
        n_struct = data.atomcoords.shape[0]
        attributes = {
            'atoms': list(zip(data.atomnos,
                         data.atomcoords[n_struct-1, :, :])),
            'spherical': (True, True, True),
            'gbasis': data.gbasis,
            'mocoeffs': data.mocoeffs,
            'mosyms': data.mosyms,
            'mooccups': mooccups,
            'moenergies': list(map(lambda x: x / 27.2113845, data.moenergies)), # eV back to a.u.
            }
        MolData.__init__(self, attributes)



def read_molecule(inputfilename, loglevel=logging.INFO, rebase_coeffs=None):
    """Read molecule from MoldenFormat or (in future) via cclib
    """
    if os.path.splitext(inputfilename)[1] == '.gz':
        with io.TextIOWrapper(gzip.open(inputfilename, mode="r")) as gzfile:
            test_phrase = gzfile.readline().strip().lower()
        if '[molden format]' in test_phrase or '[title]' in test_phrase:
            return MolData_from_gzMoldenFormat(
                inputfilename, loglevel=loglevel, rebase_coeffs=rebase_coeffs)
        else:
            return MolData_via_cclib(io.TextIOWrapper(gzip.open(inputfilename, mode="r")), loglevel)
    else:
        with open(inputfilename, "r") as infile:
            test_phrase = infile.readline().strip().lower()
        if '[molden format]' in test_phrase or '[title]' in test_phrase:
            return MolData_from_MoldenFormat(
                inputfilename, loglevel=loglevel, rebase_coeffs=rebase_coeffs)
        else:
            return MolData_via_cclib(inputfilename, loglevel)

def filter_orbitals(md, filters):
    """Filter orbitals stored in MolData object

    md         - a MolData object.
    filters    - a list of three-argument filter functions operating
                 on each orbital occupation, symmetry and coefficients.
    """
    new_mooccups = [[],[]]
    new_mosyms = [[], []]
    new_mocoeffs = [[], []]
#    print('len(md.mocoeffs): ' + str(len(md.mocoeffs)))
#    print('len(md.mooccups): ' + str(len(md.mooccups)))
#    print('len(md.mosyms): ' + str(len(md.mosyms)))
#    print(md.mooccups)
    for spin in range(0,len(md.mocoeffs)):
        for (o,s,c) in zip(
            md.mooccups[spin], md.mosyms[spin], md.mocoeffs[spin]):

            match = True
            for f in filters:
                if not f(o,s,c):
                    match = False
                    break
            if match:
                new_mooccups[spin].append(o)
                new_mosyms[spin].append(s)
                new_mocoeffs[spin].append(c)
        new_mooccups[spin] = array(new_mooccups[spin])
        new_mosyms[spin] = array(new_mosyms[spin])
        new_mocoeffs[spin] = array(new_mocoeffs[spin])

    # drop unnecessary second component in the case of
    # unrestricted calculations
    if len(new_mooccups[1]) == 0:
        new_mooccups = [new_mooccups[0]]
    if len(new_mosyms[1]) == 0:
        new_mosyms = [new_mosyms[0]]
    if len(new_mocoeffs[1]) == 0:
        new_mocoeffs = [new_mocoeffs[0]]
        
    new_md = copy.copy(md)
    new_md.mooccups = new_mooccups
    new_md.mosyms = new_mosyms
    new_md.mocoeffs = new_mocoeffs
            
    return new_md
