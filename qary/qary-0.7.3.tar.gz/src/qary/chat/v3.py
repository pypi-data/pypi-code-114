# qary.chat.v3
""" Load *.v3.dialog.yml files and execute recognize_intent() function:

  Inputs:
    lang (str): e.g. 'en', 'zh', 'es'
    state name/id (str): e.g. 'language-selected-english'
    user utterance (str): 'Hello chatobt'
  Outputs:
    id (str): state name
    text: bot utterance
"""
import logging
from collections import abc
from pathlib import Path
from qary.constants import DATA_DIR
import yaml

import pandas as pd

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


DIALOG_TREE_FILEPATH = Path(DATA_DIR) / 'chat' / 'moia-poly-dialog-tree-simplified-chinese.v3.dialog.yml'
DIALOG_TREE = yaml.full_load(DIALOG_TREE_FILEPATH.open())
DIALOG_TREE_DICT = {node['id']: node for node in DIALOG_TREE}
DIALOG_TREE_SERIES = pd.Series(DIALOG_TREE_DICT)


def normalize_state_name(name):
    return str(name).strip().lower()


def normalize_states(states=DIALOG_TREE_FILEPATH):
    """ Convert yamlfilepath->dict | dict->Series | Series.index.str.lower().str.strip()."""
    if isinstance(states, pd.Series):
        return pd.Series(
            states.values,
            index=[normalize_state_name(i) for i in states.index])
    if isinstance(states, (str, Path)):
        with Path(states).open() as fin:
            states = yaml.full_load(fin)
    if isinstance(states, list):  # TODO: make it work with any iterable of Mappings
        state_index_pairs = []
        for i, s in enumerate(states):
            state_index_pairs.append(s, s.get('id', i))
        states = pd.Series(*zip(state_index_pairs))
    # A Series is not a Mapping
    if isinstance(states, abc.Mapping):
        states = pd.Series(list(states.values()), index=list(states.keys()))
    return normalize_states(states)


class Engine:  # Engine(pd.Series)
    """ A state machine designed for managing the dialog for a rule-based chatbot """

    def __init__(self, states=DIALOG_TREE_SERIES, stateid=None):
        self.stateid = (stateid or '').strip().lower()
        self.states = normalize_states(states)
        try:
            self.statenum = self.states.index.get_loc(self.stateid)
        except KeyError as e:
            log.error(f'Unable to find stateid "{stateid}" in Engine.states.index')
            for line in str(e).split('\n'):
                log.error(f'    {line}\n')

    def run(self, user_text='', lang='en', stateid=None):
        stateid = self.stateid if stateid is None else stateid

    # self.state = states.iloc[0]
    # self.state.run()

    # def run_all(self, inputs):
    #     for i in inputs:
    #         print(i)
    #         self.currentState = self.currentState.next(i)
    #         self.currentState.run()


def next_state(states=DIALOG_TREE_SERIES, state_id=None, user_text='', lang='en'):
    r""" Recognize desired state transition and return it to the frontend

      Inputs:
        lang (str): e.g. 'en', 'zh', 'es'
        state name/id (str): e.g. 'language-selected-english'
        user utterance (str): 'Hello chatobt'
      Outputs:
        id (str): state name
        text: bot utterance

    >>> next_state(state_id='is-this-your-first-time', user_text='yes')
    {'lang': 'en',
     'state_id': 'is-this-your-first-yes',
     'bot_text': 'Which of the following do you represent?\n'}
    """
    response = {'lang': lang}
    for node in states:
        log.debug(f'Checking node id {node["id"]}...')
        if node['id'] == state_id:
            intents = node['triggers']
            log.debug(f'    triggers for node id {node["id"]}:\n{intents}')
            for intent_text in intents[lang]:
                log.debug(f'Checking intent text {node["id"]}...')
                if intent_text == user_text:
                    new_state_id = intents[lang][intent_text]
                    response['state_id'] = new_state_id
                    response['bot_text'] = states[new_state_id][lang]
                    return response

    return dict(state_id=state_id, bot_text=user_text, lang=lang)
