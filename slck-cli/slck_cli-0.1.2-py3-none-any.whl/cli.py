import os

import dotenv
import fire
from slack_sdk import WebClient
from slck.channel import ChannelManager
from slck.message import MessageManager
from slck.user import UserManager


class SlackManager:
    def __init__(self, client: WebClient) -> None:
        self.__client = client
        self.channel = ChannelManager(self.__client)
        self.user = UserManager(self.__client)
        self.message = MessageManager(self.__client)


def get_token() -> str:
    dotenv.load_dotenv()
    token: str = os.environ["SLACK_BOT_TOKEN"]
    return token


def main() -> None:
    token: str = get_token()
    client: WebClient = WebClient(token)
    slack: SlackManager = SlackManager(client)
    fire.Fire(slack)
