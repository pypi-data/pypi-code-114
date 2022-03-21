# -*- coding: utf-8 -*-


def _get_zi_index(zi, text):
    res = []
    index = text.find(zi)
    while index != -1:
        res.append(index)
        text = text.replace(zi, "*", 1)
        index = text.find(zi)
    return res


def solve_index_drift(original_text, processed_text, processed_listitem_index: list):
    original_listitem_index = []
    for listitem, index in processed_listitem_index:
        zi = listitem[0]
        zi_index_processed_text = _get_zi_index(zi, processed_text)
        if index in zi_index_processed_text:
            zi_relative_position = zi_index_processed_text.index(index)
            # print(zi_relative_position)
        zi_index_original_text = _get_zi_index(zi, original_text)
        original_index = zi_index_original_text[zi_relative_position]
        original_listitem_index.append([listitem, original_index])
    return original_listitem_index
