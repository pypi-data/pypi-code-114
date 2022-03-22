# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from datetime import datetime
from trytond.pool import Pool, PoolMeta
from trytond.model import fields
from trytond.transaction import Transaction
from trytond.pyson import Eval


class Configuration(metaclass=PoolMeta):
    __name__ = 'stock.configuration'

    update_requested_delivery_date = fields.Boolean(
        'Update Requested Delivery Date of Sale Lines',
        help='Update also the Requested Delivery Date of Sale Lines '
        'when the Planned Date of their related Sale Moves are updated.',
        states={
            'invisible': ~Eval('update_move_out'),
            })


class Move(metaclass=PoolMeta):
    __name__ = 'stock.move'

    @classmethod
    def renew_sale_line_requested_delivery_date(cls, date=None):
        pool = Pool()
        Date = pool.get('ir.date')
        SaleLine = pool.get('sale.line')

        move = cls.__table__()
        sale_line = SaleLine.__table__()
        cursor = Transaction().connection.cursor()

        if not date:
            date = Date.today()

        sql_where = (
            (~move.state.in_(['cancel', 'done']))
            & (move.planned_date < date)
            & (move.origin.like('sale.line,%')))
        cursor.execute(*move.select(move.origin, where=sql_where))
        sale_line_ids = {
            int(m[0].split(',')[1]) for m in cursor.fetchall()}
        for id_ in sale_line_ids:
            sql_where = (
                (sale_line.id == id_)
                & (sale_line.requested_delivery_date < date))
            cursor.execute(*sale_line.update(
                columns=[sale_line.requested_delivery_date,
                        sale_line.write_date],
                values=[date, datetime.now()],
                where=sql_where))

    @classmethod
    def update_planned_date(cls, date=None):
        pool = Pool()
        Configuration = pool.get('stock.configuration')
        conf = Configuration(1)

        if conf.update_move_out and conf.update_requested_delivery_date:
            cls.renew_sale_line_requested_delivery_date(date=date)
        super().update_planned_date(date)
