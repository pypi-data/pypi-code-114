"""
Script for various tasks:
1. Upload single celex into the celex_manager application.
"""
from eurlex2lexparency.celex_manager.eurlex import PreLegalContentXmlDataBase, query_templates, \
    multi_celex_query


def get_single_celex(celex):
    lcxdb = PreLegalContentXmlDataBase()
    lcxdb.pull_all_hits(query_templates['celex_wild_card'].format(celex))


def get_list_of_celexes(celexes):
    lcxdb = PreLegalContentXmlDataBase()
    lcxdb.pull_all_hits(multi_celex_query(celexes))


if __name__ == '__main__':
    # get_list_of_celexes(('32006R0865',))
    get_single_celex('52021PC0206')
    # for suffix in ('20151129', '20160430', '20170615'):
    #     get_single_celex(f'02012R0531-{suffix}')
