import io
import os
import contextlib
from pathlib import Path

import typer

import glopan
import glopan.cli as cli


def test_convert(pdf_file_single):
    new_file = pdf_file_single.replace('.pdf', '.emf')
    cli.convert(pdf_file_single, from_format=None, to_format='emf')
    assert Path(new_file).exists()
    Path(new_file).unlink()
    cli.convert(pdf_file_single, from_format='pdf', to_format='emf')
    assert Path(new_file).exists()
    Path(new_file).unlink()


def test_convert_no_filename():
    try:
        cli.convert(None, None, 'emf')
    except typer.Exit:
        assert True
    else:
        assert False


def test_convert_invalid_formats():
    try:
        cli.convert(None, 'invalid_format_1', 'invalid_format_2')
    except typer.Exit:
        assert True
    else:
        assert False


def test_convert_invalid_filename():
    try:
        cli.convert('invalid_filename.pdf', 'pdf', 'emf')
    except typer.Exit:
        assert True
    else:
        assert False


def test_convert_several(file_dir, ps_file_single, ps_file_multi):
    cwd = Path().cwd()
    os.chdir(file_dir)
    relevant_files = [
        this_file
        for this_file in Path().iterdir()
        if str(this_file).lower().endswith('.ps')
    ]
    cli.convert(None, 'ps', 'pdf')
    new_files = [
        Path(str(new_file).lower().replace('.ps', '.pdf'))
        for new_file in relevant_files
    ]
    new_files_exist = [
        new_file.exists() for new_file in new_files
    ]
    assert all(new_files_exist)
    for new_file in new_files:
        new_file.unlink()
    os.chdir(cwd)


def test_combine(pdf_file_single, pdf_file_multi):
    cli.combine([str(pdf_file_single), str(pdf_file_multi)], 'pdf', None)
    new_file = Path(pdf_file_single).parent / 'compilation.pdf'
    assert new_file.exists()
    new_file.unlink()


def test_combine_no_filenames(file_dir, pdf_file_single, pdf_file_multi):
    cwd = Path().cwd()
    os.chdir(file_dir)
    cli.combine([], 'pdf', None)
    new_file = Path(file_dir) / 'compilation.pdf'
    assert new_file.exists()
    new_file.unlink()
    os.chdir(cwd)


def test_combine_no_filename_or_format():
    try:
        cli.combine([], None, None)
    except typer.Exit:
        assert True
    else:
        assert False


def test_combine_no_combiner(ps_file_single, ps_file_multi):
    try:
        cli.combine([str(ps_file_single), str(ps_file_multi)], 'ps', None)
    except typer.Exit:
        assert True
    else:
        assert False


def test_set_config(inkscape_path):
    cli.set_config('inkscape_path', 'asdf')
    assert glopan.config.config['inkscape_path'] == 'asdf'
    cli.set_config('inkscape_path', str(inkscape_path))


def test_reset_config(inkscape_path, ps2pdf_path):
    cli.reset()
    assert glopan.config.config['inkscape_path'] is None
    assert glopan.config.config['ps2pdf_path'] is None
    cli.set_config('inkscape_path', str(inkscape_path))
    cli.set_config('ps2pdf_path', str(ps2pdf_path))


def test_list_config(inkscape_path, ps2pdf_path):
    with io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
        cli.list_config()
        printed_from_cli = buffer.getvalue().replace('\n', '').replace(' ', '')

    with io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
        path_dict = {
            'inkscape_path': str(inkscape_path),
            'ps2pdf_path': str(ps2pdf_path),
        }
        print(path_dict)
        printed_from_test = buffer.getvalue().replace('\n', '').replace(
            ' ', ''
        )
    assert printed_from_cli == printed_from_test
