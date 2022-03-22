# Handled by kuldeep
from json import loads


def get_context(dispatcher, tracker, domain):
    print('inside_get_context',tracker.sender_id.lower())
    if 'whatsapp' in tracker.sender_id.lower():
        channel = 'whatsapp'
    elif 'anon' in tracker.sender_id.lower():
        channel = 'gip'
    elif 'instagram' in tracker.sender_id.lower():
        channel = 'instagram'
    else:
        # if 'whatsapp' in str(tracker.sender_id) else "gip"
        channel = 'whatsapp'
    entities = tracker.latest_message["entities"]
    dicts = {}
    for item in entities:
        dicts[item["entity"]] = item["value"]
    entity_dict = dicts
    gs_context_dict = tracker.get_slot("gs_context")
    if gs_context_dict is None:
        slots = {}
        slots['language'] = ""
        active_menu = ""
        active_menu_state = []
        menu_handled = False
        live_dict = {}
        past_conversation = ""
    else:
        gs_context_dict = loads(gs_context_dict)
        slots = gs_context_dict["slots"]
        active_menu = gs_context_dict["active_menu"]
        active_menu_state = gs_context_dict["active_menu_state"]
        menu_handled = gs_context_dict["menu_handled"]
        live_dict = gs_context_dict["live_dict"]
        past_conversation = gs_context_dict["past_conversation"]

    gs_context = {"sender_id": tracker.sender_id, "channel": channel,
                  "active_menu": active_menu, "active_menu_state": active_menu_state, "slots": slots, "menu_handled": menu_handled, "live_dict": live_dict, "past_conversation": past_conversation}
    current_intent = {"intent": tracker.latest_message['intent'].get('name'),
                      "entities": entity_dict,
                      "user_text": tracker.latest_message["text"]}
    current_context = {"current_intent": current_intent,
                       "domain": domain, "response_queue": []}

    return gs_context, current_context
