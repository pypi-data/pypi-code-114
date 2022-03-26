import requests

class LineNotify:
    def __init__(self, token):
        self.token = token

    def notify(self, message):
        url = 'https://notify-api.line.me/api/notify'
        headers = {'content-type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + self.token}
        r = requests.post(url, headers=headers, data={'message': message})
        return r.text
