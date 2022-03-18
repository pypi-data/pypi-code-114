from pyfrench import couleur, terminal, logique, maths

Vrai = True
Faux = False

def afficher(texte: str):
    """Écrit du texte dans le terminal."""
    return print(str(texte) + couleur.FIN)
def demander(question: str, nom: str = None):
    """Écrit du texte posée en forme de question."""
    if nom == None:
        nom = 'Vous'
    return input('{}\n{}: '.format(question, nom) + couleur.FIN)

# Condition
def si(valeur: bool):
    """Retourne une valeur booléen."""
    return valeur
def replacePar(texte: str, caractère1: str, caractère2: str):
    """Remplace un caractère par un autre dans un texte."""
    return texte.replace(caractère1, caractère2)

def commencePar(texte: str, mot: str):
    """Retourne une valeur boolén si un texte commence par un certain mot."""
    return texte.startswith(mot)
def finitPar(texte: str, mot: str):
    """Retourne une valeur booléen si un texte finit par un certain mot."""
    return texte.endswith(mot)

# Fichier
def ouvrir(fichier: str):
    """Ouvre des fichiers"""
    return open(file=fichier)

# Lien
def google(recherche: str):
    """Effectue une recherche Google"""
    resutlat = recherche.replace("+", "%2B")
    return f'https://www.google.com/search?q={resutlat.replace(" ", "+")}'
def youtube(recherche: str):
    """Effectue une recherche YouTube"""
    return f'https://www.youtube.com/watch?v={recherche}'