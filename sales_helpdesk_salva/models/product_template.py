from odoo import fields,api,models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    helpdesk_tag_id = fields.Many2one(
        comodel_name = 'helpdesk.ticket.tags',
        string = 'Helpdesk Tag',
    )
