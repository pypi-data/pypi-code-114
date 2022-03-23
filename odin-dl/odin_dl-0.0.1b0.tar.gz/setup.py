import setuptools

setuptools.setup(
    name = "odin_dl",
    version = "0.0.1-beta",
    licence = 'BSD 3-Clause',
    author = "João Pedro Santana",
    author_email = 'joaopedrosantana020@gmail.com',
    description= "Visual Layer Object Detection",
    packages=["odin_dl"],
    install_requires=['fastai==1.0.61', 'google==2.0.3', 'matplotlib==3.2.2', 'numpy==1.21.5', 'opencv-python==4.1.2.30', 'ipython==5.5.0', 'ipywidgets==7.7.0']
)