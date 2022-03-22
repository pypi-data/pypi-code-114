import os
import time
import re
import pyreadr
from . import util
from .data import DATA
from .block import BLOCK
from .conf import COLNAMES, COL_JUSTIFY
from rich.console import Console
from rich.table import Table
from rich.text import Text


class RDATA():
    fid = ""
    htmlfile = ""
    rdatafile = ""
    path = ""
    udilist = []
    df = {}

    def __init__(self, fid, htmlfile):
        self.fid = fid
        self.htmlfile = htmlfile
        self.path = util.getpath(self.htmlfile)[0]
        self.rdatafile = ""
        self.df = {}
        self.udilist = []
    
    def add_udilist(self, udilist):
        self.udilist.extend(udilist)

    def find_rdatafile(self):
        for fname in util.walk(self.path):
            if fname.endswith('.RData') or fname.endswith('.Rdata') or fname.endswith('.rdata'):
                if os.path.abspath(self.htmlfile)[:-5] in fname:
                    self.rdatafile = fname

    def load_rdata(self):
        if self.rdatafile == "":
            self.find_rdatafile()
        result = pyreadr.read_r(self.rdatafile, use_objects=["data"])
        self.df = result['data']

    def convert_rcolumn_list(self, column_list):
        rst = []
        for cname in column_list:
            rst.append('f.' + cname.replace('-', '.'))
        return rst

    def get_outfilename(self, out, ext):
        outfile = out + '_' + self.fid + '.' + ext
        return outfile

    def get_selected_r_udilist(self):
        selected_r_udilist = ["f.eid"]
        selected_r_udilist.extend(self.convert_rcolumn_list(self.udilist))
        return selected_r_udilist

    def save_selected_udi_as_csv(self, outfile):
        selected_r_udilist = self.get_selected_r_udilist()
        self.df.loc[:,selected_r_udilist].to_csv(outfile, index=False)

    def save_selected_udi_as_rdata(self, outfile):
        selected_r_udilist = self.get_selected_r_udilist()
        pyreadr.write_rdata(outfile, self.df.loc[:,selected_r_udilist], df_name="data")

class UKBSearch():
    opt = None
    runtime = {}
    out = ""
    rdatafilemap = {}

    def __init__(self, opt):
        self.opt = opt
        self.has_opt_error = False
        self.out = ""
        self.rdata_file_map = {}
        self.rdata_df_map = {}

    def run(self):
        self.opt['log'].info('COMMAND: ' + self.opt['cmd'])
        t0 = time.time()
        self.dispatch()
        t2 = time.time()

        self.opt['log'].info('Total running time: ' + str(round(t2-t0, 1))+' sec')
        self.opt['log'].info('END')


    def search(self):
        data = DATA()
        data.load_html_list(self.opt['path'])
        blocklist = data.search_description(self.opt['searchterm'], self.opt['logic'])
        if "console" in self.opt['outtype']:
            self.print_blocklist(blocklist, self.opt['searchterm'])
        if "udi" in self.opt['outtype']:
            self.print_udi(blocklist)
        if "csv" in self.opt['outtype']:
            self.save_csv_block(blocklist)
            self.opt['log'].info('SAVED SEARCH RESULT: ' + self.out)
        if len(self.opt['savedata']) > 0:
            self.save_data(blocklist)
    
    def save_data(self, blocklist):
        rdatamap = {}
        for block in blocklist:
            if not block.fid in rdatamap.keys(): 
                rdatamap[block.fid] = RDATA(block.fid, block.htmlfile)
            rdatamap[block.fid].add_udilist(block.get_listudi())
        self.save_data_with_radtamap(rdatamap)
        
    def save_data_with_radtamap(self, rdatamap):
        for fid in rdatamap.keys():
            rdata = rdatamap[fid]
            rdata.find_rdatafile()
            if rdata.rdatafile == "":
                self.opt['log'].error("Cannot find .RData file for " + rdata.fid + " in " + rdata.path )
            else:
                self.opt['log'].info("LOADING RDATA.. " + rdata.rdatafile + ". It takes a few minutes..")
                rdata.load_rdata()

                if "csv" in self.opt['savedata']:
                    outfile = rdata.get_outfilename(self.opt['out'], 'csv')
                    self.opt['log'].info("SAVING CSV.. " + outfile + "  It takes a few minutes..")
                    rdata.save_selected_udi_as_csv(outfile)

                if "rdata" in self.opt['savedata']:
                    outfile = rdata.get_outfilename(self.opt['out'], 'RData')
                    self.opt['log'].info("SAVING RDATA.. " + outfile + "  It takes a few minutes..")
                    rdata.save_selected_udi_as_rdata(outfile)

    def convert_userinput_udilist_to_rdatamap(self, userinput_udilist):
        data = DATA()
        data.load_html_list(self.opt['path'])
        rdatamap =  {}
        fid = ""
        for u1 in userinput_udilist:
            if u1[:3] == "ukb":
                fid = u1
                htmlfile = data.find_htmlfile_from_fid(fid)
                rdatamap[fid] = RDATA(fid, htmlfile)
            else:
                rdatamap[fid].add_udilist([u1])
        return rdatamap

    def count_udi_from_rdatamap(self, rdatamap):
        cnt = 0
        for fid in rdatamap.keys():
            cnt += len(rdatamap[fid].udilist)
        return cnt

    def save_data_with_userinput_udilist(self):
        rdatamap = self.convert_userinput_udilist_to_rdatamap(self.opt['udilist'])
        self.opt['log'].info("SELECTED " + str(self.count_udi_from_rdatamap(rdatamap)) + " UDI(s) FROM " + str(len(rdatamap.keys())) + " FILES.")
        self.save_data_with_radtamap(rdatamap)

    def dispatch(self):
        if len(self.opt['searchterm']) > 0:
            self.search()

        if len(self.opt['udilist']) > 0:
            self.save_data_with_userinput_udilist()

    def save_csv_block(self, blocklist):
        rst = []

        header = ["HTML"]
        header.extend(COLNAMES)
        header.append("File")
        rst.append(header)

        prev_3 = ""
        prev_4 = ""
        for block in blocklist:
            for row in block.get_listrows():
                if row[3] == "":
                    row[3] = prev_3
                    row[4] = prev_4
                else:
                    prev_3 = row[3]
                    prev_4 = row[4]
                rst.append([block.fid, row[0], row[1], row[2], row[3], row[4], block.htmlfile])

        self.out = util.check_ext(self.opt['out'], '.csv')
        util.save_csv(self.out, rst)

    def print_udi(self, blocklist):
        rst = []
        for block in blocklist:
            rst.append(block.fid)
            for row in block.get_listrows():
                rst.append(row[1])
        print()
        print (' '.join(rst))
        print()

    def print_blocklist(self, blocklist, terms=[]):
        console = Console()
        table = Table(show_header=True)
        table.add_column("HTML", justify="left")
        for k in range(len(COLNAMES)):
            table.add_column(COLNAMES[k], justify=COL_JUSTIFY[k])
        table.add_column("File", justify="left")

        patterns = util.get_patterns_from_terms(terms)
        pattern = r'|'.join(patterns)
        
        for block in blocklist:
            for row in block.get_listrows():
                if row[4] != "":
                    desc = Text()
                    arr_split = re.split(pattern, block.description, flags=re.IGNORECASE)
                    arr_findall = re.findall(pattern, block.description, flags=re.IGNORECASE)
                    for k in range(len(arr_split)):
                        desc.append(arr_split[k])
                        if k < len(arr_findall):
                            desc.append(arr_findall[k], style="bold magenta")
                    # desc.append(row[4])
                else:
                    desc = ""
                table.add_row(block.fid, row[0], row[1], row[2], row[3], desc, block.htmlfile)
        console.print(table)