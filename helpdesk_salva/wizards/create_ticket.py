from odoo import fields,api,models,Command,_

class CreateTicket(models.TransientModel):
    _name='create.ticket'

    @api.model
    def _get_default_tags(self):
        if self.env.context.get('active_model') == 'helpdesk.ticket.tags':
            return [Command.set(self.env.context.get('active_ids'))]

    name = fields.Char()
    tags_ids = fields.Many2many(
        comodel_name = 'helpdesk.ticket.tags',
        string = "Tags",
        default = _get_default_tags,
    )

    def _get_ticket_values(self):
        return {
            'name': self.name,
            'tags_ids': [Command.set(self.tags_ids.ids)],
        }

    def create_ticket(self):
        # Aseguramos que solo estamos operando en un único registro
        self.ensure_one()
        # Obtenemos los valores del ticket utilizando el método get_ticket_values()
        ticket_values = self._get_ticket_values()
        # Creamos un nuevo ticket utilizando el modelo 'helpdesk.ticket' y los valores obtenidos
        new_ticket = self.env['helpdesk.ticket'].create(ticket_values)
        # Obtenemos la acción asociada al formulario de tickets
        action = self.env["ir.actions.actions"]._for_xml_id("helpdesk_salva.helpdesk_ticket_action_all")
        # Definimos las vistas que queremos mostrar para la acción
        action['views'] = [(self.env.ref('helpdesk_salva.view_helpdesk_ticket_form').id,'form')]
        # Establecemos el ID del nuevo ticket como ID de recursos para la acción
        action['res_id'] = new_ticket.id
        # Devolvemos la acción
        return action
