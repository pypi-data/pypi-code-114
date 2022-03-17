from typing import Any
from typing import Dict


def render_data_sources(hub, detector_describe: Dict[str, Any]) -> Dict[str, Any]:
    """
    The syntax for data_sources parameter is different in create and update scenarios. So to make it similar we are
    rendering the data  so that it can be used in update and describe functions.

    Returns:
        Dict

    """
    data_sources_new = {}
    if detector_describe.get("DataSources"):
        data_sources_new.update(detector_describe.get("DataSources"))
        for key, val in data_sources_new.items():
            if val["Status"] == "ENABLED":
                data_sources_new[key] = {"Enable": True}
            else:
                data_sources_new[key] = {"Enable": False}
    return data_sources_new


def compare_dicts(hub, data_sources: Dict[str, Any], data_sources_new: Dict[str, Any]):
    """
    This functions helps in comparing two dicts.
    It compares each key value in both the dicts and return true or false based on the comparison

    Returns:
        {True|False}

    """

    for key, value in data_sources.items():
        if key in data_sources_new:
            if isinstance(data_sources[key], dict):
                if not compare_dicts(hub, data_sources[key], data_sources_new[key]):
                    return False
            elif value != data_sources_new[key]:
                return False
        else:
            return False
    return True
