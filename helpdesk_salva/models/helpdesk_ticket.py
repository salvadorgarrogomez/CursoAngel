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
    sequence = fields.Integer()

    user_id = fields.Many2one(
        comodel_name = 'res.users', 
        string="Assigned to"
    )
    patner_id = fields.Many2one(
        comodel_name = 'res.partner', 
        string="Partner"
    )
    action_ids = fields.One2many(
        comodel_name = 'helpdesk.ticket.action',
        inverse_name = 'ticket_id',
        string = "Actions Done",
    )
    tags_ids = fields.Many2many(
        comodel_name = 'helpdesk.ticket.tags',
        #relation = 'table_name',
        #column1 = 'col_name',
        #column2 = 'other_col_name',
        string = "Tags",
    )

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

    # Formas distintas de hacer el mismo proceso: 1
    def to_asignado(self):
        self.ensure_one()
        self.state = 'asignado'

    # Formas distintas de hacer el mismo proceso: 2
    def to_en_proceso(self):
        self.write({'state': 'en proceso'})

    # Formas distintas de hacer el mismo proceso: 3
    def to_pendiente(self):
        for record in self:
            record.state = 'pendiente'
        
    def to_resuelto(self):
        for record in self:
            record.state ='resuelto'

    def to_cancelado(self):
        for record in self:
            record.state = 'cancelado'

    def review_actions(self):
        self.ensure_one()
        self.action_ids.review_all()