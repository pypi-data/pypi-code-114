def to_camel_case(string):
    """
    :param string: String which needs to be converted from snake case to camel case
    :return: Camel cased string
    """
    converted_string = ""
    for i, word in enumerate(string.split("_")):
        if i == 0:
            converted_string += word
            continue
        converted_string += word.title()
    return converted_string


def comel_case_dict(dictionary):
    """
    :param dictionary: A dictionary having snake case keys which need to be converted into camel case
    :return: Camel cased key value pair dictionary
    """
    updated_dictionary = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            value = comel_case_dict(value)
        updated_dictionary[to_camel_case(key)] = value
    return updated_dictionary


if __name__ == '__main__':
    dictt = {
        "id": "string",
        "field_type": "numberfield",
        "field_label": "string",
        "field_id": "string",
        "read_only": True,
        "label_column": 0,
        "field_column": 0,
        "hidden": True,
        "required": True,
        "notes": "string",

        "help_text": "string",
        "validation": {
            "unique": True,
            "size": {
                "min": 0,
                "max": 0,
                "custom_message": "string"
            }
        },
        "data_type": 0,
        "regexp": {
            "pattern": "string",
            "flags": "string",
            "custom_message": "string"
        },
        "prohibit_pattern": {
            "pattern": "string",
            "flags": "string",
            "custom_message": "string"
        },
        "on_blur": "string",
        "on_change": "string",
        "placeholder": "string"
    }
    word = {'id': 'string', 'fieldType': 'numberfield', 'fieldLabel': 'string', 'fieldId': 'string', 'readOnly': True,
            'labelColumn': 0, 'fieldColumn': 0, 'hidden': True, 'required': True, 'notes': 'string',
            'helpText': 'string',
            'validation': {'unique': True, 'size': {'min': 0, 'max': 0, 'customMessage': 'string'}}, 'dataType': 0,
            'regexp': {'pattern': 'string', 'flags': 'string', 'customMessage': 'string'},
            'prohibitPattern': {'pattern': 'string', 'flags': 'string', 'customMessage': 'string'}, 'onBlur': 'string',
            'onChange': 'string', 'placeholder': 'string'}
    word = comel_case_dict(dictt)
    print(word)
