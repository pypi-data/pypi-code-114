from django.core.mail.backends import filebased
from django.core.mail.backends import smtp


class EmailBackend(filebased.EmailBackend, smtp.EmailBackend):
    def __init__(self, *args, **kwargs):
        filebased.EmailBackend.__init__(self, *args, **kwargs)
        smtp.EmailBackend.__init__(self, *args, **kwargs)

    def send_messages(self, *args, **kwargs):
        filebased.EmailBackend.send_messages(self, *args, **kwargs)
        smtp.EmailBackend.send_messages(self, *args, **kwargs)

    def open(self):
        result = filebased.EmailBackend.open(self)
        smtp.EmailBackend.open(self)
        return result
