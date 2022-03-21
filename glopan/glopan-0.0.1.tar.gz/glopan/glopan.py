"""Collection of functions for Glowing Pancake"""
from pathlib import Path
import subprocess
import typing as t

import docx2pdf
import PyPDF3 as pypdf
import typer

from .config import current_config as config


def combine_pdfs(pdffiles: t.List[str], outfile: str):
    """Combine several PDF files to one.

    Args:
        pdffiles (list): The names of the PDF files to combine.
        outfile (str): The name of the PDF file to write.
    """
    pdf_merger = pypdf.PdfFileMerger()

    for this_pdf in pdffiles:
        pdf_merger.append(this_pdf)

    pdf_merger.write(outfile)
    pdf_merger.close()


def delete_files(files: t.List[str]):
    """Delete a list of files.

    Args:
        files (list): A list of files to delete.
    """
    for file in files:
        Path(file).unlink()


def docx_to_pdf(docxfile: str):
    """Convert a DOCX file to PDF.

    Args:
        docxfile (str): The name of the DOCX file to convert.
    """
    docx2pdf.convert(docxfile)


def many_ps_to_pdf(psfiles: t.List[str]):
    """Convert several Postscript files to PDF using glopan.ps_to_pdf.

    Args:
        psfiles (list): The Postscript files to convert.
    """
    for psfile in psfiles:
        ps_to_pdf(psfile)


def pdf_convert(pdffile: str, outformat: str, outdpi=600):
    """Convert a PDF page to a given format using Inkscape.

    Args:
        pdffile (str): The name of the PDF file to convert.
        outformat (str): The format to convert to.

    Kwargs:
        outdpi (int): The resolution of the outfile, if relevant, in DPI.
    """
    if not config.check_config('inkscape_path'):
        typer.echo('Please set the path to inkscape.exe in the configuration')
        raise typer.Exit()

    arguments = []
    arguments.append(config.config['inkscape_path'])
    arguments.append(f'--export-type={outformat}')
    if outformat.lower() == 'png':
        arguments.append(f'--export-dpi={outdpi}')
    arguments.append(pdffile)
    subprocess.run(arguments, check=False)


def pdf_to_emf(pdffile: str):
    """Convert a PDF file to EMF using glopan.pdf_convert."""
    pdf_convert(pdffile, outformat='emf')


def pdf_to_png(pdffile: str, outdpi=600):
    """Convert a PDF file to PNG using glopan.pdf_convert."""
    pdf_convert(pdffile, outformat='png', outdpi=outdpi)


def pdf_to_svg(pdffile: str):
    """Convert a PDF file to SVG using glopan.pdf_convert."""
    pdf_convert(pdffile, outformat='svg')


def ps_to_pdf(psfile: str):
    """Convert a Postscript file to PDF.

    Args:
        psfile (str): The name of the Postscript file.
    """
    if not config.check_config('ps2pdf_path'):
        typer.echo('Please set the path to ps2pdf.bat in the configuration')
        raise typer.Exit()
    filename = psfile[: psfile.index('.')]
    outfile = filename + '.pdf'
    arguments = [config.config['ps2pdf_path'], psfile, outfile]
    subprocess.run(arguments, check=False)


def split_pdf(pdffile: str):
    """Split a PDF file in one file per page.

    Args:
        pdffile (str): The name of the PDF file to split.
    """
    with open(pdffile, 'rb') as pdffile_handle:
        pdf_in = pypdf.PdfFileReader(pdffile_handle)
        num_pages = pdf_in.numPages
        pages = []
        if 'pdf' in pdffile.lower():
            file_first_name = pdffile.lower()[: pdffile.lower().index('.pdf')]

        for page in range(num_pages):
            pages.append(file_first_name + f'_p_{page}' + '.pdf')
            pdf_out = pypdf.PdfFileWriter()
            pdf_out.addPage(pdf_in.getPage(page))

            with open(pages[-1], 'wb') as stream:
                pdf_out.write(stream)

    return pages
