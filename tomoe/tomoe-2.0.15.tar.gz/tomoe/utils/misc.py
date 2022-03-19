import argparse
import os
from xhtml2pdf import pisa

def choose():
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument('--nhentai', action='store', type=int)
    my_parser.add_argument('--pururin', action='store', type=int)
    my_parser.add_argument('--simply', action='store', type=str)
    my_parser.add_argument('--hentaifox', action='store', type=int)
    my_parser.add_argument('--hentai2read', action='store', type=str)
    
    args = my_parser.parse_args()
    return args

def split_name(string):
    get_name = os.path.basename(string).split('.')[0]
    return get_name

def get_size(string):
    file = round(os.path.getsize(string) / 1024 / 1024, 2)
    return file

## create function get_size folder in MB
def get_size_folder(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return round(total_size / 1024 / 1024, 2)

def project():
    return '<p><b><h1><a href="https://pypi.org/project/tomoe/">Generated from tomoe: https://pypi.org/project/tomoe</a></b><h1>'
           
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # make the result is scrollable
    pisa_status.dest.seek(0)
    

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)