"""
Allow:
> import local_stats as ls
> ls.Cluster()

As opposed to:
> from local_stats.cluster import Cluster
> Cluster()

etc.
"""

from .cluster import Cluster
from .image import Image, DiffractionImage
