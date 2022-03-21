from ..frame.dsw_sql_result import DswSqlResult
from odps.ipython.magics import ODPSSql
from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython.display import display


@magics_class
class DswOdpsMagics(ODPSSql):
    @line_cell_magic
    def dsw_sql(self, line, cell=''):
        result = self.execute(line, cell)
        res = DswSqlResult(result.values.values.tolist(),
                           schema=result, index=1)
        display(res)


def load_ipython_extension(ip):
    ip.register_magics(DswOdpsMagics)
