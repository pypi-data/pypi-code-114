import os
import hailtop.batch as hb


def concat_job(b, infiles, n_cpu=1):
    j = b.new_job(name='concat-files')
    j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    j.cpu(n_cpu)
    j.memory('highmem')
    j.storage('20Gi')
    cmd = f'''cat {" ".join(infiles)} > {j.ofile}'''
    j.command(cmd)
    return j


def concat_and_append_header_job(b, infiles, header_list, n_cpu=1):
    j = b.new_job(name='concat_and_append_header_job')
    j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    j.cpu(n_cpu)
    j.memory('highmem')
    j.storage('20Gi')
    header_str = "\t".join(header_list)
    cmd = f'''echo -e "{header_str}" | cat - {' '.join(infiles)} > {j.ofile}'''
    j.command(cmd)
    return j


def gzip_chain_job(j):
    cmd = f'gzip -c -f {j.ofile} > tmp.gzip.chain.gz; mv tmp.gzip.chain.gz {j.ofile}'
    j.command(cmd)
    return j


def tar_job(b, dirpath):
    j = b.new_job(name=f'tar_job-{os.path.basename(dirpath)}')
    j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    j.cpu(1)
    j.memory('standard')
    j.storage('10G')
    inputdir = b.read_input(dirpath)
    j.command(f'''
    dir=`dirname {inputdir}`
    base=`basename {inputdir}`
    cd $dir
    tar -cvzf {j.ofile} $base
    ''')
    b.write_output(j.ofile, f'{dirpath}.tar.gz')
    return(j)