#!/usr/bin/python
# -*- coding: utf-8 -*-
import tempfile
import os
from Bio import AlignIO, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import re
import numpy as np
from scipy import stats
import codecs
from sweep import fas2sweep
import subprocess

def clustalo(input_file_name):
    fp = tempfile.TemporaryFile(mode='w',delete=False)
    subprocess.call("clustalo -i "+input_file_name+" -o "+fp.name+" --auto --outfmt clu --force", shell=True)
    align = AlignIO.read(fp.name, "clustal")
    fp.close()
    os.unlink(fp.name)
    return align
clustalOmega = clustalomega = clustal_omega = clustalo

def getCons(fasta):
    seq_list = list(fasta)
    fastaText = tempfile.TemporaryFile(mode='w',delete=False)
    for i in seq_list:
        fastaText.write('>'+str(i.description)+'\n'+str(i.seq)+'\n')
    fastaText.close()
    
    align = []
    if len(seq_list) > 1:
        align1 = clustalo(fastaText.name)
        align2 = []
        for i in align1:
            align2.append(list(i.seq))
            align.append(str(i.seq))
        align2 = np.array(align2)
        m = stats.mode(align2) # determine mode
        m = m[0][m[1]>=0] # filter characters by minimal occurrence
        consensus = re.sub('\-+','',''.join(m))
    else:
        consensus = str(seq_list[0].seq)
        align.append(consensus)
    
    os.unlink(fastaText.name)
    return consensus, align
getcons = get_cons = getconsensus = get_consensus = getConsensus = getCons
    
def getHeader(fasta):
    fasta = list(fasta)
    headers = []
    for i in fasta:
        header = i.description
        headers.append (header)
    return headers

def getSeq(fasta):
    fasta = list(fasta)
    seqs = []
    for i in fasta:
        seq = i.seq
        seqs.append (str(seq))
    return seqs
getseq = get_seq = getSeq

def list2bioSeqRecord(seq,header=None):
    if header == None:
        header = list(range(0,len(seq)))
    fasta = []
    for i in range(0,len(seq)):
        record = SeqRecord(Seq(seq[i]), description=str(header[i]), id=str(i))
        fasta.append(record)
    return fasta
list2SeqRecord = list2seqrecord = list2fasta = list2bioseqrecord = list2bioSeqRecord

def removePattern(fasta,rex):
    fasta = list(fasta)
    for i in range(0,len(fasta)):
        for ii in rex:
            s = re.sub(ii,'',str(fasta[i].seq)) # find and remove id
            fasta[i].seq=Seq(s)
    return fasta
removepattern = remove_pattern = removePattern
    
def fastaread(input_file_name):
    fasta = SeqIO.parse(codecs.open(input_file_name,'r','utf-8'), "fasta")
    return list(fasta)
fastaRead = fasta_read = fastaread
    
def fastawrite(fasta, output_file_name, header=None):
    fasta = list(fasta)
    
    if header != None: 
        fasta = list2fasta([str(i.seq) for i in fasta],header=header)
    
    outputFile = codecs.open(output_file_name,'w','utf-8')
    for i in fasta:
        if len(i.seq) > 0:
            outputFile.write('>'+i.description+'\n')
            seq = str(i.seq)
            seq = re.findall('[\w-]{0,'+str(100)+'}',seq)
            seq = '\n'.join(seq)
            outputFile.write(seq)
    outputFile.close()

fastaWrite = fasta_write = fastawrite

def fastatext2mat(fasta):
    fasta_aux=[]
    min_size=[]
    for i in fasta:
        if len(str(i.seq)) >= 5:
            fasta_aux.append(i)
            min_size.append(True)
        else:
            min_size.append(False)

    mat=np.zeros((len(fasta),600))
    mat_aux = fas2sweep(fasta_aux)
    mat[min_size] = mat_aux

    return mat
fastaText2mat = fasta2mat = fasta_text2mat = fastatext2mat = fastatext2mat
fastaText2vect = fasta2vect = fasta_text2vect = fastatext2vect = fastatext2mat