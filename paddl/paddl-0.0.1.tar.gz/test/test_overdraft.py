from pytest import fixture, mark
from paddl import parse


class TestMySQL:
    @fixture
    def ddl(self):
        return open('data/ddls/overdraft.sql').read()

    @mark.skip("not yet")
    def test_hello(self, ddl):
        result = parse(ddl)
        assert result['table_name'] == 'bob'
        assert list(result) == ['CREATE', 'TABLE', 'bob',
                                '(', 'id', 'int', 'name', 'varchar(255)', ')']
