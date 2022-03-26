from automagically.services.utils import AutomagicallyServiceAPI

SERVICE_URL = "emails/emails/"


class EmailsServiceAPI(AutomagicallyServiceAPI):
    def __init__(self, client, relative_url=SERVICE_URL):
        super().__init__(client, relative_url)
