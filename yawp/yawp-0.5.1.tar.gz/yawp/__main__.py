#!/usr/bin/python3

#----- imports -----

from .__init__ import __version__ as version, __doc__ as description
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from warnings import simplefilter
from shutil import copy2
from sys import argv, stdout, stderr
from time import localtime, sleep
from os.path import join as joinpath, split as splitpath, isfile
from .__init__ import longpath, shortpath, splitpath4, listfiles, getfile, lastfile, localfile
from .__init__ import listdirs, getdir, chdir2, newbackfile, oldbackfile
from .__init__ import hold, chars, upperin, lowerin, letterin, digitin, specialin, split, replace, change
from .__init__ import shrink, expand, findchar, rfindchar, chrs, ords, edit, plural, interpolx, interpoly
from .__init__ import inform, warning, error
from .__init__ import in2in, in2pt, pt2in, in2cm, cm2in, in2mm, mm2in, in2str, str2in, str2inxin, ratio
from .__init__ import retroenum, find, rfind, shell, get, term, tryfunc, dump, Setdict

#----- global data -----

class Container: pass
G = Container() # container for arguments and other global data

#----- constants -----

EMPT, CODE, TEXT, PICT, CONT, INDX, CHP1, CHP2, HEA1, HEA2 = range(10) # values for kind
KINDS = 'EMPT CODE TEXT PICT CONT INDX CHP1 CHP2 HEA1 HEA2'.split() # labels for kind
JLIN, KIND, JPAG, LPIC, LINE = range(5) # positions in buf.output[j]
PREF, TITL, jout = range(3) # positions in buf.contents[j]
FORMFEED = '\f' # page header, first character of first line
MACRON = '¯' # page header, second line, dashed
OVERLINE = '‾' # page header, second line, continuous # deprecated because misprinted by CUPS
QUOTES = "'" + '"' # single and double quotation marks
INDENT = 4 * ' ' # tab indentation
PAPERSIZE = { # names for -S
    'half letter':  '5.5x8.5in',
    'letter':       '8.5x11.0in',
    'legal':        '8.5x14.0in',
    'junior legal': '5.0x8.0in',
    'ledger':       '11.0x17.0in',
    'tabloid':      '11.0x17.0in',
    'a0':  '841x1189mm',
    'a1':  '594x841mm',
    'a2':  '420x594mm',
    'a3':  '297x420mm',
    'a4':  '210x297mm',
    'a5':  '148x210mm',
    'a6':  '105x148mm',
    'a7':  '74x105mm',
    'a8':  '52x74mm',
    'a9':  '37x52mm',
    'a10': '26x37mm',
    'b0':  '1000x1414mm',
    'b1':  '707x1000mm',
    'b1+': '720x1020mm',
    'b2':  '500x707mm',
    'b2+': '520x720mm',
    'b3':  '353x500mm',
    'b4':  '250x353mm',
    'b5':  '176x250mm',
    'b6':  '125x176mm',
    'b7':  '88x125mm',
    'b8':  '62x88mm',
    'b9':  '44x62mm',
    'b10': '31x44mm'}
# page margin correctors in mm = (portrait_xyxy, landscape_xyxy)
LXYXY = ([(10, 5), (16, 10), (24, 20), (35, 30), (43, 40), (52, 50), (62, 60), (72.5, 70), (83, 80), (92, 90)],
         [(16, 5), (20.5, 10), (29.5, 20), (39, 30), (48, 40), (57, 50), (66.5, 60), (75.5, 70), (84.5, 80), (94, 90)])
RXYXY = ([(11, 5), (15, 10), (25.5, 20), (34.5, 30), (44.5, 40), (54.5, 50), (64.5, 60), (72, 70), (81, 80), (91.5, 90)],
         [(17, 5), (22, 10), (30, 20), (40, 30), (49.5, 40), (58, 50), (68, 60), (77.5, 70), (86, 80), (96, 90)])
TXYXY = ([(7, 5), (11.5, 10), (21, 20), (30.5, 30), (39.5, 40), (49, 50), (59, 60), (68, 70), (77.5, 80), (87, 90)],
         [(6, 5), (11, 10), (20.5, 20), (30, 30), (39, 40), (48.5, 50), (57.5, 60), (67, 70), (76, 80), (85, 90)])
BXYXY = ([(19.5, 5), (24, 10), (34, 20), (43, 30), (52.5, 40), (62, 50), (71, 60), (81, 70), (90, 80), (100, 90)],
         [(19.999, 5), (24, 10), (32, 20), (42, 30), (52, 40), (60, 50), (70.5, 60), (80, 70), (88, 80), (99, 90)])
# char size correctors = (portrait_factor, landscape_factor)
CWF = (1.0528967254408061, 1.0823529411764705) # char width factor
CHF = (1.0588235294117647, 1.0738636363636365) # char height factor

#----- classes -----

class Paragraph:

    def __init__(par):
        par.string = ''
        par.indent = 0
        
    def append(par, string, indent=0):
        if par.string:
            par.string += ' ' + shrink(string)
        else:
            par.string = shrink(string)
            par.indent = indent

    def flush(par, jlin):
        if not par.string:
            return
        prefix = (par.indent - 2) * ' ' + '• ' if par.indent else ''
        while len(par.string) > G.chars_per_line - par.indent:
            jchar = rfind(par.string[:G.chars_per_line-par.indent+1], ' ')
            if jchar <= 0:
                error('Impossible to left-justify', jlin, string)
            string, par.string = par.string[:jchar], par.string[jchar+1:]
            if not G.left_only:
                try:
                    string = expand(string, G.chars_per_line - par.indent)
                except ValueError as error_message:
                    error('Impossible to right-justify', jlin, string)
            buf.append(jlin, TEXT, 0, 0, prefix + string)
            prefix = par.indent * ' '
        if  par.string:
            buf.append(jlin, TEXT, 0, 0, prefix + par.string)
            par.string = ''

par = Paragraph()

class Buffer:

    def __init__(buf):
        buf.input = [] # [[jlin, 0, 0, 0, line]] # input buffer
        buf.output = [] # [[jlin, kind, jpag, lpic, line]] # output buffer
        # jlin: line index in buf.input, for error message
        # kind: kind of line: CODE, TEXT, PICT, CONT, INDX, CHP1, CHP2, HEA1, HEA2
        # jpag: page number
        # lpic: lines in picture (in first line of pictures only, else 0)
        # line
        buf.contents = [] # [[pref, titl, jout]]
        # pref: chapter numbering, first word in chapter line as '1.', '1.1.'...
        # titl: rest of chapter line
        # jout: position of chapter line in buf.output
        buf.contents_start, buf.contents_stop = -1, -1 # start and stop of contents in output
        buf.index = Setdict() # {subject: {jout}}
        # subject: subject between double quotes in TEXT lines
        # jout: position of subject in buf.output
        buf.index_start, buf.index_stop = -1, -1 # start and stop of index in output

    def __len__(buf):
        return len(buf.output)

    def append(buf, jlin, kind, jpag, lpic, line):
        buf.output.append([jlin, kind, jpag, lpic, line])

    def char(buf, jout, jchar):
        'return buf.output[jout][LINE][jchar] for the sake of redraw_segments() and redraw_arroheads()'
        try:
            if jout < 0 or jchar < 0: return ' '
            line = buf.output[jout][LINE]
            return line[jchar] if buf.output[jout][KIND] == PICT else ' '
        except IndexError:
            return ' '

    def dump(buf):
        'for debug only'
        print(f'\n... BUFFER ...')
        print(f'... contents_start = {buf.contents_start}, contents_stop = {buf.contents_stop} ...')
        print(f'... index_start = {buf.index_start}, index_stop = {buf.index_stop} ...')
        for jout, (jlin, kind, jpag, lpic, line) in enumerate(buf.output):
            print(jout, ':', (jlin, KINDS[kind], jpag, line, lpic))
        print('\n... contents ...')
        for jout, rec in enumerate(buf.contents):
            print(jout, ':', rec)
        print('\n... index ...')
        for jout, rec in enumerate(sorted(buf.index.items())):
            print(jout, ':', rec)
        print()

buf = Buffer()

#----- functions -----

def level_title(line):
    'return (level, title) if line is a chapter-line else (0, line)'
    try:
        prefix, title = line.split(None, 1)
        numbers = prefix.split('.')
        assert len(numbers) >= 2
        assert all(int(number) >= 0 for number in numbers[:-1])
        assert not numbers[-1]
        return len(numbers) - 1, shrink(title)
    except:
        return 0, line

def check_gt0(number, argname):
    if number <= 0:
        error(f"Wrong {argname} {number}")

def check_ge0(number, argname):
    if number < 0:
        error(f"Wrong {argname} {number}")

def add_parameter(name, value):
    G.parameters.arg(name)
    G.__setattr__(name, value)

#----- actions -----

def get_arguments():
    parser = ArgumentParser(prog='yawp', formatter_class=RawDescriptionHelpFormatter, description=description)
    arg = parser.add_argument
    # general arguments
    arg('-H','--manual', action='store_true', help='open yawp Manual in PDF format and exit')
    arg('-V','--version', action='version', version=f'yawp {version}')
    arg('-v','--verbose', action='store_true', help='display information messages on stderr')
    arg('-U','--undo', action='store_true', help="restore the file from its previous version")
    arg('-N','--no-format', action='store_true', help="leave the file unchanged")
    arg('-p','--print-file', action='store_true', help="at end print file on stdout")
    # formatting arguments
    arg('-w','--chars-per-line', default='0', help="line width in chars per line (default: 0 = automatic)")
    arg('-l','--left-only', action='store_true', help="justify at left only (default: left and right)")
    arg('-g','--graphics', action='store_true', help="redraw '`'-segments and '^'-arrowheads")
    arg('-c','--contents-title', default='contents', help="title of contents chapter (default: 'contents')")
    arg('-i','--index-title', default='index', help="title of index chapter (default: 'index')")
    arg('-m','--max-subject', default='36', help="max index subject length (default: 36)")
    # paging arguments
    arg('-f','--formfeed', action='store_true', help="insert page headers on full page")
    arg('-F','--formfeed-chapters', action='store_true', help="insert page headers on full page and before contents index and level-one chapters")
    arg('-e','--even-left', default='%n/%N', help="even page headers, left (default: '%%n/%%N')")
    arg('-E','--even-right', default='%f.%e %Y-%m-%d %H:%M:%S', help="even page headers, right (default: '%%f.%%e %%Y-%%m-%%d %%H:%%M:%%S')")
    arg('-o','--odd-left', default='%c', help="odd page headers, left (default: '%%c')")
    arg('-O','--odd-right', default='%n/%N', help="odd page headers, right (default: '%%n/%%N')")
    arg('-a','--all-headers-E-e', action='store_true', help="all page headers contain -E at left and -e at right")
    # PDF exporting arguments
    arg('-P','--file-PDF', default='%P/%f.pdf', help="file name of exported PDF file (0 = no PDF export, default: '%%P/%%f.pdf')")
    arg('-W','--char-width', default='0', help="character width (pt/in/mm/cm, default: 0 = automatic)")
    arg('-A','--char-aspect', default='3/5', help="char aspect ratio = char width / char height (1 = square grid, default: 3/5')")
    arg('-S','--paper-size', default='A4', help="portrait paper size (width x height, pt/in/mm/cm, default: 'A4' = '210x297mm'")
    arg('-Z','--landscape', action='store_true', help="turn page by 90 degrees (default: portrait)")
    arg('-Q','--print-quality', default='2', help="print quality (0 1 or 2, default: 2')")
    arg('-L','--left-margin', default='2cm', help="left margin (pt/in/mm/cm, 2cm..8cm, default: 2cm)")
    arg('-R','--right-margin', default='-L', help="right margin (pt/in/mm/cm, 2cm..8cm, default: -L)")
    arg('-T','--top-margin', default='2cm', help="top margin (pt/in/mm/cm, 2cm..8cm, default: 2cm)")
    arg('-B','--bottom-margin', default='-T', help="bottom margin (pt/in/mm/cm, 2cm..8cm, default: -T)")
    # debugging arguments
    arg('-b','--dump-buffer', action='store_true', help='debug, dump content of internal buffer')
    arg('-s','--echo-shell', action='store_true', help='debug, display invoked Unix commands')
    arg('-k','--calibration', action='store_true', help="debug, don't adjust char size and page margins")
    # positional argument
    arg('file', nargs='?', help='text file to be processed')
    # arguments --> G.*
    parser.parse_args(argv[1:], G)
    
def check_arguments():
    G.start_time = localtime()[:]
    # -s
    G.shell_mode = G.echo_shell * 'co'
    # -H
    if G.manual:
        yawp_pdf = localfile('docs/yawp.pdf')
        shell(f'xdg-open {yawp_pdf}', G.shell_mode)
        exit()
    # file
    if not G.file:
        error("Mandatory positional argument 'file' not found")
    G.file = longpath(G.file)
    G.PpfeYmdHMS = splitpath4(G.file) + tuple(('%04d %02d %02d %02d %02d %02d' % G.start_time[:6]).split())
    # -U -N
    if G.undo and G.no_format:
        error("You can't set both -U and -N")
    # -w >= 0
    w = tryfunc(int, (G.chars_per_line,), -1)
    if w < 0:
        error(f'Wrong -w {G.chars_per_line}')
    G.chars_per_line = w
    # -c -i
    if not G.contents_title:
        error("Wrong -c ''")
    if not G.index_title:
        error("Wrong -i ''")
    G.contents_title = shrink(G.contents_title).upper()
    G.index_title = shrink(G.index_title).upper()
    if G.contents_title == G.index_title:
        error(f"Wrong -c = -i {G.contents_title}")
    # -m > 0
    m = tryfunc(int, (G.max_subject,), -1)
    if m <= 0:
        error(f'Wrong -w {G.max_subject}')
    G.max_subject = m
    # -f -F
    if G.file.endswith('.py'):
        if G.formfeed:
            inform("Python file, -f turned off")
            G.formfeed = False
        if G.formfeed_chapters:
            inform("Python file, -F turned off")
            G.formfeed_chapters = False
    G.formfeed = G.formfeed or G.formfeed_chapters
    # -e -E -o -O
    for char, argx in zip('eEoO', [G.even_left, G.even_right, G.odd_left, G.odd_right]):
        try:
            change(argx, 'PpfeYmdHMSnNc', 'PpfeYmdHMSnNc', '%')
        except ValueError as illegal:
            error(f'Wrong -{char} {argx!r}, illegal {str(illegal)!r}')
    # -P
    if tryfunc(float, (G.file_PDF,), -1) == 0.0:
        G.file_PDF = ''
    if G.file_PDF:
        try:
            G.file_PDF = change(G.file_PDF, 'PpfeYmdHMS', G.PpfeYmdHMS, '%')
        except ValueError as illegal:
            error(f'Wrong -P {shortpath(G.file_PDF)!r}, illegal {str(illegal)!r}')
        G.file_PDF = longpath(G.file_PDF)
        if not G.file_PDF.endswith('.pdf'):
            error(f"Wrong -P {shortpath(G.file_PDF)!r}, doesn't end with '.pdf'")
    # -Q in {0, 1, 2}
    Q = tryfunc(int, (G.print_quality,), -1)
    if Q not in {0, 1, 2}:
        error(f'Wrong -Q {G.print_quality}')
    G.print_quality = Q
    # -W >= 0
    W = tryfunc(str2in, (G.char_width,), -1.0)
    if W < 0.0:
        error(f'Wrong -W {G.char_width}')
    G.char_width = W
    # -A > 0
    A = tryfunc(ratio, (G.char_aspect,), -1.0)
    if A <= 0.0:
        error(f'Wrong -A {G.char_aspect}')
    G.char_aspect = A
    # -S 0 < Sw <= Sh
    Sw, Sh = tryfunc(str2inxin, (PAPERSIZE.get(G.paper_size.lower(), G.paper_size),), (-1.0, -1.0))
    if not 0 < Sw <= Sh:
        error(f'Wrong -S {G.paper_size}')
    G.paper_width, G.paper_height = (Sw, Sh)
    # -Z
    if G.landscape:
        G.paper_width, G.paper_height = G.paper_height, G.paper_width
    # -L
    min_inch, max_inch = (0.0, 1000.0) if G.calibration else (cm2in(1.999), cm2in(8.001))
    L = tryfunc(str2in, (G.left_margin,), -1.0)
    if not min_inch <= L <= max_inch:
        error(f'Wrong -L {G.left_margin}')
    G.left_margin = L    
    G.left_margin2 = G.left_margin if G.calibration else mm2in(interpoly(LXYXY[G.landscape], in2mm(G.left_margin)))
    # -R
    if G.right_margin == '-L':
        G.right_margin = G.left_margin
    else:
        R = tryfunc(str2in, (G.right_margin,), -1.0)
        if not min_inch <= R <= max_inch:
            error(f'Wrong -R {G.right_margin}')
        G.right_margin = R    
    G.right_margin2 = G.right_margin if G.calibration else mm2in(interpoly(RXYXY[G.landscape], in2mm(G.right_margin)))
    G.free_width = G.paper_width - G.left_margin - G.right_margin
    # -T
    T = tryfunc(str2in, (G.top_margin,), -1.0)
    if not min_inch <= T <= max_inch:
        error(f'Wrong -T {G.top_margin}')
    G.top_margin = T    
    G.top_margin2 = G.top_margin if G.calibration else mm2in(interpoly(TXYXY[G.landscape], in2mm(G.top_margin)))
    # -B
    if G.bottom_margin == '-T':
        G.bottom_margin = G.top_margin
    else:
        B = tryfunc(str2in, (G.bottom_margin,), -1.0)
        if not min_inch <= B <= max_inch:
            error(f'Wrong -B {G.bottom_margin}')
        G.bottom_margin = B    
    G.bottom_margin2 = G.bottom_margin if G.calibration else mm2in(interpoly(BXYXY[G.landscape], in2mm(G.bottom_margin)))
    G.free_height = G.paper_height - G.top_margin - G.bottom_margin
    
def restore_file():
    backfile = oldbackfile(G.file)
    if not backfile:
        error(f'Backup file for file {shortpath(G.file)!r} not found')
    shell(f'rm -f {G.file!r}', G.shell_mode)
    shell(f'mv {backfile!r} {G.file!r}', G.shell_mode)
    if G.verbose: inform(f'Restore: {shortpath(G.file)!r} <-- {shortpath(backfile)!r}')

def read_file(after_restore=False):
    if not isfile(G.file):
        error(f'File {shortpath(G.file)!r} not found')
    header_lines, body_lines, G.num_pages, max_body_width, max_header_width = 0, 0, 1, 0, 0
    for jlin, line in enumerate(open(G.file)):
        line = line.replace('\t', INDENT).rstrip()
        if line.startswith(FORMFEED):
            G.num_pages += 1
            max_header_width = max(max_header_width, len(line) - 1)
            header_lines += 1
        elif line.startswith(OVERLINE) or line.startswith(MACRON):
            max_header_width = max(max_header_width, len(line))
            header_lines += 1
        else:
            buf.input.append([jlin + 1, None, None, None, line])
            max_body_width = max(max_body_width, len(line))
            body_lines += 1
    if not after_restore and G.verbose: inform(f"Read: yawp <-- {shortpath(G.file)!r}")
    if G.verbose: inform(f"    {plural(header_lines, 'header line')}, max {plural(max_header_width, 'char')} per line, {plural(G.num_pages, 'page')}")
    if G.verbose: inform(f"    {plural(body_lines, 'body line')}, max {plural(max_body_width, 'char')} per line")
    max_total_width = max(max_header_width, max_body_width)
    if G.verbose: inform(f"    {plural(header_lines + body_lines, 'total line')}, max {plural(max_total_width, 'char')} per line")
    if not max_body_width:
        error(f'File {shortpath(G.file)!r}, no printable character found')
    if G.chars_per_line and not G.char_width: # -w > 0 and -W == 0
        G.char_width = G.free_width / G.chars_per_line # -W <-- -w
        if G.verbose: inform(f'Compute: -W {in2str(G.char_width)}')
        check_gt0(G.char_width, '-W')
    elif not G.chars_per_line and G.char_width: # -w == 0 and -W > 0
        G.chars_per_line = int(G.free_width / G.char_width) # -w <-- -W
        if G.verbose: inform(f'Compute: -w {G.chars_per_line}')
        check_gt0(G.chars_per_line, '-w')
    elif not G.chars_per_line and not G.char_width: # -w == 0 and -W == 0
        G.chars_per_line = max_body_width # -w <-- file
        if G.verbose: inform(f'Compute: -w {G.chars_per_line}')
        check_gt0(G.chars_per_line, '-w')
        G.char_width = G.free_width / G.chars_per_line # -W <-- -w
        if G.verbose: inform(f'Compute: -W {in2str(G.char_width)}')
        check_gt0(G.char_width, '-W')
    G.char_width_adj = G.char_width if G.calibration else G.char_width * CWF[G.landscape]
    G.chars_per_inch = 1.0 / G.char_width
    G.chars_per_margin2 = 1.0 / G.char_width_adj
    G.char_height = G.char_width / G.char_aspect
    G.char_height_adj = G.char_height if G.calibration else G.char_height * CHF[G.landscape]
    G.lines_per_inch = 1.0 / G.char_height
    G.lines_per_margin2 = 1.0 / G.char_height_adj
    G.lines_per_page = int(G.lines_per_inch * G.free_height) - 3
 
def justify_text():
    is_python_file = G.file.endswith('.py')
    format = not is_python_file 
    for jlin, x, x, x, line in buf.input: # input --> par --> buf.output
        is_switch_line = is_python_file and "\'\'\'" in line
        if is_switch_line:
            format = not format
        if is_switch_line or not format: # Python code
            par.flush(jlin)
            buf.append(jlin, CODE, 0, 0, line)
        elif not line: # empty-line
            par.flush(jlin)
            buf.append(jlin, EMPT, 0, 0, '')
        else:
            jdot = findchar(line, '[! ]')
            if jdot >= 0 and line[jdot:jdot+2] in ['• ','. ']: # dot-line
                par.flush(jlin)
                par.append(line[jdot+2:], indent=jdot+2)
            elif line[0] == ' ': # indented-line
                if par.string:
                    par.append(line)
                else:
                    if len(line) > G.chars_per_line:
                        error(f'Length of picture line is {len(line)} > -w {G.chars_per_line}', jlin, line)
                    buf.append(jlin, PICT, 0, 0, line)
            else: # unindented-line
                par.append(line)
    par.flush(jlin)
    if is_python_file and format:
        error('Python file, odd number of switch lines')

def delete_redundant_empty_lines():
    '''reduce multiple EMPT lines between TEXT line and TEXT line
    (or between TEXT line and EOF) to one EMPT line only'''
    jout, first, last, kind0 = 0, -1, -1, PICT
    while jout < len(buf.output):
        kind = buf.output[jout][KIND]
        if kind0 == TEXT == kind and 0 < first < last:
            del buf.output[first:last]
            jout -= last - first
        if kind == EMPT:
            if first < 0: first = jout
            last = jout
        else: # kind in [TEXT, PICT, CODE]
            kind0 = kind
            first, last, = -1, -1
        jout += 1
    if kind0 == TEXT and 0 < first < last:
        del buf.output[first:last]

def redraw_segments():
    chstr = '`─│┐│┘│┤──┌┬└┴├┼'
    #        0123456789ABCDEF
    chset = frozenset(chstr)
    for jout, (jlin, kind, jpag, lpic, line) in enumerate(buf.output):
        if kind == PICT:
            chars = list(line)
            for jchar, char in enumerate(chars):
                if char in chset:
                    chars[jchar] = chstr[1 * (buf.char(jout, jchar - 1) in chset) +
                                         2 * (buf.char(jout + 1, jchar) in chset) +
                                         4 * (buf.char(jout - 1, jchar) in chset) +
                                         8 * (buf.char(jout, jchar + 1) in chset)]
            buf.output[jout][LINE] = ''.join(chars)
    
def redraw_arrowheads():
    chstr = '^▷△^▽^^^◁^^^^^^^'
    #        0123456789ABCDEF
    chset = frozenset(chstr)
    for jout, (jlin, kind, jpag, lpic, line) in enumerate(buf.output):
        if kind == PICT:
            chars = list(line)
            for jchar, char in enumerate(chars):
                if char in chset:
                    chars[jchar] = chstr[1 * (buf.char(jout, jchar - 1) == '─') +
                                         2 * (buf.char(jout + 1, jchar) == '│') +
                                         4 * (buf.char(jout - 1, jchar) == '│') +
                                         8 * (buf.char(jout, jchar + 1) == '─')]
            buf.output[jout][LINE] = ''.join(chars)
            
def renumber_chapters():
    levels = []
    nout = len(buf.output)
    for jout, (jlin, kind, jpag, lpic, line) in enumerate(buf.output):
        prev_line = buf.output[jout-1][LINE] if jout > 0 else ''
        next_line = buf.output[jout+1][LINE] if jout + 1 < nout else ''
        if kind == TEXT and line and not prev_line and not next_line:
            level, title = level_title(line)
            if level > 0: # numbered chapter line
                if level > len(levels) + 1:
                    error(f'chapter-line level > {len(levels)+1}', jlin, line)
                elif level == len(levels) + 1:
                    levels.append(1)
                else:
                    levels = levels[:level]
                    levels[-1] += 1
                prefix = '.'.join(str(level) for level in levels) + '.'
                buf.output[jout][KIND] = CHP1 if level == 1 else CHP2
                buf.output[jout][LINE] = prefix + ' ' + shrink(title).upper()
            elif shrink(line).upper() == G.contents_title: # contents line
                buf.output[jout][KIND] = CONT
                buf.output[jout][LINE] = G.contents_title
            elif shrink(line).upper() == G.index_title: # index line
                buf.output[jout][KIND] = INDX
                buf.output[jout][LINE] = G.index_title

def fill_contents():
    for jout, (jlin, kind, jpag, lpic, line) in enumerate(buf.output):
        if kind == CONT:
            if buf.contents_start > -1:
                error('More than one contents line in file', jlin, line)
            buf.contents_start = jout
            if buf.index_stop == -1 < buf.index_start:
                buf.index_stop = jout
        elif kind == INDX:
            if buf.index_start > -1:
                error('More than one index line in file', jlin, line)
            buf.index_start = jout
            if buf.contents_stop == -1 < buf.contents_start:
                buf.contents_stop = jout
            buf.contents.append(['', G.index_title.title(), jout])
            # index is listed in contents, while contents doesn't
        elif kind in [CHP1, CHP2]:
            prefix, title = (line.split(None, 1) + [''])[:2]
            if buf.contents_stop == -1 < buf.contents_start:
                buf.contents_stop = jout
            if buf.index_stop == -1 < buf.index_start:
                buf.index_stop = jout
            buf.contents.append([prefix, title.title(), jout])
    if buf.contents_start > -1 == buf.contents_stop:
        buf.contents_stop = len(buf.output)
    elif buf.index_start > -1 == buf.index_stop:
        buf.index_stop = len(buf.output)

def fill_index():
    quote = False; subject = ''; in_contents_or_index = False
    for jout, (jlin, kind, jpag, lpic, line) in enumerate(buf.output):
        if kind in [CONT, INDX]:
            in_contents_or_index = True
        elif kind in [CHP1, CHP2]:
            in_contents_or_index = False
        if kind == TEXT and not in_contents_or_index:
            for jchar, char in enumerate(line + ' '):
                if quote:
                    if (char == '"' and
                        get(line, jchar-1, ' ') not in QUOTES and
                        get(line, jchar+1, ' ') not in QUOTES):
                        buf.index.add(shrink(subject), jout)
                        quote = False
                    else:
                        subject += char
                        if len(subject) > G.max_subject:
                            error(f'Length of subject "{subject}..." > -s {G.max_subject}')
                elif (char == '"' and
                      get(line, jchar-1, ' ') not in QUOTES and
                      get(line, jchar+1, ' ') not in QUOTES):
                    subject = ''
                    quote = True
        else:
            if quote:
                error('Unpaired \'"\' found while filling the index')
    if quote:
        error('Unpaired \'"\' found while filling the index')

def insert_contents():
    jlin = buf.output[buf.contents_start][JLIN]
    del buf.output[buf.contents_start + 1:buf.contents_stop] # delete old contents
    buf.output.insert(buf.contents_start + 1, [jlin, TEXT, 0, 0, '']) # insert new contents
    fmt_prefix = max((len(prefix) for prefix, titl, jpag in buf.contents), default=0)
    fmt_title = max((len(titl) for prefix, titl, jpag in buf.contents), default=0)
    for prefix, title, jpag in buf.contents[::-1]:
        buf.output.insert(buf.contents_start+1,
            [jlin, TEXT, 0, 0, f'{INDENT}• {edit(prefix, fmt_prefix)} {edit(title, fmt_title)}'])
    buf.output.insert(buf.contents_start+1, [jlin, TEXT, 0, 0, ''])

def insert_index():
    jlin = buf.output[buf.index_start][JLIN]
    del buf.output[buf.index_start + 1:buf.index_stop] # delete old index
    buf.output.insert(buf.index_start + 1, [jlin, TEXT, 0, 0, '']) # insert new index
    fmt_subject = max((len(subject) for subject in buf.index.keys()), default=0)
    for subject in sorted(buf.index.keys(), reverse=True):
        buf.output.insert(buf.index_start+1,
            [jlin, TEXT, 0, 0, f'{INDENT}• {edit(subject, fmt_subject)}'])
    buf.output.insert(buf.index_start+1, [jlin, TEXT, 0, 0, ''])

def insert_contents_and_index():
    if -1 < buf.contents_start < buf.index_start: 
        index_shift = (len(buf.contents) + 2) - (buf.contents_stop - buf.contents_start - 1)
        buf.index_start += index_shift
        buf.index_stop += index_shift
        insert_contents()
        insert_index()
    elif -1 < buf.index_start < buf.contents_start:
        contents_shift = (len(buf.index) + 2) - (buf.index_stop - buf.index_start - 1)
        buf.contents_start += contents_shift
        buf.contents_stop += contents_shift
        insert_index()
        insert_contents()
    elif -1 < buf.contents_start:
        insert_contents()
    elif -1 < buf.index_start:
        insert_index()

def count_picture_lines():
    jpic = 0
    for jout, (jlin, kind, jpag, lpic, line) in retroenum(buf.output):
        if kind == PICT:
            jpic += 1
            if jout == 0 or buf.output[jout-1][KIND] != PICT:
                buf.output[jout][LPIC] = jpic
        else:
            jpic = 0

def count_pages():
    jpag, jpagline = 1, 0
    for jout, (jlin, kind, zero, lpic, line) in enumerate(buf.output):
        if (jpagline + lpic * (lpic < G.lines_per_page) >= G.lines_per_page or
            G.formfeed_chapters and kind in [CONT, INDX, CHP1] and not
            (jout >= 2 and not buf.output[jout-1][LINE] and buf.output[jout-1][JPAG] > buf.output[jout-2][JPAG])):
            jpag += 1
            jpagline = 0
        else:
            jpagline += 1
        buf.output[jout][JPAG] = jpag
    G.tot_pages = jpag

def add_page_numbers_to_contents():
    if buf.contents_start > -1:
        fmt_jpag = len(str(buf.output[-1][JPAG])) + 1
        if buf.contents_start > -1:
            for jcontents, (prefix, titl, jout) in enumerate(buf.contents):
                buf.output[buf.contents_start + 2 + jcontents][LINE] += edit(buf.output[jout][JPAG], fmt_jpag)

def add_page_numbers_to_index():
    if buf.index_start > -1:
        for jindex, (subj, jouts) in enumerate(sorted(buf.index.items())):
            for strjpag in [(', ' if jjpag else ' ') + str(jpag) for jjpag, jpag in
                         enumerate(sorted(set(buf.output[jout][JPAG] for jout in jouts)))]:
                if len(buf.output[buf.index_start + 2 + jindex][LINE]) + len(strjpag) > G.chars_per_line:
                    break
                buf.output[buf.index_start + 2 + jindex][LINE] += strjpag
    
def insert_page_headers():
    jout = 0; jpag0 = 1; chapter = ''; npag = buf.output[-1][JPAG]
    header2 = G.chars_per_line * MACRON
    while jout < len(buf.output):
        jlin, kind, jpag, lpic, line = buf.output[jout]
        if kind in [CONT, INDX, CHP1]:
            chapter = line.title()
        if jpag > jpag0:
            left, right = ((G.even_right, G.even_left) if G.all_headers_E_e else
                           (G.odd_left, G.odd_right) if jpag % 2 else
                           (G.even_left, G.even_right))
            PpfeYmdHMSnNc = G.PpfeYmdHMS + (str(jpag), str(npag), chapter)
            left = change(left, 'PpfeYmdHMSnNc', PpfeYmdHMSnNc, '%')
            right = change(right, 'PpfeYmdHMSnNc', PpfeYmdHMSnNc, '%')
            blanks = ' ' * (G.chars_per_line - len(left) - len(right))
            if not blanks:
                header1 = f'{left} {right}' 
                error(f"Length of header {header1!r} is {len(header1)} > -w {G.chars_per_line}")
            header1 = f'{FORMFEED}{left}{blanks}{right}'
            buf.output.insert(jout, [0, HEA2, jpag, 0, header2])
            buf.output.insert(jout, [0, HEA1, jpag, 0, header1])
            jout += 2
            jpag0 = jpag
        elif jout >= 3 and not buf.output[jout-1][LINE] and buf.output[jout-3][LINE].startswith(FORMFEED):
            left, right = ((G.even_right, G.even_left) if G.all_headers_E_e else
                           (G.odd_left, G.odd_right) if jpag % 2 else
                           (G.even_left, G.even_right))
            PpfeYmdHMSnNc = G.PpfeYmdHMS + (str(jpag), str(npag), chapter)
            left = change(left, 'PpfeYmdHMSnNc', PpfeYmdHMSnNc, '%')
            right = change(right, 'PpfeYmdHMSnNc', PpfeYmdHMSnNc, '%')
            blanks = ' ' * (G.chars_per_line - len(left) - len(right))
            if not blanks:
                header1 = f'{left} {right}' 
                error(f"Length of header {header1!r} is {len(header1)} > -w {G.chars_per_line}")
            buf.output[jout-3][LINE] = f'{FORMFEED}{left}{blanks}{right}'
        jout += 1

def backup_file():
    backfile = newbackfile(G.file, G.start_time)
    shell(f'mv {G.file!r} {backfile}', G.shell_mode)
    if G.verbose: inform(f'Backup: {shortpath(G.file)!r} --> {shortpath(backfile)!r}')

def rewrite_file():
    header_lines, body_lines, G.num_pages, max_body_width, max_header_width = 0, 0, 1, 0, 0
    with open(G.file, 'w') as output:
        for jlin, kind, jpag, lpic, line in buf.output:
            print(line, file=output)
            if line.startswith(FORMFEED):
                G.num_pages += 1
                max_header_width = max(max_header_width, len(line) - 1)
                header_lines += 1
            elif line.startswith(OVERLINE) or line.startswith(MACRON):
                max_header_width = max(max_header_width, len(line))
                header_lines += 1
            else:
                max_body_width = max(max_body_width, len(line))
                body_lines += 1
    if G.verbose: inform(f"Rewrite: yawp --> {shortpath(G.file)!r}")
    if G.verbose: inform(f"    {plural(header_lines, 'header line')}, max {plural(max_header_width, 'char')} per line, {plural(G.num_pages, 'page')}")
    if G.verbose: inform(f"    {plural(body_lines, 'body line')}, max {plural(max_body_width, 'char')} per line")
    max_total_width = max(max_header_width, max_body_width)
    if G.verbose: inform(f"    {plural(header_lines + body_lines, 'total line')}, max {plural(max_total_width, 'char')} per line")

def print_file():
    if G.verbose: inform(f'Print: {shortpath(G.file)!r} --> stdout')
    if G.undo or G.no_format:
        for line in open(G.file):
            print(line.rstrip())
    else:
        for rec in buf.output:
            print(rec[LINE])

def export_file_PDF():
    shell(f'lp -d PDF '
          f'-o print-quality={G.print_quality+3} '
          f'-o media=Custom.{in2pt(G.paper_width)}x{in2pt(G.paper_height)} '
          f'-o cpi={G.chars_per_margin2} '
          f'-o lpi={G.lines_per_margin2} '
          f'-o page-top={in2pt(G.top_margin2)} '
          f'-o page-left={in2pt(G.left_margin2)} '
          f'-o page-right={0 if G.num_pages > 1 else in2pt(G.right_margin2)} '
          f'-o page-bottom={0 if G.num_pages > 1 else in2pt(G.bottom_margin2)} '
          f'{G.file!r}', G.shell_mode)
    file = splitpath(G.file)[-1]
    while shell(f'lpq -P PDF | grep {file}', G.shell_mode):
        sleep(0.1) # wait lp completion
    file_PDF = lastfile('~/PDF/*.pdf')
    if not file_PDF:
        error('Exported PDF file not found')
    shell(f'rm -f {G.file_PDF!r}', G.shell_mode)
    shell(f'mv {file_PDF!r} {G.file_PDF!r}', G.shell_mode)
    if G.verbose: inform(f'Exported: {shortpath(G.file)!r} --> {shortpath(G.file_PDF)!r}')

def open_file_PDF():
    shell(f'xdg-open {G.file_PDF}', G.shell_mode)

#-----main -----

def main():
    try:
        simplefilter('ignore')
        get_arguments()
        check_arguments()
        read_file()
        if G.undo:
            restore_file()
            read_file(after_restore=True)
        if not G.undo and not G.no_format:
            justify_text()
            delete_redundant_empty_lines()
            if G.graphics:
                redraw_segments()
                redraw_arrowheads()
            renumber_chapters()
            fill_contents()
            fill_index()
            insert_contents_and_index()
            if G.formfeed:
                count_picture_lines()
                count_pages()
                add_page_numbers_to_contents()
                add_page_numbers_to_index()
                insert_page_headers()
            backup_file()
            rewrite_file()
        if G.dump_buffer:
            buf.dump()
        if G.print_file:
            print_file()
        if G.file_PDF:
            export_file_PDF()
            open_file_PDF()
    except KeyboardInterrupt:
        print()

if __name__ == '__main__':
    main()

#----- end -----
