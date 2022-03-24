import typing as T
import json
import re
from devtools import debug


def query_variable_to_str(query_variable: T.Union[dict, T.List[dict]]) -> str:
    """
    INPUT(list[dict]|dict): [{"first_name":"Harry", "last_name": "Potter"}, {"first_name":"Ron", "last_name": "Weasley"}]
    OUTPUT (str): [{first_name: "Harry", last_name: "Potter"}, {first_name: "Ron", last_name: "Weasley"}]
    """
    # str everything
    # if root value (does not have a : directly infront of it), keep "". Otherwise, do not. Better yet, if has a ":" infront of it, remove the ""
    # pattern = r'[\w"\s]+:'
    pattern = r'(")([\w]+)(")(:)'
    return re.sub(pattern, r"\2\4", str(json.dumps(query_variable)))


def replace_query_variables_in_query_str(query_str: str, query_variables: dict) -> str:
    pattern = r"(\(\$[\w:\s\[!\]]+\))\s*({)"
    better_query_str = re.sub(pattern, r"\2", query_str)
    for key, val in query_variables.items():
        query_variable = query_variable_to_str(val)
        better_query_str = better_query_str.replace(f"${key}", query_variable)
    # print(f"{better_query_str=}")
    return better_query_str


"""
FROM
query_variables: {"data": [{"first_name":"Harry", "last_name": "Potter"}]}
mutation addPerson($data: [InsertPerson!]!) {
  insert_Person(data: $data) {
    id
  }
}
TO
mutation addPersonNoVar {
  insert_Person(data: [{first_name: "Harry", last_name: "Potter"}]) {
    id
  }
}
"""


def turn_set_remove_filter_ds_to_edgedb_ds(variables: dict) -> dict:
    """
    INPUT
    variables: {
        'set': {
            'title': 'New Titleman',
            'actors': {'id': '7ef21044-9fde-11ec-9407-bfe50cd00551'},
        },
        'remove': {'year': None},
        'filter': {
            'id': '663797f2-9fe0-11ec-99a0-3b9099c2b109',
        },
    }
    OUTPUT
    {
        'data': {
            'title': {'set': 'New Titleman'},
            'year': {'clear': True},
            'actors': {'set': [{'filter': {'id': {'eq': '7ef21044-9fde-11ec-9407-bfe50cd00551'}}}]}
        },
        'filter': {'id': {'eq': '663797f2-9fe0-11ec-99a0-3b9099c2b109'}}
    }
    """

    def turn_id_into_filter_id(input_d: dict) -> dict:
        """
        INPUT
        {
            "title": "New Titleman",
            "actors": {"id": "7ef21044-9fde-11ec-9407-bfe50cd00551"},
        }
        OUTPUT
        {
            "title": "New Titleman",
            "actors": {"filter": {"id": {"eq": "7ef21044-9fde-11ec-9407-bfe50cd00551"}}},
        }
        """
        output_d = {}
        for k, v in input_d.items():
            if type(v) is list:
                if v and type(v[0]) is dict and "id" in v[0]:
                    v = [{"filter": {"id": {"eq": i["id"]}}} for i in v]
            else:
                if type(v) is dict:
                    if m_id := v.get("id"):
                        v = {"filter": {"id": {"eq": m_id}}}
            output_d[k] = v
        return output_d

    new_d = {"data": {}}
    variables["set"] = turn_id_into_filter_id(input_d=variables["set"])
    variables["remove"] = turn_id_into_filter_id(input_d=variables["remove"])
    for key, val in variables["set"].items():
        if key not in new_d["data"]:
            new_d["data"][key] = {}
        existing_d = new_d["data"][key]
        existing_d["set"] = val
    for key, val in variables["remove"].items():
        if key not in new_d["data"]:
            new_d["data"][key] = {}
        existing_d = new_d["data"][key]
        if type(val) == dict and "filter" in val:
            existing_d["remove"] = val
        elif type(val) == list and "filter" in val[0]:
            existing_d["remove"] = val
        else:
            existing_d["clear"] = True
    model_id = variables["filter"]["id"]
    new_d["filter"] = {"id": {"eq": model_id}}
    return new_d


if __name__ == "__main__":
    """
    res = query_variable_to_str(
        query_variable=[
            {"first_name": "Harry", "last_name": "Potter"},
            {"first_name": "Ron", "last_name": "Weasley", "inner": {"hey": "yes"}},
        ]
    )
    print(f"{res=}")
    """
    variables = {
        "set": {
            "title": "New Titleman",
            "actors": [{"id": "7ef21044-9fde-11ec-9407-bfe50cd00551"}, {"id": "123"}],
        },
        "remove": {"year": None, "actors": {"id": "034"}},
        "filter": {
            "id": "663797f2-9fe0-11ec-99a0-3b9099c2b109",
        },
    }
    res = turn_set_remove_filter_ds_to_edgedb_ds(variables)
    debug(res)
