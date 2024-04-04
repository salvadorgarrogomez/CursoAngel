from odoo import fields,models,Command


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='sale_order_id',
        string='Tickets',
    )

    def create_ticket(self):
        self.ensure_one()
        tag_ids = self.order_line.product_id.helpdesk_tag_id.ids
        self.write({'ticket_ids': [Command.create({'name':self.name,'tag_ids': 
                                                   [Command.set(tag_ids)]})]
                    })

        # Método para crear un ticket relacionado con la orden de venta
#    def create_ticket(self):
        # Asegurarse de que solo haya una orden de venta
#        self.ensure_one()
        # Obtener las etiquetas relacionadas con los productos en la línea de la orden
#        tag_ids = self.order_line.product_id.helpdesk_tag_id.ids
        # Escribir en el campo One2many ticket_ids para crear un nuevo ticket
        # Utilizando la API Command para crear registros y establecer valores
#        self.write({
#            'ticket_ids': [
                # Crear un nuevo registro de ticket con los siguientes valores
#                Command.create({
#                    'name': self.name,  # Nombre del ticket igual al nombre de la orden de venta
#                    'tags_ids': [Command.set(tag_ids)]  # Asignar las etiquetas obtenidas anteriormente
#                })]})