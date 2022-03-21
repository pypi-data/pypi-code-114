# pylint: disable=missing-module-docstring
# pylint: disable=unused-import


# Import all the models, so that Base has them before being
# imported by Alembic
from tanzanite.backend.app.app.db.base_class import Base  # noqa
from tanzanite.backend.app.app.models.challenge import Challenge  # noqa
from tanzanite.backend.app.app.models.user import User  # noqa
