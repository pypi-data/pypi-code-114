from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pos_name = fields.Char(string="POS name")

    @api.model
    def _prepare_from_pos(self, order_data):
        vals = super()._prepare_from_pos(order_data)
        PosSession = self.env["pos.session"]
        session = PosSession.browse(order_data["pos_session_id"])
        vals["pos_name"] = session.config_id.name
        return vals
