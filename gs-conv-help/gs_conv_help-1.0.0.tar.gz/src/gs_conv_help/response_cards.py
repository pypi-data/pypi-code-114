from json import loads
from .i18n import i18n_translate
from . import gs_global


def show_response_card(gs_context,current_context,response_details):
    channel = gs_context['channel']
    lang_code = gs_context["slots"]['language']
    i18n_required = gs_global.global_context['i18n_required']
    if(i18n_required):
        response_details = i18n_translate(response_details,lang_code,channel)
    if response_details['card_type'] == 'list':
        validate_list(channel,response_details)
        list_json = render_list(channel,response_details)
        current_context['response_queue'].append(list_json)
    elif response_details['card_type'] == 'quick_reply':
        validate_quick_reply(channel,response_details)
        quick_reply_json = render_quick_reply(channel,response_details)
        current_context['response_queue'].append(quick_reply_json)
    elif response_details['card_type'] == 'text':
        text = response_details['message']
        current_context['response_queue'].append(str(text))
    elif response_details['card_type'] == 'file':
        file_json = render_file(channel,response_details)
        current_context['response_queue'].append(file_json) 
    elif response_details['card_type'] == 'image':
        img_json = render_image(channel,response_details)
        current_context['response_queue'].append(img_json)
    elif response_details['card_type'] == 'sticker':
        sticker_json = render_sticker(channel,response_details)
        current_context['response_queue'].append(sticker_json)
    elif response_details['card_type'] == 'catalogue':
        catalogue_json = render_catalogue(channel,response_details)
        current_context['response_queue'].append(catalogue_json)
    elif response_details['card_type'] == 'generic_card':
        generic_card_json = render_generic_card(channel,response_details)
        current_context['response_queue'].append(generic_card_json)
    return

def validate_list(channel,response_details):
    if channel == 'whatsapp':
        len_title = len(response_details['main_title'])
        if len_title > 60:
            raise Exception("main_title has exceeded the character limit of 60!")
        len_body = len(response_details['main_body'])
        if len_body > 1024:
            raise Exception("main_body has exceeded the character limit of 1024!")
        len_button = len(response_details['button_text'])
        if len_button > 20:
            raise Exception("button_text has exceeded the character limit of 20!")
        for section in response_details['sections']:
            if 'title' not in section.keys():
                raise Exception("Section does not have a Title!")
            for option in section['options']:
                len_opt_title = len(option['title'])
                if len_opt_title > 24:
                    raise Exception(f"'{option['title']}' has exceeded the character limit of 24!")
                if 'description' in option.keys():
                    len_desc = len(option['description'])
                    if len_desc > 72:
                        raise Exception(f"'{option['description']}' has exceeded the character limit of 72!")
    return

def render_list(channel,response_details):
    list_json = {}
    if channel == 'whatsapp':
        main_title = response_details['main_title']
        main_body = response_details['main_body']
        button_text = response_details['button_text']
        section_list = response_details['sections']
        item_list = []
        for section in section_list:
            section_body = {}
            section_body['title'] = section['title']
            elements = section['options']
            options_list = []
            for element in elements:
                options = {}
                options['type'] = 'text'
                options['title'] = element['title']
                if 'description' in element.keys():
                    options['description'] = element['description']
                if 'postbackText' in element.keys():
                    options['postbackText'] = element['postbackText']
                options_list.append(options)
            section_body['options'] = options_list
            item_list.append(section_body)
        list_json['type'] = 'list'
        list_json['title'] = main_title
        list_json['body'] = main_body
        list_json['msgid'] = 'lst1'
        list_json['globalButtons'] = []
        list_json['globalButtons'].append({"type":"text","title":str(button_text)})
        list_json['items'] = item_list
    elif channel == 'gip':
        list_json['type'] = 'list'
        if "topElementStyle" in response_details.keys():
            list_json['topElementStyle'] = response_details['topElementStyle']
        else:
            list_json['topElementStyle'] = 'compact'
        if "msgid" in response_details.keys():
            list_json['msgid'] = response_details['msgid']
        else:
            list_json['msgid'] = "list123"
        list_json['items'] = response_details['items']
        list_json['globalButtons'] = response_details['globalButtons']
    return list_json

def validate_quick_reply(channel,response_details):
    if channel == 'whatsapp':
        if 'header' in response_details.keys():
            len_header = len(response_details['header'])
            if len_header > 60:
                raise Exception("header has exceeded the character limit of 60!")
        if 'caption' in response_details.keys():
            len_caption = len(response_details['caption'])
            if len_caption > 60:
                raise Exception("cation has exceeded the character limit of 60!")
        len_options = len(response_details['options'])
        if len_options > 3:
            raise Exception("You cannot use more than 3 quick reply buttons in whatsapp!")
    return

def render_quick_reply(channel,response_details):
    quick_reply_json = {}
    if channel == 'whatsapp':
        buttons = response_details['options']
        options_list = []
        for button in buttons:
            button_dict = {}
            button_dict['type'] = 'text'
            button_dict['title'] = str(button)
            options_list.append(button_dict)
        quick_reply_json['type'] = 'quick_reply'
        quick_reply_json['content'] = {}
        quick_reply_json['content']['type'] = 'text'
        if 'content_type' in response_details.keys():
            quick_reply_json['content']['type'] = response_details['content_type']
        if 'header' in response_details.keys():
            quick_reply_json['content']['header'] = response_details['header']
        quick_reply_json['content']['text'] = response_details['body']
        if 'caption' in response_details.keys():
            quick_reply_json['content']['caption'] = response_details['caption']
        if 'url' in response_details.keys():
            quick_reply_json['content']['url'] = response_details['url']
        quick_reply_json['msgid'] = 'qr1'
        quick_reply_json['options'] = options_list
    elif channel == 'gip':
        quick_reply_json['type'] = 'quick_reply'
        quick_reply_json['content'] = {}
        quick_reply_json['content']['type'] = 'text'
        if 'content_type' in response_details.keys():
            quick_reply_json['content']['type'] = response_details['content_type']
        if 'url' in response_details.keys():
            quick_reply_json['content']['url'] = response_details['url']
        if quick_reply_json['content']['type'] == 'text':
            quick_reply_json['content']['text'] = response_details['text']
        quick_reply_json['msgid'] = 'qr1'
        options_list = []
        for button in response_details['options']:
            button_dict = {}
            button_dict['type'] = 'text'
            button_dict['title'] = button['title']
            if 'url' in button.keys():
                button_dict['iconurl'] = button['url']
            options_list.append(button_dict)
        quick_reply_json['options'] = options_list
    elif channel == 'instagram':
        quick_reply_json['type'] = 'quick_reply'
        quick_reply_json["msgid"] = "qr1"
        content = {}
        content['type'] = 'text'
        content['text'] = response_details['text']
        quick_reply_json['content'] = content
        quick_reply_json['options'] = response_details['options']
    return quick_reply_json

def render_file(channel,response_details):
    file_json = {}
    if channel == 'whatsapp':
        file_json['type'] = 'file'
        file_json['url'] = response_details['url']
        file_json['filename'] = response_details['filename']
    elif channel == 'gip':
        file_json['type'] = 'file'
        file_json['url'] = response_details['url']
        file_json['text'] = response_details['text']       
    return file_json

def render_image(channel,response_details):
    image_json = {}
    if channel == 'whatsapp':
        image_json['type'] = 'image'
        image_json['originalUrl'] = response_details['url']
        image_json['previewUrl'] = response_details['url']
        image_json['caption'] = response_details['caption']
    elif channel == 'gip':
        image_json['type'] = 'image'
        image_json['originalUrl'] = response_details['url']
        image_json['previewUrl'] = response_details['url']
    elif channel == 'instagram':
        image_json['type'] = 'image'
        image_json['originalUrl'] = response_details['url']
        image_json['previewUrl'] = response_details['url']             
    return image_json

def render_sticker(channel,response_details):
    sticker_json = {}
    if channel == 'whatsapp':
        sticker_json['type'] = 'sticker'
        sticker_json['url'] = response_details['url']
    elif channel == 'gip':
        sticker_json['type'] = 'sticker'
        sticker_json['url'] = response_details['url']
    elif channel == 'instagram':
        sticker_json['type'] = 'sticker'
        sticker_json['id'] = response_details['id']
    return sticker_json         

def render_generic_card(channel,response_details):
    generic_json = {}
    if channel == 'whatsapp':
        raise Exception('Generic Cards are not supported in Whatsapp!')
    elif channel == 'gip':
        generic_json['type'] = 'generic_card'
        generic_json['mml'] = {}
        generic_json['mml'] = response_details
        generic_json['mml']['type'] = 'generic_card'        
    return generic_json

def render_catalogue(channel,response_details):
    catalogue_json = {}
    if channel == 'whatsapp':
        raise Exception('Catalogues are not supported in Whatsapp yet!')
    elif channel == 'gip':
        catalogue_json = response_details
        catalogue_json['type'] = 'catalogue'
    elif channel == 'instagram':
        catalogue_json = response_details
        catalogue_json['type'] = 'catalogue'      
    return catalogue_json    

def behave_extract_bot_response_text(channel,bot_response):
    if channel == 'whatsapp':
        bot_text = ''
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] != '{':
                    bot_text = resp['text']
                    break
        else:
            bot_text = bot_response[0]['text']
        return bot_text
    if channel == 'gip':
        bot_text = ''
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] != '{':
                    bot_text = resp['text']
                    break
        else:
            bot_text = bot_response[0]['text']
        return bot_text
    if channel == 'instagram':
        bot_text = ''
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] != '{':
                    bot_text = resp['text']
                    break
        else:
            bot_text = bot_response[0]['text']
        return bot_text

def behave_compare_text(channel,input_text,bot_text):
    if input_text == bot_text:
        return True
    return False

def behave_extract_bot_response_quick_reply(channel,bot_response):
    if channel == 'whatsapp':
        bot_text = ''
        bot_buttons = []
        bot_header_url = ''
        bot_caption = ''
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    qr_json = loads(resp['text'])
                    bot_text = qr_json['content']['text']
                    if qr_json['content']['type'] != 'text':
                        bot_header_url = qr_json['content']['url']
                    else:
                        if 'header' in qr_json['content'].keys():
                            bot_header_url = qr_json['content']['header']
                    if 'caption' in qr_json['content'].keys():
                        bot_caption = qr_json['content']['caption']
                    for option in qr_json['options']:
                        bot_buttons.append(option['title'])  
                    break
        else:
            qr_json = loads(bot_response[0]['text'])
            bot_text = qr_json['content']['text']
            if qr_json['content']['type'] != 'text':
                bot_header_url = qr_json['content']['url']
            else:
                if 'header' in qr_json['content'].keys():
                    bot_header_url = qr_json['content']['header']
            if 'caption' in qr_json['content'].keys():
                bot_caption = qr_json['content']['caption']
            for option in qr_json['options']:
                bot_buttons.append(option['title'])
        return (bot_text.strip(),bot_buttons.sort(),bot_header_url.strip(),bot_caption.strip())
    if channel == 'gip':
        bot_content = ''
        bot_buttons = []
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    qr_json = loads(resp['text'])
                    if qr_json['content']['type'] == 'text':
                        bot_content = qr_json['content']['text']
                    else:
                        bot_content = qr_json['content']['url']
                    for option in qr_json['options']:
                        bot_buttons.append(option)  
                    break
        else:
            qr_json = loads(bot_response[0]['text'])
            if qr_json['content']['type'] == 'text':
                bot_content = qr_json['content']['text']
            else:
                bot_content = qr_json['content']['url']
            for option in qr_json['options']:
                del option['type']
                bot_buttons.append(option) 
        return (bot_content.strip(),bot_buttons)
    if channel == 'instagram':
        bot_text = ''
        bot_buttons = []
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    qr_json = loads(resp['text'])
                    bot_text = qr_json['content']['text']
                    for option in qr_json['options']:
                        bot_buttons.append(option['title'])  
                    break
        else:
            qr_json = loads(bot_response[0]['text'])
            bot_text = qr_json['content']['text']
            for option in qr_json['options']:
                bot_buttons.append(option)
        return (bot_text.strip(),bot_buttons.sort()) 

def behave_compare_quick_reply(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        input_message = input_content['message'].strip()
        button_input = input_content['buttons'].sort()
        input_content_type = 'text'
        input_header_url = ''
        input_caption = ''
        if 'content_type' in input_content.keys():
            input_content_type = input_content['content_type']
        if input_content_type == 'text':
            if 'header' in input_content.keys():
                input_header_url = input_content['header']
        else:
            input_header_url = input_content['url']
        if 'caption' in input_content.keys():
            input_caption = input_content['caption']
        bot_message = bot_resp[0]
        bot_buttons = bot_resp[1]
        bot_header_url = bot_resp[2]
        bot_caption = bot_resp[3]
        if (input_message != bot_message):
            return False, "Message comparison failed!"
        if (button_input != bot_buttons):
            return False, "Buttons did not match!"
        if (input_header_url != '') and (input_header_url.strip() != bot_header_url):
            return False, "Header/URL did not match!"
        if (input_caption != '') and (input_caption.strip() != bot_caption):
            return False, "Caption did not match!"        
        return True, None
    elif channel == 'gip':
        input_content_type = input_content['content_type']
        input_buttons = input_content['buttons']
        bot_content = bot_resp[0]
        bot_buttons = bot_resp[1]
        qr_content = ''
        if input_content_type == 'text':
            qr_content = input_content['text']
        else:
            qr_content = input_content['url']
        for button in input_buttons:
            if 'url' in button.keys():
                if button['url'].lower() in ['n.a.']:
                    del button['url']
                else:
                    button['iconurl'] = button.pop('url')
        if (qr_content != bot_content):
            return False, "Mismatch in content dict!"
        for button in input_buttons:
            if button not in bot_buttons:
                return False, "Buttons did not match!"
        return True, None
    elif channel == 'instagram':
        input_message = input_content['message'].strip()
        button_input = input_content['buttons'].sort()
        bot_message = bot_resp[0]
        bot_buttons = bot_resp[1]
        if (input_message != bot_message):
            return False, "Message comparison failed!"
        if (button_input != bot_buttons):
            return False, "Buttons did not match!"
        return True, None

def behave_extract_bot_response_list(channel,bot_response):
    if channel == 'whatsapp':
        bot_text = ''
        bot_list = []
        bot_header = ''
        bot_global_button = ''
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    list_json = loads(resp['text'])
                    bot_text = list_json['body']
                    bot_header = list_json['title']
                    bot_global_button = list_json['globalButtons']
                    for item in list_json['items']:
                        list_element = {}
                        list_element["Category"] = item['title']
                        list_element["Items"] = []
                        for option in item['options']:
                            list_element["Items"].append(option['title'])
                        bot_list.append(list_element)
                    break
        else:
            list_json = loads(bot_response[0]['text'])
            bot_text = list_json['body']
            bot_header = list_json['title']
            bot_global_button = list_json['globalButtons']
            for item in list_json['items']:
                list_element = {}
                list_element["Category"] = item['title']
                list_element["Items"] = []
                for option in item['options']:
                    list_element["Items"].append(option['title'])
                bot_list.append(list_element)
        return (bot_text.strip(),bot_list,bot_header.strip(),bot_global_button)
    elif channel == 'gip':
        bot_items = []
        bot_buttons = []
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    list_json = loads(resp['text'])
                    for item in list_json['items']:
                        bot_items.append(item)
                    for option in list_json['globalButtons']:
                        bot_buttons.append(option)
                    break
        else:
            list_json = loads(bot_response[0]['text'])
            for item in list_json['items']:
                bot_items.append(item)
            for option in list_json['globalButtons']:
                bot_buttons.append(option)           
        return (bot_items,bot_buttons)  

def behave_compare_list(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        input_message = input_content['message'].strip()
        list_input = input_content['list']
        input_header = ''
        input_global_button = ''
        if 'header' in input_content.keys():
            input_header = input_content['header'].strip()
        if 'globalButtons' in input_content.keys():
            input_global_button = input_content['globalButtons']
        bot_message = bot_resp[0]
        bot_list = bot_resp[1]
        bot_header = bot_resp[2]
        bot_buttons = bot_resp[3]
        list_comparison = True
        for category in list_input:
            category['Items'].sort()
        for category in bot_list:
            category['Items'].sort()
        for element in list_input:
            if element not in bot_list:
                list_comparison = False
        for element in bot_list:
            if element not in list_input:
                list_comparison = False
        if (input_message != bot_message):
            return False, "Message comparison failed!"
        if (list_comparison == False):
            return False, "List items did not match!"
        if (input_header != '') and (input_header != bot_header):
            return False, "Headers did not match!"
        if (input_global_button != '') and (input_global_button != bot_buttons):
            return False, "Global Buttons did not match!"
        return True, None
    if channel == 'gip':
        input_items = input_content['items']
        input_buttons = input_content['globalButtons']
        bot_items = bot_resp[0]
        bot_buttons = bot_resp[1]
        list_comparison = True
        default_actions_removed = []
        # remove N.A. default actions and webview_height_ratio in options
        for item in input_items:
            item['title'] = item['title'].encode().decode('unicode_escape')
            item['subtitle'] = item['subtitle'].encode().decode('unicode_escape')
            item['options'] = item.pop('buttons')
            item['options'] = sorted(item['options'], key=lambda d: d['title'])
            if 'url' in item.keys():
                item['imgurl'] = item.pop('url')
            if 'defaultAction' in item.keys():
                if item['defaultAction'] == 'N.A.':
                    del item['defaultAction']
                    default_actions_removed.append(item['title'])
            else:
                default_actions_removed.append(item['title'])
        for item in bot_items:
            item['title'] = item['title'].encode().decode('unicode_escape')
            item['subtitle'] = item['subtitle'].encode().decode('unicode_escape')
            item['options'] = sorted(item['options'], key=lambda d: d['title'])
            if item['title'] in default_actions_removed:
                if 'defaultAction' in item.keys():
                    del item['defaultAction']
            for option in item['options']:
                if 'webview_height_ratio' in option.keys():
                    del option['webview_height_ratio']
        # compare items
        for item in input_items:
            if item not in bot_items:
                return False, "Item Comparison Failed!"
        # compare buttons/options
        input_buttons = sorted(input_buttons, key=lambda d: d['title'])
        bot_buttons = sorted(bot_buttons, key=lambda d: d['title'])
        if (input_buttons != bot_buttons):
            return False, "Button Comaparison Failed!"
        return True, None

def behave_extract_bot_response_file(channel,bot_response):
    if channel == 'whatsapp':
        file_json = loads(bot_response[0]['text'])
        bot_filename = file_json['filename']
        bot_url = file_json['url']
        return (bot_filename,bot_url)
    elif channel == 'gip':
        file_json = loads(bot_response[0]['text'])
        bot_text = file_json['text']
        bot_url = file_json['url']
        return (bot_text,bot_url)

def behave_compare_file(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        input_filename = input_content['filename']
        input_url = input_content['url']
        bot_filename = bot_resp[0]
        bot_url = bot_resp[1]
        if (input_filename != bot_filename):
            return False, "Filename did not match!"
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None
    elif channel == 'gip':
        input_text = input_content['text']
        input_url = input_content['url']
        bot_filename = bot_resp[0]
        bot_url = bot_resp[1]
        if (input_text != bot_filename): 
            return False, "Text did not match!"
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None       

def behave_extract_bot_response_image(channel,bot_response):
    if channel == 'whatsapp':
        image_json = loads(bot_response[0]['text'])
        bot_caption = image_json['caption']
        bot_url = image_json['originalUrl']
        return (bot_caption,bot_url)
    elif channel == 'gip':
        image_json = loads(bot_response[0]['text'])
        bot_url = image_json['originalUrl']
        return bot_url,None
    elif channel == 'instagram':
        image_json = loads(bot_response[0]['text'])
        bot_url = image_json['originalUrl']
        return bot_url,None

def behave_compare_image(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        input_url = input_content['url']
        input_caption = input_content['caption']
        bot_caption = bot_resp[0]
        bot_url = bot_resp[1]
        if (input_caption != bot_caption):
            return False, "Caption did not match!"
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None
    elif channel == 'gip':
        input_url = input_content['url']
        bot_url = bot_resp[0]
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None
    elif channel == 'instagram':
        input_url = input_content['url']
        bot_url = bot_resp[0]
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None

def behave_extract_bot_response_sticker(channel,bot_response):
    if channel == 'whatsapp':
        sticker_json = loads(bot_response[0]['text'])
        bot_url = sticker_json['url']
        return bot_url
    elif channel == 'gip':
        sticker_json = loads(bot_response[0]['text'])
        bot_url = sticker_json['url']
        return bot_url
    elif channel == 'instagram':
        sticker_json = loads(bot_response[0]['text'])
        bot_id = sticker_json['id']
        return bot_id

def behave_compare_sticker(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        input_url = input_content['url']
        bot_url = bot_resp
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None
    elif channel == 'gip':
        input_url = input_content['url']
        bot_url = bot_resp
        if (input_url != bot_url):
            return False, "URLs did not match!"
        return True, None
    elif channel == 'instagram':
        input_url = input_content['id']
        bot_url = bot_resp
        if (input_url != bot_url):
            return False, "IDs did not match!"
        return True, None 

def behave_extract_bot_response_catalogue(channel,bot_response):
    if channel == 'whatsapp':
        raise Exception('Catalogue not supported in Whatsapp yet!')
    elif channel == 'gip':
        bot_items = []
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    cat_json = loads(resp['text'])
                    for item in cat_json['items']:
                        bot_items.append(item)
                    break
        else:
            cat_json = loads(bot_response[0]['text'])
            for item in cat_json['items']:
                bot_items.append(item)           
        return bot_items
    elif channel == 'instagram':
        bot_items = []
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    cat_json = loads(resp['text'])
                    for item in cat_json['items']:
                        bot_items.append(item)
                    break
        else:
            cat_json = loads(bot_response[0]['text'])
            for item in cat_json['items']:
                bot_items.append(item)           
        return bot_items    

def behave_compare_catalogue(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        raise Exception('Catalogue not supported in Whatsapp yet!')
    if channel == 'gip':
        input_items = input_content['items']
        bot_items = bot_resp
        default_actions_removed = []
        # remove N.A. default actions and webview_height_ratio in options
        for item in input_items:
            item['title'] = item['title'].encode().decode('unicode_escape')
            item['subtitle'] = item['subtitle'].encode().decode('unicode_escape')
            item['options'] = item.pop('buttons')
            item['options'] = sorted(item['options'], key=lambda d: d['title'])
            if 'url' in item.keys():
                item['imgurl'] = item.pop('url')
            if 'defaultAction' in item.keys():
                if item['defaultAction'] == 'N.A.':
                    del item['defaultAction']
                    default_actions_removed.append(item['title'])
            else:
                default_actions_removed.append(item['title'])
        for item in bot_items:
            item['title'] = item['title'].encode().decode('unicode_escape')
            item['subtitle'] = item['subtitle'].encode().decode('unicode_escape')
            item['options'] = sorted(item['options'], key=lambda d: d['title'])
            if item['title'] in default_actions_removed:
                if 'defaultaction' in item.keys():
                    del item['defaultaction']
            for option in item['options']:
                if 'webview_height_ratio' in option.keys():
                    del option['webview_height_ratio']
        # compare items
        for item in input_items:
            if item not in bot_items:
                title = item['title']
                fstr = f"Item with title {title} did not match!"
                return False, fstr
        return True, None
    if channel == 'instagram':
        input_items = input_content['items']
        bot_items = bot_resp
        default_actions_removed = []
        # remove N.A. default actions and webview_height_ratio in options
        for item in input_items:
            item['title'] = item['title'].encode().decode('unicode_escape')
            item['subtitle'] = item['subtitle'].encode().decode('unicode_escape')
            item['options'] = item.pop('buttons')
            item['options'] = sorted(item['options'], key=lambda d: d['title'])
            if 'url' in item.keys():
                item['imgurl'] = item.pop('url')
            if 'defaultAction' in item.keys():
                if item['defaultAction'] == 'N.A.':
                    del item['defaultAction']
                    default_actions_removed.append(item['title'])
                else:
                    item['defaultaction'] = item.pop('defaultAction')
            else:
                default_actions_removed.append(item['title'])
        for item in bot_items:
            item['title'] = item['title'].encode().decode('unicode_escape')
            item['subtitle'] = item['subtitle'].encode().decode('unicode_escape')
            item['options'] = sorted(item['options'], key=lambda d: d['title'])
            if item['title'] in default_actions_removed:
                if 'defaultaction' in item.keys():
                    del item['defaultaction']
            for option in item['options']:
                if 'webview_height_ratio' in option.keys():
                    del option['webview_height_ratio']
        # compare items
        for item in input_items:
            if item not in bot_items:
                title = item['title']
                fstr = f"Item with title {title} did not match!"
                return False, fstr
        return True, None

def behave_extract_bot_response_generic_card(channel,bot_response):
    if channel == 'whatsapp':
        raise Exception("Generic Cards are not supported on Whatsapp!")
    elif channel == 'gip':
        bot_dict = {}
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    gencard = loads(resp['text'])
                    bot_dict = gencard['mml']
                    break
        else:
            gencard = loads(bot_response[0]['text'])
            bot_dict = gencard['mml']           
        return bot_dict

def behave_compare_generic_card(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        raise Exception("Generic Cards are not supported on Whatsapp!")
    elif channel == 'gip':
        gencard_input = {}
        gencard_input['message'] = input_content['message']
        i=0
        for title in input_content['titles']:
            key_str = 'title_' + str(i)
            gencard_input[key_str] = title
            i = i+1
        if 'core_entity' in input_content.keys():
            if (type(input_content['core_entity']) == str):
                if input_content['core_entity'] != 'N.A.':
                    gencard_input['core_entity'] = input_content['core_entity']
            else:
                gencard_input['core_entity'] = input_content['core_entity']['text']
                gencard_input['action0_rank'] = 0
                gencard_input['action0_type'] = int(input_content['core_entity']['type'])
                gencard_input['action0_to'] = input_content['core_entity']['url']
                if gencard_input['action0_type'] == 4:
                    gencard_input['action0_content'] = gencard_input['core_entity']
                    gencard_input['action0_to'] = gencard_input['core_entity']
                else:
                    gencard_input['action0_content'] = gencard_input['action0_to']
        j=1
        for action in input_content['actions']:
            key_rank = 'action' + str(j) + '_rank'
            key_type = 'action' + str(j) + '_type'
            key_to = 'action' + str(j) + '_to'
            key_content = 'action' + str(j) + '_content'
            gencard_input[key_rank] = 1
            gencard_input[key_type] = action['type']
            gencard_input[key_to] = action['to']
            gencard_input[key_content] = action['content']
            j=j+1
        for key,value in gencard_input.items():
            if key not in bot_resp.keys():
                reason = f"Key={key} not found in bot response!"
                return False, reason
            if gencard_input[key] != bot_resp[key]:
                reason = f"Values for Key={key} did not match!"
                return False, reason
        return True, None

def behave_extract_bot_response_generic_card_media(channel,bot_response):
    if channel == 'whatsapp':
        raise Exception("Generic Cards are not supported on Whatsapp!")
    elif channel == 'gip':
        bot_dict = {}
        if len(bot_response) > 1:
            for resp in bot_response:
                if resp['text'][0] == '{':
                    gencard = loads(resp['text'])
                    bot_dict = gencard['mml']
                    break
        else:
            gencard = loads(bot_response[0]['text'])
            bot_dict = gencard['mml']           
        return bot_dict

def behave_compare_generic_card_media(channel,input_content,bot_resp):
    if channel == 'whatsapp':
        raise Exception("Generic Cards are not supported on Whatsapp!")
    elif channel == 'gip':
        gencard_input = {}
        gencard_input['message'] = input_content['message']
        i=0
        for title in input_content['titles']:
            key_str = 'title_' + str(i)
            gencard_input[key_str] = title
            i = i+1
        if 'media' in input_content.keys():
            if (type(input_content['media']) == str):
                if input_content['media'] != 'N.A.':
                    gencard_input['media'] = input_content['media']
            else:
                gencard_input['media1_type'] = int(input_content['media']['type'])
                gencard_input['media1_url'] = input_content['media']['url']
                if gencard_input['media1_type'] != 1:
                    gencard_input['media1_cover'] = gencard_input['media']['cover']
        j=1
        for action in input_content['actions']:
            key_rank = 'action' + str(j) + '_rank'
            key_type = 'action' + str(j) + '_type'
            key_to = 'action' + str(j) + '_to'
            key_content = 'action' + str(j) + '_content'
            gencard_input[key_rank] = 1
            gencard_input[key_type] = action['type']
            gencard_input[key_to] = action['to']
            gencard_input[key_content] = action['content']
            j=j+1
        for key,value in gencard_input.items():
            if key not in bot_resp.keys():
                reason = f"Key={key} not found in bot response!"
                return False, reason
            if gencard_input[key] != bot_resp[key]:
                reason = f"Values for Key={key} did not match!"
                return False, reason
        return True, None

    
