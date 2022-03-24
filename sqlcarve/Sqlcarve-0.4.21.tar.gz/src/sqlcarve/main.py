from sqlcarve.validator.validator import *
import logging as log
import json as js


def analyse(fichier, referencefile):
    log.info("Start of validation")
    valid = Validator()
    dico = {}
    with open(fichier, "r") as f_content:
        stmnt_list = Preprocessor.extract_stmnts(f_content)
        for stmnt in stmnt_list:
            dico = valid.validate(statement=stmnt, ref_statement=stmnt, ref_comments=referencefile, type="all")

    print(js.dumps(dico, ensure_ascii=False, indent=2))

    log.info("End of validation")


if __name__ == "__main__":
    # referencefile = "../../resources/reference.json"
    # archive = zipfile.ZipFile('../../resources/prese-structure-devoir.zip', 'r')
    # analyse("../resources/prese-structure-devoir.zip", "../resources/reference.json")
    analyse("../resources/queries/samples01/qry005.sql", "../resources/reference.json")
    # analyse("../resources/queries/queries_tests/qryTests.sql", "../resources/reference.json")
