"""
Modul Pertama
def nested_item(data, indent=False, level=0):
        for each_item in data:
                if isinstance(each_item, list):
                        nested_item(each_item, indent, level+1)
                else:
                        if indent:
                                for tab_stop in range(level):
                                        print("\t", end='')
                        print(each_item);"""

"""
Penambahan Parameter Keempat Untuk Standar Output
"""
import sys

def nested_item(data, indent=False, level=0, fh=sys.stdout):
        for each_item in data:
                if isinstance(each_item, list):
                        nested_item(each_item, indent, level+1, fh)
                else:
                        if indent:
                                for tab_stop in range(level):
                                        print("\t", end='', file=fh)
                        print(each_item, file=fh);
