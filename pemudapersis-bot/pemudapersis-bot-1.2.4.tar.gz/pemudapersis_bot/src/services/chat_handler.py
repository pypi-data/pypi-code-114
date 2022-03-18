import logging
from datetime import datetime
from telegram import Chat as TelegramChat
from pemudapersis_bot.src.configs.environment import EnvConfig as Conf
from pemudapersis_bot.src.models.user import BotUser
from pemudapersis_bot.src.models.chat import Chat

logging.basicConfig(format=Conf.LOG_FORMAT, level=Conf.LOG_LEVEL)


class ChatHandler:
    """Chat Handler"""

    def handler(self, chat: Chat):
        """Method for handing text chats"""

        # process reply
        reply: str = "Untuk sementara hanya berjalan di Group"
        if self:
            return reply

    def magic_keyword(self, keyword: str):
        magic_reply: str
        logging.info("Magic keyword : %s", keyword)
        magic_reply = "No such magic!"
        if self:
            return magic_reply

    @staticmethod
    def log_users(user: BotUser):
        """method for storing users to db"""
        chat_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log: list = [user.user_id, user.name, chat_timestamp]
        logging.info("Storing user %s", log)
