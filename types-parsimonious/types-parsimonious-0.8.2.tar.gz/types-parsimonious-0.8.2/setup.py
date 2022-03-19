from setuptools import setup

name = "types-parsimonious"
description = "Typing stubs for parsimonious"
long_description = '''
## Typing stubs for parsimonious

This is a PEP 561 type stub package for the `parsimonious` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `parsimonious`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/parsimonious. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `1acc8f3bd645aea6b18cf15d5fca271b9c3cd785`.
'''.lstrip()

setup(name=name,
      version="0.8.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/parsimonious.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['parsimonious-stubs'],
      package_data={'parsimonious-stubs': ['__init__.pyi', 'exceptions.pyi', 'expressions.pyi', 'grammar.pyi', 'nodes.pyi', 'utils.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Stubs Only",
      ]
)
