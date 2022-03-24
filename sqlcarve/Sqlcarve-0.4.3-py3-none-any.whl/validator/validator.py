from sqlcarve.validator.semanticValidator import *
from sqlcarve.validator.syntaxValidator import *
from sqlcarve.validator.commentsValidator import *


class Validator:
    to_execute = []
    validation_report = {}

    def __init__(self):
        self.helper = Preprocessor()
        self.comment = CommentsValidator()
        self.syntax = SyntaxValidator()
        self.semantic = SemanticValidator()


    def validate(self, **kwargs):

        # conn = Connexion.json_connect()
        # connexion_string = kwargs.get('conn')
        statement = kwargs.get('statement')
        ref_statement = kwargs.get('ref_statement', None)
        type = kwargs.get('type')
        ref_comments = kwargs.get('ref_comments', None)
        stmnt_without_comments = self.helper.remove_comments(statement)

        log.debug(type)

        if type == "syntax":
            self.validation_report["syntax"] = self.syntax.validate_syntax(stmnt_without_comments)

        elif type == "semantic":
            if self.syntax.is_valid():
                self.validation_report["semantic"] = self.semantic.validate_semantic(stmnt_without_comments,
                                                                                           ref_statement)
                # self.semantic.validate_semantic(self.to_execute, ref_statement, conn)

        elif type == "comments":
            self.validation_report["comments"] = self.comment.validate_comment(statement, ref_comments)

        elif type == "all":
            self.validation_report["comments"] = self.comment.validate_comment(statement, ref_comments)

            self.validation_report["syntax"] = self.syntax.validate_syntax(stmnt_without_comments)

            if self.syntax.is_valid():
                self.validation_report["semantic"] = self.semantic.validate_semantic(stmnt_without_comments,
                                                                                           ref_statement)

        else:
            log.error("Ce type de validation n'est pas fonctionnel")

        return self.validation_report

        # return self.to_execute, self.syntax.syntax_error.get_files_errors()

    # def process_to_syntax_mode(self, file):
    #     # Step validate syntax
    #     for statement in self.helper.get_queries_parsed():
    #         # result = validate_query_exercices(statement[1])
    #         log.debug(statement)
    #         self.syntax.validate_syntax(statement[1])
    #
    #         if self.syntax.etat:
    #             log.debug("est valide")
    #             log.debug(statement[0])
    #             self.to_execute.append(statement[0])
    #         else:
    #             stmnt_error_list = self.syntax.syntax_error.get_list_errors()
    #             self.syntax.syntax_error.add_errors_to_filename(file, stmnt_error_list)
    #
    # def process_to_semantic_mode(self):
    #     self.semantic.validate_semantic(self.to_execute, self.syntax)
