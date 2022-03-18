import logging

logger = logging.getLogger(__name__)


class DictAdapter:
    """
    Dict adapter.
    """

    def __init__(self, data):
        self.data = iter(data)

    def get_cursor(self):
        """
        Return next row in data
        execute_query() should be executed before calling this method.
        :return: next data row.
        """
        return next(self.data)
        # return None

    def execute_query(self, query_string):
        """
        Query a database table.
        :param query_string: query string to execute.
        :return: list of column names.
        """
        if self.data is None:
            return None
        else:
            return next(self.data)

    def fetch_row(self):
        if self.data is None:
            return None
        else:
            try:
                return next(self.data)
            except StopIteration as err:
                return None

    def close_cursor(self):
        """
        Close query execution cursor and connection.
        """
        del self.data


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    data_config = {"adapter": "dict", "data": [{"test_row": "1", "testing": "2"}]}

    adapter = DictAdapter(data_config.get("data"))
    header = adapter.execute_query("")
    logger.info(header)
    adapter.close_cursor()
