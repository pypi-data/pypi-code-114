import datetime
import re


def is_bytes(data):
    """
    Check if data is of type byte or bytearray.
    :param data:
    :return:
    """
    try:
        data = data.decode()
        return False
    except AttributeError:
        return True


def add_attr2attributes(element, attributes, prefix=None):
    """
    Add attributes of elements to 'attributes' dictionary.
    :param element:
    :param attributes:
    :param prefix:
    :return:
    """
    attr = element.get("attr")
    if attr is not None:
        for key, value in attr.items():
            if prefix is None:
                dict_key = key
            else:
                dict_key = prefix + key[0].upper() + key[1:]
            if value.isdigit():
                attributes[dict_key] = int(value)
            else:
                attributes[dict_key] = value
    # return attributes


# def replace_fields(field_dict, expression, row_data, attributes):
def replace_fields(report, expression, attributes):
    """
    Replace fields with value from data source.
    If the field is not in the database, do not replace.
    :param report:
    :param expression: text to be processed
    :param attributes: attribute of the element being processed (i.e. 'isBlankWhenNull')
    :return: expression with $F{} replaced with values from data source when they exist
    """
    if expression is None or report["row_data"] is None:
        return None
    else:
        # find all field keys in specified expression
        new_keys = [
            key[key.find("$F{") + 3 : key.find("}")]
            for key in re.findall(r"\$F\{.*?\}", expression)
        ]
        if report.get("field_dict") is not None:
            for key in new_keys:
                data_type = report["field_dict"].get(key)
                if data_type == "java.lang.Integer":
                    data_value = str(report["row_data"].get(key, "$F{" + key + "}"))
                elif data_type == "java.sql.Timestamp":
                    date_time = report["row_data"].get(key, "$F{" + key + "}")
                    if type(date_time) is not datetime.datetime:
                        data_value = date_time
                    else:
                        data_value = (
                            "datetime.datetime("
                            + str(date_time.year)
                            + ","
                            + str(date_time.month)
                            + ","
                            + str(date_time.day)
                            + ","
                            + str(date_time.hour)
                            + ","
                            + str(date_time.minute)
                            + ","
                            + str(date_time.second)
                            + ","
                            + str(date_time.microsecond)
                            + ","
                            + str(date_time.tzinfo)
                            + ")"
                        )
                elif data_type == "java.lang.Object":
                    return report["row_data"].get(key, "$F{" + key + "}")
                else:
                    is_blank_when_null = convert2boolean(attributes.get("isBlankWhenNull"))
                    value = report["row_data"].get(key, "$F{" + key + "}")
                    if is_blank_when_null and value is None:
                        # data_value = ''
                        return ""
                    else:
                        data_value = '"' + str(report["row_data"].get(key, "$F{" + key + "}")) + '"'
                if key is not None and data_value is not None:
                    expression = expression.replace("$F{" + key + "}", data_value)
        return expression


def replace_variables(variables, expression, attributes):
    """
    Replace variables with value from data source.
    If the variable is not in the database, do not replace.
    :param variables:
    :param expression:
    :param attributes:
    :return:
    """
    return replace_data("V", variables, expression, attributes)


def replace_parameters(parameters, expression, attributes):
    """
    Replace parameters with value from data source.
    If the variable is not in the database, do not replace.
    :param parameters:
    :param expression:
    :param attributes:
    :return:
    """
    return replace_data("P", parameters, expression, attributes)


def replace_data(type: str, variables, expression, attributes):
    """
    Replace field/variables/parameter with value from respective source.
    If the variable is not found, do not replace.
    :param type:
    :param variables:
    :param expression:
    :param attributes:
    :return:
    """

    if type != "V" and type != "P":
        raise ValueError("Invalid type! Must be 'V' or 'P'!")

    regex_str = r"\$" + type + r"\{.*?\}"

    # Find all keys in specified expression
    new_keys = [
        key[key.find(f"${type}{{") + 3 : key.find("}")] for key in re.findall(regex_str, expression)
    ]

    for key in new_keys:
        var_str = f"${type}{{{key}}}"
        var_info = variables.get(key)
        data_value = var_str
        if var_info is not None:
            if isinstance(var_info, dict):
                data_type = var_info.get("class")

                if data_type == "java.lang.Integer":
                    data_value = str(var_info.get("value", var_str))
                elif data_type == "java.sql.Timestamp":
                    date_time = var_info.get("value", var_str)
                    data_value = date_time
                    if isinstance(date_time, datetime.datetime):
                        data_value = (
                            "datetime.datetime("
                            + str(date_time.year)
                            + ","
                            + str(date_time.month)
                            + ","
                            + str(date_time.day)
                            + ","
                            + str(date_time.hour)
                            + ","
                            + str(date_time.minute)
                            + ","
                            + str(date_time.second)
                            + ","
                            + str(date_time.microsecond)
                            + ","
                            + str(date_time.tzinfo)
                            + ")"
                        )
                else:
                    is_blank_when_null = convert2boolean(attributes.get("isBlankWhenNull"))
                    value = var_info.get("value", var_str)
                    if is_blank_when_null and value is None:
                        data_value = ""
                    else:
                        data_value = '"' + str(var_info.get("value", var_str)) + '"'
            elif isinstance(var_info, str):
                data_value = str(var_info)

        expression = expression.replace(var_str, data_value)
    return expression


def replace_text(report, expression, attributes):
    """
    Replace Field and Variables with values ($F{} and $V{}) and evaluate expression.
    :report: dictionary holding report information
    :param report: dictionary holding report information
    :param expression: text element to evaluate
    :param attributes: attributes of text element to output
    :return: evaluated expression ready for output
    """
    expression = replace_fields(report, expression=expression, attributes=attributes)
    if isinstance(expression, (bytes, memoryview)):
        return expression
    expression = replace_variables(report.get("variables"), expression, attributes)
    expression = replace_parameters(report.get("parameters"), expression, attributes)

    try:
        return eval(expression)
    except SyntaxError:
        return expression
    except NameError:
        return expression


def strip_fname(name):
    """
    strip wrapper (e.g. F${}, V${}, P${}) from name to get ID.
    :param name: string to strip
    :return: element name without wrapper text
    """
    return name[3:-1]


def convert2boolean(text):
    """
    Convert a string to a boolean type.
    :param text: text to convert to boolean
    :return: 'True' if text is 'true' (case ignored). 'False' otherwise.
    """
    return text is not None and text.lower() == "true"
