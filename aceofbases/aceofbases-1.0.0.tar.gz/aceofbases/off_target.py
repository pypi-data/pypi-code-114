'''
Created on Jul 24, 2018

@author: Juan L. Mateo
'''
from aceofbases.sequence_methods import reverse_complement

class OffTarget:
    "Class representing an off-taget site"
    # New offtarget site coming for forward search, TTTN
    def __new_fwd(self, chromosome, strand, start, substitutions, sequence, length_seq, length_pam, core_range):
        self.chromosome = chromosome
        self.strand = strand
        if strand == "+":  # the search is done with the forward sequence!
            self.sequence = list(sequence)  # to make the string modifiable
        else:
            self.sequence = list(reverse_complement(sequence))  # to make the string modifiable
        self.start = start  # assuming bed coordinates
        self.end = start + length_seq

        tmp = substitutions.split(",")

        ####self.mismatches = len(tmp) - 1
        self.mismatches = 0
        self.alignment = ['|'] * (length_seq - length_pam)
        self.score = 0
        for substitution in tmp:
            if not ":" in substitution: # No mismatch, ignoring
                continue
            [idx,base] = substitution.split(':')
            idx = int(idx)
            if strand == "+":
                self.sequence[idx] = base[0]
            else:
                self.sequence[idx] = reverse_complement(base[0])
            if idx < length_pam:  # The mismatch in the PAM is not considered for score calculation of alignment
                continue
            self.mismatches += 1
            self.score = self.score + pow(1.2, idx - length_pam + 1)
            self.alignment[idx - length_pam] = '-'
        if core_range != "NA" and core_range > 0:
            self.alignment = "PAM[" + "".join(self.alignment[:core_range]) + "]" + "".join(self.alignment[core_range:])
        else:
            self.alignment = "PAM" + "".join(self.alignment)
        self.sequence = "".join(self.sequence)
        # self.sequence = reverse_complement("".join(self.sequence))

    # New offtarget site coming for reverse search, NGG and other PAMs
    def __new_rev(self, chromosome, strand, start, substitutions, sequence, length_seq, length_pam, core_range):
        self.chromosome = chromosome
        if strand == "+":  # the search is done with the reverse complemented sequence!
            self.strand = "-"
            self.sequence = list(sequence)  # to make the string modifiable
        else:
            self.strand = "+"
            self.sequence = list(reverse_complement(sequence))  # to make the string modifiable
        self.start = start  # assuming bed coordinates
        self.end = start + length_seq

        tmp = substitutions.split(",")

        ####self.mismatches = len(tmp) - 1
        self.mismatches = 0
        self.alignment = ['|'] * (length_seq - length_pam)
        self.score = 0
        for substitution in tmp:
            if not ":" in substitution: # No mismatch, ignoring
                continue
            [idx, base] = substitution.split(':')
            idx = int(idx)
            if strand == "+":
                self.sequence[idx] = base[0]
            else:
                self.sequence[idx] = reverse_complement(base[0])
            if idx < length_pam:  # The mismatch in the PAM is not considered for score calculation of alignment
                continue
            self.mismatches += 1
            self.score = self.score + pow(1.2, length_seq - idx)
            self.alignment[length_seq - 1 - idx] = '-'
        if core_range != "NA" and core_range > 0:
            self.alignment = "".join(self.alignment[:-core_range]) + "[" + "".join(self.alignment[-core_range:]) + "]PAM"
        else:
            self.alignment = "".join(self.alignment) + "PAM"
        self.sequence = reverse_complement("".join(self.sequence))


    def __init__(self, forward, chromosome, strand, start, substitutions, sequence,
                 length_seq, length_pam, core_range):
        if forward:
            self.__new_fwd(chromosome, strand, start, substitutions, sequence, length_seq, length_pam, core_range)
        else:
            self.__new_rev(chromosome, strand, start, substitutions, sequence, length_seq, length_pam, core_range)

    def set_gene_info(self, exons, genes):
        "Sets the information relates to the closest gene"
        closest = exons.closest(self.chromosome, self.start, self.end)

        self.gene_id = closest[0]
        self.gene_name = closest[1]
        self.distance = closest[2]
        self.intragenic = genes.overlaps(self.chromosome, self.start, self.end)

    def get_genomic_coordinates(self):
        "Returns the off-target coordinates"
        return [self.chromosome, str(self.start + 1), str(self.end)]
    def get_bed_coordinates(self):
        "Return the off-target coordinates in bed format"
        return [self.chromosome, str(self.start), str(self.end)]
