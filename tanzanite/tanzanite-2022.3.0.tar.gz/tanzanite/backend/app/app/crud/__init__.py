# pylint: disable=missing-module-docstring


from .crud_challenge import challenge  # noqa
from .crud_user import user  # noqa

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from tanzanite.backend.app.app.models.challenge import Challenge
# from tanzanite.backend.app.app.schemas.challenge import (
#     ChallengeCreate,
#     ChallengeUpdate,
# )

# challenge = CRUDBase[Challenge, ChallengeCreate, ChallengeUpdate](Challenge)
