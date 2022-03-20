import telegram
from flask import Flask, request

from pemudapersis_bot.src.configs.environment import EnvConfig as Config
from pemudapersis_bot.src.receivers.telegram_bot import (
    handler,
    start_command,
    help_command,
    contact_command,
)

BOT = telegram.Bot(token=Config.BOT_TOKEN)
CERT = "cert.pem"
CERT_KEY = "key.pem"
CONTEXT = (CERT, CERT_KEY)
APP = Flask(__name__)


@APP.route("/pemudapersis-bot", methods=["POST"])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), BOT)

    if update.message.text == "/start":
        start_command(update)
    elif update.message.text == "/help":
        help_command(update)
    elif update.message.text == "/contact":
        contact_command(update)
    else:
        handler(update)

    return "ok"


@APP.route("/set_webhook", methods=["GET", "POST"])
def set_webhook():
    s = BOT.setWebhook(Config.WEBHOOK_URL, certificate=open(CERT, "rb"))
    if s:
        return f"Webhook setup OK : {Config.WEBHOOK_URL}"
    else:
        return f"Webhook setup failed : {Config.WEBHOOK_URL}"


@APP.route("/")
def index():
    return "<h1>Pemuda Persis Bot webhook is running</h1>"


def start():
    APP.run(
        threaded=True,
        port=Config.WEBHOOK_PORT,
        host=Config.WEBHOOK_HOST,
        ssl_context=CONTEXT,
    )


if __name__ == "__main__":
    start()
