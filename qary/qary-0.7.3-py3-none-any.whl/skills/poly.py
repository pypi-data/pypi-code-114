""" Pattern and template based chatbot dialog engines """
import logging

from qary.chat.v3 import Engine
from qary.skills.base import normalize_replies, ContextBaseSkill  #


log = logging.getLogger(__name__)


class Skill(ContextBaseSkill):
    r""" Skill that can reply with answers to frequently asked questions using data/faq/*.yml

    >>> bot = Skill()
    >>> bot.reply(None)
    [(0.01, 'What?')]
    """

    def __init__(self, *args, **kwargs):
        """ Load the v3.dialog.yaml file to initialize the dialog state machine (dialog engine) """
        self.engine = Engine(*args, **kwargs)
        super().__init__(*args, **kwargs)

    def reply(self, statement, context=None):
        """ Suggest responses to a user statement string with [(score, reply_string)..]"""
        statement = statement or ''
        responses = [(.01, 'What?')]
        normalize_replies(responses)
        return responses
