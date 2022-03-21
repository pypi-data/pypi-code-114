from pathlib import Path

import glopan


def test_split_pdf(pdf_file_multi):
    new_filenames = glopan.split_pdf(pdf_file_multi)
    new_files = [Path(new_filename) for new_filename in new_filenames]
    new_files_exist = [new_file.is_file() for new_file in new_files]
    assert all(new_files_exist)


def test_combine_pdf(pdf_file_multi):
    new_filenames = glopan.split_pdf(pdf_file_multi)
    outfile = 'test_combine.pdf'
    glopan.combine_pdfs(new_filenames, outfile)
    new_file = Path(outfile)
    assert new_file.is_file()
    new_file.unlink()


def test_delete_files(pdf_file_multi):
    new_filenames = glopan.split_pdf(pdf_file_multi)
    glopan.delete_files(new_filenames)
    new_files_are_deleted = [
        Path(new_filename).is_file() is not True
        for new_filename in new_filenames
    ]
    assert all(new_files_are_deleted)
