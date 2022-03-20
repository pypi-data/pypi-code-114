"""" Command line interface for the bot"""
import logging
import os
import click
import colorama
from pyfiglet import figlet_format
from termcolor import colored
from pemudapersis_bot.src.configs.environment import EnvConfig as Conf
from pemudapersis_bot.src.receivers import telegram_webhook, telegram_bot

logging.basicConfig(format=Conf.LOG_FORMAT, level=Conf.LOG_LEVEL)
colorama.init()


@click.command()
@click.option("--poll", is_flag=True, help="Start the bot with polling method")
@click.option("--start", is_flag=True, help="Start the bot webhook")
def handle_commands(poll, start):
    """Main method for handling commands through CLI"""
    if not Conf.BOT_TOKEN:
        stdout(
            "ERROR: please set BOT_TOKEN to start the bot! ",
            color="red",
        )
        return
    stdout("\nPemuda Persis Bot", color="green", figlet_flag=True)
    if poll:
        stdout("Starting polling messages...", color="green")
        try:
            telegram_bot.start_bot()
            stdout("Server completed", color="green")
        except Exception as exc:
            stdout("Starting server failed! : {}".format(exc), color="red")

    if start:
        if not Conf.WEBHOOK_URL:
            stdout(
                "ERROR: WEBHOOK_URL needs to be set for starting webhook server! ",
                color="red",
            )
        if not Conf.WEBHOOK_HOST:
            stdout(
                "WARNING: WEBHOOK_HOST is not set, set default value : 0.0.0.0",
                color="yellow",
            )
        if not Conf.WEBHOOK_PORT:
            stdout(
                "WARNING: WEBHOOK_PORT is not set, set default value : 8443",
                color="yellow",
            )
        else:
            stdout(f"WEBHOOK_URL : {os.environ['WEBHOOK_URL']}", color="yellow")
        stdout("Starting Tabayyun webhook server...", color="green")
        telegram_webhook.start()
        try:
            telegram_webhook.start()
        except Exception as e:
            stdout("Starting server failed! : {}".format(e), color="red")


def stdout(string: str, color: str, font: str = "slant", figlet_flag: bool = False):
    """A helper method to print logs to stdout"""
    if not figlet_flag:
        logging.info(colored(string, color))
    else:
        logging.info(colored(figlet_format(string, font=font), color))


if __name__ == "__main__":
    handle_commands()
