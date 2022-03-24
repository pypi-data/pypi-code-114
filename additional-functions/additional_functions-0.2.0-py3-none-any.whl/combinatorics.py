def permutations(n, k):

    def factorial(n):
        if n == 0: return 1
        else: return n * factorial(n - 1)

    return int(factorial(n) / factorial(n - k))
    
def combinations(n, k):

    def factorial(n):
        if n == 0: return 1
        else: return n * factorial(n - 1)

    return int(factorial(n) / (factorial(k) * factorial(n - k)))