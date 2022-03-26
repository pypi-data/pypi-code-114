"""
This python based project help generating visio drawing from the excel database.
Tested on MS-Visio Professional 2013. other version support is not tested. it may or may not work as described.

Requirements
--------------------
Database: update your data in Excel.   Two tabs are necessary, one with devices details, another with connectivity details.

MS-Visio: to generate the drawing.

Stencils: [optional] folder from where project can find visio stencils.

"""

__ver__ = "0.0.5"

# ------------------------------------------------------------------------------

from .stencils import get_list_of_stencils
from .database import DeviceData, CableMatrixData
from .gui import UserForm
from .entities import ItemObjects, Connectors
from .visio import VisioObject
# ------------------------------------------------------------------------------

