from nerdvision import TYPES
from nerdvision.Utils import Utils

if TYPES:
    from typing import Optional


class ClientConfig(object):
    """
    This is the configuration of the client, this is controlled by NV and not the users

    :ivar redaction_black_list: the list of rules for black listing variables
    :ivar redaction_skip_list: the list of rules for skipping variables
    :ivar max_process_time: the max time to process a single line
    :ivar max_line_tps: the max number of tracepoints to process per line
    :ivar decorators: the decorators that are registered
    :ivar tags: the static set of tags calculated on client registration
    """

    def __init__(self):
        self.redaction_black_list = []
        self.redaction_skip_list = []
        self.max_process_time = 500
        self.max_line_tps = 5
        self.decorators = {}
        self.tags = {}
        self.session_id = None  # type: Optional[str]

    def update_config(self, config):
        if 'redaction_black_list' in config:
            self.redaction_black_list = config['redaction_black_list'].split(',')
        if 'redaction_skip_list' in config:
            self.redaction_skip_list = config['redaction_skip_list'].split(',')

        if 'max_process_time' in config:
            self.max_process_time = int(config['max_process_time'])
        if 'max_line_tps' in config:
            self.max_line_tps = int(config['max_line_tps'])

    def black_list(self, key):
        """
        Checks if the variable is black listed

        :param key: the variable name
        :return: true if value is black listed
        """

        return key in self.redaction_black_list

    def skip_list(self, key):
        """
        Checks if the variable is skip listed

        :param key: the variable name
        :return: true if value is skip listed
        """

        return key in self.redaction_skip_list

    def append_decorators(self, decorator):
        """
        Append a new decorator to the client

        :param decorator: a function that accepts a snapshot, and returns the decorator name and a dict of attributes.
        :return: the id of the decorator, used to remove the decorator
        :rtype: str
        """

        uid = Utils.generate_uid()
        self.decorators[uid] = decorator
        return uid

    def remove_decorator(self, uid):
        """
        Remove an existing decorator

        :param uid: the decorator id to remove
        :type uid: str
        """

        if uid in self.decorators:
            del self.decorators[uid]
