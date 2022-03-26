from setuptools import setup, Extension
setup(
  name = 'fetchabi',         # How you named your package folder (MyLib)
  packages = ['fetchabi'],   # Chose the same as "name"
  version = '0.12',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A quick python script used to fetch an ethereum smart contracts ABI, if it is available on etherscan.',   # Give a short description about your library
  long_description = open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Koray',                   # Type in your name
  author_email = 'korre.remix@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kkayam/fetchabi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kkayam/fetchabi/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['Ethereum', 'smart', 'contract',"abi","fetch"],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)