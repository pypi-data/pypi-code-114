def bin2(x):
    if not isinstance(x, int):
        raise TypeError("Not an 'int': bin2() accepts only integer.")
    bits = x.bit_length() + 1
    n = (1 << bits) - 1
    x = n & x
    return f"{x:#0{bits + 2}b}"

if __name__ == '__main__':
    print(" 5's binnary form is {}".format(bin2(5)))
    print("-5's binnary form is {}".format(bin2(-5)))
    print("2.3's binnaryform is {}".format(bin2(2.3)))

