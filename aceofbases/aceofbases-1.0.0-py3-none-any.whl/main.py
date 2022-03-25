#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Created on 16 Jun 2015

@author: juanlmateo
'''

import sys
import re
from argparse import ArgumentTypeError, ArgumentParser, RawTextHelpFormatter, FileType
import textwrap
from subprocess import Popen, PIPE, DEVNULL
import os
import math

from bx.seq.twobit import TwoBitFile

from aceofbases.bed_interval import BedInterval
from aceofbases.generate_target_site_svg import get_svg
from aceofbases.sequence_methods import build_expression, reverse_complement, iupac_code
from aceofbases.sequence_methods import CDS, get_translations, get_window_translations
from aceofbases.editing_sites import EditingSites
from aceofbases.base_editor import factory
from aceofbases.off_target import OffTarget


OPTIMAL_WINDOW_BG = "rgba(153, 204, 255, 1)"
EXTENDED_WINDOW_BG = "rgba(153, 204, 255, 0.5)"


def run_bowtie(options, bowtie_path, index_path, input_params, output_params):
    '''
    Runs the bowtie command to find hits in the genome
    It expects a list of options parameters,
    the path to the bowtie binary,
    the path to the index incluiding the index name,
    a list with the input parameters
    and another list with the output parameters
    or None if the function should return the output from bowtie
    '''
    bowtie_output = []# list of lines

    cmd = [bowtie_path + 'bowtie'] + options + [index_path] + input_params
    if output_params is None:# the output from bowtie must be returned as a PIPE
        p = Popen(cmd, stdout=PIPE, stderr=DEVNULL, universal_newlines=True)
        if p.wait() == 0:
            bowtie_output = bowtie_output + p.stdout.readlines()
    else:
        cmd = cmd + output_params
        p = Popen(cmd, stderr=DEVNULL)
    if p.wait() != 0:
        sys.stderr.write("Error running Bowtie (" + str(p.wait()) + ")")
        sys.stderr.write(";".join(cmd))
        raise RuntimeError
    if output_params is None:
        return bowtie_output
    return None

def get_formatted_coords(coords):
    return coords[0] + ":" + str(coords[1]) + "-" + str(coords[2])

def get_wrapped_seq(seq, length):
    if len(seq) <= length:
        return seq
    ret_seq = ''
    for idx in range(int(math.ceil(len(seq) / float(length)))):
        ret_seq = ret_seq + seq[length * idx:length * idx + length] + "<br>"
    return ret_seq[:-4]

def show_u6_termination_warning(seq, fwd_primer):
    if(fwd_primer == 'CACCG' and seq.find('TTTT')!=-1):
        return '<span class="hover"><img class="moveimage" src="../../problem_icon.png" style="width: 11px; height: 11px">\
                    <div style="font-family:sans-serif;" class=tooltip>You selected to use the U6 promoter and this cantidate contains a possible termination signal for RNA Pol III.</div> </span>'
    return ''

def get_formatted_ot_position(distance, intragenic):
    if distance == 0:
        return "</td><td bgcolor='ff9999' align='middle'>E"
    if intragenic:
        return "</td><td bgcolor='ffff99' align='middle'>I"
    return "</td><td bgcolor='99ff99' align='middle'>-"

def get_plain_ot_position(distance, intragenic):
    if distance == 0:
        return "Exonic"
    if intragenic:
        return "Intronic"
    return "Intergenic"

def get_formatted_target_seq(candidate, base_editor):

    html = '%s<span style="background:' + EXTENDED_WINDOW_BG + '">%s</span>\
<span style="background:' + OPTIMAL_WINDOW_BG + '">%s</span>\
<span style="background:' + EXTENDED_WINDOW_BG + '">%s</span>\
%s</td>\
    <td>&nbsp;&nbsp;Window translation: <span name="candidateFrame"></span></td><td class="mono"><span name="candidateTranslation" id="%s"></span>'
    if base_editor.get_pam().is5prime:
        pam_length = len(base_editor.get_pam().pam_str)
        return html % (candidate.sequence[0:base_editor.get_window_start()+pam_length],
                   candidate.sequence[base_editor.get_window_start()+pam_length:base_editor.get_optimal_window_start()+pam_length],
                   candidate.sequence[base_editor.get_optimal_window_start()+pam_length:base_editor.get_optimal_window_end()+pam_length],
                   candidate.sequence[base_editor.get_optimal_window_end()+pam_length:base_editor.get_window_end()+pam_length],
                   candidate.sequence[base_editor.get_window_end()+pam_length:],
                       candidate.label)
    return html % (candidate.sequence[0:base_editor.get_window_start()],
                   candidate.sequence[base_editor.get_window_start():base_editor.get_optimal_window_start()],
                   candidate.sequence[base_editor.get_optimal_window_start():base_editor.get_optimal_window_end()],
                   candidate.sequence[base_editor.get_optimal_window_end():base_editor.get_window_end()],
                   candidate.sequence[base_editor.get_window_end():],
                   candidate.label)


def get_formatted_ot_seq(seq, core_length, mm, base_editor):
    pam_size = len(base_editor.get_pam().pam_str)
    if mm.startswith("PAM"):  # the PAM is 5'
        if core_length != "NA" and core_length > 0:
            tmp_seq = 'PAM[' + seq[pam_size:pam_size + core_length] + ']' + seq[pam_size + core_length:]
        else:
            tmp_seq = 'PAM' + seq[pam_size:]
        ret_seq = ''
        for idx in range(len(mm)):
            if mm[idx] == '-':
                ret_seq = ret_seq + '<span style="font-weight:bold;color:red">' + tmp_seq[idx] + '</span>'
            else:
                ret_seq = ret_seq + tmp_seq[idx]

        return ret_seq[3:]  # it will be displayed without the characters 'PAM'
    # the PAM is 3'
    if core_length != "NA" and core_length > 0:
        tmp_seq = seq[0:base_editor.get_target_size() - (core_length)] + '[' + seq[base_editor.get_target_size() - core_length:-pam_size] + ']' + "PAM"
    else:
        tmp_seq = seq[0:-pam_size] + "PAM"
    ret_seq = ''
    brackets_seen = 0
    for idx in range(len(mm)):
        if mm[idx] in "[]":
            brackets_seen += 1

        if idx==base_editor.get_window_start() + brackets_seen:
            ret_seq = ret_seq + '<span style="background:' + EXTENDED_WINDOW_BG + '">'
        if idx==base_editor.get_optimal_window_start() + brackets_seen:
            ret_seq = ret_seq + '</span><span style="background:' + OPTIMAL_WINDOW_BG + '">'
        if idx==base_editor.get_optimal_window_end() + brackets_seen:
            ret_seq = ret_seq + '</span><span style="background:' + EXTENDED_WINDOW_BG + '">'
        if idx==base_editor.get_window_end() + brackets_seen:
            ret_seq = ret_seq + '</span>'
        if mm[idx] == '-':
            ret_seq = ret_seq + '<span style="font-weight:bold;color:red">' + tmp_seq[idx] + '</span>'
        else:
            ret_seq = ret_seq + tmp_seq[idx]

    return ret_seq[:-3]  # it will be displayed without the characters 'PAM'

def is_within_exons(target_start,strand,target_seq, cds, base_editor):

    if strand=='+':
        pos = target_start + cds.start
        for exon in cds.exons:
            if (exon.start<=pos+base_editor.window_end and pos+base_editor.window_start<=exon.end):
                # now checking if there is editable base
                w_start = max(base_editor.get_window_start(), exon.start - pos - 1)
                w_end = min(base_editor.get_window_end(), exon.end-pos-1)
                return base_editor.get_base_to_edit() in target_seq[w_start:w_end]
        return False
    #reverse
    pos = target_start + len(base_editor.get_pam().pam_str) + len(target_seq)-1 + cds.start
    for exon in cds.exons:
        if (exon.start<=pos-base_editor.window_start and pos-base_editor.window_end<=exon.end):
            w_start = max(base_editor.get_window_start(), pos-exon.end+1)
            w_end = min(base_editor.get_window_end(), pos - exon.start+1)
            return base_editor.get_base_to_edit() in target_seq[w_start:w_end]

    return False

def add_candidate_targets(base_editor, five_prime, three_prime, genomic, cds, strand, candidates, fwd_primer, rev_primer, max_ot = float('inf')):
    reg_exp = build_expression(base_editor.get_pam().pam_str)
    five_prime_re = '^' + build_expression(five_prime)
    three_prime_re = build_expression(three_prime) + '$'
    if base_editor.get_pam().is5prime:
        indices = [m.start() for m in re.finditer('(?=' + reg_exp + ')', genomic, re.I)]
        for index in indices:
            if (index + base_editor.get_target_size() + len(base_editor.get_pam().pam_str)) > len(genomic):
                continue
            candidate_sequence = genomic[index + len(base_editor.get_pam().pam_str):index + len(base_editor.get_pam().pam_str) + base_editor.get_target_size()]
            pam_sequence = genomic[index:index + len(base_editor.get_pam().pam_str)]
            if (not re.search(five_prime_re, candidate_sequence) is None) and (not re.search(three_prime_re, candidate_sequence) is None):
                # we need to transform the index from the reversed sequence to the forward sequence
                if strand == '+':
                    candidates.add(candidate_sequence, pam_sequence + candidate_sequence, index, strand, fwd_primer, rev_primer, base_editor, max_ot)
                else:
                    candidates.add(candidate_sequence, pam_sequence + candidate_sequence, len(genomic) - (index + base_editor.get_target_size() + len(base_editor.get_pam().pam_str)), strand, fwd_primer, rev_primer, base_editor, max_ot)
    else:
        indices = [m.start() for m in re.finditer('(?=' + reg_exp + ')', genomic, re.I)]
        for index in indices:
            if (index - base_editor.get_target_size()) < 0:
                continue
            candidate_sequence = genomic[index - base_editor.get_target_size():index]
            pam_sequence = genomic[index:index + len(base_editor.get_pam().pam_str)]
            if (not re.search(five_prime_re, candidate_sequence) is None) and (not re.search(three_prime_re, candidate_sequence) is None):
                #if base_editor.get_base_to_edit() not in candidate_sequence[base_editor.get_window_start():base_editor.get_window_end()]:
                #    continue
                # we need to transform the index from the reversed sequence to the forward sequence
                if strand == '+':
                    # Checking if the candidate is within the exons defined in the cds
                    if is_within_exons(index - base_editor.get_target_size(), strand, candidate_sequence, cds, base_editor):
                        candidates.add(candidate_sequence, candidate_sequence + pam_sequence, index - base_editor.get_target_size(), strand, fwd_primer, rev_primer, base_editor, max_ot)
                else:
                    # Checking if the candidate is within the exons defined in the cds
                    if is_within_exons(len(genomic) - (index + len(base_editor.get_pam().pam_str)), strand, candidate_sequence, cds, base_editor):
                        candidates.add(candidate_sequence, candidate_sequence + pam_sequence, len(genomic) - (index + len(base_editor.get_pam().pam_str)), strand, fwd_primer, rev_primer, base_editor, max_ot)

def find_ot(candidates, base_editor, output_path, core_mismatches, core_range, total_mismatches, bowtie_path, index_path, exons, genes):
    seqs = base_editor.get_pam().get_sequences_for_bowtie(candidates.get_sites())
    with open(output_path + '/bowtie_input.fasta','w') as bowtie_input:
        bowtie_input.write(seqs)

    bowtie_options = base_editor.get_pam().get_bowtie_options(core_mismatches, core_range, total_mismatches)
    run_bowtie(bowtie_options, bowtie_path, index_path, ['-f', output_path + '/bowtie_input.fasta'], [output_path + '/bowtie_output'])

    # process output and add off-target info
    with open(output_path + '/bowtie_output', 'r') as bowtie_output:
        for line in bowtie_output:
            columns = line.split('\t')
            if base_editor.get_pam().is_bowtie_hit_consistent(columns):
                #                     forward?                        chromosome  strand      start            substitutions sequence  lengthSeq        lengthPAM                           core_range
                off_target = OffTarget(base_editor.get_pam().is5prime, columns[2], columns[1], int(columns[3]), columns[7], columns[4], len(columns[4]), len(base_editor.get_pam().pam_str), core_range)
                if base_editor.get_pam().is5prime:
                    pass
                else:
                    if base_editor.get_base_to_edit() not in off_target.sequence[base_editor.get_window_start():base_editor.get_window_end()]:
                        continue
                candidates.get_site(columns[0]).add_offtarget(off_target, exons, genes)
    # cleaning
    os.remove(output_path + '/bowtie_input.fasta')
    os.remove(output_path + '/bowtie_output')

def get_html_translations(candidates, cds, base_editor):
    translations = get_translations(cds.sequence)
    html = '<table>\
<tbody>\
<tr><td>Translation<br>Frame \
<select id="frame"\
    onchange="updateTranslation();">\
    <option value="F1">F1</option>\
    <option value="F2">F2</option>\
    <option value="F3">F3</option>\
    <option value="F-1">F-1</option>\
    <option value="F-2">F-2</option>\
    <option value="F-3">F-3</option>\
</select>\
</td>\
<td class="mono">\
<span id="translation">%s</span>\
</td>\
</tr></tbody>\
</table>\
<script>\
var translationsText = \'%s\';\
var translationsJson = JSON.parse(translationsText);\
function updateTranslation() {\
    var frame = document.getElementById("frame").value;\
    var x = document.getElementsByName("candidateFrame");\
    for (var i =0; i<x.length; i++){\
        x[i].innerHTML = frame;\
    }\
    var x = document.getElementsByName("candidateTranslation");\
    for (var i =0; i<x.length; i++){\
        var label = x[i].id;\
        x[i].innerHTML = translationsJson[label][frame];\
    }\
    var boxes = document.getElementsByClassName("non-synonymous");\
    for (var i =0; i<boxes.length; i++){\
        boxes[i].style.setProperty("display","none");\
    }\
    var boxes = document.getElementsByClassName("nss-" + frame);\
    for (var i =0; i<boxes.length; i++){\
    boxes[i].style.setProperty("display","inline");\
    }\
    if(frame=="F1") document.getElementById("translation").innerHTML="%s";\
    if(frame=="F2") document.getElementById("translation").innerHTML="%s";\
    if(frame=="F3") document.getElementById("translation").innerHTML="%s";\
    if(frame=="F-1") document.getElementById("translation").innerHTML="%s";\
    if(frame=="F-2") document.getElementById("translation").innerHTML="%s";\
    if(frame=="F-3") document.getElementById("translation").innerHTML="%s";\
}\
    window.onload = updateTranslation\
</script>'

    return html % (get_wrapped_seq(translations[0], 60),\
                   get_candidates_json_translations(candidates, cds, base_editor),\
                   get_wrapped_seq(translations[0], 60),get_wrapped_seq(translations[1], 60),get_wrapped_seq(translations[2], 60),\
                   get_wrapped_seq(translations[3], 60),get_wrapped_seq(translations[4], 60),get_wrapped_seq(translations[5], 60))

def get_formatted_translation(translation):
    html = '<table><tr>'
    for idx in range(len(translation.translation)):
        aa = translation.translation[idx]
        if ">" in aa:
            if "*" in aa:
                color = "black;color:white"
            else:
                color = "purple;color:white"
        else:
            color = "white"
            aa = '&nbsp;' + aa + '&nbsp;'

        if translation.window_start_aa <= idx < translation.window_end_aa:
            html =html + '<td style=\\\'background-color:' + OPTIMAL_WINDOW_BG +';padding: 3px\\\'><span style=\\\'background-color:' + color + '\\\'>' + aa + '</span></td>'
        else:
            html = html + '<td>' + aa + '</td>'
    return html + '</tr></table>'

def get_formatted_translations(translations):
    formatted_translations = []

    formatted_translations.append(get_formatted_translation(translations.frames[0]))
    formatted_translations.append(get_formatted_translation(translations.frames[1]))
    formatted_translations.append(get_formatted_translation(translations.frames[2]))
    formatted_translations.append(get_formatted_translation(translations.frames[3]))
    formatted_translations.append(get_formatted_translation(translations.frames[4]))
    formatted_translations.append(get_formatted_translation(translations.frames[5]))
    return formatted_translations

def get_candidates_json_translations(candidates, cds, base_editor):
    text = '{'
    for candidate in candidates:
        translations = get_window_translations(candidate, cds, base_editor)
        formatted_translations = get_formatted_translations(translations)
        text = text + '"%s":{"F1":"%s","F2":"%s","F3":"%s","F-1":"%s","F-2":"%s","F-3":"%s"},'\
            % (candidate.label, formatted_translations[0],formatted_translations[1],formatted_translations[2],\
             formatted_translations[3],formatted_translations[4],formatted_translations[5])
    text = text[:-1] + '}'
    return text


def get_cds_context(seq, blat_path, two_bit_file, output_path):
    '''
    This functions returns a CDS object with the coordinates of the query
    sequence in the target species, plus the genomic sequences. Both as a
    tuple
    '''
    output_filename = output_path + "output.psl"
    query_filename = output_path + "query.fa"
    with open(query_filename,"wt") as f:
        f.write(">query\n" + seq)
    options = ['-minIdentity=98', '-noHead']
    cmd = [blat_path + 'blat'] + [two_bit_file] + [query_filename] + options + [output_filename]
    p = Popen(cmd, stdout=DEVNULL,stderr=PIPE)
    p.communicate()

    if p.returncode != 0:
        msg = "Error running Blat (" + str(p.returncode) + ")"
        raise RuntimeError(msg)

    while not os.path.isfile(output_filename):
        pass
    with open(output_filename, "rt") as o:
        match = o.readlines()

    # cleaning
    os.remove(output_filename)
    os.remove(query_filename)

    if len(match)!=1: # if not a single match (possibly with many exons)
        cds = CDS("unknown",1,len(seq),"+",seq)
        cds.add_exon(1,len(seq))
        return (cds,seq)

    columns = match[0].split("\t")

    # blat returns coordinates in bed format, the object CDS needs gff
    cds = CDS(columns[13], 1, int(columns[0]), columns[8],seq)
    genomic_exon_start = columns[20].split(",")
    exon_length = columns[18].split(",")
    exon_start = 1
    if cds.strand == "+":
        for idx in range(len(exon_length)-1): # There is an extra comman in these fields
            cds.add_exon(exon_start,exon_start-1+int(exon_length[idx]))
            exon_start += int(exon_length[idx])
            # adding intron
            if idx < len(exon_length)-2:
                exon_start += int(genomic_exon_start[idx+1])-int(genomic_exon_start[idx])-int(exon_length[idx])
    else:
        for idx in reversed(range(len(exon_length)-1)): # There is an extra comman in these fields
            cds.add_exon(exon_start,exon_start-1+int(exon_length[idx]))
            exon_start += int(exon_length[idx])
            # adding intron
            if idx > 0:
                exon_start += int(genomic_exon_start[idx])-int(genomic_exon_start[idx-1])-int(exon_length[idx-1])

    with open(two_bit_file, "br") as f:
        two_bit_file = TwoBitFile(f)# ATTENTION: two_bit_file uses bed coordinates -> start-1
        genomic = two_bit_file[cds.chrom.encode("utf-8")][int(columns[15]):int(columns[16])]

    if cds.strand=="-":
        genomic = reverse_complement(genomic)

    return (cds,genomic)

def valid_dinucleotide_iupac(string):
    valid_chars = ['A', 'C', 'G', 'T', 'N'] + list(iupac_code.keys())
    string = string.upper()
    if string != ''.join(c for c in string if c in valid_chars) or len(string) != 2:
        msg = "%r is not a valid dinucleotide sequence" % string
        raise ArgumentTypeError(msg)
    return string

def valid_overhang(string):
    valid_chars = ['A', 'C', 'G', 'T', 'N']
    string = string.upper()
    if string != ''.join(c for c in string if c in valid_chars) or len(string) > 5:
        msg = "%r is not a valid overhang sequence (up to 5 nt)" % string
        raise ArgumentTypeError(msg)
    return string

def read_multi_fasta(input_file):
    '''
    This function parses the content of a file, as the input string, checking that it has a multifasta format
    and returns a list for each entry that is itself another list with the name and sequence.
    '''
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    file_content = []
    seq_line = ""
    state = 0 # to represent a finate-state machine
              # 0 -> intial state, waiting for a header
              # 1 -> header read, waiting for sequence line
              # 2 -> at least one sequence read, waiting for more or another header
    for line in input_file:
        line = line.strip()
        if len(line) == 0:
            continue
        if state == 0:
            if len(line) > 1 and line[0] == ">":  # header
                state = 1
                name = ''.join(c for c in line if c in valid_chars)
                file_content.append([name])
            else:
                raise Exception("The first line of the file should contain a valid header")
        elif state == 1:
            if re.fullmatch('[ACGTNacgtn]+', line) is not None: # seq
                seq_line = seq_line + line
                state = 2
            else:
                raise Exception("Expected a valid nucleotide sequence after \"%s\"" % file_content[-1][0])
        elif state == 2:
            if len(line) > 1 and line[0] == ">" and state==2:  # header
                file_content[-1].append(seq_line)
                seq_line = ""
                name = ''.join(c for c in line if c in valid_chars)
                file_content.append([name])
                state = 1
            elif re.fullmatch('[ACGTNacgtn]+', line) is not None: # seq
                seq_line = seq_line + line
                state = 2
            else:
                raise Exception("Invalid line \"%s\"" % line)
    #At the end the state must be 2
    if state==2:
        file_content[-1].append(seq_line)
    else:
        raise Exception("Unexpected end of the file")

    return file_content

def do_search(name, query, base_editor, total_mismatches, core_length, core_mismatches, five_prime, three_prime, fwd_primer, rev_primer, output_path, bowtie_path, index_path, two_bit, blat_path, exons_file, genes_file, max_ot):
    base_editor = factory(base_editor)

    if not base_editor.get_pam().core_allowed:
        core_length = "NA"
        core_mismatches = "NA"

    # exons and genes
    exons = BedInterval()
    genes = BedInterval()
    if exons_file is not None and genes_file is not None:
        exons.load_file(exons_file)
        genes.load_file(genes_file)

    (cds, genomic) = get_cds_context(query, blat_path, two_bit, output_path)

    candidates = EditingSites()

    add_candidate_targets(base_editor, five_prime, three_prime, genomic, cds, '+', candidates, fwd_primer, rev_primer, max_ot)
    add_candidate_targets(base_editor, five_prime, three_prime, reverse_complement(genomic), cds, '-', candidates, fwd_primer, rev_primer, max_ot)

    if len(candidates.sites) < 1:
        print("No target sites were found.")
        sys.exit(0)

    # finding off-target sites
    find_ot(candidates, base_editor, output_path, core_mismatches, core_length, total_mismatches, bowtie_path, index_path, exons, genes)

    candidates.sort_offtargets()
    candidates.scale_score_and_relabel()

    sorted_sites = candidates.get_sites_sorted()

    # reporting

    plot_svg = get_svg(cds, candidates, base_editor)

    output_html = open(output_path + 'result_' + name +'.html', 'w')

    output_html.write("<! DOCTYPE html>\n<h2>Detailed results</h2><br>\n")
    output_html.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n')
    
    output_html.write('<style type="text/css"> td.mono {font-family: "Courier New", Courier, monospace}\n')
    output_html.write('table.fancyTable, tr.fancyTable, td.fancyTable{border: 1px solid black;border-collapse: collapse;}\n')
    output_html.write('.moveimage {\
    position: relative;\
    top: 1px;\
}\
.tooltip {\
    font-size: 10px;\
    display: none;\
    position: absolute;\
    border: 1px solid #cccccc;\
    padding: 0px 5px;\
    background-color: #f2f2f2;\
    text-align: justify;\
    box-shadow: 5px 5px 8px #AAA;\
    width: 300px;\
    line-height: 10px;\
}\
.hover:hover .tooltip {\
    z-index: 10;\
    text-decoration: none;\
    display: block;\
    position: absolute;\
}</style></head>')
    output = open(output_path + name + '.xls', 'w')
    fasta_output = ""
    output_html.write("<tr><td>Input:</td><td class='mono'>" + get_wrapped_seq(query, 60) + "</td></tr> </table></td>\n")
    output.write("Input:\t" + query + "\n")
    output_html.write("<td> <table> <tr><td>Editor:</td><td class='mono'>" + base_editor.__class__.__name__ + "</td></tr>\n")
    output.write("Editor:\t" + base_editor.__class__.__name__ + "\n")
    output_html.write("<tr><td>Target site 5&#39; limitation:</td><td class='mono'>" + five_prime + "</td></tr>\n")
    output.write("Target site 5' limitation:\t" + five_prime + "\n")
    output_html.write("<tr><td>Target site 3&#39; limitation:</td><td class='mono'>" + three_prime + "</td></tr>\n")
    output.write("Target site 3' limitation:\t" + three_prime + "\n")
    output_html.write("<tr><td>Core length:</td><td>" + str(core_length) + "</td></tr>\n")
    output.write("Core length:\t" + str(core_length) + "\n")
    output_html.write("<tr><td>Core MM:</td><td>" + str(core_mismatches) + "</td></tr>\n")
    output.write("Core MM:\t" + str(core_mismatches) + "\n")
    output_html.write("<tr><td>Total MM:</td><td>" + str(total_mismatches) + "</td></tr>\n")
    output.write("Total MM:\t" + str(total_mismatches) + "\n")

    output.write("\n")
    output_html.write("</table> </td></tr></table>\n")

    output_html.write(get_html_translations(sorted_sites, cds, base_editor))
    output_html.write('<br>' + plot_svg + '<br>\n')

    # legend for the OT position
    output_html.write('Legend for off-target site positon: <span style="background-color:#ff9999">E = exonic</span>; <span style="background-color:#ffff99">I = intronic</span>; <span style="background-color:#99ff99">- = intergenic</span>\n')

    # now the off-targets table
    for idx in range(0, len(sorted_sites)):
        fasta_output = fasta_output + '>' + sorted_sites[idx].label + '\n'
        fasta_output = fasta_output + sorted_sites[idx].sequence + '\n'

        output_html.write('<table><tr><td id="' + sorted_sites[idx].label + '" style="font-weight:bold;font-size:20px">' + sorted_sites[idx].label + '</td><td>out of ' + str(len(sorted_sites)) + '</td></tr></table>\n')

        if idx > 0:
            output_html.write('<a href="#' + sorted_sites[idx - 1].label + '">&lt;Previous</a>\n')
        else:
            output_html.write('&lt;Previous\n')
        if idx < len(sorted_sites) - 1:
            output_html.write('<a href="#' + sorted_sites[idx + 1].label + '">Next&gt;</a>\n')
        else:
            output_html.write('Next&gt;\n')
        output_html.write('<br>')
        output_html.write('<table><tr>')
        output_html.write('<td>Sequence:</td><td class="mono">' + show_u6_termination_warning(sorted_sites[idx].sequence,fwd_primer) + get_formatted_target_seq(sorted_sites[idx], base_editor) + '</td></tr>\n')

        output_html.write('</table><table>')

        output.write(sorted_sites[idx].label + '\t' + sorted_sites[idx].sequence + '\t' + str(int(sorted_sites[idx].score)) + '\n')

        if sorted_sites[idx].oligo1 != '':
            output_html.write('<tr><td>Oligo pair</td><td>fwd:</td><td class="mono">' + str(sorted_sites[idx].oligo1) + '</td>\n')
            output_html.write('<td>rev:</td><td class="mono">' + str(sorted_sites[idx].oligo2) + '</td></tr></table>\n')

            output.write('Oligo fwd\t' + str(sorted_sites[idx].oligo1) + '\n')
            output.write('Oligo rev\t' + str(sorted_sites[idx].oligo2) + '\n')
        else:
            output_html.write('<tr><td>Oligo pair with 5&#39; extension</td><td>fwd:</td><td class="mono">' + str(sorted_sites[idx].oligo_a_fwd) + '</td>\n')
            output_html.write('<td>rev:</td><td class="mono">' + str(sorted_sites[idx].oligo_a_rev) + '</td></tr>\n')
            if sorted_sites[idx].oligo_s_fwd != "" and sorted_sites[idx].oligo_s_rev != "":
                output_html.write('<tr><td>Oligo pair with 5&#39; substitution</td><td>fwd:</td><td class="mono">' + str(sorted_sites[idx].oligo_s_fwd) + '</td>\n')
                output_html.write('<td>rev:</td><td class="mono">' + str(sorted_sites[idx].oligo_s_rev) + '</td></tr>')
            output_html.write('</table>\n')

            output.write('Oligo adding fwd\t' + str(sorted_sites[idx].oligo_a_fwd) + '\n')
            output.write('Oligo adding rev\t' + str(sorted_sites[idx].oligo_a_rev) + '\n')
            if sorted_sites[idx].oligo_s_fwd != "" and sorted_sites[idx].oligo_s_rev != "":
                output.write('Oligo substituting fwd\t' + str(sorted_sites[idx].oligo_s_fwd) + '\n')
                output.write('Oligo substituting rev\t' + str(sorted_sites[idx].oligo_s_rev) + '\n')
        if len(sorted_sites[idx].off_targets) > 20:
            output_html.write("<div>Top 20 offtarget sites out of " + str(len(sorted_sites[idx].off_targets) + 1) + " (including on target; for full list see xls file)</div>")
        if base_editor.get_pam().is5prime:
            output_html.write("<table class='fancyTable' border=1 width='1000px'><tr><th>Coordinates</th><th>strand</th><th>MM</th><th>PAM</th><th>target_seq</th><th colspan='2'>distance</th><th>gene name</th><th>gene id</th></tr>\n")
            output.write('Chromosome\tstart\tend\tstrand\tMM\tPAM\ttarget_seq\talignment\tdistance\tposition\tgene name\tgene id\n')
        else:
            output_html.write("<table class='fancyTable' border=1 width='1000px'><tr><th>Coordinates</th><th>strand</th><th>MM</th><th>target_seq</th><th>PAM</th><th colspan='2'>distance</th><th>gene name</th><th>gene id</th></tr>\n")
            output.write('Chromosome\tstart\tend\tstrand\tMM\ttarget_seq\tPAM\talignment\tdistance\tposition\tgene name\tgene id\n')
        for idx2 in range(0, len(sorted_sites[idx].off_targets)):
            # in html output only top 20 offtarget sites
            off_target = sorted_sites[idx].off_targets[idx2]
            if idx2 < 20:
                output_html.write("<tr><td>" + get_formatted_coords(off_target.get_genomic_coordinates()))

                output_html.write("</td><td align='middle'>" + off_target.strand + "</td><td align='middle'>" + str(off_target.mismatches))
                if base_editor.get_pam().is5prime:
                    output_html.write("</td><td class='mono'>" + off_target.sequence[:len(base_editor.get_pam().pam_str)] + "</td><td class='mono'>" + get_formatted_ot_seq(off_target.sequence, core_length, off_target.alignment, base_editor))
                else:  # is the off-target site PAM is NAG the background of the cell is grey
                    output_html.write("</td><td class='mono'>" + get_formatted_ot_seq(off_target.sequence, core_length, off_target.alignment, base_editor) + "</td><td class='mono'>" + off_target.sequence[-len(base_editor.get_pam().pam_str):])
                output_html.write("</td><td>" + str(off_target.distance) + get_formatted_ot_position(off_target.distance, off_target.intragenic))
                output_html.write("</td><td>" + off_target.gene_name + "</td><td>")
                output_html.write(off_target.gene_id + "</td></tr>\n")

            output.write("\t".join(off_target.get_genomic_coordinates()))
            output.write("\t" + off_target.strand)
            output.write("\t" + str(off_target.mismatches))
            if base_editor.get_pam().is5prime:
                output.write("\t" + off_target.sequence[:len(base_editor.get_pam().pam_str)] + "\t" + off_target.sequence[len(base_editor.get_pam().pam_str):])
            else:
                output.write("\t" + off_target.sequence[:-len(base_editor.get_pam().pam_str)] + "\t" + off_target.sequence[-len(base_editor.get_pam().pam_str):])
            output.write("\t" + off_target.alignment + "\t" + str(off_target.distance) + "\t" + get_plain_ot_position(off_target.distance, off_target.intragenic))
            output.write("\t" + off_target.gene_name + "\t" + off_target.gene_id + "\n")
        output_html.write("</table>\n")
        output.write("\n")

    output_html.write("".join("<br>"*15) + "\n")
    output_html.close()
    output.close()
    fasta = open(output_path + name + '.fasta', 'w')
    fasta.write(fasta_output)
    fasta.close()

def main():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="ACEofBASEs is a careful evaluation of BaseEdits.", epilog=textwrap.dedent('''\
        If you use this tool please cite it as:
        
        
        Have fun using ACEofBASEs!
        '''))
    parser.add_argument("--input", metavar="<file>", type=FileType('r'), help="Fasta file containing the sequence(s) to be scanned for sgRNA candidates.", required=True)
    parser.add_argument("--index", metavar="<file>" , help="Path to the bowtie index files including the name of the index.", required=True)
    parser.add_argument("--bowtie", metavar="<folder>", help="Path to the folder where the executable bowtie is.", default="")
    parser.add_argument("--twobit", metavar="<file>", help="Path to the twoBit file containing the genome sequence of the target species.", required=True)
    parser.add_argument("--blat", metavar="<folder>", help="Path to the folder where the executable blat is.", default="")
    parser.add_argument("--editor", help="Base editor. (default: %(default)s)", default="BE4-Gam", choices=['BE4-Gam', 'ancBE4max', 'evoBE4max', 'ABE8e'])
    parser.add_argument("--five_prime", metavar="<sequence>", type=valid_dinucleotide_iupac, help="Filter candidates target sites with the most 5 prime nucleotides defined by this sequence. IUPAC code allowed. (default: %(default)s)", default="NN")
    parser.add_argument("--three_prime", metavar="<sequence>", type=valid_dinucleotide_iupac, help="Filter candidates target sites with the most 5 prime nucleotides defined by this sequence. IUPAC code allowed. (default: %(default)s)", default="NN")
    parser.add_argument("--fwdOverhang", metavar="<sequence>", type=valid_overhang, help="Sequence of the 5 prime forward cloning oligo. (default: %(default)s)", default="TAGG")
    parser.add_argument("--revOverhang", metavar="<sequence>", type=valid_overhang, help="Sequence of the 5 prime reverse cloning oligo. (default: %(default)s)", default="AAAC")
    parser.add_argument("--totalMM", metavar="<int>", help="Number of total maximum mismatches allowed in the off-target sites. (default: %(default)s)", default=4, type=int)
    parser.add_argument("--core_length", metavar="<int>", help="Number of bases that enclose the core of the target site. (default: %(default)s)", default=12, type=int)
    parser.add_argument("--coreMM", metavar="<int>", help="Number of maximum mismatches allowed in the core of the off-target sites. (default: %(default)s)", default=2, type=int)
    parser.add_argument("--maxOT", metavar="<int>", help="Maximum number of off-target sites to be reported. (default: %(default)s)", default=float("inf"), type=int)
    parser.add_argument("--output", metavar="<folder>", help="Output folder. (default: %(default)s)", default="." + os.path.sep)
    parser.add_argument("--exons_file", metavar="<file>", help="Path to the pseudo-bed file containing the coordinate of exons in the target genome. (default: NotUsed)", default=None)
    parser.add_argument("--genes_file", metavar="<file>", help="Path to the pseudo-bed file containing the coordinate of genes in the target genome. (default: NotUsed)", default=None)
    args = parser.parse_args()

    with args.input:
        file_content = read_multi_fasta(args.input)

    for sequence in file_content:
        sys.stdout.write("Working on sequence '%s'\n" % sequence[0])
        do_search(sequence[0], sequence[1].upper(), args.editor, args.totalMM, args.core_length, args.coreMM, args.five_prime, args.three_prime, args.fwdOverhang, args.revOverhang, args.output, args.bowtie, args.index, args.twobit, args.blat, args.exons_file, args.genes_file, args.maxOT)

