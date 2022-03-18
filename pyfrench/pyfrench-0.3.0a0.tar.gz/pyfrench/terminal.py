from os import *
from pyfrench import couleur

def write(commande: str):
    """Effectue une commande  dans un terminal."""
    print(couleur.GRAS + couleur.VERT + "[pyfrench]" + couleur.FIN + couleur.GRAS + " -> {}".format(commande) + couleur.FIN)
    return system(commande)