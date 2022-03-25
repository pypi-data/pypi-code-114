from setuptools import setup,find_packages
 
setup(name='calc_plus',
      version='0.2',
      description='test',
      url='https://github.com/keegang6705/calc_plus',
      author='keegang_6705',
      author_email='darunphobwi@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires= ['numpy'],
      python_requires='>=3.8',
      zip_safe=False)