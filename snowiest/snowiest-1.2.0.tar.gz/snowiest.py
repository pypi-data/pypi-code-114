"""提供print_lol（）函数,
作用是打印列表，支持打印嵌套列表"""


def print_lol(the_list, level=0):
    """这个函数取the_list为一个位置参数，
    可以是任何python列表，包含嵌套列表"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)
