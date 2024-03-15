from odoo import fields,models

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"

    name = fields.Char()
    description = fields.Text()
    date = fields.Date(help= "Date of the ticket")
    limit_date = fields.Date(help= "Limit date of the ticket")
    assigned = fields.Boolean(help = "Is the ticket assigned")
    acctions_todo = fields.Html()


