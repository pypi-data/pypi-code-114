# logic_puzzle_tools.py
import itertools


def logic_puzzle_setup ():
    '''
    Set up to solve a 'new' puzzle.
    It would not do to use an old dictionart cat_of
    '''
    global cat_of
    cat_of = dict()


def fails (v : bool) -> bool:
    '''
    A function to make the source more like the text of the problem.
    The tests can be stated like the problem and if they fail
    we continue with the next permutation.
    '''
    return not v


def permute (things : str, cat : list) -> list:
    '''
    Return a generator which gives new permutations of things.
    And map each element to the category cat
    '''
    things = things.replace(' ', '')            # spaces and tabs gone
    things = things.replace('\t', '')
    things = things.split(sep=',')              # need a list of things to permute
                                                # exiting a choose function and
                                                # reentering later means false duplicates
    for n in things:                            # name to category
        cat_of[n] = cat
    return itertools.permutations(things)


def category (cat : list, permutation : list):
    '''
    Assign all the things in the list permutation to the category cat.
    It can not be assigned as cat = permutation. 'cat' is a category and
    is global thier exist references to it else where. To break cat's reference
    and make it refer to a permutation would invalidate all the other
    references. So we change each element in the reference instead.
    '''
    for i in range(len(permutation)):
        cat[i] = permutation[i]


def fixed_cat (cat: list) -> None:
    '''
    The category cat is fixed and will not be allowed to change.
    All we do is map the elements to the fixed cat.
    '''
    for n in cat:
        assert n not in cat_of, f"{n} cannot be put in two categories, fixed_cat"
        cat_of[n] = cat


def set_difference (one:list, two:list) -> list:
    '''
    return a list of elements in only one, but not both
    '''
    L = list()
    for i in one:
        if i not in two:
            L.append(i)
    return L


def is_associated (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 associated with arg2 in list2.
    That is has the same index j e.g. arg1==list1[j] and arg2==list2[j]
    '''
    list1 = cat_of[arg1]
    list2 = cat_of[arg2]
    indx1 = list1.index(arg1)
    indx2 = list2.index(arg2)
    return indx1 == indx2


def is_not_associated (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is not associated with arg2 in list2.
    That is there is no j in range(len(list1))
    e.g. arg1 == list1[j] and arg2 == list2[j]
    '''
    list1 = cat_of[arg1]
    list2 = cat_of[arg2]
    indx1 = list1.index(arg1)
    indx2 = list2.index(arg2)
    return indx1 != indx2


def is_just_left_of (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is immeadiatly before arg2 in list2. e.g.
    there exists a j so arg1 == list1[j] and arg2 == list2[j+1]
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return (indx1 + 1) == indx2


def is_just_right_of (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is immeadiatly after arg2 in list2. e.g.
    there exists a j so arg1 == list1[j+1] and arg2 == list2[j]
    '''
    return is_just_left_of(arg2, arg1)


def is_just_above (arg1 : str, arg2 : str) -> bool:
    ''' AKA is_just_right_of. The thought pattern is just up to down
    and not right to left.'''
    return is_just_right_of(arg1, arg2)


def is_just_below (arg1 : str, arg2 : str) -> bool:
    ''' AKA is_just_left_of. The thought pattern is just up to down
    and not right to left.'''
    return is_just_left_of(arg1, arg2)


def is_below (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is below/leftof arg2 in list2. e.g.
    there exist i,j i < j so arg1== list1[i] and arg2 == list2[j]
    '''
    idex1 = idx(arg1)
    idex2 = idx(arg2)
    return idex1 < idex2


def is_above (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is above/righttof arg2 in list2. e.g.
    there exist i,j i > j so arg1== list1[i] and arg2 == list2[j]
    '''
    idex1 = idx(arg1)
    idex2 = idx(arg2)
    return idex1 > idex2


def is_adjacent_to (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is_just_below arg2 in list2 or
    arg1 in list1 is_just_above arg2 in list2
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return abs(indx2 - indx1) == 1


def is_not_adjacent_to (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 is not adjacent to arg2 in list2 e.g.
    there is no value for i for which arg1==list1[i] and arg2==list2[i+1] and also
    arg1==list1[i+1] and arg2==list2[i]
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return abs(indx2 - indx1) != 1


def after (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 coming after arg2 in list2. e.g.
    there are no i,j such that i > j and arg1==list1[i] and arg2==list2[j]
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return indx1 > indx2


def before (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 coming before arg2 in list2. e.g.
    there are no i,j such that i < j and arg1==list1[i] and arg2==list2[j]
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return indx1 < indx2


def just_after (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 coming just after arg2 in list2. e.g.
    there exists an i such that arg1==list1[i+1] and arg2==list2[i]
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return indx1 == (indx2 + 1)


def just_before (arg1 : str, arg2 : str) -> bool:
    '''
    return the truth of arg1 in list1 coming just before arg2 in list2. e.g.
    there exists an i such that arg1==list1[i] and arg2==list2[i+1]
    '''
    indx1 = idx(arg1)
    indx2 = idx(arg2)
    return (indx1 + 1) == indx2


def idx (element : str) -> int:
    '''
    return where in listset element is to be found.
    '''
    cat = cat_of[element]
    if element in cat:
        return cat.index(element)
    return None


def PrintSolution (fmt_str, *ListSet):
    '''
    print one line for each element of solution ListSet[0]
    such that line i (i in range(len(ListSet[0]))) has the i th
    element of each ordered group of things.
    use fmt_str as guidance as to how they are to printed.
    '''
    nSets = len(ListSet)
    Len = len(ListSet[0])
    for i in range(Len):
        itemlist = list()
        for j in range(nSets):
            itemlist.append(ListSet[j][i])
        print(fmt_str % tuple(itemlist))

logic_puzzle_setup()
