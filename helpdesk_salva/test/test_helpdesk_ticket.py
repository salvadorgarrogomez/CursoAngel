from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase

class TestHelpdeskTicket(TransactionCase):
    def setUp(self):
        super (TestHelpdeskTicket, self).setUp()
        # Un self u otro, no los dos al mismo tiempo
        self.ticket = self.env['helpdesk.ticket'].create({
            'name': 'test ticket',
        })

        #self.ticket = self.env.ref('helpdesk_salva.demo_admin_ticket')

    def test_time_can_not_be_negative(self):
        self.ticket.time = 3
        self.assertEqual(self.ticket.time,3)
        self.ticket.time = 8
        self.assertEqual(self.ticket.time,8)
        with self.assertRaises(ValidationError):
            self.ticket.time = -1

    def test_states(self):
        self.assertEqual(self.ticket.state, 'nuevo')
        self.ticket.to_asignado()
        self.assertEqual(self.ticket.state, 'asignado')
        self.ticket.to_en_proceso
        self.assertEqual(self.ticket.state, 'en proceso')
        self.ticket.to_pendiente
        self.assertEqual(self.ticket.state, 'pendiente')
        self.ticket.to_resuelto
        self.assertEqual(self.ticket.state, 'resuelto')
        self.ticket.to_cancelado
        self.assertEqual(self.ticket.state, 'cancelado')

