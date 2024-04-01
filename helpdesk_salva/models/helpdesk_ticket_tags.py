from odoo import fields, models, api, Command

class HelpdeskTicketTags(models.Model):
    _name = "helpdesk.ticket.tags"
    _description = "Helpdesk Ticket Tags"

    @api.model
    def _get_default_ticket(self):
        # Verifica si el modelo activo es un ticket de helpdesk
        if self.env.context.get('active_model') == 'helpdesk.ticket':
            # Si es así, devuelve un comando para establecer el valor predeterminado como los IDs de tickets activos
            return [Command.set(self.env.context.get('active_ids'))]
        # Si el modelo activo no es un ticket de helpdesk, devuelve False
        return False


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
        default = _get_default_ticket
    )

    @api.model
    def _clean_unused_tags(self):
        unused_tags = self.search([('ticket_ids','=',False)])  
        unused_tags.unlink()

