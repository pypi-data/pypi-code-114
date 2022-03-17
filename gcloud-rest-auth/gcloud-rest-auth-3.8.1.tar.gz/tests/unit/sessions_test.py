from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import super
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from future import standard_library
standard_library.install_aliases()
import pytest
from gcloud.rest.auth.build_constants import BUILD_GCLOUD_REST
from gcloud.rest.auth.session import SyncSession

if BUILD_GCLOUD_REST:
    import requests

    class Session(requests.Session):
        def __init__(self, *args, **kwargs)        :
            self._called = False
            super(requests.Session, self).__init__(*args, **kwargs)

        def close(self)        :
            self._called = True
            super(requests.Session, self).close()

        @property
        def closed(self)        :
            return self._called

    requests.Session = Session
else:
    from aiohttp import ClientSession as Session


#@pytest.mark.asyncio
def test_unmanaged_session():
    with Session() as session:
        gcloud_session = SyncSession(session=session)
        assert gcloud_session._shared_session  # pylint: disable=protected-access
        gcloud_session.close()

        assert not session.closed


#@pytest.mark.asyncio
def test_managed_session():
    gcloud_session = SyncSession()
    # create new session
    gcloud_session.session  # pylint: disable=pointless-statement
    if BUILD_GCLOUD_REST:
        gcloud_session._session = Session()  # pylint: disable=protected-access
    assert not gcloud_session._shared_session  # pylint: disable=protected-access
    gcloud_session.close()

    assert gcloud_session._session.closed  # pylint: disable=protected-access
