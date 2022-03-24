from sqlcarve.validator.executor import *
from sqlcarve.validator.helpers import *
from sqlcarve.validator.errorManager import *


class SemanticValidator:
    is_same = False

    def validate_query_result(self, reference_stmnt, result_stmnt):

        reference_stmnt = list(reference_stmnt)
        reference_stmnt.sort()

        result_stmnt = list(result_stmnt)
        result_stmnt.sort()

        compare = list(set(reference_stmnt) & set(result_stmnt))

        # if (set(reference_stmnt) == set(result_stmnt)):
        #     print("Lists are equal")
        # else:
        #     print("Lists are not equal")

        if len(compare) == len(reference_stmnt):
            self.is_same = True

    def validate_semantic(self, to_execute, ref_stmnt, conn=''):

        # Step validate semantic
        # Part 1: Execution

        log.info("Start of connexion")
        # conn = Connection.connect('mysql','sqlcarve.sqlite')
        conn = Connexion.connect('mysql', 'db-classicmodels', 'mysqlconnector', 'demo-gta', 'demo$GTA311',
                                  'gta-ins04.fadm.usherbrooke.ca', '3304')

        # conn = Connexion.json_connect()
        ref_result = Executor.execute_query(to_execute, conn)
        statement_result = Executor.execute_query(to_execute, conn)

        Connexion.close(conn)
        log.info("End of connexion")

        # Part 2: Validation

        self.validate_query_result(ref_result, statement_result)

        if self.is_same:
            log.debug("Les résutats sont pareils")
            return get_error("semanticIsValid")
        else:
            log.debug("Les résutats sont différents")
            return get_error("errorInValidations")
