import re


def _get_pattern(prefix: str, suffix: str) -> str:
    return prefix + '([0-9]+)' + suffix + '$'


def _get_str_number_list(pattern: str, strings_to_match: list) -> list:
    r = re.compile(pattern)
    matches = list(map(r.findall, strings_to_match))
    matches_filtered = list(filter(lambda x: len(x) is not 0, matches))
    str_number_list = [match[0] for match in matches_filtered]
    return str_number_list


def _get_number_list(pattern: str, strings_to_match: list) -> list:
    matches_filtered = _get_str_number_list(pattern, strings_to_match)
    number_list = [int(match) for match in matches_filtered]
    return number_list
