from odoo import fields, models

class HelpdeskTicketTags(models.Model):
    _name = "helpdesk.ticket.tags"
    _description = "Helpdesk Ticket Tags"

    name = fields.Char(
        required=True,
    )
    description = fields.Text()
    duration = fields.Float()
    ticket_ids = fields.Many2many(
        comodel_name = 'helpdesk.ticket',
        relation = 'helpdesk_ticket_tag_rel',
        column1 = 'tag_id',
        column2 = 'ticket_id',
        string = "Ticket",
    )
