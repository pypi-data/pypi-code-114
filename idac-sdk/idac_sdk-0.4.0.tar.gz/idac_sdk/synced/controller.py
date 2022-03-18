from idac_sdk.asynced.controller import IDACController as IDACControllerAsync
from idac_sdk.synced.helpers import sync_method


class IDACController(IDACControllerAsync):
    __idac_synced_obj__ = True

    @sync_method
    def get_auth_token(self, creds: str, datacenter: str, use_as_auth: bool = True) -> str:
        """Requests auth token from controller synchronously. Required for DCLOUD_SESSION auth type.

        Args:
            creds (str): `creds` token from session.xml dCloud file
            datacenter (str): dCloud datacenter where session runs
            use_as_auth (bool, optional): If True, response will be used as `auth` for
                `auth_headers` & `with_auth` methods. Defaults to True.

        Raises:
            NoAuthTokenInResponse: Raised if no token received in response

        Returns:
            str: Auth token
        """
        return super().get_auth_token(creds=creds, datacenter=datacenter, use_as_auth=use_as_auth)  # type: ignore
