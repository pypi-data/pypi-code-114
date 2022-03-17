#!/usr/bin/env python
import pytest
import os
import pandas as pd
import dandelion as ddl
from pathlib import Path

from fixtures import (fasta_10x, annotation_10x, create_testfolder,
                      database_paths, dummy_adata, processed_files)

try:
    os.environ.pop('IGDATA')
    os.environ.pop('GERMLINE')
    os.environ.pop('BLASTDB')
except:
    pass


@pytest.mark.parametrize("filename,expected",
                         [pytest.param('filtered', 1),
                          pytest.param('all', 2)])
def test_write_fasta(create_testfolder, fasta_10x, filename, expected):
    out_fasta = str(create_testfolder) + "/" + filename + "_contig.fasta"
    fh = open(out_fasta, "w")
    fh.close()
    out = ''
    for l in fasta_10x:
        out = '>' + l + '\n' + fasta_10x[l] + '\n'
        ddl.utl.Write_output(out, out_fasta)
    assert len(list(create_testfolder.iterdir())) == expected


@pytest.mark.parametrize("filename,expected",
                         [pytest.param('filtered', 3),
                          pytest.param('all', 4)])
def test_write_annotation(create_testfolder, annotation_10x, filename,
                          expected):
    out_file = str(
        create_testfolder) + "/" + filename + "_contig_annotations.csv"
    annotation_10x.to_csv(out_file, index=False)
    assert len(list(create_testfolder.iterdir())) == expected


@pytest.mark.parametrize("filename,expected", [
    pytest.param(None, 2),
    pytest.param('filtered', 2),
    pytest.param('all', 4)
])
def test_formatfasta(create_testfolder, filename, expected):
    ddl.pp.format_fastas(str(create_testfolder), filename_prefix=filename)
    assert len(list((create_testfolder / 'dandelion').iterdir())) == expected


def test_reannotate_fails(create_testfolder, database_paths):
    with pytest.raises(KeyError):
        ddl.pp.reannotate_genes(str(create_testfolder),
                                filename_prefix='filtered')
    with pytest.raises(KeyError):
        ddl.pp.reannotate_genes(str(create_testfolder),
                                igblast_db=database_paths['igblast_db'],
                                filename_prefix='filtered')
    with pytest.raises(KeyError):
        ddl.pp.reannotate_genes(str(create_testfolder),
                                germline=database_paths['germline'],
                                filename_prefix='filtered')


@pytest.mark.parametrize("filename,expected",
                         [pytest.param('filtered', 5),
                          pytest.param('all', 10)])
def test_reannotategenes(create_testfolder, database_paths, filename,
                         expected):
    ddl.pp.reannotate_genes(str(create_testfolder),
                            igblast_db=database_paths['igblast_db'],
                            germline=database_paths['germline'],
                            filename_prefix=filename)
    assert len(list(
        (create_testfolder / 'dandelion/tmp').iterdir())) == expected


def test_reassign_alleles_fails(create_testfolder, database_paths):
    with pytest.raises(TypeError):
        ddl.pp.reassign_alleles(str(create_testfolder),
                                filename_prefix='filtered')
    with pytest.raises(KeyError):
        ddl.pp.reassign_alleles(str(create_testfolder),
                                combined_folder='reassigned_filtered',
                                filename_prefix='filtered')


@pytest.mark.parametrize("filename,combine,expected", [
    pytest.param('filtered', 'reassigned_filtered', 13),
    pytest.param('all', 'reassigned_all', 16)
])
def test_reassignalleles(create_testfolder, database_paths, filename, combine,
                         expected):
    ddl.pp.reassign_alleles(str(create_testfolder),
                            combined_folder=combine,
                            germline=database_paths['germline'],
                            filename_prefix=filename,
                            novel=True,
                            save_plot=True,
                            show_plot=False)
    assert len(list(
        (create_testfolder / 'dandelion/tmp').iterdir())) == expected


def test_updateblastdb(database_paths):
    ddl.utl.makeblastdb(database_paths['blastdb_fasta'])
    assert len(list(Path(database_paths['blastdb']).iterdir())) == 10


@pytest.mark.parametrize("filename, expected",
                         [pytest.param('filtered', 5),
                          pytest.param('all', 4)])
def test_assignsisotypes(create_testfolder, database_paths, filename,
                         expected):
    ddl.pp.assign_isotypes(str(create_testfolder),
                           blastdb=database_paths['blastdb_fasta'],
                           filename_prefix=filename,
                           save_plot=True,
                           show_plot=False)
    assert len(list((create_testfolder / 'dandelion').iterdir())) == expected


@pytest.mark.parametrize("filename", ['all', 'filtered'])
def test_checkccall(create_testfolder, processed_files, filename):
    f = create_testfolder / str('dandelion/' + processed_files[filename])
    dat = pd.read_csv(f, sep='\t')
    assert not dat['c_call'].empty


def test_create_germlines_fails(create_testfolder, processed_files):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    with pytest.raises(KeyError):
        ddl.pp.create_germlines(f)


def test_create_germlines(create_testfolder, processed_files, database_paths):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    ddl.pp.create_germlines(f, germline=database_paths['germline'])
    f2 = create_testfolder / str('dandelion/' +
                                 processed_files['germline-dmask'])
    dat = pd.read_csv(f2, sep='\t')
    assert not dat['germline_alignment_d_mask'].empty


def test_update_germlines_fail(create_testfolder, processed_files):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    vdj = ddl.Dandelion(f)
    with pytest.raises(KeyError):
        vdj.update_germlines()


def test_update_germlines(create_testfolder, processed_files, database_paths):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    vdj = ddl.Dandelion(f)
    vdj.update_germlines(database_paths['germline'])
    assert len(vdj.germline) > 0


@pytest.mark.parametrize(
    "freq,colname,dtype",
    [pytest.param(True, 'mu_freq', float),
     pytest.param(False, 'mu_count', int)])
def test_quantify_mut(create_testfolder, processed_files, freq, colname, dtype):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    ddl.pp.quantify_mutations(f, frequency=freq)
    dat = pd.read_csv(f, sep='\t')
    assert not dat[colname].empty
    assert dat[colname].dtype == dtype


@pytest.mark.parametrize(
    "freq,colname",
    [pytest.param(True, 'mu_freq'),
     pytest.param(False, 'mu_count')])
def test_quantify_mut_2(create_testfolder, processed_files, freq, colname):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    vdj = ddl.Dandelion(f)
    ddl.pp.quantify_mutations(vdj, frequency=freq)
    assert not vdj.data[colname].empty
    if colname == 'mu_freq':
        assert vdj.data[colname].dtype == float
    else:
        assert vdj.data[colname].dtype == int


@pytest.mark.parametrize("filename,simple,size", [
    pytest.param('filtered', True, 8),
    pytest.param('filtered', False, 7),
    pytest.param('all', True, 8),
    pytest.param('all', False, 7),
])
def test_filtercontigs(create_testfolder, processed_files, dummy_adata,
                       filename, simple, size):
    f = create_testfolder / str('dandelion/' + processed_files[filename])
    dat = pd.read_csv(f, sep='\t')
    vdj, adata = ddl.pp.filter_contigs(dat, dummy_adata, simple=simple)
    assert dat.shape[0] == 9
    assert vdj.data.shape[0] == size
    assert vdj.metadata.shape[0] == 4
    assert adata.n_obs == 5


def test_assign_isotypes_fails(create_testfolder, database_paths):
    with pytest.raises(FileNotFoundError):
        ddl.pp.assign_isotypes(str(create_testfolder),
                               filename_prefix='filtered',
                               plot=False)
    ddl.pp.format_fastas(str(create_testfolder), filename_prefix='filtered')
    with pytest.raises(KeyError):
        ddl.pp.assign_isotypes(str(create_testfolder),
                               filename_prefix='filtered',
                               plot=False)


@pytest.mark.parametrize("prefix,suffix,sep,remove", [
    pytest.param('test', None, None, True),
    pytest.param('test', None, None, False),
    pytest.param(None, 'test', None, True),
    pytest.param(None, 'test', None, False),
    pytest.param(None, None, '-', True),
    pytest.param(None, None, '-', False),
    pytest.param('test', 'test', '-', True),
    pytest.param('test', 'test', '-', False),
])
def test_formatfasta2(create_testfolder, prefix, suffix, sep, remove):
    ddl.pp.format_fastas(str(create_testfolder),
                         filename_prefix='filtered',
                         prefix=prefix,
                         suffix=suffix,
                         sep=sep,
                         remove_trailing_hyphen_number=remove)
    f = create_testfolder / 'dandelion' / 'filtered_contig_annotations.csv'
    df = pd.read_csv(f)
    contig = list(df['contig_id'])[0]
    if prefix is None:
        if remove:
            if suffix is not None:
                if sep is None:
                    assert contig.split('_contig')[0].endswith('_' + suffix)
                else:
                    assert contig.split('_contig')[0].endswith(sep + suffix)
            else:
                assert contig.split('_contig')[0].endswith('-1')
        else:
            if suffix is None:
                assert contig.split('_contig')[0].endswith('-1')
            else:
                if sep is None:
                    assert contig.split('_contig')[0].endswith('_' + suffix)
                else:
                    assert contig.split('_contig')[0].endswith(sep + suffix)
    else:
        if sep is None:
            assert contig.startswith(prefix + '_')
        else:
            assert contig.startswith(prefix + sep)


def test_update_germlines_fail(create_testfolder, processed_files):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    vdj = ddl.Dandelion(f)
    with pytest.raises(KeyError):
        vdj.update_germline()


def test_update_germlines(create_testfolder, processed_files, database_paths,
                          fasta_10x):
    f = create_testfolder / str('dandelion/' + processed_files['filtered'])
    vdj = ddl.Dandelion(f)
    vdj.update_germline(germline=database_paths['germline'])
    assert len(vdj.germline) > 0
    out_file = str(create_testfolder) + "/test_airr_reannotated.h5"
    vdj.write_h5(out_file)
    tmp = ddl.read_h5(out_file)
    assert len(tmp.germline) > 0
    vdj.update_germline(germline=database_paths['germline'],
                        corrected=str(create_testfolder) +
                        "/filtered_contig.fasta")
    assert len(vdj.germline) > 0
    vdj.update_germline(germline=database_paths['germline'],
                        corrected=fasta_10x)
    assert len(vdj.germline) > 0
    with pytest.raises(TypeError):
        vdj.update_germline(germline=database_paths['germline'], corrected=[])
