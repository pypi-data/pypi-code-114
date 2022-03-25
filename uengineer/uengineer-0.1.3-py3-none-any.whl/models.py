from .modelpyfe3d import ModelPyfe3D
from .dataset import zenodo_urls, files_from_urls


def pcrm9_wing():
    doi = 'https://doi.org/10.5281/zenodo.6384060'
    file_names = [
            'pCRM9_103_MAIN_FILE.bdf',
            'pCRM9_CONM2_MTOW.dat',
            'pCRM9_mat.dat',
            'pCRM9_model_2.dat',
            'pCRM9_PSHELL.dat',
            'pCRM9_ribs_fem.dat',
            ]
    model = ModelPyfe3D()

    urls = zenodo_urls(doi, file_names)
    files_from_urls(urls)

    model = ModelPyfe3D()
    model.read_nastran('pCRM9_103_MAIN_FILE.bdf', spcid=1)

    return model
