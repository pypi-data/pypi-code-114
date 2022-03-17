from gendiff import formaters
import json
import yaml


def search_way(file_name: str):
    if 'json' in file_name:
        return json.load(open(file_name))
    if 'yaml' in file_name:
        with open(file_name) as f:
            file = yaml.safe_load(f)
        return file
    elif 'yml' in file_name:
        with open(file_name) as f:
            file = yaml.safe_load(f)
        return file
    else:
        return -1


def refactor_keys(diction: dict):
    keys = list(diction.keys())
    for node in keys:
        flag = str(node)[-1]
        list_of_flag = [' ', '-', '+']
        if isinstance(diction[node], dict):
            if flag in list_of_flag:
                refactor_keys(diction[node])
            else:
                value = diction.pop(node)
                diction[node + ' '] = value
                refactor_keys(diction[node + ' '])
        elif flag in list_of_flag:
            continue
        else:
            value = diction.pop(node)
            diction[node + ' '] = value
    return diction


def difference(dict1, dict2, depth=1):
    result = dict()
    main1, main2 = set(dict1.keys()), set(dict2.keys())
    file_1set, file_2set = (main1 - main2), (main2 - main1)
    common_keys = sorted(main1 | main2)
    for node in common_keys:
        if node in (main1 & main2):
            if isinstance(dict1[node], dict) and (isinstance(dict2[node], dict)):
                depth += 1
                result[node + ' '] = difference(dict1[node], dict2[node], depth=depth)
            elif dict1[node] == dict2[node]:
                result[node + ' '] = dict2[node]
            elif dict2[node] != dict1[node]:
                result[node + '-'] = dict1[node]
                result[node + '+'] = dict2[node]
        elif node in file_1set:
            result[node + '-'] = dict1[node]
        elif node in file_2set:
            result[node + '+'] = dict2[node]
    return result


def generate_diff(path1, path2, mode='stylish'):
    dict_1 = search_way(path1)
    dict_2 = search_way(path2)
    result_dict = difference(dict_1, dict_2)
    refactor_dict = refactor_keys(result_dict)
    finally_ = formaters.stylish(refactor_dict, mode)
    return finally_
