import zipfile

import sqlparse as parse
from sqlcarve.validator.parser import SqlParser
import logging as log
import sqlvalidator
import json

FORMAT = '%(asctime)s : %(message)s'
# formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
#                               "%Y-%m-%d %H:%M:%S")

log.basicConfig(format=FORMAT, filename='trace.log', encoding='utf-8', level=log.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')


class Preprocessor:
    sql_stmnts = []
    queries_parsed = []
    query_parsed = []
    to_execute = []
    file_comments = ""

    sql_keywords = (
        "ADD", "ADD CONSTRAINT", "ALL", "ALTER", "ALTER COLUMN", "ALTER TABLE", "AND", "ANY", "AS", "BACKUP DATABASE",
        "BETWEEN", "CASE", "CHECK", "COLUMN", "CONSTRAINT", "CREATE", "CREATE DATABASE", "CREATE INDEX",
        "CREATE OR REPLACE VIEW", "CREATE TABLE", "CREATE PROCEDURE", "CREATE UNIQUE INDEX", "CREATE VIEW", "DATABASE",
        "DEFAULT", "DELETE, DESC", "DISTINCT", "DROP", "DROP COLUMN", "DROP CONSTRAINT", "DROP DATABASE",
        "DROP DEFAULT",
        "DROP INDEX", "DROP TABLE", "DROP VIEW", "EXEC", "EXISTS", "FOREIGN KEY", "FROM", "FULL OUTER JOIN", "GROUP BY",
        "HAVING", "IN", "INDEX", "INNER JOIN", "INSERT INTO", "INSERT INTO SELECT", "IS NULL", "IS NOT NULL", "JOIN",
        "LEFT JOIN", "LIKE", "LIMIT", "NOT", "NOT NULL", "OR", "ORDER BY", "OUTER JOIN", "PRIMARY KEY", "PROCEDURE",
        "RIGHT JOIN", "ROWNUM", "SELECT", "SELECT DISTINCT", "SELECT INTO", "SELECT TOP", "SET", "TABLE", "TOP",
        "TRUNCATE TABLE", "UNION", "UNION ALL", "UNIQUE", "UPDATE", "VALUES", "VIEW", "WHERE")
    select_keywords = (
        "SELECT", "DISTINCT", "FROM", "JOIN", "RIGTH JOIN", "LEFT JOIN", "INNER JOIN", "WHERE", "ORDER BY", "GROUP BY",
        "HAVING", "AND", "OR")

    def keywords_exist(self, without_as):
        pos_all_next_keyword = []
        for word in self.select_keywords:
            pos_next_keyword = without_as.find(word)
            if pos_next_keyword != -1:
                pos_all_next_keyword.append([pos_next_keyword, len(word)])

        return pos_all_next_keyword

    def space_exist(self, to_check):
        if to_check.find(' ') != -1:
            return True
        else:
            return False

    def remove_comments(self, statement):
        return parse.format(statement, strip_comments=True, reindent=True)

    # def extract_comments(self, file_contents_comments, referencefile):
    #     f_contents_comments = file_contents_comments
    #     f_contents_comments = parse.format(f_contents_comments, strip_comments=False, reindent=True)
    #
    #     stmnt_comment_list = parse.split(f_contents_comments)
    #
    #     if len(stmnt_comment_list) != 0:
    #         for stmt in stmnt_comment_list:
    #             comment = CommentsValidator()
    #             # lisbdjcb = comment.get_comment_element(stmt)
    #
    #             comment.validate_comment(stmt, referencefile)
    #             print('\n')

    @staticmethod
    def extract_stmnts(file_contents):
        f_contents = file_contents

        f_contents = parse.format(f_contents, strip_comments=False, reindent=True)
        stmnt_list = parse.split(f_contents)

        # tab = []
        #
        # for stmnt in stmnt_list:
        #     stmnt = stmnt.replace('\n', ' ')
        #     stmnt = stmnt.replace('\t', ' ')
        #     tab.append(stmnt)

        return stmnt_list

    def set_sql_stmnts(self, filename, statement):
        self.sql_stmnts.append([filename, statement])

    """
    
    getZipStatement:
    -------------
    Description: Fonction permettant d'obtenir les requetes contenu dans un zip
    
    Entrée: Objet zip contenant le travail de l'étudiant
    Sortie: liste de requêtes dans le zip
    
    
    """

    def get_zip_statement(self, archive, referencefile):
        with archive as zip:
            Files = zip.filelist
            path = []
            for file in Files:

                if file.filename.endswith('.sql') and file.filename != '__MACOSX/exercices/._functions-scalaires03.sql':
                    f_contents = zip.read(file.filename)
                    tab = self.extract_stmnts(f_contents)
                    f_contents_comments = f_contents
                    path.append(file)

                    print(Files.index(file), file.filename)
                    self.extract_comments(f_contents_comments, referencefile)

                    if len(tab) != 0:
                        for stmnt in tab:
                            self.set_sql_stmnts(file.filename, stmnt)

                    else:
                        self.set_sql_stmnts(file.filename, "")

            return self.sql_stmnts

    """

            get_query_to_execute:
            -------------

            Fonction permettant de generer les requetes qui peuvent être execute

        """

    def get_query_to_execute(self, result):
        for i in range(len(self.query_parsed[1])):
            for file in result[0]:
                if self.query_parsed[1][i][0] == file:
                    self.to_execute.append(self.query_parsed[1][i])

        return self.to_execute, result[1]

    """

    choose_dir:
    -------------

    Fonction permettant de choisir le répertoire pour chaque type de requete

    """

    def choose_dir_for_validation(self):
        demonstration = []
        problemes = []
        exercices = []

        for i in range(len(self.query_parsed[1])):
            if self.query_parsed[1][i][0].startswith('demonstration/'):
                demonstration.append([self.query_parsed[1][i][0], self.query_parsed[0][i][1]])
            elif self.query_parsed[1][i][0].startswith('exercices/'):
                exercices.append(self.query_parsed[0][i])
            elif self.query_parsed[1][i][0].startswith('problemes/'):
                problemes.append(self.query_parsed[1][i])

        # validateQueryDemo(demonstration)
        # result = validateQueryExercices(demonstration)

        return self.get_query_to_execute("result")
        # validateQueryProblemes(problemes)
        # print(len(exercices))
        # validateQueryExercices(exercices)

        # f_contents = open(r"../../resources/queries/queries_tests/qryTests.sql")
        # f_contents = parse.format(f_contents, strip_comments=True, reindent=True)
        # stmnt_list = parse.split(f_contents)
        # tab = []
        # for stmnt in stmnt_list:
        #     tab.append(parse.parse(stmnt)[0].tokens)
        # print(stmnt)

        # validateQueryProblemes([["myFile", f_contents]])
        # validateQueryExercices(tab)
        # validateQueryExercices([exercices[1]])

    def parse_queries(self, statement_list):

        for statement in statement_list:
            parser = SqlParser()
            parser.parse_statement(statement)
            self.queries_parsed.append(parser.get_query_parsed())

    def get_queries_parsed(self):
        return self.queries_parsed

    def process_parsing(self, f_contents):

        statement_list = self.extract_stmnts(f_contents)
        self.parse_queries(statement_list)

    def choose_structure(self, fichier, referencefile=""):
        print(fichier)
        if fichier.endswith('.sql'):
            with open(fichier) as f_contents:
                f_contents_comments = f_contents

                self.process_parsing(f_contents)

                # self.extract_comments(f_contents, referencefile)

                # if len(statement_list) != 0:
                #     for stmnt in statement_list:
                #         self.set_sql_stmnts(fichier, stmnt)
                # else:
                #     self.set_sql_stmnts(fichier, "")
                #
                # self.query_parsed = [self.valid_parser(), self.sql_stmnts]
                # result = validateQueryExercices(self.query_parsed[0])

                # return self.get_query_to_execute(result)

        elif fichier.endswith('.zip'):
            print("start")
            archive = zipfile.ZipFile(fichier, 'r')
            self.get_zip_statement(archive, referencefile)
            print("end")
            # self.query_parsed = [self.valid_parser(), self.sql_stmnts]

            # return self.choose_dir_for_validation()


class GestionJsonHelper:

    def json_extract(self, obj, key):
        """Recursively fetch values from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Return all matching values in an object."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        if k == key:
                            arr.append(v)
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        to_return = []
        for result in results:
            if type(result) == list:
                for item in result:
                    to_return.append(item)
            else:
                to_return.append(result)
        return to_return
