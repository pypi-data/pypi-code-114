import json
import pkg_resources

TYPE_ERROR = "El campo de consulta debe ser del tipo str"


def set_file_path():
    file_path = pkg_resources.resource_stream(__name__, 'currency.json')
    with open(file_path.name, encoding="utf-8") as file:
        data = json.load(file)
    file.close()
    return data


def return_data(data, param, value):
    data_list = []
    if value:
        country_currency = {}
        for i in data:
            if i[param].lower() == value.lower():
                country_currency['position'] = i['position']
                country_currency['code'] = i['code']
                country_currency['country'] = i['country']
                country_currency['currency'] = i['currency']
                country_currency['decimals'] = i['decimals']
                data_list.append(country_currency)
                country_currency = {}
    return data_list


def verify_field_str(value):
    return True if type(value) == str else False


def search_by(concept, value):
    data = set_file_path()
    if verify_field_str(value):
        try:
            data = return_data(data, concept, value)
        except:
            data = f"No se encontraron divisas con el valor {value}"
        return data
    else:
        return(TYPE_ERROR)


def search_by_code(value):
    return search_by("code", value)


def search_by_country(value):
    return search_by("country", value)


def search_by_currency(value):
    return search_by("currency", value)


def search_decimals(value):
    data = set_file_path()
    if verify_field_str(value):
        data_list = return_data(data, "code", value)
        try:
            data = int(data_list[0]['decimals'])
        except:
            data = f"No se encontraron divisas con el valor {value}"
        return data
    else:
        return(TYPE_ERROR)


def show_list():
    return set_file_path()
