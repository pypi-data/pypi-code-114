import json


def format_string(new_value, path, node, action: str, result: list, old_value=None):
    path += node
    f_string = ""
    strange_means = ["false", "true", "null", "[complex value]"]
    if isinstance(new_value, dict):
        new_value = "[complex value]"
    if isinstance(old_value, dict):
        old_value = "[complex value]"
    else:
        pass
    if new_value not in strange_means and type(new_value) != int:
        new_value = f'\'{new_value}\''
    if old_value not in strange_means and type(old_value) != int:
        old_value = f'\'{old_value}\''
    if action == "delete":
        f_string = f'Property \'{path}\' was removed\n'
    elif action == "add":
        f_string = f'Property \'{path}\' was added with value: {new_value}\n'
    elif action == "update":
        f_string = f'Property \'{path}\' was updated. From {old_value} to {new_value}\n'
    result.extend(f_string)
    return result


def status_node(list_of_node, node, status):
    count, result = 0, "status"
    for point in list_of_node:
        if point == node:
            count += 1
    if count == 1 and status == "+":
        result = "add"
    elif count == 2 and status == "-":
        result = "update"
    elif count == 1 and status == " ":
        result = "not change"
    elif count == 1 and status == "-":
        result = "delete"
    return result


def separate_status_of_name(list_of_node):
    formate_node = []
    for point in list_of_node:
        point = point[0:len(point) - 1]
        formate_node.append(point)
    return formate_node


def status_key(diction: dict, result, path="", depth=1):
    keys = list(diction.keys())
    formate_keys_name = separate_status_of_name(keys)
    for node in keys:
        status = str(node)[-1]
        node_for_check = node[0:len(str(node)) - 1]
        what_hapend = status_node(formate_keys_name, node_for_check, status)
        if isinstance(diction[node], dict) and status == " ":
            path += str(node_for_check) + "."
            length_node = len(str(node_for_check))
            depth += 1
            status_key(diction[node], result, path, depth)
            path = path[0:len(path) - (length_node + 1)]
            depth -= 1
            if depth == 1:
                path = ""
        elif what_hapend == "add":
            format_string(diction[node], path, node_for_check, what_hapend, result)
        elif what_hapend == "update":
            old_value = diction[node_for_check + "-"]
            new_value = diction[node_for_check + "+"]
            format_string(new_value, path, node_for_check, what_hapend, result, old_value)
        elif what_hapend == "delete":
            format_string(diction[node], path, node_for_check, what_hapend, result)
    return result


def convert_to_json(diction: dict):
    keys = list(diction.keys())
    for node in keys:
        if isinstance(diction[node], dict):
            convert_to_json(diction[node])
        else:
            value = diction[node]
            if value is False:
                value = "false"
            elif value is None:
                value = "null"
            elif value is True:
                value = "true"
            diction[node] = value
    return diction


def convert_str(string, depth):
    convert = "    " * depth
    length = len(convert)
    convert = convert[2:length] + string[-1] + " " + string[0:len(string) - 1]
    return convert


def convert_dict_to_list(diction, result_list, depth=1):
    keys = diction.keys()
    for node in keys:
        if isinstance(diction[node], dict):
            ma_str = convert_str(str(node), depth)
            result_list.extend(ma_str)
            result_list.extend(": {\n")
            depth += 1
            convert_dict_to_list(diction[node], result_list, depth)
            depth -= 1
            result_list.extend("    " * depth + "}\n")
        else:
            ma_str = convert_str(str(node), depth)
            result_list.extend(ma_str)
            result_list.extend(": ")
            result_list.extend(list(str(diction[node])))
            result_list.extend("\n")
    return result_list, depth


def stylish(diction, mode):
    result_list = []
    finally_str = ""
    convert_to_json(diction)
    if mode == "json":
        convert_dict_to_list(diction, result_list)
        finally_str = "{\n"
        for sym in result_list:
            finally_str += sym
        finally_str += "}"
        finally_str = json.dumps(finally_str)
    if mode == "plain":
        result_list = status_key(diction, result_list)
        result_list = result_list[0:len(result_list) - 1]
        for i in result_list:
            finally_str += i
    if mode == 'stylish':
        convert_dict_to_list(diction, result_list)
        finally_str = "{\n"
        for sym in result_list:
            finally_str += sym
        finally_str += "}"
    return finally_str
