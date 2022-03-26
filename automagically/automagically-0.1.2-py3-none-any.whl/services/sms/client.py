from automagically.services.utils import AutomagicallyServiceAPI


class SmsServiceAPI(AutomagicallyServiceAPI):
    def __init__(self, client, relative_url="sms/sms/"):
        super().__init__(client, relative_url)
