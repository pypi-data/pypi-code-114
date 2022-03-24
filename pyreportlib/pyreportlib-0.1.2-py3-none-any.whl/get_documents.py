# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:06:22 2020

@author: MadsFredrikHeiervang
"""
from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number, Command, \
    Figure, Package, SubFigure
from pylatex.utils import bold, NoEscape
from pylatex.base_classes import CommandBase, Arguments
import os
import datetime

_fig_ext = u'.pdf'


class HyperrefCommand(CommandBase):
    _latex_name = 'hypersetup'
    packages = [Package('hyperref')]


def get_document(document_title='Report', author='Entail AS', fig_ext=u'.pdf',
                 header_logofilename='entail.pdf',
                 logo_image_option_header="width=250px", workflow_ID = 0):
    global _fig_ext
    _fig_ext = fig_ext

    geometry_options = {
        "head": "70pt",
        "margin": "1.5cm",
        "bottom": "1.5cm",
        "includeheadfoot": True
    }
    document_options = ['a4paper']
    doc = Document(geometry_options=geometry_options,
                   document_options=document_options)

    # packages
    doc.packages.append(Package('booktabs'))
    doc.packages.append(Package('chngcntr'))
    doc.packages.append(Package('longtable'))
    doc.packages.append(Package('titlepic'))
    doc.packages.append(Package('float'))
    doc.packages.append(Package('lscape'))
    doc.packages.append(Package('multirow'))


    # Force sections to start at new page
    doc.preamble.append(NoEscape(r'\AddToHook{cmd/section/before}{\cleardoublepage}'))

        # Add 4th section level
    doc.packages.append(Package('titlesec'))
    doc.packages.append(Command('setcounter', arguments='secnumdepth', extra_arguments='4'))
    doc.preamble.append(NoEscape(r'\setcounter{secnumdepth}{4}'))
    doc.preamble.append(NoEscape(r'\titleformat{\paragraph}'))
    doc.preamble.append(NoEscape(r'{\normalfont\normalsize\bfseries}{\theparagraph}{1em}{}'))
    doc.preamble.append(NoEscape(r'\titlespacing*{\paragraph}'))
    doc.preamble.append(NoEscape(r'{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}'))
    doc.preamble.append(NoEscape(r'\def\toclevel@paragraph{4}'))
    doc.preamble.append(NoEscape(r'\def\l@paragraph{\@dottedtocline{4}{7em}{4em}}'))
    doc.preamble.append(NoEscape(r'\setcounter{tocdepth}{4}'))

    # page style
    first_page = PageStyle("firstpage")

    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.25\textwidth"),
                                         pos='c')) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     header_logofilename).replace('\\', '/')
            logo_wrapper.append(StandAloneGraphic(image_options="width=80px",
                                                  filename=logo_file))

    # Add document title
    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(width=NoEscape(r"0.75\textwidth"),
                                          pos='c', align='r')) as title_wrapper:
            title_wrapper.append(LargeText(bold(document_title)))
            title_wrapper.append(LineBreak())
            title_wrapper.append(MediumText(bold(NoEscape(r'\today'))))

    # Add footer
    with first_page.create(Foot("C")) as center_footer:
        center_footer.append(simple_page_number())
    with first_page.create(Foot("R")) as right_footer:
        with right_footer.create(MiniPage(width=NoEscape(r"0.15\textwidth"),
                                          pos='r')) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'tailor.png').replace('\\', '/')
            logo_wrapper.append(StandAloneGraphic(image_options="width=50px",
                                                  filename=logo_file))

    doc.preamble.append(first_page)
    doc.change_document_style("firstpage")
    doc.preamble.append(Command('title', document_title))
    logo_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             header_logofilename).replace('\\', '/')
    doc.preamble.append(Command('titlepic', StandAloneGraphic(image_options=
                                                              logo_image_option_header,
                                                              filename=logo_file)))
    # doc.preamble.append(Command('author', author))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.preamble.append(
        Command('hypersetup', arguments='colorlinks, citecolor=black, filecolor=black, linkcolor=black, urlcolor=black',
                packages=[Package('hyperref')]))
    doc.preamble.append(NoEscape(r'\counterwithin{figure}{section}'))
    doc.append(NoEscape(r'\maketitle'))

    # Add disclaimer
    doc.append(NewPage())
    doc.append(NoEscape(r'\textbf{Disclaimer}'))
    doc.append(NoEscape(r'\newline'))
    doc.append(NoEscape(r'\vspace{0.2in}'))

    temptext = f'This is in automatically generated report. '
    if workflow_ID == 0:
        temptext += f'The report was generated '
    else:
        temptext += f'The results are extracted from Workflow ID {workflow_ID} '
    temptext += f'on the {datetime.datetime.now().strftime("%m/%d/%Y at %H:%M:%S")}. '
    temptext += f'Errors may occur and it is the user’s responsibility to interpret the reported data '
    temptext += f'with sound engineering judgement.'
    doc.append(temptext)

    doc.append(NewPage())
    doc.append(Command('tableofcontents'))
    doc.append(NewPage())

    return doc
