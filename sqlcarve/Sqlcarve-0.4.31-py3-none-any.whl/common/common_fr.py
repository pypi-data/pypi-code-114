selectErrors = {"orderError": "Inversion de l'ordre des mots clés SQL dans la requête (ex. ORDER BY avant GROUP BY)",
                "wordsStmntError1": "Absence du mot clé SELECT",
                "wordsStmntError2": "Absence de champs devant un ou plusieurs mot(s) clé de la requête",
                "argsError1": "Présence d'une virgule avant le premier champs champs de la sélection (souvent dû au copier-coller)",
                "argsError2": "Présence d'une virgule après le dernier champs de la sélection (souvent dû au copier-coller)",
                "argsError3": "Absence d'une virgule après un champs dans la sélection (souvent dû au copier-coller)",
                "caractsError": "Utilisation d'un nom de champs ou un alias contenant un caractère spécial (ex. espace) sans gestion de chaîne.",
                "error7": "Utilisation des caractères définissant un object plutôt qu'une chaîne et vice-versa (ex. MySQL utilise les caractères objet et 'chaîne')",
                "missON": "Absence de certains mots clés requis lors d'opération spécifique (ex. ON dans un JOIN)",
                "error9": "Utilisation des mots clés d'un autre dialecte que celui identifié (ex. TOP/LIMIT)",
                "syntaxIsValid": "Validation syntaxique réussie",
                "semanticIsValid": "Validation sémantique réussie",
                "comparisionError": "Mauvaise utilisation de l'égalité dans la comparaison qui suit le ON",
                "commentIsValid": "JCDSJBCIS",
                "noHeadComment": "No header comment found.",
                "noComments":"",
                "errorInValidations": "Erreur : vérifier le fichier trace.log",
                "debug": "Tran",
                "sbxjksb": "Erreur : vérifier le fichier trace.log",
                "hksbhkbdxhs": "Tran",
                "snbxjsbk": "Erreur : vérifier le fichier trace.log"
                }


def get_error(erroType):
    return selectErrors[erroType]

# print(getError("error13"))
