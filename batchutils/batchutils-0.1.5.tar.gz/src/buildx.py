# %%
import hailtop.batch as hb
import batchutils

version = batchutils.__version__.split('+')[0]

# %%
image = hb.build_python_image(
    f'gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas-batchutils:{version}',
    requirements=['pandas', 'batchutils'])
