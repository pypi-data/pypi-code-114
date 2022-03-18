from math import *

def calcul(calcul: str):
    """Effectue un calcul."""
    return print(int(eval(calcul)))
def nombreNonDuplique(liste: list):
    """Trouve le nombre non dupliqué dans une liste."""
    resultat = 0
    for e in liste:
        resultat ^= e
    return resultat
def num(nombre: str):
    """Convertit un nombre textuel en nombre entier."""
    return int(nombre)
def txt(nombre: int):
    """Convertit un nombre entier en nombre texutel."""
    return str(nombre)
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679