'''
Created on Jul 23, 2018

@author: Juan L. Mateo
'''

iupac_code = {'R':'[AG]', 'Y':'[CT]', 'S':'[GC]', 'W':'[AT]', 'K':'[GT]','M':'[AC]',
              'B':'[CGT]', 'D':'[AGT]', 'H':'[ACT]', 'V':'[ACG]', 'N':'[ACGT]'}
dna_codons = {
    # 'M' - START, '*' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "*", "TAG": "*", "TGA": "*"
}

def build_expression(seq):
    "Returns a regular expression to model a IUPAC sequence"
    result = ''
    for char in seq:
        if char in iupac_code:
            result = result + iupac_code[char]
        else:
            result = result + char

    return result


def reverse_complement(sequence):
    "Returns the reverse complement of the input sequence"
    rev_comp = []

    for idx in range(len(sequence) - 1, -1, -1):
        if sequence[idx] == 'A':
            rev_comp = rev_comp + ['T']
        elif sequence[idx] == 'C':
            rev_comp = rev_comp + ['G']
        elif sequence[idx] == 'G':
            rev_comp = rev_comp + ['C']
        elif sequence[idx] == 'T':
            rev_comp = rev_comp + ['A']
        else:
            rev_comp = rev_comp + ['N']
    return "".join(rev_comp)

def get_translations(seq):
    "Returns the 6 translation of the input sequence according to the standard code"
    translations = []
    for init in range(0,3):
        translations.append("".join([dna_codons[seq[pos:pos + 3]] for pos in range(init, len(seq) - 2, 3)]))
    seq = reverse_complement(seq)
    for init in range(0,3):
        translations.append("".join([dna_codons[seq[pos:pos + 3]] for pos in range(init, len(seq) - 2, 3)]))
    return translations

class EditingWindowTranslation:
    "A class that represents a translation of an editing window"
    def __init__(self, translation, window_start_aa, window_end_aa, window_start_nt, window_end_nt):
        self.translation = translation
        self.window_start_aa = window_start_aa
        self.window_end_aa = window_end_aa
        self.window_start_nt = window_start_nt
        self.window_end_nt = window_end_nt

class EditingWindowTranslations:
    "A class that represents the translations of an editing window"
    def __init__(self, translations, padding_sequences, base_editor):
        self.frames = []

        for frame in range(0,3):
            window_start_nt = len(padding_sequences[0])-frame
            window_end_nt = window_start_nt + (base_editor.window_end-base_editor.window_start)
            window_start_aa = window_start_nt//3
            window_end_aa = (window_end_nt-1)//3+1#len(translations[frame]) - len(padding_sequences[1])//3
            self.frames.append(EditingWindowTranslation(translations[frame],window_start_aa,window_end_aa,window_start_nt,window_end_nt))
        for frame in range(0,3):
            window_start_nt = len(padding_sequences[1])-frame
            window_end_nt = window_start_nt + (base_editor.window_end-base_editor.window_start)#len(translations[frame])*3 - len(padding_sequences[0])
            window_start_aa = window_start_nt//3
            window_end_aa = (window_end_nt-1)//3+1#len(translations[frame]) - len(padding_sequences[0])//3
            self.frames.append(EditingWindowTranslation(translations[frame+3],window_start_aa,window_end_aa, window_start_nt,window_end_nt))


class CDS:
    "A class that represents the CDS of a transcript"
    def __init__(self, chrom, start, end, strand, sequence):
        self.chrom = chrom
        self.strand = strand
        self.start = start
        self.end = end
        self.exons = []
        self.length = 0
        self.sequence = sequence
    def add_exon(self, start, end):
        "Adds a new exon to the CDS"
        self.exons.append(Exon(start, end))
        self.length = self.length + end-start + 1

class Exon:
    "A class tha represents an Exons"
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    def __hash__(self):
        return hash((self.start, self.end))



def get_window_coords_within_cds(candidate,cds, base_editor):
    '''
    Returns the coordinates of the editing window wrt. the CDS.
    This method assumes that the candidate editing window overlaps with a single exon.
    It returns coordinates valid to slice the cds sequence.
    '''
    exon_length = 0
    if candidate.strand=='+':
        pos = candidate.position + cds.start
        for exon in cds.exons:
            if (exon.start<=pos+base_editor.window_end and pos+base_editor.window_start<=exon.end):
                w_start = max(base_editor.get_window_start()+pos-exon.start, 0)
                w_end = min(base_editor.get_window_end()+pos-exon.start, exon.end-exon.start+1)
                return [w_start+exon_length,w_end+exon_length]
            exon_length = exon_length + exon.end - exon.start + 1
        return None
    # reverse
    pos = candidate.position + len(candidate.sequence) - 1 + cds.start
    for exon in cds.exons:
        if (exon.start<=pos-base_editor.window_start and pos-base_editor.window_end<=exon.end):
            w_start = max(pos-base_editor.get_window_end()-exon.start+1, 0)
            w_end = min(pos-base_editor.get_window_start()-exon.start+1, exon.end-exon.start+1)
            return [w_start+exon_length,w_end+exon_length]
        exon_length = exon_length + exon.end - exon.start + 1
    return None


def get_padding_sequences(cds,window_coords):
    "Returns the sequence of the editing window padded with flaking sequences form the CDS"
    pad = 9
    upstream = window_coords[0] - pad - window_coords[0]%3
    upstream = max(upstream,0)
    downstream = window_coords[1] + pad + (len(cds.sequence)-window_coords[1])%3
    downstream = min(downstream,len(cds.sequence))
    return [cds.sequence[upstream:window_coords[0]],cds.sequence[window_coords[1]:downstream]]

baseEditors = {'C':'T','A':'G'}

def get_window_translations(candidate, cds, base_editor):
    "Returns the 6 translations of the editing window"
    window_coords = get_window_coords_within_cds(candidate,cds,base_editor)
    padding_sequences = get_padding_sequences(cds, window_coords)

    window_seq = cds.sequence[window_coords[0]:window_coords[1]]
    if candidate.strand=='+':
        edited_seq = window_seq.replace(base_editor.base_to_edit,baseEditors[base_editor.base_to_edit])
    else:
        temp = reverse_complement(window_seq)
        edited_seq = temp.replace(base_editor.base_to_edit,baseEditors[base_editor.base_to_edit])
        edited_seq = reverse_complement(edited_seq)

    for_translation = padding_sequences[0] + window_seq + padding_sequences[1]
    for_translation_edited = padding_sequences[0] + edited_seq + padding_sequences[1]

    translations = [list(i) for i in get_translations(for_translation)]
    translations_edited = [list(i) for i in get_translations(for_translation_edited)]

    # Annotating the substitutions
    for frame,translation in enumerate(translations):
        for pos,residue in enumerate(translation):
            if residue != translations_edited[frame][pos]:
                translations[frame][pos] =  residue + ">" + translations_edited[frame][pos]

    return EditingWindowTranslations(translations, padding_sequences, base_editor)
