from odoo import fields,models

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _order = "sequence"

    name = fields.Char(
        required = True,
    )
    description = fields.Text()
    date = fields.Date(
        help= "Date of the ticket"
    )
    limit_date = fields.Date(
        help= "Limit date of the ticket"
    )
    assigned = fields.Boolean(
        help = "Is the ticket assigned",
        readonly = True,
    )
    actions_todo = fields.Html()
    user_id = fields.Many2one(
        comodel_name = 'res.users', 
        string="Assigned to")
    sequence = fields.Integer()

    state = fields.Selection(
        [('nuevo', "Nuevo"),
         ('asignado', "Asignado"),
         ('en proceso', "En proceso"),
         ('pendiente', "Pendiente"),
         ('resuelto', "Resuelto"),
         ('cancelado', "Cancelado")],
         string = "State",
         default = "nuevo",
    )



