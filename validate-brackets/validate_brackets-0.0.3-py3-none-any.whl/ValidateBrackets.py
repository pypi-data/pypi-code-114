def validate_brackets(str):
    l1 = []
    d1 = {')': '(', ']': '[', '}': '{'}
    try:
        for s in str:
            if s in d1.values():
                l1.append(s)

            elif s in d1.keys():
                if d1.get(s) == l1[-1]:
                    l1.pop()
                else:
                    return False
            else:
                pass
    except IndexError:
        return False
    return True
