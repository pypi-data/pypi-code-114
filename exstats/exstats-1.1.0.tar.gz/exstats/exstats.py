# Checking if numbers are odd.
def odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# Getting the median (Middle most item in a sorted list, also works for strings)
def median(ls):
    if odd(len(ls)):
        return ls[len(ls)//2]
    else:
        return (ls[len(ls)//2-1] + ls[len(ls)//2])/2

def quartileList(ls):
    if odd(len(ls)):
        medianPlace = (len(ls) + 1) / 2
        q1List = ls[:int(medianPlace -1)]
        q3List = ls[-int(medianPlace -1):]
    else:
        q1List = ls[:len(ls)//2]
        q3List = ls[len(ls)//2:]
    
    return q1List, q3List

def quartiles(ls):
    q1 = median(quartileList(ls)[0])
    q3 = median(quartileList(ls)[1])
    
    return q1, q3
def iqr(ls):
    iqr = quartiles(ls)[1] - quartiles(ls)[0]
    return iqr

def mode(ls):
    mode = max(set(ls), key = ls.count)
    return mode

def mean(ls):
    mean = sum(ls) / len(ls)
    return mean



