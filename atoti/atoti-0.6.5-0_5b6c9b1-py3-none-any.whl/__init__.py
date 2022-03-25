import sys
from typing import Final

from atoti_core import BaseSession, get_env_flag

# pylint: disable=wrong-import-position
from ._runtime_type_checking_utils import _instrument_typechecking, typecheck

# This needs to be done here so that the runtime type checking decoration can be done before evaluating any classes inheriting from `BaseSession`.
# Otherwise the monkey-patching mechanism used by plugins will target the incorrect method references.
typecheck(BaseSession)

from atoti_query import (
    BasicAuthentication as BasicAuthentication,
    OAuth2ResourceOwnerPasswordAuthentication as OAuth2ResourceOwnerPasswordAuthentication,
    TokenAuthentication as TokenAuthentication,
)

from . import (  # pylint: disable=redefined-builtin
    agg as agg,
    array as array,
    comparator as comparator,
    experimental as experimental,
    math as math,
    query as query,
    scope as scope,
    string as string,
    type as type,
)
from ._create_session import *
from ._eula import (
    EULA as __license__,
    hide_new_eula_message as hide_new_eula_message,
    hide_new_license_agreement_message as hide_new_license_agreement_message,
    print_eula_message,
)
from ._plugins import register_active_plugins
from ._telemetry import telemeter
from ._version import VERSION as __version__
from .column import *
from .config import *
from .copy_tutorial import *
from .cube import Cube as Cube
from .function import *
from .hierarchy import *
from .level import *
from .measure import *
from .order import *
from .query import Auth as Auth, ClientCertificate as ClientCertificate
from .query.cube import *
from .query.hierarchy import *
from .query.level import *
from .query.measure import *
from .query.query_result import *
from .query.session import *
from .session import Session as Session, _sessions as sessions
from .table import Table as Table
from .type import DataType as DataType

# pylint: enable=wrong-import-position

print_eula_message()

# pylint: disable=invalid-name
open_query_session: Final = sessions._open_query_session
# pylint: enable=invalid-name


def close() -> None:
    """Close all opened sessions."""
    sessions.close()


register_active_plugins()

if not get_env_flag("DISABLE_RUNTIME_TYPECHECKING"):
    _instrument_typechecking(sys.modules[__name__])

telemeter()
