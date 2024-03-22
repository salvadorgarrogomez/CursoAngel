from odoo import fields, models

class HelpdeskTicketTags(models.Model):
    _name = "helpdesk.ticket.tags"
    _description = "Helpdesk Ticket Tags"

    name = fields.Char(
        required=True,
    )
    description = fields.Text()
    duration = fields.Float()
