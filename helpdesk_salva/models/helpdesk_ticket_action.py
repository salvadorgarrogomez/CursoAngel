from odoo import fields,models

class HelpdeskTicketAction(models.Model):
    _name = "helpdesk.ticket.action"
    _description = "Helpdesk Ticket Action"
    _order = "sequence"

    name = fields.Char(
        required = True,
    )
    description = fields.Text()
    sequence = fields.Integer()
    duration = fields.Float()
    user_id = fields.Many2one(
        comodel_name = 'res.users', 
        string="Assigned to"
    )
    ticket_id = fields.Many2one(
        comodel_name = 'helpdesk.ticket',
    )

    def review_all(self):
        for record in self:
            record.description = '%s\n\n%s' % (record.description,'Ok')