from setuptools import setup, find_packages
 
setup(name="WOPkg",
      version="0.8",
      url="https://github.com/Wolframoviy/WOPkg/",
      license="MIT",
      author="WolframoviyI",
      author_email="arseniysstrim@gmail.com",
      description="Small lib for Python.\nrun(\"url_to_raw\") - run online code.\nsave(\"url_to_raw\", \"path.py\") - save online code.",
      packages=["WOPkg"],
      long_description=open("README.md").read(),
      zip_safe=False)