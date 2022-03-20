'''
Desige: declassed site generator
================================

Concepts
--------

Page source
-----------

Source file is always metadata file in YAML format.

In the very basic form this metadata is the only source for the page.
Example: desige.pages.status_page.

More complex pages may contain additional files so a separate directory for each page
is preferred. Anyway, this directory always contains metadata file.

Metadata file consists of two documents. The first one defines page class, the second one
defines page data.


Classes
-------

Desige provides a set of mixins which can be combined by the user to get required functionality.
Because this is fully configurable, any mixin can be replaced, including very basic classes.
Such a flexibility is impossible with direct inheritance.
See sample configuration.


Layouts
-------

Layout classes establish relation between source files/directories, output files and URLs.


Processing
----------

Static pages are generated for each server and language.
Sitemaps include all alternative pages.


:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

__version__ = '0.0.18'

from .core import SiteGenerator, CopyTree, MakeBase, MakePages, MakeSitemap
