#!/usr/bin/python
# -*- coding: utf-8 -*-
from Bio import SeqIO
def fastaread(fastaname):
    records = list(SeqIO.parse(fastaname, "fasta"))
    return records