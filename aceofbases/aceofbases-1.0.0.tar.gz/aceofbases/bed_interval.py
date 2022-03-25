'''
Created on Mar 20, 2014

@author: juan
'''

import gzip

from bx.intervals.intersection import IntervalTree


class MyInterval():
    def __init__(self,start,end,value=None):
        self.start = start
        self.end = end
        self.value = value

class BedInterval():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.chroms = {}

    def insert( self, chrom, start, end, gene_id=None, gene_name=None ):
        if chrom in self.chroms:
            if(gene_id is None or gene_name is None):
                self.chroms[chrom].insert( start, end, MyInterval(start,end) )
            else:
                self.chroms[chrom].insert( start, end, MyInterval(start,end,[gene_id, gene_name]) )
        else:
            self.chroms[chrom] = IntervalTree()
            if(gene_id is None or gene_name is None):
                self.chroms[chrom].insert( start, end, MyInterval(start,end) )
            else:
                self.chroms[chrom].insert( start, end, MyInterval(start,end,[gene_id, gene_name]) )

    def load_file(self, file):
        if file.endswith('.bed.gz'):
            bed_file = gzip.open(file,'rt')
        elif file.endswith('.bed'):
            bed_file = open(file,'r')
        else:
            raise Exception("Unsupported file type, only .bed or .bed.gz")
        for line in bed_file:
            line = line.rstrip('\n').split('\t')
            if len(line)==3:
                self.insert(line[0], int(line[1]), int(line[2]))
            else:
                self.insert(line[0], int(line[1]), int(line[2]), line[3], line[4])
        bed_file.close()

    def overlaps(self, chrom, start, end):
        if not chrom in self.chroms:
            return False
        overlapping = self.chroms[chrom].find(start, end)
        return len(overlapping)>0

    def closest(self,chrom, start, end):
        if not chrom in self.chroms:
            return ['NA', 'NA', 'NA']

        #first checking if this site overlaps any from the loaded file
        overlapping = self.chroms[chrom].find(start, end)
        if len(overlapping)>0:
            return [overlapping[0].value[0],overlapping[0].value[1],0]

        #to the left
        #it finds features with a start > than 'position'
        left = self.chroms[chrom].before(start, max_dist=1e5)

        #to the right
        #it finds features with a end < than 'position'
        right = self.chroms[chrom].after(end, max_dist=1e5)

        if len(left)>0:
            if len(right)>0:
                dist_left = max(0,1 + start - left[0].end)
                dist_right = max(0,1 + right[0].start - end)
                if dist_left < dist_right:
                    return [left[0].value[0],left[0].value[1],dist_left]
                return [right[0].value[0],right[0].value[1],dist_right]
            else:
                dist_left = max(0,1 + start - left[0].end)
                return [left[0].value[0],left[0].value[1],dist_left]
        else:
            if len(right)>0:
                dist_right = max(0,1 + right[0].start - end)
                return [right[0].value[0],right[0].value[1],dist_right]
            return ['NA', 'NA', 'NA']
