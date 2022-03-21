from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
    name="dsbox_graphs",
    version="1.0.0",
    description="Graph Embedding and Convolution primitives",
    author="Rob Brekelmans",
    author_email="brekelma@usc.edu",
    keywords='d3m_primitive',
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=[
        'd3m',
        'd3m-common-primitives',
        'numpy>=1.12.0',
        'tensorflow==2.2.0',
        'keras==2.3.1',
        'scikit-learn>=0.18.1',
        'scipy>=0.19.0',
        'networkx',
        'matplotlib>=2.0.0',
    ],
    url='https://gitlab.com/datadrivendiscovery/contrib/dsbox-graphs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python"
    ],
    entry_points = {
    'd3m.primitives': [
        'feature_construction.sdne.DSBOX = dsbox_graphs.sdne:SDNE',
        'feature_construction.gcn_mixhop.DSBOX = dsbox_graphs.gcn_mixhop:GCN'
        #'data_transformation.graph_to_edge_list.DSBOX = graph_dataset_to_list:GraphDatasetToList',
        #'feature_construction.graph_transformer.SDNE = sdne:SDNE',
	#'data_transformation.graph_to_edge_list.DSBOX = graph_dataset_to_list:GraphDatasetToList',
	#'feature_construction.graph_transformer.GCN = gcn_mix:GCN'
    ],
    }

)
