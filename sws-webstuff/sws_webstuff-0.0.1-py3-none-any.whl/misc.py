

def get_json_from_args(*args):
    temp_dict = {}

    for arg in args:
        if type(arg) == Alert or type(arg) == Modal or type(arg) == Redirect:
            temp_dict.update({type(arg).__name__: arg.to_dict()})
        elif type(arg) == type({}):
            temp_dict.update(arg)
        else:
            print("got unsupported var o-o")

    return temp_dict
