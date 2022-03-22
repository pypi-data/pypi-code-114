from . import gs_global
## Get connection object from global_context


## List of all the keys that are present in response_details & should also be translated
## In case any text to be translated from response_details dict is present in nested lists & dicts, translatable_keys must contain all keys needed to traverse the path until it reaches the text to be translated
whatsapp_translatable_keys_text = ['message']
whatsapp_translatable_keys_quickreply = ['header', 'body', 'caption', 'options']
whatsapp_translatable_keys_list = ['main_title', 'main_body', 'button_text', 'sections', 'title', 'options', 'description', 'postbackText']
gip_translatable_keys_text = ['message']
gip_translatable_keys_quickreply = ['text', 'options','title']
gip_translatable_keys_list = ['globalbuttons', 'title', 'items', 'subtitle', 'options']
gip_translatable_keys_generic_card = ['message','title_0','action0_content','action0_to','title_1','action1_content','action1_to','title_2','action2_content','action2_to','title_3','action3_content','action3_to','title_4','action4_content','action4_to''title_5','action5_content','action5_to','title_6','action6_content','action6_to','title_7','action7_content','action7_to','title_8','action8_content','action8_to','title_9','action9_content','action9_to']
gip_translatable_keys_catalogue = ['items','title','subtitle','options','buttons']
insta_translatable_keys_quickreply = ['text', 'options']
insta_translatable_keys_catalogue = ['items','title','subtitle','options']
insta_translatable_keys_text = ['message']

translatable_keys_for_channel = {
    'whatsapp':{'text':whatsapp_translatable_keys_text, 'quick_reply':whatsapp_translatable_keys_quickreply,'list':whatsapp_translatable_keys_list},
    'gip':{'text':gip_translatable_keys_text, 'quick_reply':gip_translatable_keys_quickreply,'list':gip_translatable_keys_list,'generic_card':gip_translatable_keys_generic_card,'catalogue':gip_translatable_keys_catalogue},
    'instagram':{'text':insta_translatable_keys_text,'quick_reply':insta_translatable_keys_quickreply,'catalogue':insta_translatable_keys_catalogue}
    }

## default settings
translatable_keys = []
lang_code = 'en'

def get_translatable_keys(channel, card_type):
    return translatable_keys_for_channel[channel][card_type]


## Below functions to iterate through nested dicts and lists and return translated strings at the end of the heirarchy
def handle_type(obj):
    if(type(obj)==list):
        obj = handle_list(obj)
    if(type(obj)==dict):
        obj = handle_dict(obj)
    if(type(obj)==str):
        obj = handle_str(obj)
    return obj

def handle_list(list):
    temp_list=[]
    for item in list:
        item = handle_type(item)
        temp_list.append(item)
    return temp_list

def handle_dict(dict):
    for key in dict:
        if(key in translatable_keys):
            dict[key] = handle_type(dict[key])
    return dict

def handle_str(string):
    translated_text = return_if_translation_exists(string)
    return translated_text

## Get translated string from mongodb
def return_if_translation_exists(text):
    db = gs_global.global_context['mongo_connection']
    translated_text = db.get_translated_text_for_lang(text, lang_code)
    return translated_text if(translated_text is not None) else text


def i18n_translate(response_details: dict, lang_code: str, channel: str) -> dict:
    if lang_code != 'en':
        try:
            globals()['lang_code'] = lang_code
            try:
                globals()['translatable_keys'] = get_translatable_keys(channel, response_details['card_type'])
            except:
                print("Invalid card type or channel")
                return response_details
            translated_response_details = handle_type(response_details)
            return translated_response_details
        except:
            print("Translation failed")
            return response_details
    else:
        return response_details

def i18n_extract(response_details: dict):
    pass
