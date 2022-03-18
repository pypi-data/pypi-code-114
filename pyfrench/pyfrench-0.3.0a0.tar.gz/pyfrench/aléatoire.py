import random

def choisit(liste: list):
    """Choisit un objet dans une liste."""
    return random.choice(liste)
def choisitEntre(nombre1: int, nombre2: int):
    """Choisit un nombre entier entre deux certain nombres."""
    return random.randint(nombre1, nombre2)