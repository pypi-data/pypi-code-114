def mean(n1, n2):
    return (n1+n2)/2 

def select(n1, n2, how):
    if how == 'min':
        return min(n1, n2)
    if how == 'max':
        return max(n1, n2)