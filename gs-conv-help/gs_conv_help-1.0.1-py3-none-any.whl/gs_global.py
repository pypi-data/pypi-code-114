global_context = {}

global_context['mongo_connection'] = ""
global_context['i18n_required'] = False

def set_mongo_connection_object(mongo_connection):
    global global_context
    global_context['mongo_connection'] = mongo_connection

def set_i18n_required_flag(i18n_required):
    global global_context
    global_context['i18n_required'] = i18n_required
