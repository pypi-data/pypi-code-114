from typing import Optional

from injector import inject
import logging

from ..providers.oidc_provider import JWTEncoded
from ..providers.identity_provider import JWTIdentityDlcClient
from ..services.abstract_external_service import ExternalService

logger = logging.getLogger(__name__)


class IdentityService(ExternalService):
    """
    Data Lake interface service, for interfacing
    with said interface.

    The JWTIdentityDlcClient should ONLY be responsible
    for authentication and connection pooling. This class
    should be responsible for implementation of high level
    interfacing with the interface component.
    """
    @inject
    def __init__(
        self,
        identity_session: JWTIdentityDlcClient
    ):
        logger.debug('Init IdentityService')
        self.identity_session = identity_session

    def get_organisation_for_id(self, id, jwt_encoded=None):
        kwargs = {'hooks': self._make_hook(f'No organisation for id: {id}')}
        if jwt_encoded:
            kwargs['headers'] = {'Authorization': f'Bearer {jwt_encoded}'}
        return self.identity_session.get(
            f'/__api_v2/organisations/{id}',
            **kwargs
        ).json()

    def get_visible_organisations(self):
        return self.identity_session.get(
            '/__api_v2/organisations/visible',
            hooks=self._make_hook('No visible organisations.')
        ).json()

    def me(self, jwt_encoded: Optional[JWTEncoded] = None):

        kwargs = {'hooks': self._make_hook(f'Cannot access identity/me')}
        if jwt_encoded:
            # we must avoid 'current_app' in the adapter when working outside flask context (middleware)
            kwargs['headers'] = {'Authorization': f'Bearer {jwt_encoded}'}

        return self.identity_session.get(
            '/__api_v2/me',
            **kwargs
        ).json()