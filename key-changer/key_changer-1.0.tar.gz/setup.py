from setuptools import setup,find_packages
 #releases
setup(name='key_changer',
      version='1.0',
      description='change key th/en\ntype:auto1\nchange key eng to thai first and thai to eng\n\nauto2\change key thai to eng first and eng to thai\n\nth>en and TH>EN\nchange thai to eng only\n\nen>th and EN>TH\nchange eng to thai only\n\n',
      url='https://github.com/keegang6705/en-th-keyboard-translator',
      author='keegang_6705',
      author_email='darunphobwi@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires= [''],
      python_requires='>=3.0',
      zip_safe=False)