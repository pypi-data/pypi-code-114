'''
Created on May 5, 2021

@author: Juan L. Mateo
'''

from aceofbases.sequence_methods import reverse_complement


class EditingSite:
    "A class to define the targeted editing site"
    def __init__(self, target_seq, sequence, position, strand, fwd_primer, rev_primer, max_ot = float('inf')):
        self.sequence = sequence
        self.position = position  # leftmost coordinates, including the PAM if 5'
        self.strand = strand
        self.score = 100
        self.label = None
        self.oligo1 = ""  # leading GG, forward
        self.oligo2 = ""  # leading GG, reverse
        self.oligo_a_fwd = ""  # adding, forward
        self.oligo_a_rev = ""  # adding, reverse
        self.oligo_s_fwd = ""  # substituting, forward
        self.oligo_s_rev = ""  # substituting, reverse
        self.off_targets = []
        self.max_ot = max_ot

        # oligos
        if fwd_primer == "TAGG":  # T7
            if target_seq[0] == 'G' and target_seq[1] == 'G':
                self.oligo1 = 'TA' + target_seq
                self.oligo2 = 'AAAC' + reverse_complement(target_seq[2:])
            elif target_seq[0] == 'G' and not target_seq[1] == 'G':
                self.oligo_a_fwd = 'TAg' + target_seq
                self.oligo_a_rev = 'AAAC' + reverse_complement(self.oligo_a_fwd[4:])
                self.oligo_s_fwd = 'TAGg' + target_seq[2:]
                self.oligo_s_rev = 'AAAC' + reverse_complement(self.oligo_s_fwd[4:])
            else:
                self.oligo_a_fwd = 'TAgg' + target_seq
                self.oligo_a_rev = 'AAAC' + reverse_complement(self.oligo_a_fwd[4:])
                self.oligo_s_fwd = 'TAgg' + target_seq[2:]
                self.oligo_s_rev = 'AAAC' + reverse_complement(self.oligo_s_fwd[4:])
        elif fwd_primer == "CACCG":
            if target_seq[0] == 'G':
                self.oligo1 = 'CACC' + target_seq
                self.oligo2 = 'AAAC' + reverse_complement(target_seq)
            else:
                self.oligo_a_fwd = 'CACCg' + target_seq
                self.oligo_a_rev = 'AAAC' + reverse_complement('G' + self.oligo_a_fwd[5:])
                self.oligo_s_fwd = 'CACCg' + target_seq[1:]
                self.oligo_s_rev = 'AAAC' + reverse_complement('G' + self.oligo_s_fwd[5:])
        else:
            self.oligo1 = fwd_primer + target_seq
            self.oligo2 = rev_primer + reverse_complement(target_seq)

    def add_offtarget(self, offtarget, exons, genes):
        "Adds a new off-target to this site"
        if len(self.off_targets)>self.max_ot:
            return

        offtarget.set_gene_info(exons, genes)
        self.off_targets.append(offtarget)


class EditingSites:
    "A class as a container of editing sites"
    def __init__(self):
        self.sites = dict() # sites indexes by the label

    def add(self, target_seq, sequence, position, strand, fwd_primer, rev_primer, base_editor, max_ot = float('inf')):
        "Adds a new editing site to the container"
        new_site = EditingSite(target_seq, sequence, position, strand, fwd_primer, rev_primer, max_ot)
        # initial label
        new_site.label = "C" + str(len(self.sites)+1)
        new_site.score = base_editor.score_target(sequence)
        self.sites[new_site.label] = new_site

    def get_sites(self):
        "Returns the editing sites as a list"
        return list(self.sites.values())
    def get_sites_sorted(self):
        "Returns the editing sites sorted by label"
        # notice that to sort the keys we discard the leading character ('T')
        return [value for (key, value) in sorted(list(self.sites.items()),key= lambda item: int(item[0][1:]))]

    def get_site(self, label):
        "Returns the site identified by its label"
        return self.sites[label]

    def sort_offtargets(self):
        "Sorts the off-targets based on their score"
        for site in list(self.sites.values()):
            site.off_targets.sort(key=lambda offtarget: (offtarget.score,
                                                        (lambda dist: 0 if dist=="NA" else dist)(offtarget.distance)))

    def scale_score_and_relabel(self):
        "Sorts the sites by score and relabel them starting by 'T1'"
        new_dict = dict()
        sorted_sites_by_score = list(self.sites.values())
        sorted_sites_by_score.sort(key=lambda site: (site.score), reverse=True)

        for idx, site in enumerate(sorted_sites_by_score):
            new_label = 'T' + str(idx + 1)
            site.label = new_label
            new_dict[new_label] = site

        self.sites = new_dict
