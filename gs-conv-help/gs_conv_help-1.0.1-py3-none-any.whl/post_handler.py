from json import dumps
from rasa_sdk.events import (SlotSet)


def post_handle(dispatcher, gs_context, current_context):
    response_queue = current_context["response_queue"]
    for element in response_queue:
        if type(element) == (str):
            dispatcher.utter_message(text=element)
        else:
            dispatcher.utter_message(text=dumps(element))
    return


def get_events(gs_context, current_context):

    return SlotSet('gs_context', dumps(gs_context))
