
#GFF3 format definition
#https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md

import argparse
import gzip
import sys

class Gene:
    def __init__(self, chrom, start, end, strand, geneId, geneName=''):
        self.chrom = chrom
        self.strand = strand
        self.geneId = geneId
        self.geneName = geneName
        self.start = start
        self.end = end
        self.exons = set()
        
    def setGeneName(self, name):
        self.geneName = name
    def setGeneId(self, geneId):
        self.geneId = geneId
    def addExon(self, start, end):
        self.exons.add(Exon(start, end))
        
    def toGeneFile(self):
        return '%s\t%s\t%s\n' % (self.chrom, self.start - 1, self.end)
        
    def toExonFile(self):
        if len(self.exons) == 0:
            # transcript without exons
            return '%s\t%s\t%s\t%s\t%s\n' % (self.chrom, self.start - 1, self.end, self.geneId, self.geneName)
        string = ''
        for exon in list(self.exons):
            string = string + '%s\t%s\t%s\t%s\t%s\n' % (self.chrom, exon.start - 1, exon.end, self.geneId, self.geneName)
        return string
    
    def __eq__(self, other):
        return self.chrom == other.chrom and self.strand == other.strand and self.exons == other.exons
    
class Exon:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    def __hash__(self):
        return hash((self.start, self.end))
        
class Genes:
    def __init__(self):
        self.genes = dict()
        
    def add(self, gene_id, gene):
        return self.genes.setdefault(gene_id,gene)
        
    def getGeneContent(self):
        return [x for x in (gene.toGeneFile() for gene in list(self.genes.values()))]
    
    def getExonContent(self):
        allExons = ''
        for gene in list(self.genes.values()):
            allExons = allExons + gene.toExonFile()
        return allExons

def findTopParent(parent,parents, parentSoFar = None):
    if not parent in parents:
        return parentSoFar
    return findTopParent(parents[parent][0], parents, parents[parent])
def readGFF(gff):
    genes = Genes()
    parents = {}
    if (gff.readline().strip()!='##gff-version 3'):
        raise Exception("The input file is not in gff version 3 format")
    for line in gff:
        if (line.startswith('#')):
            continue
        line = line.strip()
        if (len(line) == 0):
            continue
        
        cols = line.split('\t')
        if (len(cols) != 9):
            continue
        
        seqname = cols[0]
        feature = cols[2]
        start = int(cols[3])
        end = int(cols[4])
        strand = cols[6]
        attributes = cols[8]
        f_id = None
        f_name = ''
        f_parent = None
        
        if feature != 'exon':
            idx1 = attributes.find('ID')
            if(idx1==-1):
                continue
            idx2 = attributes.find(';',idx1)
            if(idx2==-1): # if it is the last attribute, go until the end
                idx2 = len(attributes)
            f_id = attributes[idx1+3:idx2]
            idx1 = attributes.find('Parent')
            if(idx1!=-1):
                idx2 = attributes.find(';',idx1)
                if(idx2==-1): # if it is the last attribute, go until the end
                    idx2 = len(attributes)
                f_parent = attributes[idx1+7:idx2]
            idx1 = attributes.find('Name')
            if(idx1!=-1):
                idx2 = attributes.find(';',idx1)
                if(idx2==-1): # if it is the last attribute, go until the end
                    idx2 = len(attributes)
                f_name = attributes[idx1+5:idx2]
            
            parents.setdefault(f_id,[f_parent,seqname,start,end,strand,f_id,f_name])
            if feature == 'gene':
                genes.add(f_id,Gene(seqname,start,end,strand,f_id,f_name))
            continue
            
        if feature == 'exon':
            idx1 = attributes.find('Parent')
            idx2 = attributes.find(';',idx1)
            if(idx2==-1): # if it is the last attribute, go until the end
                idx2 = len(attributes)
            exon_parent = attributes[idx1+7:idx2]
            
            parent_info = findTopParent(exon_parent, parents)
            if parent_info is None:
                sys.stderr.write('Parent %s not found for exon\n' %exon_parent )
            else:
                try:
                    gene = genes.genes[parent_info[5]]
                except KeyError:
                    gene = genes.add(parent_info[5],Gene(parent_info[1],parent_info[2],parent_info[3],parent_info[4],parent_info[5],parent_info[6]))
                gene.addExon(start, end)
                    
            
    return(genes)

def create_files(input_filename, prefix, folder):
    if input_filename.endswith("gz"):
        with gzip.open(input_filename, 'rt') as gff:
            genes = readGFF(gff)
    else:
        with open(input_filename, 'rt') as gff:
            genes = readGFF(gff)
    
    with gzip.open(folder + prefix + '_genes.bed.gz','wt') as geneFile:
       	for line in genes.getGeneContent():
       		geneFile.write(line)
    with gzip.open(folder + prefix +'_exons.bed.gz','wt') as exonFile:
       	exonFile.write(genes.getExonContent())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the input gff file (gzipped)")
    parser.add_argument("prefix", help="the prefix used for the name of the output files")
    parser.add_argument('--folder', default = './',help='folder where to put the output files, default current folder')
    args = parser.parse_args()
    
    create_files(args.input, args.prefix, args.folder)
