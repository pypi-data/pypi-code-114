from pathlib import Path

import typer

import glopan


def test_docx_to_pdf(docx_file):
    glopan.docx_to_pdf(docx_file)
    new_file = Path(docx_file.replace('.docx', '.pdf'))
    assert new_file.is_file()
    new_file.unlink()


def test_pdf_to_emf(pdf_file_single):
    glopan.pdf_to_emf(pdf_file_single)
    new_file = Path(pdf_file_single.replace('.pdf', '.emf'))
    assert new_file.is_file()
    new_file.unlink()


def test_pdf_to_png(pdf_file_single):
    glopan.pdf_to_png(pdf_file_single)
    new_file = Path(pdf_file_single.replace('.pdf', '.png'))
    assert new_file.is_file()
    new_file.unlink()


def test_pdf_to_svg(pdf_file_single):
    glopan.pdf_to_svg(pdf_file_single)
    new_file = Path(pdf_file_single.replace('.pdf', '.svg'))
    assert new_file.is_file()
    new_file.unlink()


def test_ps_to_pdf_single(ps_file_single):
    glopan.ps_to_pdf(ps_file_single)
    new_file = Path(ps_file_single.replace('.ps', '.pdf'))
    assert new_file.is_file()
    new_file.unlink()


def test_ps_to_pdf_multi(ps_file_multi):
    glopan.ps_to_pdf(ps_file_multi)
    new_file = Path(ps_file_multi.replace('.ps', '.pdf'))
    assert new_file.is_file()
    new_file.unlink()


def test_many_ps_to_pdf(ps_file_single, ps_file_multi):
    glopan.many_ps_to_pdf([ps_file_single, ps_file_multi])
    new_files = [
        this_file.replace('.ps', '.pdf')
        for this_file in [ps_file_single, ps_file_multi]
    ]
    new_files_exist = [
        Path(new_file).exists() for new_file in new_files
    ]
    assert all(new_files_exist)
    for new_file in new_files:
        Path(new_file).unlink()


def test_ps_to_pdf_no_path(ps_file_single):
    temp_config = {**glopan.config.config}
    glopan.config.reset()
    try:
        glopan.ps_to_pdf(ps_file_single)
    except typer.Exit:
        new_file = Path(ps_file_single.replace('.ps', '.pdf'))
        assert Path(new_file).exists() is False
    for key, value in temp_config.items():
        glopan.config.set(key, value)


def test_pdf_to_emf_no_path(pdf_file_single):
    temp_config = {**glopan.config.config}
    glopan.config.reset()
    try:
        glopan.pdf_to_emf(pdf_file_single)
    except typer.Exit:
        new_file = Path(pdf_file_single.replace('.pdf', '.emf'))
        assert Path(new_file).exists() is False
    for key, value in temp_config.items():
        glopan.config.set(key, value)
