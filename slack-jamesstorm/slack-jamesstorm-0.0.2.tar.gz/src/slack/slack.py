from slack_sdk.webhook.client import WebhookClient

class StormSlack:
    def __init__(self, slack_webhook_url):
        self.slack_webhook_url = slack_webhook_url

    def send_slack_message(self, msg):
        webhook = WebhookClient(config.slack_webhook_url)
        webhook.send(text=msg)






