from pMgr import *
import os
import numpy as np
from qpython import qconnection
os.environ['QHOME'] = '/home/chenduo/miniconda3/q'


class qSaver:
    def __init__(self, db_path, port, set_logger=False) -> None:
        self.p_mgr = pMgr(file=__file__, set_logger=set_logger)
        self.port = port
        self.q_proc = self.p_mgr.restart_current_q(
            'qSaver/qdb_saver.q', port=port)
        self.db_path = db_path
        self.q_dumper = qconnection.QConnection(
            host='localhost', port=port, numpy_temporals=True, pandas=True, single_char_strings=True)
        if set_logger:
            logging.info(f'qsaver starts on port : {port}')

    def save_pdbx(self, db_path, date, tname, t):
        """
        date = dt.date()
        """
        if not self.q_proc or self.q_proc.poll() is not None:
            self.q_proc = self.p_mgr.restart_current_q(
                'qSaver/qdb_saver.q', port=self.port)
        try:
            self.q_dumper.open()
            self.q_dumper('.db.upsertx', db_path,
                          np.datetime64(date), tname, t)
            self.q_dumper.close()
        except Exception:
            print('Exception')
            pass
            # exit(1)

    def rm_pdb_dtx(self, db_path, date, tname):
        if not self.q_proc or self.q_proc.poll() is not None:
            self.q_proc = self.p_mgr.restart_current_q(
                'qSaver/qdb_saver.q', port=self.port)
        try:
            self.q_dumper.open()
            self.q_dumper('.db.rm_dt', db_path,
                          np.datetime64(date), tname)
            self.q_dumper.close()
        except Exception:
            pass
            # exit(1)

    def rm_pdb_dx(self, db_path, date):
        if not self.q_proc or self.q_proc.poll() is not None:
            self.q_proc = self.p_mgr.restart_current_q(
                'qSaver/qdb_saver.q', port=self.port)
        try:
            self.q_dumper.open()
            self.q_dumper('.db.rm_d', db_path,
                          np.datetime64(date))
            self.q_dumper.close()
        except Exception:
            pass
            # exit(1)

    def save_pdb(self, date, tname, t):
        """
        date = dt.date()
        """
        self.save_pdbx(self.db_path, date, tname, t)

    def rm_pdb_dt(self, date, tname):
        self.rm_pdb_dtx(self.db_path, date, tname)

    def rm_pdb_d(self, date):
        self.rm_pdb_dx(self.db_path, date)
