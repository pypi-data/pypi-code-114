'''
Created on Jul 20, 2018

@author: Juan L. Mateo
'''

import json
from aceofbases.sequence_methods import reverse_complement


class PAM:
    '''
    Generic class to define the different PAM types and the methods needed
    The seed for Bowtie will be always 5
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.core_allowed = False  # By default a PAM is not compatible with the core region
        self.is5prime = False # Is the PAM at the 5' end, by default it is false
        self.pam_str = self.__class__.__name__
        self.pam_rev = reverse_complement(self.pam_str)  # any ambiguous base is turned into N
        self.mismatches_in_pam = self.pam_rev.count('N')
        self.mismatches_in_seed = min(3,self.pam_rev[0:5].count('N')) # Value for the -n parameter of Bowtie


    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # By default all PAM are in the 3' end and the sequence is reversed to match the seed definition of Bowtie
        fasta = ""
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + self.pam_rev + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
        return fasta

    def get_bowtie_options(self, core_mismatches, core_range, total_mismatches):
        "Returns the options string to run bowtie"
        if not self.core_allowed or core_mismatches == "NA" or core_range == "NA":
            return ["-a", "--quiet", "-y", "-n" + str(self.mismatches_in_seed), "-l5",
                    "-e" + str((total_mismatches + self.mismatches_in_pam) * 30)]

        if (core_mismatches + self.mismatches_in_pam)>3:
            raise ValueError('The value for the parameter core_mismatches is not valid: ' + str(core_mismatches))
        if core_mismatches > total_mismatches:
            raise ValueError('The value for core_mismatches cannot be greater than total_mismatches:'
                             + str(core_mismatches) + ">" + str(total_mismatches))
        return ["-a", "--quiet", "-y", "-n" + str(core_mismatches + self.mismatches_in_pam),
                "-l" + str(core_range + len(self.pam_str)),
                "-e" + str((total_mismatches + self.mismatches_in_pam) * 30)]

    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        '''
        Tells if the hit found show a set of mismatches, if any, consistent with the variable positions in the PAM
        '''
        # This generic version works for PAMs (5' or 3') where only the first position is an N
        # and the other position are not variables
        # NGG, NGA, NGCG, TTTN, NAAAAC
        # This is also fine for NRG because we search twice for NGG and NAG
        # The same for YTN (CTN, TTN)
        mismatches = bowtie_line_columns[7].split(',')
        pos_first_mm = int(mismatches[0].split(":")[0])
        return pos_first_mm >= (len(self.pam_str) - 1)

class NGG(PAM):
    "Class that represents the NGG PAM"
    def __init__(self):
        super().__init__()
        self.core_allowed = True
        self.mismatches_in_seed = 3

class NRG(PAM):
    "Class that represents the NRG PAM"
    def __init__(self):
        super().__init__()
        self.core_allowed = True
        self.mismatches_in_pam = 1
        self.mismatches_in_seed = 3

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # As there are too many variable positions it is necessary to search
        # two sequences fixing the 'R' with 'A' or 'G' in each case
        fasta = ""
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CCN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CTN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
        return fasta

class NG(PAM):
    "Class that represents the NG PAM"
    def __init__(self):
        super().__init__()
        self.core_allowed = True
        self.mismatches_in_pam = 0
        self.mismatches_in_seed = 3

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # As there are too many variable positions it is necessary to search
        # four sequences fixing the 'N' with the four possible bases
        fasta = ""
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CT" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CG" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CC" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CA" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
        return fasta
    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        # It is possible to get 0 mismatches, in that case it is consistent
        if not ":" in mismatches[0]:
            return True
        pos_first_mm = int(mismatches[0].split(":")[0])
        return pos_first_mm >= len(self.pam_str)

class NGA(PAM):
    "Class that represents the NGA PAM"
    def __init__(self):
        super().__init__()
        self.core_allowed = True
        self.mismatches_in_seed = 3

class NGCG(PAM):
    "Class that represents the NGCG PAM"
    def __init__(self):
        super().__init__()
        self.core_allowed = True
        self.mismatches_in_seed = 2

class TTTN(PAM):
    "Class that represents the TTTN PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_seed = 2
        self.is5prime = True

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # In this case the PAM is 5'
        fasta = ""
        pam_str = self.__class__.__name__
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + pam_str + candidate.sequence[len(pam_str):] + "\n"
        return fasta

class TTTV(PAM):
    "Class that represents the TTTV PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_seed = 1
        self.is5prime = True
        self.mismatches_in_pam = 0 # The variable position is replaced by the 3 possible bases

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # In this case the PAM is 5'
        fasta = ""
        pam_str = self.__class__.__name__
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TTTA" + candidate.sequence[len(pam_str):] + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TTTC" + candidate.sequence[len(pam_str):] + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TTTG" + candidate.sequence[len(pam_str):] + "\n"
        return fasta

    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        # It is possible to get 0 mismatches, in that case it is consistent
        if not ":" in mismatches[0]:
            return True
        pos_first_mm = int(mismatches[0].split(":")[0])
        return pos_first_mm >= len(self.pam_str)

class YTN(PAM):
    "Class that represents the YTN PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_pam = 1
        self.mismatches_in_seed = 3
        self.is5prime = True

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # In this case the PAM is 5'
        fasta = ""
        pam_str = self.__class__.__name__
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TTN" + candidate.sequence[len(pam_str):] + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CTN" + candidate.sequence[len(pam_str):] + "\n"
        return fasta

class TTN(PAM):
    "Class that represents the TTN PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_pam = 1
        self.mismatches_in_seed = 3
        self.is5prime = True

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # In this case the PAM is 5'
        fasta = ""
        pam_str = self.__class__.__name__
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + pam_str + candidate.sequence[len(pam_str):] + "\n"
        return fasta

class YTTN(PAM):
    "Class that represents the YTTN PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_pam = 1
        self.mismatches_in_seed = 2
        self.is5prime = True

    def get_sequences_for_bowtie(self, sites):
        # In this case the PAM is 5'
        fasta = ""
        pam_str = self.__class__.__name__
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TTTN" + candidate.sequence[len(pam_str):] + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CTTN" + candidate.sequence[len(pam_str):] + "\n"
        return fasta

class NNNRRT(PAM):
    "Class that represents the NNNRRT PAM"
    def __init__(self):
        super().__init__()
        # One of the variable position will be fixed so that the number or real mismatches is one less
        self.mismatches_in_pam = 4

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # As there are too many variable positions it is necessary to search
        # two sequences fixing the most 3' 'R' with 'A' or 'G' in each case
        fasta = ""
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "ACNNNN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "ATNNNN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
        return fasta

    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        first_mm = mismatches[0].split(":")
        pos_first_mm = int(first_mm[0])
        if pos_first_mm > 2:
            return True
        if pos_first_mm == 2:
            if bowtie_line_columns[1] == '+':
                return first_mm[1][0] in 'CT'
            return first_mm[1][0] in 'AG'

        return False

class NNGRRT(PAM):
    "Class that represents the NNGRRT PAM"
    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        first_mm = mismatches[0].split(":")
        pos_first_mm = int(first_mm[0])
        if pos_first_mm > 3:
            return True
        if pos_first_mm == 1:
            return (bowtie_line_columns[1] == '+'
                    and (mismatches[0][2] in 'CT' and mismatches[1][2] in 'CT')) or (bowtie_line_columns[1] == '-' and (mismatches[0][2] in 'AG' and mismatches[1][2] in 'AG'))
        return False

class NNNNGATT(PAM):
    "Class that represents the NNNNGATT PAM"
    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        return True

class NNAGAAW(PAM):
    "Class that represents the NNAGAAW PAM"
    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        first_mm = mismatches[0].split(":")
        pos_first_mm = int(first_mm[0])
        if pos_first_mm > 4:
            return True
        if pos_first_mm == 0:
            return mismatches[0][2] in 'AT'
        return False

class NAAAAC(PAM):
    "Class that represents the NAAAAC PAM"
    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        return True

class NNNNRYAC(PAM):
    "Class that represents the NNNNRYAC PAM"
    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        first_mm = mismatches[0].split(":")
        pos_first_mm = int(first_mm[0])
        if pos_first_mm > 3:
            return True
        if pos_first_mm == 2:
            return (bowtie_line_columns[1] == '+' and (mismatches[0][2] in 'AG' and mismatches[1][2] in 'CT')) or (bowtie_line_columns[1] == '-' and (mismatches[0][2] in 'CT' and mismatches[1][2] in 'AG'))
        return False

class NRN(PAM):
    "Class that represents the NRN PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_pam = 1

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # By default all PAM are in the 3' end and the sequence is reversed to match the seed definition of Bowtie
        fasta = ""
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "ACN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CCN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "GCN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TCN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "ATN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CTN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "GTN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TTN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"

        return fasta

    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        mismatches = bowtie_line_columns[7].split(',')
        pos_first_mm = int(mismatches[0].split(":")[0])
        if pos_first_mm > 1:
            return True
        return False

class NYN(PAM):
    "Class that represents the NYN PAM"
    def __init__(self):
        super().__init__()
        self.mismatches_in_pam = 1

    def get_sequences_for_bowtie(self, sites):
        '''
        Receives a list of EditingSite objects and returns a string with the
        fasta sequences formatted to perform the search of off-target sites with
        Bowtie
        '''
        # By default all PAM are in the 3' end and the sequence is reversed to match the seed definition of Bowtie
        fasta = ""
        for candidate in sites:
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "AAN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CAN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "GAN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TAN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "AGN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "CGN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "GGN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"
            fasta = fasta + ">" + candidate.label + "\n"
            fasta = fasta + "TGN" + reverse_complement(candidate.sequence[:-len(self.pam_str)]) + "\n"

        return fasta

    def is_bowtie_hit_consistent(self, bowtie_line_columns):
        '''
        Tells if the hit found show a set of mismatches, if any, consistent with the variable positions in the PAM
        '''
        mismatches = bowtie_line_columns[7].split(',')
        pos_first_mm = int(mismatches[0].split(":")[0])
        if pos_first_mm > 1:
            return True
        return False

def factory(type):
    "Method following the factory patern to create the different PAM objects"
    pams = {
        "NGG": NGG,
        "NRG": NRG,
        "NG": NG,
        "NGA": NGA,
        "NGCG": NGCG,
        "TTTN": TTTN,
        "TTTV": TTTV,
        "YTN": YTN,
        "TTN": TTN,
        "YTTN": YTTN,
        "NNNRRT": NNNRRT,
        "NNGRRT": NNGRRT,
        "NNNNGATT": NNNNGATT,
        "NNAGAAW": NNAGAAW,
        "NAAAAC": NAAAAC,
        "NNNNRYAC": NNNNRYAC,
        "NRN": NRN,
        "NYN": NYN,
        }
    if not type in pams:
        assert 0, "Wrong PAM type: " + type
    return pams[type]()



if __name__ == "__main__":
    dictionary = {}
    for cls in PAM.__subclasses__():
        obj = cls()
        dictionary[obj.__class__.__name__] = obj.__dict__
    with open("pams.js", "w") as fp:
        fp.write("var jsonPAMs=")
        json.dump(dictionary, fp, default=vars)
