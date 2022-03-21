import logging
import unittest
from contextlib import contextmanager

from tests.context import logger, QueryLogHandler, db_loader
from tisdb.client import TsdbClient
from tisdb.client2 import MetricdbClient


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self._qh = QueryLogHandler()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self._qh)

    def tearDown(self):
        logger.removeHandler(self._qh)

    def assertIsNone(self, value):
        self.assertTrue(value is None, "%r is not None" % value)

    def assertIsNotNone(self, value):
        self.assertTrue(value is not None, "%r is None" % value)

    def assertValueEqual(self, val1, val2):
        self.assertTrue(
            str(val1) == str(val2), u"{} != {}".format(str(val1), str(val2))
        )

    @contextmanager
    def assertRaisesCtx(self, exceptions):
        try:
            yield
        except Exception as exc:
            if not isinstance(exc, exceptions):
                raise AssertionError("Got %s, expected %s" % (exc, exceptions))
        else:
            raise AssertionError("No exception was raised.")

    @property
    def history(self):
        return self._qh.queries

    def reset_sql_history(self):
        self._qh.queries = []

    @contextmanager
    def assertQueryCount(self, num):
        qc = len(self.history)
        yield self.assertEqual(len(self.history) - qc, num)


class TsdbTestCase(BaseTestCase):
    def setUp(self):
        super(TsdbTestCase, self).setUp()
        self.tsdb: TsdbClient = db_loader(
            "porm", user="root", password="root", host="localhost", port=3306
        )

    def tearDown(self):
        super(TsdbTestCase, self).tearDown()


class MetricdbTestCase(BaseTestCase):
    def setUp(self):
        super(MetricdbTestCase, self).setUp()
        self.metricdb: MetricdbClient = db_loader(
            "porm", 
            client='METRICDB',
            user="root", password="root", host="localhost", port=3306
        )

    def tearDown(self):
        super(MetricdbTestCase, self).tearDown()
