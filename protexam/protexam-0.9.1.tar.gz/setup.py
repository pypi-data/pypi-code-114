from setuptools import setup
from pathlib import Path

curr_dir = Path(__file__).parent

setup(
    name = 'protexam',
    version = '0.9.1',
    author = 'Proteome Proteomicsson 101',
    author_email = 'proteomicsson@gmail.com',
    description = ('Inspect your quantitative proteomics results using this streamlit-powered dashboard. The app is specifically tailored for comprehensive examination of result files from isobaric labeling-based quantitative experiments.'),
    license = 'BSD',
    license_files = ('LICENSE',),
    keywords = 'proteomics mass-spectrometry visualization streamlit',
    url = 'https://github.com/dev-ev/protexam',
    packages=['protexam'],
    long_description = (curr_dir / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires = [
        'bokeh <= 2.4.1', 'matplotlib < 4.0',
        'numpy', 'pandas', 'scikit-learn',
        'scipy', 'seaborn < 1.0', 'streamlit >= 1.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: BSD License',
    ],
)
