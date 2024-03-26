from odoo import fields,api,models,_
from odoo.exceptions import UserError

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _order = "sequence"

    name = fields.Char(
        required= True,
        copy= False
    )
    description = fields.Text(
        translate= True
    )
    date = fields.Date(
        help= "Date of the ticket"
    )
    limit_date = fields.Date(
        help= "Limit date of the ticket"
    )
    assigned = fields.Boolean(
        help = "Is the ticket assigned",
        compute='_compute_assigned',
        search='_search_assigned', 
        inverse='_set_assigned'
    )
    time = fields.Float(
        string = "Time",
    )
    actions_todo = fields.Html()
    sequence = fields.Integer()

    user_id = fields.Many2one(
        comodel_name = 'res.users', 
        string="Assigned to"
    )
    user_email= fields.Char(
        string = "User Email",
        related="user_id.partner_id.email"
    )
    partner_id = fields.Many2one(
        comodel_name = 'res.partner', 
        string="Partner"
    )
    partner_email= fields.Char(
        string = "Partner Email",
        related="partner_id.email"
    )
    action_ids = fields.One2many(
        comodel_name = 'helpdesk.ticket.action',
        inverse_name = 'ticket_id',
        string = "Actions Done",
    )
    tags_ids = fields.Many2many(
        comodel_name = 'helpdesk.ticket.tags',
        relation = 'helpdesk_ticket_tag_rel',
        column1 = 'ticket_id',
        column2 = 'tag_id',
        string = "Tags",
    )
    tag_name = fields.Char(
        string = "Tag name",
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
    color = fields.Integer(
        string = "Color",
        default = 0,
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

    @api.model
    def get_amount_tickets(self):
        return self.search_count([('user_id', '=', self.env.user.id)])
    
    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            if record.user_id:
                record.assigned = True
            else:
                record.assigned = False

    def _search_assigned(self, operator, value):
        if operator not in ['=', '!='] or not isinstance(value, bool):
            raise UserError(_('Operation is not supported.'))
        if (operator == '=' and value) or (operator == '!=' and not value):
            new_operator = '!='
        else:
            new_operator = '='
        return  [('user_id',new_operator,False)]

    def _set_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            elif not record.user_id:
                record.user_id = self.env.user


    # Ejemplos de de uso de Metodos ORM, copy
    # action_values = []
    # for action in xxx:
    #    action_values.append((0, 0, {'sequence':1, 'name': 'Accion 1', 'description': 'Description'}))
    #
    # ticket.write({
    #    'action_ids': action_values
    # })

    # Ejemplos de de uso de Metodos ORM, write

    def create_and_link_tag(self):
        self.ensure_one()
        #   Creo el ticket y lo asigno
        tag = self.env['helpdesk.ticket.tags'].create({'name': self.tag_name})
        #   Odoo version 14 y posteriores
        self.write({'tags_ids': [fields.Command.link(tag.id, 0)],
                    'tag_name': False
                    })
        # Odoo version 12 y anteriores
        # self.write({'tags_ids': [(4, tag.id, 0)],
        #             'tag_name': False
        #             })

    # Creo el ticket desde la escritura del tag_ids
    def create_and_link_ticket(self):
        self.ensure_one()
        # Comprueba si la etiqueta ya existe
        tag = self.env['helpdesk.ticket.tags'].search([('name', '=', self.tag_name)], limit=1)
        if not tag:
            # Si no existe, crea la etiqueta
            tag = self.env['helpdesk.ticket.tags'].create({'name': self.tag_name})
        # Crea la relación entre el ticket y la etiqueta
        self.write({
            'tags_ids': [(4, tag.id, 0)],  # Agrega la etiqueta existente
            'tag_name': False  # Limpia el campo tag_name
        })

        
    # Crear el tag asociado al ticket
    def create_and_link_ticket_tag(self):
        self.ensure_one()
        #  Odoo version 14 y posteriores
        tag = self.env['helpdesk.ticket.tags'].create({
            'name': self.tag_name,
            'ticket_ids':[fields.Command.set(self.ids)]
            })
        # Odoo version 12 y anteriores
        # tag = self.env['helpdesk.ticket.tags'].create({
        #    'name': self.tag_name,
        #    'ticket_ids':[(6.0, self.ids)]
        #    })
        self.write({
            'tag_name': False
            })
