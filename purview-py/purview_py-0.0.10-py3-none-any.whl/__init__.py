"""
OWLPy
~~~~~~~~~~~~~~~~~~~~~
An extension module to facilitate API Models and functionality.
:copyright: (c) 2019 Spydernaz
:license: MIT, see LICENSE for more details.
"""
# name = "OWLPy"
from .auth.TokenAuth import TokenAuth
from .conn.Connection import PurviewConnection
from .controller.Controller import PurviewController
from .controller.type.PurviewType import PurviewType
from .controller.type.Attribute import PurviewAttribute, PurviewRelationshipAttribute