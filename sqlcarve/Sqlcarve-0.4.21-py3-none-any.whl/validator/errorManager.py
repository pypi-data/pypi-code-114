import logging

import colorama
from colorama import Fore

from sqlcarve.common.common_fr import *


class ErrorManager:
    list_of_syntaxe_error = []
    files_errors = []

    def add_errors_to_filename(self, file_name, errors_list):
        self.files_errors.append([file_name, errors_list])

    def add_errors_to_list(self, text_error):
        msg = get_error(text_error)
        self.list_of_syntaxe_error.append(msg)
        logging.debug(msg)

    def add_error_to_log(self):
        for err in self.list_of_syntaxe_error:
            logging.error(err)

    def get_list_errors(self):
        return self.list_of_syntaxe_error

    def get_files_errors(self):
        return self.files_errors

    def printError(name, lang):
        print("data[name]")

# def orderError(precedent_word, actual_word):
#     # selectErrors["orderError"] = "Ordre incorrect pour" + precedent_word + "et" + actual_word
#     print(Fore.RED + "Ordre incorrect pour " + precedent_word + " et " + actual_word + Fore.RESET)
#
# def wordsStmntError1():
#     # selectErrors["argsError1"] = "Attention! Absence de SELECT \n"
#     print(Fore.RED + "Attention! Absence de SELECT \n" + Fore.RESET)
#
# def wordsStmntError2(value):
#     # selectErrors["argsError2"] = "Attention! Absence de champs devant le mot " + value
#     print(Fore.RED + "Attention! Absence de champs devant le mot " + value + Fore.RESET)
#
# def argsError3(champs):
#     # selectErrors["argsError2"] = "Attention! Absence de champs devant le mot " + value
#     print(Fore.RED + "Attention! Absence d'une ponctuation dans " + champs + Fore.RESET)
#
# def argsError4():
#     # selectErrors["argsError2"] = "Attention! Absence de champs devant le mot " + value
#     print(Fore.RED + "Attention! Présence d'une virgule après le dernier champs de la sélection" + Fore.RESET)
#
# def argsError5(col_value):
#     colorama.init()
#     # selectErrors["argsError2"] = "Attention! Absence de champs devant le mot " + value
#     print(Fore.RED + "Erreur space in <" + col_value + ">" + Fore.RESET)
