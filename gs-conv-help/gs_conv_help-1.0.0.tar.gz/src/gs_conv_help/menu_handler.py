from .response_cards import show_response_card

import difflib
import warnings
warnings.filterwarnings('ignore')
from fuzzywuzzy import fuzz
from  . import gs_global

def format_response_card_quick_reply(gs_context, current_context, response):
#     print(response)
    response_json_quick = {}
    response_json_quick['content_type'] = 'image'
    response_json_quick["card_type"] = "quick_reply"
    response_json_quick["header"] = ""
    response_json_quick["body"] = response["title"]
    response_json_quick["caption"] = ""
    if response['url']!='None':
        response_json_quick['url'] = response["url"]
    else:
        response_json_quick['content_type'] = 'text'
        response_json_quick['url'] = ''
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url']
    response["options"] = [x for x in response['options'] if x not in filter_buttons]
    response_json_quick["options"] = response["options"]
#     print('45121',response["options"])
#     print(response_json_quick)
    show_response_card(gs_context, current_context, response_json_quick)


def format_response_card_list(gs_context, current_context, response, temp_menu):
#     print(response)
    channel = gs_context['channel']
    response_json_list = {}
    # print(temp_menu)
    response_json_list['card_type'] = temp_menu['card_type_{}'.format(channel)]
    response_json_list['main_title'] = temp_menu['List_Header']
    response_json_list['main_body'] = response['title']
    response_json_list['button_text'] = "Show list"
    response_json_list["sections"] = []
    response_json_list_cat1 = {}
    response_json_list_cat1["title"] = temp_menu['List_Category']
    options = []
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url']
    response["options"] = [x for x in response['options'] if x not in filter_buttons]
    if response['option_desc']!='None':    
        lookup_desc_dict = response['option_desc']
    else:
        lookup_desc_dict = {}
    for button in response["options"]:
        each_option = {}
        each_option["title"] = button
        try:
            each_option['description'] = lookup_desc_dict[button]
        except:
            pass
        options.append(each_option)
    response_json_list_cat1["options"] = options
#     print('451212',response["options"])
    response_json_list["sections"].append(response_json_list_cat1)
    show_response_card(gs_context, current_context, response_json_list)
#     print(response_json_list)
# 
'''Additional thing for gip'''

def create_items_list_url(title,url):
    sample = {
                "title": title,
                "subtitle": "",
                "options": [
                    {
                        "title": title,
                        "type": "url",
                        "url": url
                    }
                ]
            }
    return sample

def create_items_list_text(title,description):
    sample = {
                "title": title,
                "subtitle": "",
                "options": [
                    {
                        "title": description,
                        "type": "text"
                    }
                ]
            }
    return(sample)

def response_card_distributor(gs_context, current_context, response, temp_menu):
    channel = gs_context['channel']
    if gs_context['channel']=='gip':
        if temp_menu['card_type_{}'.format(channel)] == 'list':
            format_gip_list_card(gs_context, current_context, response, temp_menu)
        elif temp_menu['card_type_{}'.format(channel)] == 'quick_reply':
            format_gip_quick_reply_card(gs_context, current_context, response, temp_menu)
        # elif temp_menu['card_type_{}'.format(channel)] == 'file':
        #     format_gip_file_card(gs_context, current_context, response, temp_menu)
        # elif temp_menu['card_type_{}'.format(channel)] == 'sticker':
        #     format_gip_sticker_card(gs_context, current_context, response, temp_menu)
        elif temp_menu['card_type_{}'.format(channel)] == 'catalogue':
            format_gip_catalogue_card(gs_context, current_context, response, temp_menu)
        elif temp_menu['card_type_{}'.format(channel)] == 'generic_card':
            format_gip_generic_card(gs_context, current_context, response, temp_menu)
    elif gs_context['channel']=='whatsapp':
        if temp_menu['card_type_{}'.format(channel)] == 'list':
            format_wapp_list_card(gs_context, current_context, response, temp_menu)
        elif temp_menu['card_type_{}'.format(channel)] == 'quick_reply':
            format_wapp_quick_reply_card(gs_context, current_context, response, temp_menu)
        # elif temp_menu['card_type_{}'.format(channel)] == 'file':
        #     format_wapp_file_card(gs_context, current_context, response, temp_menu) 
        # elif temp_menu['card_type_{}'.format(channel)] == 'sticker':
        #     format_wapp_sticker_card(gs_context, current_context, response, temp_menu)       
    elif gs_context['channel']=='instagram':
#         if temp_menu['card_type_{}'.format(channel)] == 'list':
#             format_insta_list_card(gs_context, current_context, response, temp_menu)
        if temp_menu['card_type_{}'.format(channel)] == 'quick_reply':
            format_insta_image_quick_reply(gs_context, current_context, response, temp_menu)
#         elif temp_menu['card_type_{}'.format(channel)] == 'file':
#             format_insta_file_card(gs_context, current_context, response, temp_menu)
        # elif temp_menu['card_type_{}'.format(channel)] == 'sticker':
        #     format_insta_sticker_card(gs_context, current_context, response, temp_menu)
        elif temp_menu['card_type_{}'.format(channel)] == 'catalogue':
            format_insta_catalogue_card(gs_context, current_context, response, temp_menu)
#         elif temp_menu['card_type_{}'.format(channel)] == 'generic_card':
#             format_insta_generic_card(gs_context, current_context, response, temp_menu)
    # if temp_menu['card_type_{}'.format(channel)] == 'image':
    #     format_all_image_card(gs_context, current_context, response, temp_menu)
        

def format_gip_list_card(gs_context, current_context, response, temp_menu):
    response_json_gip_list = {}
    response_json_gip_list['globalbuttons'] = {}
    response_json_gip_list['card_type'] = "list"
    response_json_gip_list['globalbuttons']['type'] = 'text'
    response_json_gip_list['globalbuttons']['title'] = "View More"
    response_json_list_cat1 = {}
    options = []
    response_json_list_cat1["title"] = temp_menu['list_header']
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url']
    response["options"] = [x for x in response['options'] if x not in filter_buttons]        
    if response['option_desc']!='None':    
        lookup_desc_dict = response['option_desc']
    else:
        lookup_desc_dict = {}
    response_json_gip_list['items'] = []
    for button in response["options"]:
        each_option = {}
        each_option["title"] = button
        try:
            each_option['description'] = lookup_desc_dict[button]
        except:
            pass
        options.append(each_option)
    
    for option in options:
        print(option)
        response_json_gip_list['items'].append(create_items_list_text(option['title'], option['description']))
    show_response_card(gs_context, current_context, response_json_gip_list)
    print(response_json_gip_list)

def format_gip_quick_reply_card(gs_context, current_context, response, temp_menu):
    response_json_quick = {}
    response_json_quick['content_type'] = 'text'
    response_json_quick["card_type"] = "quick_reply"
    response_json_quick["text"] = response["title"]
    if response['url'] != 'None':
        response_json_quick['url'] = response["url"]
    else:
        response_json_quick['content_type'] = 'text'
        response_json_quick['url'] = ''
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url', 'bot_header']
    response["options"] = [
        x for x in response['options'] if x not in filter_buttons]
    lst = []
    for i in response["options"]:
        dct = {}
        dct["title"] = i
        lst.append(dct)
    response_json_quick["options"] = lst
    print(f"response_json_quick......................{response_json_quick}")
    show_response_card(gs_context, current_context, response_json_quick)
    print(response_json_quick)

def format_gip_catalogue_card(gs_context, current_context, response, temp_menu,deals_df):
    response_json_list = {}
    response_json_list['card_type'] = temp_menu['card_type_gip']
    response_json_list['items'] = []
    deal_end_count = min(7,deals_df.shape[0])
    response_json_list["options"] = []
    for deals in range(deal_end_count):
        temp_dict = {}
        temp_dict['title'] = deals_df.iloc[deals,:]['title']
        temp_dict['subtitle'] = deals_df.iloc[deals,:]['long_offer']
        temp_dict['imgurl'] = deals_df.iloc[deals,:]['image_url']
        temp_dict['options'] = [{'title':'View Details','type':'url','url':deals_df.iloc[deals,:]['url']},
                               {'title':'Buy','type':'text'}]
        response_json_list['items'].append(temp_dict)
    gs_context['past_conversation'] = {'count_deals':deal_end_count,'prev_intent':'deals','deals_df':deals_df.to_dict('dict')}
    show_response_card(gs_context, current_context, response_json_list)
    print(response_json_list)


def format_gip_generic_card(gs_context, current_context, response, temp_menu):
    response_json_gip = {}
    response_json_gip['card_type'] = "generic_card"
    print(f"response..........................{response}")
    if response['url']!='None':
        response_json_gip['url'] = response["url"]
    else:
        response_json_gip['url'] = ''
    response_json_gip['title_0'] = temp_menu["bot_header"]
    response_json_gip['message'] = response["title"]
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url', 'bot_header']
    response["options"] = [x for x in response['options'] if x not in filter_buttons]
    for index,option in enumerate(response["options"]):
            response_json_gip['action{}_rank'.format(index)] = 1
            response_json_gip['action{}_type'.format(index)] = 7
            response_json_gip['action{}_content'.format(index)] = option
            response_json_gip['action{}_to'.format(index)] = option
    print(response_json_gip)
    show_response_card(gs_context, current_context, response_json_gip)

##  Wapp

def format_wapp_quick_reply_card(gs_context, current_context, response,temp_menu):
    response_json_quick = {}
    response_json_quick['content_type'] = 'image'
    response_json_quick["card_type"] = "quick_reply"
    response_json_quick["header"] = ""
    response_json_quick["body"] = response["title"]
    response_json_quick["caption"] = ""
    if response['url'] != 'None':
        response_json_quick['url'] = response["url"]
    else:
        response_json_quick['content_type'] = 'text'
        response_json_quick['url'] = ''
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url']
    response["options"] = [
        x for x in response['options'] if x not in filter_buttons]
    response_json_quick["options"] = response["options"]
    show_response_card(gs_context, current_context, response_json_quick)
    print(response_json_quick)




def format_wapp_list_card(gs_context, current_context, response, temp_menu):
    response_json_list = {}
    response_json_list['card_type'] = temp_menu['card_type_whatsapp']
    response_json_list['main_title'] = temp_menu['prompt']
    response_json_list['main_body'] = response['title']
    response_json_list['button_text'] = "Show list"
    response_json_list["sections"] = []
    response_json_list_cat1 = {}
    response_json_list_cat1["title"] = temp_menu['List_Category']
    options = []
    filter_buttons = ['Invalid-choice-message', 'prompt',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url','Value_Description']
    response["options"] = [
        x for x in response['options'] if x not in filter_buttons]
    if response['option_desc'] != 'None':
        lookup_desc_dict = response['option_desc']
    else:
        lookup_desc_dict = {}
    for button in response["options"]:
        each_option = {}
        each_option["title"] = button
        try:
            each_option['description'] = lookup_desc_dict[button]
        except:
            each_option['description'] = " "
        options.append(each_option)
    response_json_list_cat1["options"] = options
    print(9336396175,response_json_list)
    response_json_list["sections"].append(response_json_list_cat1)
    show_response_card(gs_context, current_context, response_json_list)
    
    

## Insta

def format_insta_image_quick_reply(gs_context, current_context, response, temp_menu):
    response_image_insta = {}
    if response['url'] != 'None':
        response_image_insta['url'] = response["url"]
    response_image_insta['card_type'] = 'image'
    response_image_insta['caption'] = 'Caption'
    print(response_image_insta)
    # show_response_card(gs_context, current_context, response_image_insta)
    response_json_quick = {}
    response_json_quick["card_type"] = "quick_reply"
    response_json_quick["text"] = response["title"]
    filter_buttons = ['Invalid-choice-message', 'prompt','Value_Description',
                      'card_type_gip','card_type_instagram','card_type_whatsapp', 'List_Header', 'List_Category', 'url']
    # print(response["options"])
    all_keys = [
        x for x in response['options'] if x not in filter_buttons]
    print('93369',all_keys)
    response_json_quick["options"] = all_keys
    print(response_json_quick)
    show_response_card(gs_context, current_context, response_json_quick)

def format_insta_catalogue_card(gs_context, current_context, response, temp_menu,deals_df):
    response_json_list = {}
    response_json_list['card_type'] = temp_menu['card_type_instagram']
    response_json_list['items'] = []    
    deal_end_count = min(7,deals_df.shape[0])
    response_json_list["options"] = []
    for deals in range(deal_end_count):
        temp_dict = {}
        temp_dict['title'] = deals_df.iloc[deals,:]['title']
        temp_dict['subtitle'] = deals_df.iloc[deals,:]['long_offer']
        temp_dict['imgurl'] = deals_df.iloc[deals,:]['image_url']
        temp_dict['options'] = [{'title':'View Details','type':'url','url':deals_df.iloc[deals,:]['url']},
                               {'title':'Buy','type':'text'}]
        response_json_list['items'].append(temp_dict)
    gs_context['past_conversation'] = {'count_deals':deal_end_count,'prev_intent':'deals','deals_df':deals_df.to_dict('dict')}
    print(response_json_list)
    show_response_card(gs_context, current_context, response_json_list)
    


'''Additional thing for gip'''

def activate_menu(gs_context, current_context, selection):
    '''
        This function activates the handle active menu until
        the menu_handled is true.
    '''
    current_context['current_intent']['user_text'] = selection
    gs_context['active_menu'] = selection
    # gs_context['active_menu_state'].append(selection)
    gs_context['menu_handled'] = True
    handle_active_menu(gs_context, current_context)
    return

# options = ['Entertainment','Fashion','Electronics & Gadgets','Home & Living','Stationary','Kids & Toddlers','Health & Beauty','Online Recharge','Gift Items','Travel']
def partial_match(x,y):
    return(fuzz.ratio(x,y))
def closest_matcher(word,options,gs_context,current_context):
    try:
        closest_match = (difflib.get_close_matches(word, options))[0]
        print(closest_match,word)
        match_score = (fuzz.ratio(closest_match,word))
        print(match_score)
        if match_score>80:
            return(closest_match)
        elif 40<match_score<80:
            response_json ={}
            response_json["card_type"] = "text"
            response_json["message"] = 'Did you mean this {}'.format(closest_match)
            show_response_card(gs_context,current_context,response_json)
            # print(response_json)
            return(closest_match)
        else:
            return(word)
    except:
        return(word)

def handle_active_menu(gs_context,current_context):
    """
        This function will come handy when it is a live dictionary
    """
#     selection = current_context['current_intent']['user_text']
#     print('Print whether the live dictionary is list',isinstance(gs_context['live_dict'][selection],dict))
    if gs_context['menu_handled']:
        channel = gs_context['channel']
        selection = current_context['current_intent']['user_text']
        db = gs_global.global_context['mongo_connection']
        temp_selection = selection.split(" ")
        if len(temp_selection) >1 and temp_selection[-1].isdigit():
            selection = " ".join(temp_selection[:-1])
        if gs_context["slots"]['language']!='en':
            selection = db.reverse_translate(selection)
        response ={}
        if isinstance(gs_context['live_dict'],dict):
            available_key_live_dict = list(gs_context['live_dict'].keys())
        elif isinstance(gs_context['live_dict'],list):
            available_key_live_dict = gs_context['live_dict']
        selection = closest_matcher(selection,available_key_live_dict,gs_context,current_context)
        try:
            if selection in available_key_live_dict:
                temp_menu = gs_context['live_dict'][selection].copy()
                # print('8858',temp_menu)
                try:
                    option_to_user = list(temp_menu.keys())#available dictionary
                    response['title'] = temp_menu['prompt']
                except:
                    option_to_user = temp_menu
                    response['title'] = 'Please select the options'
                gs_context['menu_handled'] = True
                option_to_user = [x for x in option_to_user if x not in ['Invalid-choice-message','prompt']]
                # response['title'] = temp_menu['prompt']
                if 'Category' not in option_to_user:
                    response['options'] = option_to_user
                    gs_context['live_dict'] = temp_menu
                    # print('options without Category')
                    gs_context['active_menu'] = selection
                    gs_context['active_menu_state'].append(selection)
                    # print('normal',response)
                else:
                    category_options = temp_menu['Category']
                    print('options with Category')
                    other_option = temp_menu.keys()
                    left_options = [x for x in other_option if x not in ['Category']]
                    temp_temp_menu = {}
                    for key,value in temp_menu.items():
                        if key in left_options:
                            temp_temp_menu[key] = value
                    for keys in category_options:
                        temp_temp_menu[keys] = ''
                    # print(temp_temp_menu)
                    gs_context['live_dict'] = temp_temp_menu
                    gs_context['active_menu'] = selection
                    gs_context['active_menu_state'].append(selection)
                    left_options.extend(category_options)
                    response['options'] = left_options
                    # print(left_options)
            else:
                temp_menu = gs_context['live_dict'].copy()
                print('Wrong option else')
                response['title'] = gs_context['live_dict']['Invalid-choice-message']
                option_to_user = gs_context['live_dict'].keys()
                option_to_user = [x for x in option_to_user if x not in ['Invalid-choice-message','prompt']]
                response['options'] = option_to_user
            if temp_menu['card_type_{}'.format(channel)] == 'list':
                try:
                    response['option_desc'] = gs_context['live_dict']['Value_Description']
                except:
                    response['option_desc'] = 'None' ## Also handle this in the format_response_card_list
                response_card_distributor(gs_context,current_context,response,temp_menu)
            else:
                try:
                    response['url'] = gs_context['live_dict']['url']
                    print('This is here 4598')
                except:
                    response['url'] = 'None' ## Also change the card type to text
                response_card_distributor(gs_context,current_context,response,temp_menu)
        except Exception as e:
            if selection in gs_context['live_dict']:
                print('Here I am in the except command')
                gs_context['active_menu_state'].append(selection)
                gs_context['menu_handled']=False
                current_context["current_intent"]={'intent': 'Menu_Completed', 'entities': {}, 'user_text': ''}
            else:
                print(e, 'Thas is a wrong option please choose the one from the below')
                response['title'] = 'Thas is a wrong option please choose the one from the below'
                option_to_user = gs_context['live_dict']
                gs_context['menu_handled']=True
                response['options'] = option_to_user
                temp_menu = option_to_user
                if temp_menu['card_type_{}'.format(channel)] == 'list':
                    try:
                        response['option_desc'] = gs_context['live_dict']['Value_Description']
                    except:
                        response['option_desc'] = 'None' ## Also handle this in the format_response_card_list
                    response_card_distributor(gs_context,current_context,response,temp_menu)
                else:
                    try:
                        response['url'] = gs_context['live_dict']['url']
                    except:
                        response['url'] = 'None'
                        print('This is here 4598_2')
                    response_card_distributor(gs_context,current_context,response,temp_menu)
    #             print(option_to_user)
                return
        return