from . import _fetch_data

try:
    from importlib.metadata import version as _v
except ImportError:
    from importlib_metadata import version as _v


# Set version -----------------------------------------------------------------


__version__ = _v("lahman")

del _v

# Main ------------------------------------------------------------------------

# Potentially unpack data ----
if not (_fetch_data.SOURCE_DIR / "AllstarFull.csv").exists():
    print("Unpacking data...")
    _fetch_data.unpack_data()

# Load data ----
_lahman_fnames = list(_fetch_data.SOURCE_DIR.glob("*.csv"))

_accessors = _fetch_data.create_data_accessors(_lahman_fnames)
globals().update(_accessors)
