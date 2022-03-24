"""
CommentsValidator Class:
-------------
Cette classe est une classe allouée aux a la recuperation
et la validation des commentaires.
"""

from sqlcarve.validator.helpers import *
from sqlcarve.validator.errorManager import *
import re

regex = r"(?:\/\/[^\n]*|\/\*(?:(?!\*\/).)*\*\/)|(--.*?\n)"


# regex = r"\/\*.*?\*\/|--.*?\n"


class CommentsValidator:
    """
    Classe commentaire
    """

    def __init__(self):
        """
        Cette classe initialisation un commentaire
        """
        self.comment_error = ErrorManager()

    def get_comment_element(self, statement):
        """
        Cette fonction permet de recuperer une liste d'elements d'un fichier
        sql et retourne une liste contenant seulement les commentaires
        :param statement
        :return words_tokens
        """
        matches = re.finditer(regex, statement, re.DOTALL)
        # pat = regex.join(field_labels) + regex
        words_tokens = []
        for matchNum, match in enumerate(matches, start=1):
            for line in (match.group().split('*')):
                line = line.replace('/', ' ')
                line = line.replace('--', ' ')
                words_tokens.append(line.strip())

            log.debug("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=matchNum,
                                                                                start=match.start(),
                                                                                end=match.end(),
                                                                                group=match.group()))
        # log.debug(words_tokens)
        return words_tokens

    # Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

    def validate_comment(self, statement, fichierjson):

        elemnt_list = self.get_comment_element(statement)

        """
       Cette fonction permet de valider la liste de commentaires
       grace a un fichier de reference contenant les champs qui doivent s'y trouver
       :param statement, fichierjson
       :return str()
       """
        list = []
        content_list = []

        for i in elemnt_list:
            if not (i == '' or i == '\n'):
                list.append(i)
                log.debug(i)

        log.debug(list)

        for element in list:
            element = element.replace('\n', '')
            # if element[0] == ' ':
            #     element = element.replace(' ', '', 1)
            result = re.split(regex, element)
            content_list.append(result)

        with open(fichierjson) as jf:
            data = json.loads(jf.read())
            prof_data = data["profcomments"]
            student_data = data["studentcomments"]
            prof_pattern = zip(prof_data, content_list)
            student_pattern = zip(student_data, content_list)
            start = 0

            for (i, l), (j, k) in zip(prof_pattern, student_pattern):
                # print(i, l, ":", j, k)
                present_prof = l[0].find(i)
                present_student = k[0].find(j)
                # print(present_student)
                taille = len(l[0])
                # print(taille)
                x = l[0][:taille]
                if present_prof == -1 and present_student == -1:
                    start = start + 1
                    if start == 3:
                        log.debug("No header comment found.")
                elif present_prof != -1:
                    log.debug(i + ' found')
                elif present_student != -1:
                    log.debug(j + ' found')

            return list