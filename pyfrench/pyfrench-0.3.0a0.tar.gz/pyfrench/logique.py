def égale(valeur1: int, valeur2: int):
    """Retourne une valeur booléen si les deux valeurs sont égaux."""
    if valeur1 == valeur2:
        return True
    else:
        return False
def différentDe(valeur1: int, valeur2: int):
    """Retourne une valeur booléen si les deux valeurs sont différentes."""
    if valeur1 != valeur2:
        return True
    else:
        return False
def plusGrand(valeur1: int, valeur2: int):
    """Retourne une valeur booléen si la première valeur est plus grande que la deuxième."""
    if valeur1 > valeur2:
        return True
    else:
        return False
def plusPetit(valeur1: int, valeur2: int):
    """Retourne une valeur booléen si la première valeur est plus petite que la deuxième."""
    if valeur1 < valeur2:
        return True
    else:
        return False 
def égalePlusGrand(valeur1: int, valeur2: int):
    """Retourne une valeur booléen si la première valeur est égale ou plus grande que la deuxième."""
    if valeur1 >= valeur2:
        return True
    else:
        return False
def égalePlusPetit(valeur1: int, valeur2: int):
    """Retourne une valeur booléen si la première valeur est égale ou plus petit que la deuxième."""
    if valeur1 <= valeur2:
        return True
    else:
        return False
def AND(A: int, B: int):
    """Porte logique AND"""
    return A & B
def NOT(A: int):
    """Porte logique NOT"""
    return ~A+2
def XOR(x: int, y: int):
    """Porte logique XOR"""
    return bool((x and not y) or (not x and y))
def NAND(A: int, B: int):
    """Porte logique NAND"""
    return NOT(AND(A, B))
def OR(A: int, B: int):
    """Porte logique OR"""
    return A | B
def NOR(A: int, B: int):
    """Porte logique NOR"""
    return NOT(OR(A, B))
def XNOR(A: int, B: int):
    """Porte logique XNOR"""
    return NOT(XOR(A, B))