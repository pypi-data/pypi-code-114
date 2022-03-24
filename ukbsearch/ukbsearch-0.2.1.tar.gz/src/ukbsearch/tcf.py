from . import util
import math
import os
import tabix
import pandas as pd
import pyreadr
import time


class TABINDEX():

    def __init__(self, tabfile, log=""):
        self.tabfile = tabfile
        self.tcf = tabfile + '.tcf'
        self.tcf = "/Users/pcaso/work/ukbsearchdata/" + tabfile + '.tcf'
        self.tcfgz = "/Users/pcaso/work/ukbsearchdata/" + tabfile + '.tcf.gz'
        self.tcfgzidx = "/Users/pcaso/work/ukbsearchdata/" + tabfile + '.tcf.gz.idx'
        self.log = log
        self.colsize = 0
        self.rowsize = 0
        self.totalsize = 0
        self.blocksize = 100

    def cal_size(self):
        i = 0
        for line in util.gzopen(self.tabfile):
            line = util.decodeb(line)
            if i == 0:
                arr = line.split('\t')
                self.colsize = len(arr)
            i += 1
        self.rowsize = i
        self.totalsize = self.colsize * self.rowsize
        self.log.info(str(self.colsize-1) + " COLUMNS, " + str(self.rowsize-1) + " ROWS")
        self.blocksize = int(5000000 / self.rowsize)
        if self.blocksize < 100:
            self.blocksize = 100
        self.log.info("BLOCK SIZE:" + str(self.blocksize))

    def transpose(self):
        f = open(self.tcf, 'w')
        f.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')

        self.header = util.readhead(self.tabfile)
        total_round = math.ceil(len(self.header)/self.blocksize)

        pos = 0
        udiidxcont = ""
        processed_block = 0
        for i_round in range(total_round):

            i = 0
            mat = []
            for line in util.gzopen(self.tabfile):
                line = util.decodeb(line)
                arr = line.split('\t')
                arr[-1] = arr[-1].strip()
                spos = (i_round*self.blocksize)
                epos = ((i_round+1)*self.blocksize)
                if epos > len(self.header):
                    epos = len(self.header)
                mat.append(arr[spos:epos])
                i += 1
            total_line = i
            this_blocksize = len(mat[0])

            for j in range(this_blocksize):
                pos += 1
                line = '1' + '\t' + str(pos)
                line += '\t' + '.' # ID
                line += '\t' + 'A' # REF
                line += '\t' + 'C' # ALT
                line += '\t' + '' # QUAL
                line += '\t' + '' # FILTER
                line += '\t'  # INFO
                for i in range(total_line):
                    if i > 0:
                        line += ';'
                    line += mat[i][j]
                    if i == 0:
                        udiidxcont += mat[i][j]  + '\t' + str(pos) + '\n'
                f.write(line+'\n')
            
            processed_block += this_blocksize
            self.log.info('INDEXING.... ' + str(round(100.0*(processed_block*total_line)/self.totalsize,1)) + "%")

        f.close()
        util.fileSave(self.tcfgzidx, udiidxcont, 'w')


    def index(self):
        self.log.info('BGZIPING AND TABIX INDEXING.... ')
        cmd = "bgzip -f "+self.tcf+" && tabix -f -p vcf "+self.tcf+".gz"
        util.run_cmd(cmd)


class TCF():
    fid = ""
    tcfgz = ""
    tcfgzidx = ""
    path = ""
    udilist = ['eid']
    udiidx = {}
    tb = ""
    rst_df = None
    log = ""

    def __init__(self, fid, path, log=""):
        self.fid = fid
        self.path = path
        self.tcfgz = os.path.join(path, fid + '.tab.tcf.gz')
        self.tcfgzidx = os.path.join(path, fid + '.tab.tcf.gz.idx')
        self.tb = ""
        self.udilist = ['eid']
        self.udimap = {}
        self.rst_df = None
        self.log = log
    
    def add_udilist(self, udilist):
        self.udilist.extend(udilist)

    def load_tcf(self):
        flag = False
        if not util.is_exist(self.tcfgz):
            self.log.error("Cannot find " + self.tcfgz + " file in " + self.path )
            self.log.error("You have to make " + self.fid + ".tcf.gz file by indexing "+self.fid+".tab file.")
        elif not util.is_exist(self.tcfgz + '.tbi'):
            self.log.error("Cannot find " + self.tcfgz + ".tbi file in " + self.path )
            self.log.error("You have to index "+self.fid+".tab file again.")
        elif not util.is_exist(self.tcfgzidx):
            self.log.error("Cannot find " + self.tcfgzidx + " file for in " + self.path )
            self.log.error("You have to index "+self.fid+".tab file again.")
        else:
            self.tb = tabix.open(self.tcfgz)
            for line in open(self.tcfgzidx):
                arr = line.strip().split('\t')
                self.udimap[arr[0]] = arr[1] ## keep position only
            flag = True
        return flag

    def get_outfilename(self, out, ext, subtype = ""):
        outfile = out + '_' + self.fid + subtype + '.' + ext
        return outfile

    def convert_udi(self, udi):
        arr = udi.replace('f.','').split('.')
        if len(arr) > 1:
            cudi = arr[0] + '-' + '.'.join(arr[1:])
        else:
            cudi = arr[0]
        return cudi

    def set_result_dataframe(self):
        d = {}
        for udi in self.udilist:
            self.log.info("APPENDING " + udi + " data")
            rudi = util.convert_udi_to_rudi(udi)
            recs = self.tb.querys("1:" + self.udimap[rudi] +"-"+ self.udimap[rudi])
            for rec in recs:
                arr = rec[7].split(';')
                d[arr[0]] = arr[1:]
                # d[self.convert_udi(arr[0])] = arr[1:]
        self.rst_df = pd.DataFrame(data=d)

    def save_selected_udi_as_csvi(self, outfile):
        f = open(outfile, 'w')
        for udi in self.udilist:
            self.log.info("APPENDING " + udi + " data")
            rudi = util.convert_udi_to_rudi(udi)
            recs = self.tb.querys("1:" + self.udimap[rudi] +"-"+ self.udimap[rudi])
            for rec in recs:
                f.write(rec[7].replace(';', ',') + '\n')
        f.close()

    def save_selected_udi_as_csv(self, outfile):
        if self.rst_df is None:
            self.set_result_dataframe()
        self.rst_df.to_csv(outfile, index=False, quotechar="'")

    def save_selected_udi_as_rdata(self, outfile):
        if self.rst_df is None:
            self.set_result_dataframe()
        pyreadr.write_rdata(outfile, self.rst_df, df_name="data")


