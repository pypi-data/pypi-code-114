import os
import re
import csv


def walk(dirPath, ext=""):
    flist = []
    for root, dirs, files in os.walk(dirPath):
        for fname in files:
            if (len(ext) > 0 and fname.endswith(ext)) or len(ext) == 0:
                fullpath = os.path.join(root, fname)
                flist.append(fullpath)
    flist.sort()
    return flist

def strip_tag(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

def get_patterns_from_terms(terms):
    patterns = []
    for term in terms:
        patterns.append(convert_term2pattern(term))
    return patterns

def convert_term2pattern(term):
    aterm = ""
    if term[0] == "*":
        if term[-1] == "*":
            aterm += term[1:-1]
        else:
            aterm += term[1:] + r'\b'
    else:
        if term[-1] == "*":
            aterm += r'\b' + term[:-1]
        else:
            aterm += r'\b' + term + r'\b'
    return aterm

def save_csv(out, data):
    with open(out, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def check_ext(out, ext):
    dext = ext
    if dext[0] != '.':
        dext = '.' + ext
    if not out.endswith(ext):
        out += ext 
    return out

def getpath(filename):
    return os.path.split(os.path.abspath(filename))