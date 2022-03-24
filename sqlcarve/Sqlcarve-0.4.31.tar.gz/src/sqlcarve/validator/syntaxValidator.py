import sqlvalidator
from sqlparse.sql import Where, IdentifierList, Identifier, Comparison, Function
from sqlparse.tokens import Keyword, DML, Wildcard, Whitespace, Newline
# from sqlvalidator.grammar.lexer import ExpressionParser
# from sqlvalidator.grammar.sql import Alias
# from sqlvalidator.grammar.tokeniser import to_tokens

from sqlcarve.validator.helpers import *
from sqlcarve.validator.errorManager import *


class SyntaxValidator:

    def __init__(self):
        self.helper = Preprocessor()
        self.syntaxe_error = ErrorManager()
        self.get_fquery_valid = []
        self.etat = False

    def is_valid(self) -> bool:
        return self.etat

    """

    validateQueryDemo:
    -------------
    Description: Fonction permettant de valider les requetes du dossier Demo

    Entrée: Liste de requetes
    Sortie: Affiche erreur, s'il y a lieu

    """

    def validateQueryDemo(self, statement):
        # for queries in stmtList:
        #     stmt = queries[0]
        #     # print(stmtList.index(queries), stmt)
        #     log.info(stmtList.index(queries), stmt)
        #     query_f = sqlvalidator.parse(queries[1])
        #     get_fquery_valid.append(query_f)
        #
        #     try:
        #
        #         if not query_f.is_valid():
        #             print(query_f.errors)
        #     except NameError:
        #         print()
        #
        #     print(stmtList.index(queries), stmt)
        #     log.info(statement)
        #
        #     get_fquery_valid.append(query_f)

        try:

            log.debug(statement)
            query_f = sqlvalidator.parse(statement)

            log.debug("here")
            log.debug(query_f)
            if query_f.is_valid():
                self.etat = True
                print("here")

        except query_f.errors:
            print(query_f.errors)

    # """
    #
    # validateQueryProblemes:
    # -------------
    # Description: Fonction permettant de valider les requetes du dossier Probleme
    #
    # Entrée: Liste de requetes
    # Sortie: Affiche erreur, s'il y a lieu
    #
    # """
    #
    #
    # def validateQueryProblemes(stmtList):
    #     for queries in stmtList:
    #         stmt = queries[0]
    #         # print(stmtList.index(queries), stmt)
    #         log.info(stmtList.index(queries), stmt)
    #         query_f = sqlvalidator.parse(queries[1])
    #         get_fquery_valid.append(query_f)
    #         if not query_f.is_valid():
    #             print(query_f.errors)

    """

    validate_query_exercices:
    -------------
    Description: Fonction permettant de valider les requetes dans le dossier exercices

    Entrée: Liste de requetes contenu dans chaque fichier

    """

    def validate_syntax(self, statement):

        # self.validateQueryDemo(statement)

        self.helper.process_parsing(statement)
        for stmnt in self.helper.get_queries_parsed():
            self.validate_query_exercices(stmnt[1])

        if len(self.syntaxe_error.get_list_errors()) == 0:
            self.etat = True

            return get_error("syntaxIsValid")
        else:
            # self.syntaxe_error.add_error_to_log()
            return get_error("errorInValidations")

    """

    validate_query_exercices:
    -------------
    Description: Fonction permettant de valider les requetes dans le dossier exercices

    Entrée: Liste de requetes contenu dans chaque fichier

    """

    def validate_query_exercices(self, statement):

        # log.info("\n" + file_name)
        self.check_words_stmnt(statement)

        # stmnt_error_list = self.syntaxe_error.get_list_errors()
        # # self.syntaxe_error.add_errors_to_filename(file_name, sample_list)
        # if len(stmnt_error_list) == 0:
        #     self.etat = True

    """

    check_words_stmnt:
    -------------
    Description: Fonction permettant de vérifier chaque mot cle dans une requete

    Entrée: Requete à vérifier
    Sortie: Affiche erreur s'il y a lieu

    """

    def check_words_stmnt(self, requete):
        statement = []
        if str(requete[0]).upper() != "SELECT":
            self.syntaxe_error.add_errors_to_list("wordsStmntError1")
        else:
            precedent_word = ""

            for element in requete:
                if element.ttype is not Whitespace and (element.ttype is not Newline):
                    statement.append(element)

            for i in range(len(statement)):
                value = str(statement[i].value)

                if statement[i].ttype is DML:
                    log.info("SELECT clause")

                    self.check_keyword_order(precedent_word, value)
                    precedent_word = value
                    if i + 1 < len(statement) and (
                            statement[i + 1].ttype is Wildcard or statement[i + 1].value.isnumeric() or isinstance(
                        statement[i + 1], IdentifierList) or isinstance(statement[i + 1], Identifier)):
                        self.check_args(statement[i + 1])
                    else:
                        self.syntaxe_error.add_errors_to_list("wordsStmntError2")
                        log.info(statement[i + 1].ttype)
                elif statement[i].ttype is Keyword:
                    log.info(value + " clause")

                    self.check_keyword_order(precedent_word, value)
                    precedent_word = value

                    if i + 2 < len(statement) and (statement[i + 1].value.isnumeric()
                                                   or isinstance(statement[i + 1], IdentifierList)
                                                   or isinstance(statement[i + 1], Identifier)
                                                   or isinstance(statement[i + 1], Function)
                                                   or isinstance(statement[i + 1], Comparison)):
                        rest = statement[i + 1].value
                        sub_query_position_start = rest.upper().find("(SELECT")
                        sub_query_position_end = rest.upper().find(")", sub_query_position_start)
                        if sub_query_position_start != -1 and sub_query_position_end != -1:
                            sub_query = rest[sub_query_position_start + 1:sub_query_position_end]
                            log.info("\nSub-query")

                            self.helper.process_parsing(sub_query)
                            for statement in self.helper.get_queries_parsed():
                                self.validate_query_exercices(statement[1])
                            log.info("End of Sub-query\n")
                        else:
                            if isinstance(statement[i + 1], Comparison):
                                log.debug(statement[i + 1].value)
                                self.check_join(statement[i + 1])
                            else:
                                self.check_args(statement[i + 1])
                    else:
                        self.syntaxe_error.add_errors_to_list("wordsStmntError2")

                elif isinstance(statement[i], Where):
                    log.info("WHERE clause")
                    self.check_keyword_order(precedent_word, value)
                    precedent_word = value
                    if len(value) < 7:
                        self.syntaxe_error.add_errors_to_list("wordsStmntError2")
                    else:
                        rest = value[6:]
                        sub_query_position_start = rest.upper().find("(SELECT")
                        sub_query_position_end = rest.upper().find(")", sub_query_position_start)

                        if sub_query_position_start != -1 and sub_query_position_end != -1:
                            sub_query = rest[sub_query_position_start + 1:sub_query_position_end]
                            log.info("\nSub-query")

                            self.helper.process_parsing(sub_query)
                            for statement in self.helper.get_queries_parsed():
                                self.validate_query_exercices(statement[1])
                            log.info("End of Sub-query\n")

                        postion_LIKE = rest.upper().find("LIKE")
                        if postion_LIKE != -1:
                            log.info("LIKE clause")
                            part_LIKE = rest[postion_LIKE:]
                            if len(part_LIKE) < 6:
                                self.syntaxe_error.add_errors_to_list("wordsStmntError2")

            log.info(statement)

    """

    check_keyword_order:
    -------------
    Description: Fonction permettant de vérifier l'ordre des mots cle dans une requete

    Entrée1: Precedent mot cle
    Entrée2: Actuel mot cle
    Sortie: Affiche erreur s'il y a lieu

    """

    def check_keyword_order(self, precedent_word, actual_word):
        log.info("Check order process")
        if precedent_word.upper() == "SELECT" and (actual_word.upper() != "DISTINCT"
                                                   and actual_word.upper() != "FROM"):
            self.syntaxe_error.add_errors_to_list("orderError")

        elif precedent_word.upper() == "DISTINCT" and (actual_word.upper() != "FROM"):
            self.syntaxe_error.add_errors_to_list("orderError")

        elif precedent_word.upper() == "FROM" and (actual_word.upper() != "SELECT"
                                                   and actual_word.upper() != "JOIN"
                                                   and actual_word.upper() != "LEFT JOIN"
                                                   and actual_word.upper() != "RIGHT JOIN"
                                                   and actual_word.upper() != "INNER JOIN"
                                                   and actual_word.upper()[:5] != "WHERE"
                                                   and actual_word.upper() != "ORDER BY"
                                                   and actual_word.upper() != "GROUP BY"
                                                   and actual_word.upper() != ""):
            self.syntaxe_error.add_errors_to_list("orderError")

        elif precedent_word.upper() == "JOIN" and (actual_word.upper() != "ON"):
            self.syntaxe_error.add_errors_to_list("missON")

        elif precedent_word.upper() == "RIGTH JOIN" and (actual_word.upper() != "ON"):
            self.syntaxe_error.add_errors_to_list("missON")

        elif precedent_word.upper() == "LEFT JOIN" and (actual_word.upper() != "ON"):
            self.syntaxe_error.add_errors_to_list("missON")

        elif precedent_word.upper() == "INNER JOIN" and (actual_word.upper() != "ON"):
            self.syntaxe_error.add_errors_to_list("missON")

        elif precedent_word.upper() == "WHERE" and (actual_word.upper() != "SELECT"
                                                    and actual_word.upper() != "ORDER BY"
                                                    and actual_word.upper() != "GROUP BY"
                                                    and actual_word.upper() != ""):
            self.syntaxe_error.add_errors_to_list("orderError")

        elif precedent_word.upper() == "GROUP BY" and (actual_word.upper() != "HAVING"
                                                       and actual_word.upper() != "ORDER BY"
                                                       and actual_word.upper() != ""):
            self.syntaxe_error.add_errors_to_list("orderError")

        elif precedent_word.upper() == "HAVING" and (actual_word.upper() != "ORDER BY"
                                                     and actual_word.upper() != "AND"
                                                     and actual_word.upper() != "OR"
                                                     and actual_word.upper() != ""):
            self.syntaxe_error.add_errors_to_list("orderError")

        elif precedent_word.upper() == "ORDER BY" and (actual_word.upper() != ""):
            self.syntaxe_error.add_errors_to_list("orderError")

    """

    check_args:
    -------------
    Description: Fonction permettant de vérifier les arguments devant un mot cle

    Entrée: liste d'arguments
    Sortie: Affiche erreur s'il y a lieu

    """

    def check_args(self, arguments):
        colorama.init()
        if type(arguments.value) is Identifier:
            log.info("----Identifier----")
            self.check_identifier(arguments)
        elif type(arguments) is IdentifierList:
            log.info("----IdentifierList----")
            for element in arguments:
                if len(element.value) != 1:
                    self.check_identifier(element.value)

            if arguments[0].value[0] == ",":
                self.syntaxe_error.add_errors_to_list("argsError1")
            elif arguments[-1].value[-1] == ",":
                log.info(arguments[-1].value)
                self.syntaxe_error.add_errors_to_list("argsError2")
        else:
            log.info("----Other----")

    def check_identifier(self, col_value):
        col_value = col_value.replace('\n', ' ')
        col_value = col_value.replace('\t', ' ')
        log.debug(col_value)

        up_as = col_value.find(" AS ")
        if up_as != -1:
            before_as = col_value[:up_as]
            log.debug(before_as)
            # self.check_column_value(before_as)

            if self.helper.space_exist(before_as):
                self.syntaxe_error.add_errors_to_list("caractsError")
            else:
                self.check_alias(col_value, up_as + 1)

        elif col_value.find(" DESC") == -1 and col_value.find(" ASC") == -1:
            if self.helper.space_exist(col_value):
                self.syntaxe_error.add_errors_to_list("caractsError")
        else:
            self.check_column_value(col_value)

    def check_column_value(self, column):

        column_part = column.split(".")
        # for part, caract in column_part, specials_caracts:
        for part in column_part:
            if part.find("`") != -1:
                if part.count("`") != 2 or part[0] != "`" or part[-1] != "`":
                    self.syntaxe_error.add_errors_to_list("caractsError")

        # if column.find("``") != -1:
        #     self.syntaxe_error.add_errors_to_list("argsError3")

    def check_alias(self, column, up_as):

        x = up_as

        sub_txt = column[x:]
        without_as = sub_txt.strip("AS ")

        pos_all_next_keyword = self.helper.keywords_exist(without_as)

        if len(pos_all_next_keyword) != 0:
            pos_all_next_keyword.sort()
            pos_first_word = pos_all_next_keyword[0]
            first_word_start = pos_first_word[0]
            if first_word_start == 0:
                log.debug("incomplete AS")
                self.syntaxe_error.add_errors_to_list("wordsStmntError2")
            else:
                alias_name = without_as[:first_word_start]
                if self.helper.space_exist(alias_name):
                    self.syntaxe_error.add_errors_to_list("caractsError")
        else:
            if self.helper.space_exist(without_as):
                self.syntaxe_error.add_errors_to_list("caractsError")

    def check_join(self, element):
        comparision_value = element.value

        if comparision_value.count("=") != 1:
            self.syntaxe_error.add_errors_to_list("comparisionError")
        else:
            comparision_part = comparision_value.split("=")

            for part in comparision_part:
                self.check_identifier(part.strip())
