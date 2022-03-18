import sqlparse as parse
import logging as log


class SqlParser:
    request = []

    def parse_statement(self, statement):

        try:
            if len(statement) != 0:
                self.request = [statement, parse.parse(statement)[0].tokens]
                # self.req = parse.parse(statement)[0].tokens
        except parse.exceptions.SQLParseError:
            # print("Bad statement. Ignoring.\n'%s'" % statement)
            log.error("Bad statement. Ignoring.\n'%s'" % statement)

    def get_query_parsed(self):
        return self.request
