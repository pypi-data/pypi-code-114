from pathlib import Path
import subprocess

import pytest

import glopan

from . import create_files

CURRENT_DRIVE = Path(Path.home().drive)


@pytest.fixture(scope='session')
def ps2pdf_path():
    this_path = (
        Path(CURRENT_DRIVE)
        / '/'
        / 'Program Files'
        / 'gs'
        / 'gs9.26'
        / 'lib'
        / 'ps2pdf.bat'
    )
    return this_path


@pytest.fixture(scope='session')
def pdf2ps_path():
    this_path = (
        Path(CURRENT_DRIVE)
        / '/'
        / 'Program Files'
        / 'gs'
        / 'gs9.26'
        / 'lib'
        / 'pdf2ps.bat'
    )
    return this_path


@pytest.fixture(scope='session')
def inkscape_path():
    this_path = (
        Path(CURRENT_DRIVE)
        / '/'
        / 'Program Files'
        / 'inkscape'
        / 'bin'
        / 'inkscape.exe'
    )
    return this_path


@pytest.fixture(scope='session')
def file_dir(tmpdir_factory):
    return tmpdir_factory.mktemp('files')


@pytest.fixture(scope='session')
def docx_file(file_dir, title: str = 'document_to_convert.docx'):
    file_name = str(file_dir.join(title))
    create_files.create_test_docx(file_name)
    return file_name


@pytest.fixture(scope='session')
def pdf_file_single(file_dir, title: str = 'document_to_convert_single.pdf'):
    file_name = str(file_dir.join(title))
    create_files.create_test_pdf_single(file_name)
    return file_name


@pytest.fixture(scope='session')
def pdf_file_multi(file_dir, title: str = 'document_to_convert_multi.pdf'):
    file_name = str(file_dir.join(title))
    create_files.create_test_pdf_multi(file_name)
    return file_name


@pytest.fixture(scope='session')
def ps_file_single(
    file_dir, pdf2ps_path, title: str = 'ps_document_to_convert_single.ps'
):
    pdf_title = title.replace('.ps', '.pdf')
    pdf_file_name = str(file_dir.join(pdf_title))
    ps_file_name = str(file_dir.join(title))
    create_files.create_test_pdf_single(pdf_file_name)
    arguments = [
        pdf2ps_path,
        pdf_file_name,
        ps_file_name,
    ]
    subprocess.run(arguments, check=False)
    Path(pdf_file_name).unlink()
    return ps_file_name


@pytest.fixture(scope='session')
def ps_file_multi(
    file_dir, pdf2ps_path, title: str = 'ps_document_to_convert_multi.ps'
):
    pdf_title = title.replace('.ps', '.pdf')
    pdf_file_name = str(file_dir.join(pdf_title))
    ps_file_name = str(file_dir.join(title))
    create_files.create_test_pdf_multi(pdf_file_name)
    arguments = [
        pdf2ps_path,
        pdf_file_name,
        ps_file_name,
    ]
    subprocess.run(arguments, check=False)
    Path(pdf_file_name).unlink()
    return ps_file_name


@pytest.fixture(autouse=True)
def set_config(inkscape_path, ps2pdf_path):
    glopan.config.set('inkscape_path', str(inkscape_path))
    glopan.config.set('ps2pdf_path', str(ps2pdf_path))
