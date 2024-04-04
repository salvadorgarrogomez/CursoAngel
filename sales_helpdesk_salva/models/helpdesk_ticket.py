from odoo import fields,api,models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        inverse_name='ticket_ids',
        string='Sale Order',
    )
