def object_to_str(obj, keys):
    """Return a string representation of an object."""
    s = ""
    for key in keys:
        value = eval("obj." + key)
        key = key.replace("()", "")
        if type(value) == str:
            s += f"{key} = {value}\n"
        elif type(value) == list:
            for idx, vv in enumerate(value):
                if not vv:
                    s += f"{key}[{idx}] = \n"
                    continue
                s += f"{key}[{idx}] = {vv}\n"
        elif type(value) == dict:
            for vv_key in value.keys():
                vv_value = value[vv_key]
                if not vv_value:
                    s += f"{key}.{vv_key} = \n"
                    continue
                s += f"{key}.{vv_key} = {vv_value}\n"
        else:
            s += f"{key} = {str(value)}\n"
    return s
