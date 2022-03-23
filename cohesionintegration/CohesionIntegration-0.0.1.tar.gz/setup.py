from setuptools import setup, find_packages
import pkutils

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = list(pkutils.parse_requirements('CohesionIntegration/requirements.txt'))

setup(
    name='CohesionIntegration',
    version='0.0.1',
    packages=find_packages(),
    url='http://cohesion.regione.marche.it/cohesioninformativo',
    license='MIT License',
    author='Saverio Delpriori',
    author_email='saveriodelpriori@gmail.com',
    description='Cohesion integration package'
)
