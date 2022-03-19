"""Functions to help with module hygiene!

The main function exported is `cleanup`. The `cleanup`
function generates code which, upon execution, will
`del` every `local` variable that is not in some 
pre-defined list of `export` variables.

The version-finding code was generated with PyScaffold!
"""

__export__ = [
    "__version__",
    "cleanup",
]

import sys
if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

def cleanup(export: str = "__export__") -> str:
    """ Generate code to clean up the current namespace!
    
    Usage: `exec(cleanup())`
    """
    from textwrap import dedent
    return dedent(
        f"""
        for variable in locals().copy():
            if variable != "{export}" and variable not in {export}:
                del locals()[variable]
        del variable, {export}
        """
    )

exec(cleanup())