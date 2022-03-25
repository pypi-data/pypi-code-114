import pytest
import pathlib

import miyadaiku.core
import miyadaiku.core.site  # install pyyaml converter

#miyadaiku.core.SHOW_TRACEBACK = True
#miyadaiku.core.DEBUG = True

from miyadaiku.core.site import Site

@pytest.fixture
def sitedir(tmpdir):
    d = tmpdir.mkdir('site')
    d.mkdir('contents')
    d.mkdir('templates')
    return pathlib.Path(str(d))

def test_install(sitedir):
    (sitedir / 'config.yml').write_text('''
themes:
    - miyadaiku.themes.bootstrap4

''')

    (sitedir /'contents/index.rst').write_text('''

test
---------------

abc 

.. jinja::

   {{ bootstrap4.load_css(page) }}
   {{ bootstrap4.load_js(page) }}
''')

    site = Site(sitedir)
    site.build()

    ret = (sitedir / 'outputs/index.html').read_text()

    assert '<link href="static/bootstrap4/bootstrap.min.css" rel="stylesheet"/>' in ret
    assert '<script src="static/bootstrap4/bootstrap.min.js"></script>' in ret

    assert (sitedir / 'outputs/static/bootstrap4/bootstrap.min.css').exists()
    assert (sitedir / 'outputs/static/bootstrap4/bootstrap.min.js').exists()
