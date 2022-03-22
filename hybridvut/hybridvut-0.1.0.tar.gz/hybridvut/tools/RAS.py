import pandas as pd
import numpy as np

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def RAS_U(self, q, x, y, v, n, include_e_v=False):
    """Simple iterative fitting procedure for matrix U.

    Fits the matrix U so that its sum over columns equals q-y,
    and its sum over rows equals x-v.
    IN INPUT-OUTPUT ECONOMICS THIS IS CALLED RAS.
    """
    if self.U is not None:
        ix = self.U.index.copy()
        co = self.U.columns.copy()
        U_next = self.U.values.copy()
    else:
        logger.warning("Nothing to RAS - total U matrix is not defined")
        return
    m = n  # max iterations
    toler = 0.001  # tolerance

    if include_e_v == False:
        q_y = np.subtract(q, y).values  # known columns sum
        x_v = np.subtract(x, v).values  # known row sum
        # Set negative values to zero
        q_y = np.where(q_y < 0.0, 0.0, q_y)
        x_v = np.where(x_v < 0.0, 0.0, x_v)

        # Pre-adjustment of q_y and x_v to fulfill q_y.sum() = x_v.sum()
        # if q_y.sum() != x_v.sum():
        #    q_y = (q_y / q_y.sum()) * x_v.sum()

        # Delete values in rows and columns those are zero in x_v and q_y, respectively
        rows = np.where(q_y == 0.0)
        columns = np.where(x_v == 0.0)
        for r in rows:
            U_next[r, :] = 0.0
        for c in columns:
            U_next[:, c] = 0.0

    else:
        total_v = v.sum()
        total_y = y.sum()
        if total_y != total_v:
            total_v = total_v.copy()
        q_y = np.append(q.values, total_v)
        x_v = np.append(x.values, total_y)

        _y = np.append(y, 0)
        U_next = np.append(
            self.U.values, v.values.reshape(len(v), 1).transpose(), axis=0
        )
        U_next = np.append(U_next, _y.reshape(len(_y), 1), axis=1)

    # RAS
    while n > 0:
        n -= 1
        U_prev = U_next.copy()
        # Step 1: Row Scaling
        row_current = U_prev.sum(1)
        with np.errstate(
            divide="ignore", invalid="ignore"
        ):  # supress divide by zero warning
            R = np.diag(q_y / row_current)
        R = np.nan_to_num(R)
        U_next = np.matmul(R, U_prev)
        # Step 2: Column Scaling
        col_current = U_next.sum(0)
        with np.errstate(
            divide="ignore", invalid="ignore"
        ):  # supress divide by zero warning
            S = np.diag(x_v / col_current)
        S = np.nan_to_num(S)
        U_next = np.matmul(U_next, S)
        # Check Tolerance
        check_row = np.absolute(np.subtract(x_v, U_next.sum(0)))
        check_col = np.absolute(np.subtract(q_y, U_next.sum(1)))
        tol_check_row = np.all(check_row <= toler)
        tol_check_col = np.all(check_col <= toler)
        if tol_check_row == True and tol_check_col == True:
            break

    if include_e_v == False:
        U_rased = pd.DataFrame(U_next, index=ix, columns=co)
    else:
        U_rased = pd.DataFrame(
            U_next,
            index=ix.append(v.to_frame().columns),
            columns=co.append(y.to_frame().columns),
        )

    logger.info(
        "Terminated after iteration %s of %s. And with row tol: %s and col tol: %s (target: %s)",
        m - n,
        m,
        check_row.max(),
        check_col.max(),
        toler,
    )
    if tol_check_row == False or tol_check_col == False:
        index_com = U_rased.index[np.where(check_col > toler)]
        index_ind = U_rased.columns[np.where(check_row > toler)]
        logger.warning(
            "Row sum constraint not fulfilled at %s. Column sum constraint not fulfilled at %s",
            index_com,
            index_ind,
        )
    if include_e_v == False:
        return U_rased
    else:
        y = y.to_frame()
        v = v.to_frame()
        y.update(U_rased)
        v.update(U_rased.transpose())
        U_rased.drop(y.columns, axis=1, inplace=True)
        U_rased.drop(v.columns, axis=0, inplace=True)
        U_rased = pd.DataFrame(U_rased.values, index=ix, columns=co)
        return U_rased, y, v
